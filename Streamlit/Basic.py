import streamlit as st


st.title('AI Research Paper Finder')
st.subheader('Search latest AI research papers from arXiv.')
st.write("Enter keyword (e.g., 'neural', 'robotics', 'vision'):")

#***************selectbox***************
select = st.selectbox('select from box:',["neural" , "robotics", "vision"])
# st.write(select)

#***************Radio***************
st.radio('Which one you choose:', ['AI' , 'WEB', 'MOB APP'])


#***************Button***************
st.button('click me')
st.success('button pressed')
st.write('button pressed')


#***************Slider***************
quantity = st.slider("select the ratio:",0,5,2)  #2 is default value
st.write('quantity is:', {quantity})

#***************number_input***************
st.number_input("select the quantity:", min_value=1 , max_value=5 , step=1)

#***************text_input***************
name = st.text_input("enter your name:")
if name:
    st.write(f'your order is on the way {name}')
    
 #***************DATE***************
st.date_input("select date")
    
