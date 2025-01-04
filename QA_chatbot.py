from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline
import re

# Cache the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("bert-large-uncased-whole-word-masking-finetuned-squad")
model = AutoModelForQuestionAnswering.from_pretrained("bert-large-uncased-whole-word-masking-finetuned-squad")

# Initialize the pipeline for question answering
qa_pipeline = pipeline("question-answering", model=model, tokenizer=tokenizer)

def preprocess_context(context):
    # Clean the context
    context = re.sub(r'\s+', ' ', context)
    context = context.strip()
    return context

def ask_question(question, context):
    context = preprocess_context(context)
    result = qa_pipeline(question=question, context=context)
    return result['answer']
