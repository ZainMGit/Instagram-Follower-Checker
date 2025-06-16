import streamlit as st
from bs4 import BeautifulSoup

def extract_usernames(html):
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("a", href=True)
    usernames = {link.get_text().strip() for link in links if link.get("href").startswith("https://www.instagram.com/")}
    return usernames

st.title("Instagram Unfollowers Checker")
st.write("Upload your `followers_1.html` and `following.html` files to see who's not following you back.")

followers_file = st.file_uploader("Upload your followers_1.html file", type=["html"])
following_file = st.file_uploader("Upload your following.html file", type=["html"])

if followers_file and following_file:
    followers = extract_usernames(followers_file.read())
    following = extract_usernames(following_file.read())
    not_following_back = sorted(following - followers)

    st.subheader("Users not following you back:")
    for user in not_following_back:
        st.write(user)
    
    st.success(f"Total: {len(not_following_back)} users not following you back.")
