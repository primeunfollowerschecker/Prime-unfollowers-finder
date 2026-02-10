import streamlit as st

FREE_LIMIT = 5

# ---------------- SESSION STATE ----------------
if "unlocked" not in st.session_state:
    st.session_state.unlocked = False


# ---------------- VALID CODES (HIDDEN FROM USERS) ----------------
VALID_CODES = [
"A123","B456","C789","D102","E204","F305","G406","H507","I608","J709",
"K810","L911","M112","N213","O314","P415","Q516","R617","S718","T819",
"U920","V021","W122","X223","Y324","Z425","AA11","BB22","CC33","DD44",
"EE55","FF66","GG77","HH88","II99","JJ10","KK20","LL30","MM40","NN50",
"OO60","PP70","QQ80","RR90","SS01","TT02","UU03","VV04","WW05","XX06",
"YY07","ZZ08","AB12","BC23","CD34","DE45","EF56","FG67","GH78","HI89",
"IJ90","JK01","KL12","LM23","MN34","NO45","OP56","PQ67","QR78","RS89",
"ST90","TU11","UV22","VW33","WX44","XY55","YZ66","ZA77","XB88","WC99",
"VD10","UE20","TF30","SG40","RH50","QI60","PJ70","OK80","NL90","MK01",
"LJ12","KI23","JH34","IG45","HF56","GE67","FD78","EC89","DB90","CA01"
# continue all your codes here
]


# ---------------- USED CODES FILE ----------------
USED_CODES_FILE = "used_codes.txt"

# Load used codes
try:
    with open(USED_CODES_FILE, "r") as f:
        USED_CODES = f.read().splitlines()
except:
    USED_CODES = []


# ---------------- PAGE UI ----------------
st.title("🔒 Premium Unlock System")

st.info("💎 Enter your unlock code to view the full unfollowers list.")


# ---------------- UNLOCK INPUT ----------------
unlock_code = st.text_input("🔑 Enter Unlock Code")


if st.button("🚀 Unlock Premium"):

    if unlock_code in VALID_CODES and unlock_code not in USED_CODES:

        # Save used code
        with open(USED_CODES_FILE, "a") as f:
            f.write(unlock_code + "\n")

        st.session_state.unlocked = True
        st.success("✅ Premium Unlocked Successfully!")

    elif unlock_code in USED_CODES:
        st.error("⚠️ This code has already been used.")

    else:
        st.error("❌ Invalid Unlock Code")


# ---------------- SHOW PREMIUM DATA ----------------
if st.session_state.unlocked:
    st.subheader("🎉 Full Unfollowers List")
    st.success("✅ All results unlocked!")

    st.write(st.session_state.unfollowers)
