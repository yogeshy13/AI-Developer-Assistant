import streamlit as st
import requests
import time

st.set_page_config(page_title="AI Dev Assistant", layout="wide")

# ---------- THEME ----------

theme = st.sidebar.radio("🌗 Theme", ["Dark", "Light"])

if theme == "Dark":
    st.markdown(""" <style>
    body { background-color: #0e1117; color: white; } </style>
    """, unsafe_allow_html=True)

# ---------- HEADER ----------

st.markdown("""

# 🤖 AI Dev Assistant

### 🚀 AI-first Engineering Copilot

""")

# ---------- SIDEBAR ----------

st.sidebar.title("⚙️ Tools")

tool = st.sidebar.selectbox(
"Choose Tool",
["Agent (Smart Mode)", "Ask", "Fix Code", "Generate Tests", "Architecture"]
)

st.sidebar.markdown("---")

# ---------- INPUT SOURCES ----------

repo_url = st.sidebar.text_input("🔗 GitHub Repo URL")

uploaded_file = st.sidebar.file_uploader(
"📂 Upload Code File",
type=["py", "js", "ts", "java"]
)

file_content = None
if uploaded_file:
    file_content = uploaded_file.read().decode("utf-8")

# ---------- CODE EDITOR ----------

code_input = st.text_area("📝 Paste your code here", height=300)

final_code = code_input if code_input else file_content

# ---------- CHAT STATE ----------

if "chat" not in st.session_state:
    st.session_state.chat = []

# ---------- USER INPUT ----------

query = st.chat_input("Ask anything about your code...")

endpoint_map = {
"Ask": "/ask",
"Fix Code": "/fix",
"Generate Tests": "/tests",
"Architecture": "/architecture",
"Agent (Smart Mode)": "/agent"
}

# ---------- HANDLE INPUT ----------

if query:
    endpoint = endpoint_map[tool]

    payload = {
        "query": query,
        "repo": repo_url,
        "code": final_code
    }
    with st.spinner("🧠 Thinking..."):
        try:
            response = requests.post(
                f"http://127.0.0.1:8000{endpoint}",
                json=payload
            )

            if response.status_code == 200:
                result = list(response.json().values())[0]

                # Save chat
                st.session_state.chat.append(("user", query))
                st.session_state.chat.append(("ai", result))
            else:
                st.session_state.chat.append(("ai", "❌ Backend error"))

        except Exception as e:
            st.session_state.chat.append(("ai", f"❌ Connection failed: {e}"))

# ---------- CHAT DISPLAY ----------

for role, message in st.session_state.chat:
    if role == "user":
        with st.chat_message("user"):
            st.markdown(message)
    else:
        with st.chat_message("assistant"):
            placeholder = st.empty()
            full_text = ""


        # Streaming effect
        for char in message:
            full_text += char
            placeholder.code(full_text)
            time.sleep(0.002)