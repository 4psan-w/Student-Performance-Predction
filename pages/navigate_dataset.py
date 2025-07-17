import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class ExploreDataset:
    def __init__(self):
        self.file = None
        self.df = None
        self.default_file = "./dataset/Student_Performance (1).csv"  # Change path as per your file

        # Load default dataset ONCE here
        try:
            self.default_df = pd.read_csv(self.default_file)
        except Exception as e:
            self.default_df = None
            st.error(f"❌ Failed to load default dataset: {e}")

        self.intro()

    def intro(self):
        st.set_page_config(page_title="Explore Dataset", page_icon="📊", layout="wide")
        st.title("🚀 Navigate or Explore the Dataset")
        st.subheader("Gain insights, analyze patterns, and discover the story behind the numbers!")

        st.markdown("""
        <div style='padding: 15px; border-radius: 10px; border-left: 6px solid #4A90E2;'>
            <h4>📌 What you can do here:</h4>
            <ul>
                <li>🔍 Browse through different datasets</li>
                <li>📈 Explore visualizations</li>
                <li>📊 Analyze statistics & trends</li>
                <li>🧠 Prepare data for machine learning</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### 🧭 Choose how you'd like to load your dataset:")
        self.load_file()

    def load_file(self):
        expected_cols = list(self.default_df.columns.str.strip()) if self.default_df is not None else []

        file_method = st.radio("How would you like to proceed?", ["Upload Your Own CSV", "Use Default Dataset"])

        if file_method == "Upload Your Own CSV":
            uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

            if uploaded_file is not None:
                if uploaded_file.name.endswith('.csv'):
                    try:
                        uploaded_df = pd.read_csv(uploaded_file)

                        uploaded_cols = set(uploaded_df.columns.str.strip())
                        expected_cols_set = set(expected_cols)

                        missing_cols = expected_cols_set - uploaded_cols
                        extra_cols = uploaded_cols - expected_cols_set

                        if missing_cols or extra_cols:
                            st.warning("⚠️ Column mismatch detected!")
                            if missing_cols:
                                st.warning(f"Missing columns: {', '.join(missing_cols)}")
                            if extra_cols:
                                st.warning(f"Extra columns: {', '.join(extra_cols)}")
                            st.info("Please upload a CSV with columns matching the default dataset.")
                        else:
                            self.df = uploaded_df
                            st.success("✅ File uploaded successfully and columns matched!")
                            self.show_data()

                    except Exception as e:
                        st.error(f"❌ Error reading the uploaded file: {e}")

                else:
                    st.error("❌ Please upload a valid CSV file.")
        else:
            if self.default_df is not None:
                self.df = self.default_df.copy()
                st.success("📄 Default dataset loaded.")
                self.show_data()
            else:
                st.error("❌ Default dataset not available.")

    def show_data(self):
        if self.df is not None:
            st.markdown("### 📌 Dataset Preview")
            st.dataframe(self.df.head(50), use_container_width=True)

            st.markdown("### 📊 Basic Statistics")
            st.dataframe(self.df.describe().T)

            st.markdown("### 📈 Visual Insights")

            if st.checkbox("📉 Show Distribution Plots"):
                num_cols = self.df.select_dtypes(include=['int64', 'float64']).columns
                for col in num_cols:
                    st.markdown(f"**Distribution for `{col}`**")
                    fig, ax = plt.subplots()
                    sns.histplot(self.df[col], kde=True, ax=ax, color='teal')
                    st.pyplot(fig)

            if st.checkbox("📊 Show Bar Plots for Categorical Columns"):
                cat_cols = self.df.select_dtypes(include=['object']).columns
                for col in cat_cols:
                    st.markdown(f"**Bar plot for `{col}`**")
                    fig, ax = plt.subplots()
                    self.df[col].value_counts().plot(kind='bar', ax=ax, color='coral')
                    st.pyplot(fig)

            if st.checkbox("🔗 Show Correlation Heatmap"):
                num_cols = self.df.select_dtypes(include=['int64', 'float64']).columns
                if len(num_cols) >= 2:
                    fig, ax = plt.subplots(figsize=(10, 6))
                    sns.heatmap(self.df[num_cols].corr(), annot=True, cmap="coolwarm", ax=ax)
                    st.pyplot(fig)
                else:
                    st.warning("Not enough numerical columns to generate a correlation matrix.")

            if st.checkbox("🧠 Show Pie Chart (for 1 Categorical Column)"):
                cat_cols = self.df.select_dtypes(include=['object']).columns
                if len(cat_cols) > 0:
                    selected = st.selectbox("Select categorical column:", cat_cols)
                    fig, ax = plt.subplots()
                    self.df[selected].value_counts().plot.pie(autopct='%1.1f%%', ax=ax, figsize=(6,6))
                    ax.set_ylabel("")
                    st.pyplot(fig)
                else:
                    st.warning("No categorical column found.")


if __name__ == "__main__":
    ExploreDataset()
