import streamlit as st
from logic import get_recommendation, get_followup_response

st.set_page_config(page_title="AI Supplement Recommender", page_icon="💬")


st_ui_css = """
<style>
    #MainMenu {
        visibility: hidden;
    }
    footer {
        visibility: hidden;
        }
    header {
        visibility: hidden; 
        height:0;
        }
    .block-container {
      margin-top: 25px;
      padding-top: 0;
    }
    .main-header {
        text-align: center;
        color: #2E86AB;
        padding: 1rem 0;
    }
    .user-info-box {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .recommendation-box {
        background-color: #e8f4fd;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #2E86AB;
    }
    
</style>
"""

st.markdown(st_ui_css, unsafe_allow_html=True)


st.write("## 💊 AI Supplement Recommender")
st.caption("Get personalized supplement suggestions based on your health goals.")

# User info
with st.sidebar:

    st.write("### 👤 Your Information")

    user_name = st.text_input("Name", placeholder="Enter your name")

    age = st.selectbox("Age Group", [
        "18-25", "26-35", "36-45", "46-55", "56-65", "65+"
    ])

    gender = st.selectbox("Gender", ["Male", "Female", "Other"])

    health_goal = st.selectbox("Health Goal", [
        "Muscle Gain & Strength",
        "Weight Loss & Fat Burning",
        "Immune System Support",
        "Energy & Endurance"
    ])

    st.write("# ")
    st.write("# ")
    st.write("# ")
    if st.button("🗑️ Clear Recommendations"):
        st.session_state.messages = []
        st.rerun()


if "messages" not in st.session_state:
    st.session_state.messages = []

if not st.session_state.messages:
    welcome_msg = "Hi! 👋 Please fill in your information above and click 'Get Recommendations' to receive personalized supplement suggestions."
    st.session_state.messages.append({"role": "assistant", "content": welcome_msg})

st.subheader("💬 Recommendations")
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        if msg["role"] == "assistant" and "recommendation" in msg.get("type", ""):
            st.markdown(f'<div class="recommendation-box">{msg["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(msg["content"])

if st.button("🔍 Get Personalized Recommendations", type="primary", use_container_width=True):
    if user_name and age and gender and health_goal:
        user_profile = {
            "name": user_name,
            "age": age,
            "gender": gender,
            "health_goal": health_goal
        }

        st.session_state.current_user_profile = user_profile

        request_msg = f"**{user_name}** (Age: {age}, Gender: {gender}) is looking for supplements for: **{health_goal}**"
        st.session_state.messages.append({"role": "user", "content": request_msg})

        with st.chat_message("user"):
            st.markdown(request_msg)

        with st.chat_message("assistant"):
            with st.spinner("Analyzing your profile and generating personalized recommendations..."):
                response = get_recommendation(user_profile)
                st.markdown(f'<div class="recommendation-box">{response}</div>', unsafe_allow_html=True)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": response,
                    "type": "recommendation"
                })
    else:
        st.error("Please fill in all your information before getting recommendations.")

if st.session_state.messages and len(st.session_state.messages) > 1:

    # chat for follow-up questions
    followup_input = st.chat_input("Ask me anything about your recommendations...")

    if followup_input:
        st.session_state.messages.append({"role": "user", "content": followup_input})

        with st.chat_message("user"):
            st.markdown(followup_input)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                current_profile = st.session_state.get('current_user_profile', {
                    "name": user_name,
                    "age": age,
                    "gender": gender,
                    "health_goal": health_goal
                })

                response = get_followup_response(followup_input, st.session_state.messages, current_profile)
                st.markdown(response)

                st.session_state.messages.append({"role": "assistant", "content": response})

