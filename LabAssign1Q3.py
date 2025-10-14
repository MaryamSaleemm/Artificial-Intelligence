

import streamlit as st
import numpy as np
import random
from typing import Optional, Tuple, List

st.set_page_config(page_title="Tic-Tac-Toe", page_icon="🎮")

def check_winner(board: np.ndarray) -> int:
   
    # Check rows 
    for i in range(3):
        first = board[i, 0]
        if first == 0:
            continue
        same = True
        for j in range(1, 3):          
            if board[i, j] != first:
                same = False
                break
        if same:
            return int(first)

  
    for j in range(3):
        first = board[0, j]
        if first == 0:
            continue
        same = True
        for i in range(1, 3):            
            if board[i, j] != first:
                same = False
                break
        if same:
            return int(first)

    # Diagonals (explicit)
    if board[0, 0] == board[1, 1] == board[2, 2] != 0:
        return int(board[1, 1])
    if board[0, 2] == board[1, 1] == board[2, 0] != 0:
        return int(board[1, 1])

    # Draw?
    if np.all(board != 0):
        return -1

    return 0  # ongoing

def find_empty_cells(board: np.ndarray) -> List[Tuple[int,int]]:
    return list(zip(*np.where(board == 0)))

def ai_move_simple(board: np.ndarray) -> Optional[Tuple[int,int]]:
    """
    Simple AI:
    1) If AI can win in one move -> play that move
    2) Else if opponent can win next -> block that move
    3) Else play center if free
    4) Else play a corner (random)
    5) Else random empty
    """
    empties = find_empty_cells(board)
    if not empties:
        return None

    # 1) AI tries to win (simulate placing 2)
    for (r, c) in empties:
        board[r, c] = 2
        if check_winner(board) == 2:
            board[r, c] = 0
            return (r, c)
        board[r, c] = 0

    
    for (r, c) in empties:
        board[r, c] = 1
        if check_winner(board) == 1:
            board[r, c] = 0
            return (r, c)
        board[r, c] = 0

  
    if board[1, 1] == 0:
        return (1, 1)

    
    corners = [(0,0), (0,2), (2,0), (2,2)]
    random.shuffle(corners)
    for rc in corners:
        if board[rc] == 0:
            return rc

    # 5) Random empty
    return random.choice(empties)

if "board" not in st.session_state:
    st.session_state.board = np.zeros((3, 3), dtype=int) 
    st.session_state.turn = 1   
    st.session_state.game_over = False
    st.session_state.message = "Player 1's turn (X)"
    st.session_state.winner = 0

st.sidebar.header("Settings")
mode = st.sidebar.selectbox("Mode", ["Player vs AI", "Player vs Player"])
start_choice = st.sidebar.radio("Who starts?", ["Player 1 (X)", "Player 2 (O)"])
start_player = 1 if start_choice.startswith("Player 1") else 2

def restart_game(starting_player:int = 1):
    st.session_state.board = np.zeros((3, 3), dtype=int)
    st.session_state.turn = starting_player
    st.session_state.game_over = False
    st.session_state.winner = 0
    st.session_state.message = f"Player {starting_player}'s turn ({'X' if starting_player==1 else 'O'})"

if st.sidebar.button("Start New Game (apply starter)"):
    restart_game(start_player)
   
    if mode == "Player vs AI" and st.session_state.turn == 2:
        ai_cell = ai_move_simple(st.session_state.board)
        if ai_cell:
            st.session_state.board[ai_cell] = 2
            winner = check_winner(st.session_state.board)
            if winner == 2:
                st.session_state.message = "🤖 AI wins!"
                st.session_state.game_over = True
            elif winner == -1:
                st.session_state.message = "🤝 It's a Draw!"
                st.session_state.game_over = True
            else:
                st.session_state.turn = 1
                st.session_state.message = "Player 1's turn (X)"

st.title("🎮 Tic-Tac-Toe")
st.write("Board uses `np.zeros((3,3), dtype=int)` where 0=empty, 1=X (Player 1), 2=O (Player 2/AI).")
st.write(f"Mode: **{mode}** — Starting player: **{start_choice}**")
st.markdown("---")

cols_gap = "small"
for i in range(3):
    cols = st.columns(3, gap=cols_gap)
    for j in range(3):
        val = st.session_state.board[i, j]
        symbol = " " if val == 0 else ("❌" if val == 1 else "⭕")
        key = f"cell-{i}-{j}"

      
        clicked = cols[j].button(symbol, key=key, use_container_width=True)
        if clicked and not st.session_state.game_over:
            
            if mode == "Player vs Player":
                allowed = (st.session_state.turn in [1,2])
            else:  # Player vs AI
               
                allowed = (st.session_state.turn == 1)

            if allowed and st.session_state.board[i, j] == 0:
            
                st.session_state.board[i, j] = st.session_state.turn
                winner = check_winner(st.session_state.board)
                if winner == 1:
                    st.session_state.message = "🎉 Player 1 (X) wins!"
                    st.session_state.game_over = True
                    st.session_state.winner = 1
                elif winner == 2:
                    st.session_state.message = "🎉 Player 2 (O) wins!"
                    st.session_state.game_over = True
                    st.session_state.winner = 2
                elif winner == -1:
                    st.session_state.message = "🤝 It's a Draw!"
                    st.session_state.game_over = True
                    st.session_state.winner = -1
                else:
                   
                    if mode == "Player vs Player":
                        st.session_state.turn = 2 if st.session_state.turn == 1 else 1
                        st.session_state.message = f"Player {st.session_state.turn}'s turn ({'X' if st.session_state.turn==1 else 'O'})"
                    else:
                        
                        st.session_state.turn = 2
                        st.session_state.message = "AI's turn (O)"
                        ai_cell = ai_move_simple(st.session_state.board)
                        if ai_cell:
                            st.session_state.board[ai_cell] = 2
                            winner = check_winner(st.session_state.board)
                            if winner == 2:
                                st.session_state.message = "🤖 AI wins!"
                                st.session_state.game_over = True
                                st.session_state.winner = 2
                            elif winner == -1:
                                st.session_state.message = "🤝 It's a Draw!"
                                st.session_state.game_over = True
                                st.session_state.winner = -1
                            else:
                                st.session_state.turn = 1
                                st.session_state.message = "Player 1's turn (X)"

st.markdown("### Game status")
st.write(st.session_state.message)

with st.expander("Show board array (for debugging / clarity)", expanded=False):
    st.write(st.session_state.board)

if st.button("🔄 Restart Game"):
    restart_game(start_player)

    if mode == "Player vs AI" and st.session_state.turn == 2:
        ai_cell = ai_move_simple(st.session_state.board)
        if ai_cell:
            st.session_state.board[ai_cell] = 2
            winner = check_winner(st.session_state.board)
            if winner == 2:
                st.session_state.message = "🤖 AI wins!"
                st.session_state.game_over = True
            elif winner == -1:
                st.session_state.message = "🤝 It's a Draw!"
                st.session_state.game_over = True
            else:
                st.session_state.turn = 1
                st.session_state.message = "Player 1's turn (X)"

st.markdown("---")
st.caption("Implementation: NumPy board + nested loop win-check + Streamlit UI. AI is simple but effective for demo purposes.")
