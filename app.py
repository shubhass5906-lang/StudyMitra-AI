import streamlit as st
from google import genai

# -----------------------------
# Gemini Setup
# -----------------------------

api_key = st.secrets["GEMINI_API_KEY"]

client = genai.Client(api_key=api_key)

if not api_key:
    st.error("Gemini API key not found. Please configure your .env file.")
    st.stop()

client = genai.Client(api_key=api_key)

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="StudyMitra AI",
    page_icon="🎓",
    layout="wide"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>
.main-title {
    font-size: 42px;
    font-weight: 700;
    text-align: center;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    margin-bottom: 30px;
}

.info-box {
    padding: 20px;
    border-radius: 12px;
    background-color: #f0f2f6;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------
st.markdown(
    '<div class="main-title">🎓 StudyMitra AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Your personal AI study partner powered by Google Gemini</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="info-box">
    Enter any topic and StudyMitra AI will create a personalized
    learning session with explanations, examples, practice questions,
    quizzes, and revision notes.
    </div>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Topic Input
# -----------------------------
topic = st.text_input(
    "📚 Enter a topic",
    placeholder="Example: Python loops, DBMS, Photosynthesis, Machine Learning..."
)

# -----------------------------
# Generate
# -----------------------------
if st.button("🚀 Start Learning", type="primary", use_container_width=True):

    if not topic.strip():
        st.warning("Please enter a topic first.")

    else:

        prompt = f"""
You are StudyMitra AI, a friendly AI tutor.

Create a beginner-friendly learning session about:
{topic}

Use exactly these sections:

## Simple Explanation
Explain clearly using simple language.

## Real-Life Example
Give one relatable example.

## Technical Example
Give a simple technical or programming example when relevant.

## Key Points
Give 5 important points.

## Practice Questions
Give 5 questions from easy to medium difficulty.

## Quick Quiz
Give 3 multiple-choice questions with four options each.
Give the correct answers at the end.

## Quick Revision
Give a concise revision summary.

Make the content educational, accurate, and easy for a college student to understand.
"""

        with st.spinner("🤖 Gemini is preparing your learning session..."):

            try:

                response = client.models.generate_content(
                    model="gemini-3.5-flash-lite",
                    contents=prompt
                )

                st.success("✅ Learning session ready!")

                # Display result
                st.markdown(response.text)

                # Download option
                st.download_button(
                    "📥 Download Study Notes",
                    response.text,
                    file_name=f"{topic.replace(' ', '_')}_StudyMitra_Notes.txt",
                    mime="text/plain"
                )

            except Exception as e:

                st.error("Unable to generate the learning session.")

                st.info(
                    "Gemini may be temporarily busy. Please try again."
                )

# -----------------------------
# Footer
# -----------------------------
st.divider()

st.markdown(
    """
    <div style="text-align:center;">
    <b>StudyMitra AI</b><br>
    Powered by Google Gemini<br>
    Built for Campulsy Hack Days 2026
    </div>
    """,
    unsafe_allow_html=True
)