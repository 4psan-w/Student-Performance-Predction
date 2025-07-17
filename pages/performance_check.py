import streamlit as st
import joblib
import numpy as np

@st.cache_resource
def load_model():
    model = joblib.load("./Model/Linear_reg_model.joblib")
    return model

model = load_model()

if 'username' in st.session_state:
    name = st.session_state['username']
else:
    name = None

st.title("🎓 What's Your Student Swagger? Let's Predict Your Performance! 🚀")

if name:
    st.write(f"Hey **{name}**, ready to see how you're doing on the grind? Answer these questions below:")

    hours_per_week = st.slider("⏰ How many hours you been grinding **per week**?", 0, 168, 20)  # max 24*7=168 hours
    avg_per_day = hours_per_week / 7
    hours_studied = avg_per_day
    st.write(f"🗓️ That’s about **{avg_per_day:.2f} hours per day** on average.")

    previous_scores = st.number_input("📚 What was your average previous score? (0 - 100)", 0, 100, 75)
    extracurricular = st.number_input("🎨 How many extracurricular activities you rockin’?", 0, 20, 3)

    sleep_hours = st.slider("💤 How many hours of sleep do you catch on average?", 0, 14, 7)

    if sleep_hours < 5:
        st.warning("⚠️ You’re **sleep deprived** — try to get more rest!")
    elif 5 <= sleep_hours <= 7:
        st.info("👍 You have a **moderate** amount of sleep — steady grind, nice!")
    elif 8 <= sleep_hours <= 10:
        st.success("💪 You’re **energized** with good sleep — keep it up!")
    else:
        st.error("😴 Whoa! You’re **LAZY** or maybe just really enjoying the bed, huh? Time to get moving!")

    sample_papers = st.number_input("📄 How many sample question papers did you practice?", 0, 50, 10)

    input_features = np.array([[hours_studied, previous_scores, extracurricular, sleep_hours, sample_papers]])

    if st.button("🔮 Predict My Performance!"):
        try:
            prediction = model.predict(input_features)
            score = prediction[0]

            st.success(f"🔥 {name}, your predicted Performance Index is: {score:.2f}!")

            if score >= 80:
                st.balloons()
                st.snow()
                st.snow()  # extra snow for hype
                st.markdown(
                    "<h2 style='color: #28a745; font-weight: bold;'>🎉 Amazing job! You're absolutely smashing it! Keep shining! 🌟</h2>",
                    unsafe_allow_html=True,
                )
            elif score >= 50:
                st.snow()
                st.markdown(
                    "<h3 style='color: #007bff; font-weight: bold;'>👏 Good going! Keep pushing, success is on its way! 💪</h3>",
                    unsafe_allow_html=True,
                )
            else:
                st.markdown(
                    "<h3 style='color: #dc3545; font-weight: bold;'>💪 Don't sweat it! Keep grinding and improving every day! You got this! 🔥</h3>",
                    unsafe_allow_html=True,
                )

        except Exception as e:
            st.error(f"⚠️ Oops, something went wrong with prediction: {e}")
else:
    st.write("Hey! Looks like we don't know your name yet. Please go back to the home page and enter your name first.")
