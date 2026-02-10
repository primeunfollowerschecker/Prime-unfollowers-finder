import streamlit as st
import json

st.title("📂 Upload Instagram Files")

st.markdown("""
### 📥 How to get your Instagram files

1️⃣ Open Instagram in browser  
2️⃣ Settings → Accounts Center  
3️⃣ Your information and permissions  
4️⃣ Download your information  
5️⃣ Select Followers & Following  
6️⃣ Choose JSON format
""")

followers_file = st.file_uploader("Upload followers_1.json", type="json")
following_file = st.file_uploader("Upload following.json", type="json")

if followers_file and following_file:

    followers_data = json.load(followers_file)
    following_data = json.load(following_file)

    followers = [i["string_list_data"][0]["value"] for i in followers_data]
    following = [i["string_list_data"][0]["value"] for i in following_data]

    st.session_state["followers"] = followers
    st.session_state["following"] = following

    st.success("✅ Files uploaded successfully! Go to Find Unfollowers page.")
