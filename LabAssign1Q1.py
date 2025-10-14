import requests
from bs4 import BeautifulSoup
import streamlit as st


URL = "https://arxiv.org/list/cs.AI/recent"
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

papers = []
for dt, dd in zip(soup.find_all("dt"), soup.find_all("dd")):
    
    link_tag = dt.find("a", title="Abstract")
    link = "https://arxiv.org" + link_tag["href"] if link_tag else "No link available"

    
    title = dd.find("div", class_="list-title mathjax").text.replace("Title:", "").strip()

  
    authors = dd.find("div", class_="list-authors").text.replace("Authors:", "").strip()

 
    abstract_tag = dd.find("p", class_="mathjax")
    abstract = abstract_tag.text.strip() if abstract_tag else "No abstract available."

    papers.append({
        "title": title,
        "authors": authors,
        "abstract": abstract,
        "link": link
    })

# Streamlit
st.title("🤖 AI Research Paper Finder")
st.write("Search latest **AI research papers** from arXiv.")

keyword = st.text_input("Enter keyword (e.g., 'neural', 'robotics', 'vision'):")

if st.button("Search"):
    results = [p for p in papers if keyword.lower() in p['title'].lower() or keyword.lower() in p['abstract'].lower()]

    if results:
        st.success(f"Found {len(results)} papers!")
        for p in results:
            st.subheader(p['title'])
            st.write(f"**Authors:** {p['authors']}")
            st.write(f"**Abstract:** {p['abstract'][:250]}...")  
            st.markdown(f"[Read Full Paper]({p['link']})")
            st.write("---")
    else:
        st.warning("No matching papers found.")
