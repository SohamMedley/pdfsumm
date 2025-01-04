# PDF Summarizer & Q&A Chatbot

![Logo](https://via.placeholder.com/150)

## Overview

The PDF Summarizer & Q&A Chatbot is a powerful tool that extracts text from PDF files, summarizes the content, and answers questions based on the extracted text. This project leverages advanced NLP models to provide accurate and concise summaries and answers.

## Features

- **PDF Text Extraction**: Extracts text from PDF files using `pdfplumber`.
- **Text Summarization**: Summarizes the extracted text using the LED model.
- **Question Answering**: Answers questions based on the extracted text using a fine-tuned BERT model.
- **Streamlit Interface**: User-friendly web interface for uploading PDFs, viewing extracted text, and interacting with the summarizer and chatbot.

## Demo

![Demo](https://via.placeholder.com/800x400)

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Step-by-Step Guide

1. **Clone the Repository**

    ```sh
    git clone https://github.com/yourusername/pdf-summarizer-chatbot.git
    cd pdf-summarizer-chatbot
    ```

2. **Create a Virtual Environment**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**

    ```sh
    pip install -r requirements.txt
    ```

4. **Run the Application**

    ```sh
    streamlit run app.py
    ```

## Usage

1. **Upload a PDF File**

    - Click on the "Upload a PDF file" button.
    - Select a PDF file from your local machine.

2. **View Extracted Text**

    - The extracted text from the PDF will be displayed in the "Extracted Text" section.

3. **Summarize Text**

    - Click on the "Summarize" button to generate a summary of the extracted text.
    - The summary will be displayed in the "Summary" section.

4. **Ask Questions**

    - Enter a question in the text input field under "Ask Questions About the PDF".
    - The answer will be displayed in the "Answer" section.

## Project Structure

```
pdf-summarizer-chatbot/
├── app.py
├── pdf_extractor.py
├── summarizer.py
├── QA_chatbot.py
├── text_cleaner.py
├── requirements.txt
└── README.md
```

## Models Used

- **Text Summarization**: [allenai/led-base-16384](https://huggingface.co/allenai/led-base-16384)
- **Question Answering**: [bert-large-uncased-whole-word-masking-finetuned-squad](https://huggingface.co/bert-large-uncased-whole-word-masking-finetuned-squad)

## Custom CSS

The application includes custom CSS for a better user experience. The styles are defined in the `app.py` file.

```css
<style>
    .main {
        background-color: #e6f0ff; /* Light Blue */
    }
    .stTextInput > div > div > input {
        border: 2px solid #004080; /* Dark Blue */
    }
    .stButton>button {
        background-color: #004080; /* Dark Blue */
        color: white;
        border-radius: 5px;
        border: 2px solid #004080; /* Dark Blue */
    }
    .stButton>button:hover {
        background-color: #003366; /* Darker Blue */
        border: 2px solid #003366; /* Darker Blue */
    }
    .header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        background-color: #b3d9ff; /* Light Blue Background for header */
        padding: 10px;
        border-radius: 5px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }
    .logo {
        width: 100px;
    }
</style>
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Hugging Face](https://huggingface.co/) for providing the pre-trained models.
- [Streamlit](https://streamlit.io/) for the easy-to-use web application framework.
- [pdfplumber](https://github.com/jsvine/pdfplumber) for the PDF text extraction library.

## Contact

For any questions or suggestions, please contact [yourname@example.com](mailto:yourname@example.com).
