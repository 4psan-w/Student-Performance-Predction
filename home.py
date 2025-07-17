import streamlit as st
from streamlit.components.v1 import html

# 🌟 App config
st.set_page_config(page_title="Student Performance App", page_icon="🎓", layout="centered")

# --- Help sidebar toggle ---
def show_help():
    with st.sidebar:
        st.header("🆘 Need Help?")
        st.markdown("""
        - **Are You A Student?**: Select Yes or No to start.
        - **If Yes**: Enter your name and choose what you want to do.
        - **Check My Performance Index**: Predict your performance based on your inputs.
        - **Navigate the Dataset**: Explore the student dataset with visuals.
        - **If No**: You can still explore the dataset or just browse around.
        """)
        st.markdown("---")
        st.markdown("""
        <p style = "text-align: center ; ">An Estimation Model Made by two classmates </p>   
        <p style = "text-align: center ; ">Inorder To learn Through Real Life Problem Solving</p>          
    <p style="font-size:10px; text-align:center; color:gray;">
        Linear Regression Model | Streamlit | Machine Learning <br>
        Made by 
        <a href="https://github.com/ritesh0614" target="_blank" style="text-decoration:none; color:#1f77b4;">Ritesh Khatri</a> &amp; 
        <a href="https://github.com/4psan-w" target="_blank" style="text-decoration:none; color:#1f77b4;">Apsan Karki</a>
    </p>
""", unsafe_allow_html=True)


# Button to toggle help sidebar
if st.button("Info"):
    show_help()

# 🌟 Title
st.markdown("<h1 style='text-align: center;'>🎓 Are You A Student?</h1>", unsafe_allow_html=True)

# Bored option toggle
# bored = st.checkbox("😴 Bored? Play some music!")

# if bored:
#     # Embed the song "About You" by The 1975 (YouTube embed)
#     st.markdown("""
#     <iframe width="100%" height="80" src="https://www.youtube.com/embed/nQQzC7Ld2N8?autoplay=1&loop=1&playlist=nQQzC7Ld2N8" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
#     """, unsafe_allow_html=True)

# 👇 Ask if the user is a student
if_student = st.radio(label="Select one:", options=["No", "Yes"], horizontal=True)

# 👉 If user is a student
if if_student == 'Yes':
    st.markdown("### 😊 That's great to hear!")
    name = st.text_input("👉 Please enter your name:")
    if name:
        st.session_state['username'] = name
    if name.strip():
        st.markdown(f"---\n### 👋 Welcome, **{name}**! What would you like to do?")
        
        actions = [
            "",
            "🔍 Just Checking Around",
            "📊 Check My Performance Index",
            "📁 Navigate the Dataset"
        ]
        
        act = st.selectbox("👇 Choose your action:", options=actions, index=0, placeholder="Select an option")

        # Handle actions
        if act:
            match act:
                case "🔍 Just Checking Around":
                    st.success("✨ No worries! Feel free to explore. Let me know if you need help.")

                case "📊 Check My Performance Index":
                    st.info("🚀 Redirecting to performance check page...")
                    st.switch_page("pages/performance_check.py")
                
                case "📁 Navigate the Dataset":
                    st.info("📂 Loading dataset exploration page...")
                    st.switch_page("pages/navigate_dataset.py")
                
                case _:
                    st.warning("⚠️ Invalid Action. Please select a valid option.")

# 👉 If user is NOT a student
else:
    st.markdown("💡 This application is mainly for students to check and analyze their performance using machine learning.")
    st.info("Not a student? You can still explore the dataset if you're curious!")

    st.markdown("---")
    st.markdown("### 🌐 Explore the Dataset")
    st.write("Click below to navigate through the student dataset.")
    
    if st.button("📁 Go to Dataset Navigator"):
        st.switch_page("pages/navigate_dataset.py")
