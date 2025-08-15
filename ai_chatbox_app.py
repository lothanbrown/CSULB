import requests
import streamlit as st

# AI Chatbox for Azure Foundry Agent via Logic App REST API
def show_ai_chatbox():
    with st.sidebar:
        st.markdown(
            '''
            <style>
            .main {
                background-color: #f8fafc;
            }
            .stButton>button {
                background-color: #2563eb;
                color: white;
                border-radius: 6px;
                padding: 0.5em 1.5em;
                font-weight: 600;
                border: none;
                transition: background 0.2s;
            }
            .stButton>button:hover {
                background-color: #1e40af;
                color: #fff;
            }
            .stSidebar {
                background-color: #e0e7ef;
            }
            .css-1d391kg {  /* Chatbox header */
                font-size: 1.2em;
                font-weight: bold;
                color: #2563eb;
            }
            .css-1cpxqw2 {  /* Chat messages */
                border-radius: 8px;
                padding: 0.5em 1em;
                margin-bottom: 0.5em;
            }
            </style>
            ''',
            unsafe_allow_html=True
        )
        st.markdown("## 💬 AI Tutor")
        if "chat_history" not in st.session_state:
            st.session_state["chat_history"] = []

        for sender, msg in st.session_state["chat_history"]:
            if sender == "user":
                st.markdown(f"<div style='text-align:right; color:#1a73e8;'><b>You:</b> {msg}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div style='text-align:left; color:#444;'><b>AI:</b> {msg}</div>", unsafe_allow_html=True)

        user_input = st.text_input("Type your message...", key="user_input_sidebar")
        if st.button("Send", key="send_btn_sidebar") and user_input:
            st.session_state["chat_history"].append(("user", user_input))

            # --- Azure Logic App REST API call ---
            endpoint = "https://YOUR_LOGIC_APP_ENDPOINT_URL"  # TODO: Replace with your Logic App endpoint
            headers = {
                # "Authorization": "Bearer YOUR_API_KEY",  # Uncomment and set if needed
                "Content-Type": "application/json"
            }
            payload = {"message": user_input}
            try:
                response = requests.post(endpoint, json=payload, headers=headers, timeout=30)
                response.raise_for_status()
                ai_reply = response.json().get("reply", "[No reply received]")
            except Exception as e:
                ai_reply = f"[Error: {e}]"
            st.session_state["chat_history"].append(("ai", ai_reply))