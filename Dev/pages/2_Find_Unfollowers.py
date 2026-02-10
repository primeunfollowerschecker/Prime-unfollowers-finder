import streamlit as st
import json

st.set_page_config(page_title="Find Unfollowers", page_icon="📉")

st.title("📉 Instagram Unfollowers Finder")

st.info("📂 Upload your Instagram JSON files below to find who doesn't follow you back.")

# ---------------- FILE UPLOAD ----------------

followers_file = st.file_uploader(
    "👥 Upload followers_1.json",
    type=["json"]
)

following_file = st.file_uploader(
    "➡️ Upload following.json",
    type=["json"]
)

# ---------------- FUNCTION ----------------

def extract_usernames(data):
    usernames = []
    for item in data:
        try:
            usernames.append(
                item["string_list_data"][0]["value"]
            )
        except:
            pass
    return usernames


# ---------------- MAIN LOGIC ----------------

if followers_file and following_file:

    followers_data = json.load(followers_file)
    following_data = json.load(following_file)

    followers = extract_usernames(followers_data)
    following = extract_usernames(following_data)

    unfollowers = list(set(following) - set(followers))

    st.success(f"✅ Found {len(unfollowers)} unfollowers")

    FREE_LIMIT = 5

    # -------- FREE RESULTS --------
    st.subheader("🎁 Free Results")
    st.write(unfollowers[:FREE_LIMIT])

    # -------- LOCKED PREVIEW --------
    if len(unfollowers) > FREE_LIMIT:

        st.subheader("🔒 Locked Results Preview")

        locked_users = unfollowers[FREE_LIMIT:]

        blurred_list = []

        for user in locked_users[:10]:
            if len(user) > 3:
                blurred_list.append(user[:2] + "****")
            else:
                blurred_list.append("****")

        st.write(blurred_list)

        st.warning("🚀 Full list locked. Upgrade to see all results.")

else:
    st.warning("⚠️ Please upload both JSON files to continue.")
