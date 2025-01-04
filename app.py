import streamlit as st
from summarizer import summarize_text
from pdf_extractor import extract_text_from_pdf
from text_cleaner import clean_text
from QA_chatbot import ask_question
import base64
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Set page title and icon
st.set_page_config(
    page_title="PDF Summarizer & Q&A Chatbot",
    page_icon="📚",
    layout="centered"
)

# Function to load and encode the logo
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Path to the logo
logo_path = "8943377.png"
logo_base64 = get_base64_of_bin_file(logo_path)

# Custom CSS with premium styling
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
        
        /* Global styles */
        * {
            font-family: 'Inter', sans-serif;
        }
        
        .main {
            background: linear-gradient(135deg, #f8fafc, #f1f5f9);
            padding: 2rem;
        }
        
        /* Header styles */
        .header {
            background: white;
            border-radius: 1rem;
            padding: 1.5rem 2rem;
            margin-bottom: 2rem;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        
        .header h2 {
            color: #1e293b;
            font-weight: 600;
            font-size: 1.5rem;
            margin: 0;
        }
        
        .logo {
            width: 80px;
            height: auto;
        }
        
        /* Input fields */
        .stTextInput > div > div > input {
            border: 1px solid #e2e8f0;
            border-radius: 0.75rem;
            padding: 0.75rem 1rem;
            font-size: 1rem;
            transition: all 0.2s;
        }
        
        .stTextInput > div > div > input:focus {
            border-color: #3b82f6;
            box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
        }
        
        /* Buttons */
        .stButton > button {
            background: linear-gradient(135deg, #3b82f6, #2563eb);
            color: white;
            border: none;
            padding: 0.75rem 1.5rem;
            border-radius: 0.75rem;
            font-weight: 500;
            transition: all 0.2s;
            box-shadow: 0 4px 6px -1px rgba(59, 130, 246, 0.2);
        }
        
        .stButton > button:hover {
            transform: translateY(-1px);
            box-shadow: 0 6px 8px -1px rgba(59, 130, 246, 0.3);
        }
        
        /* Text areas */
        .stTextArea > div > div > textarea {
            border: 1px solid #e2e8f0;
            border-radius: 0.75rem;
            padding: 1rem;
            font-size: 1rem;
            background: white;
        }
        
        /* Success/Info messages */
        .element-container div[data-testid="stMarkdownContainer"] > div {
            padding: 1rem;
            border-radius: 0.75rem;
            margin: 1rem 0;
        }
        
        .stSuccess {
            background: #f0fdf4;
            border: 1px solid #86efac;
            color: #166534;
        }
        
        .stInfo {
            background: #eff6ff;
            border: 1px solid #93c5fd;
            color: #1e40af;
        }
        
        /* Subheaders */
        .stMarkdown h3 {
            color: #1e293b;
            font-weight: 600;
            margin: 1.5rem 0 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# App header with logo
st.markdown(f"""
    <div class="header">
        <h2>PDF Text Summarization and Q&A Chatbot</h2>
        <img src="data:image/png;base64,{logo_base64}" class="logo" alt="Logo">
    </div>
""", unsafe_allow_html=True)

# File uploader with custom styling
st.markdown("""
    <h3>Upload Your Document</h3>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader("", type=["pdf"])  # Empty label as we use custom header above

if uploaded_file is not None:
    try:
        raw_text = extract_text_from_pdf(uploaded_file)
        cleaned_text = clean_text(raw_text)
        
        st.markdown("<h3>Extracted Text</h3>", unsafe_allow_html=True)
        st.text_area("", cleaned_text, height=300)  # Empty label as we use custom header above
        
        # Summarization section
        if st.button("Generate Summary"):
            summary = summarize_text(cleaned_text)
            st.markdown("<h3>Summary</h3>", unsafe_allow_html=True)
            st.markdown(f"""
                <div class="stSuccess">
                    {summary}
                </div>
            """, unsafe_allow_html=True)
        
        # Q&A section
        st.markdown("<h3>Ask Questions About the PDF</h3>", unsafe_allow_html=True)
        question = st.text_input("", placeholder="Type your question here...")  # Empty label for custom styling
        if question:
            answer = ask_question(question, cleaned_text)
            st.markdown("<h3>Answer</h3>", unsafe_allow_html=True)
            st.markdown(f"""
                <div class="stInfo">
                    {answer}
                </div>
            """, unsafe_allow_html=True)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        st.error(f"An error occurred: {e}")
