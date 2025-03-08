import os
import fitz  # PyMuPDF
from flask import Flask, request, render_template
import openai
from dotenv import load_dotenv
from fuzzywuzzy import fuzz  

load_dotenv()

app = Flask(__name__)

openai.api_key = os.getenv('OPENAI_API_KEY')

def extract_text_from_pdf_folder(folder_path):
    text_dict = {}
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            pdf_file_path = os.path.join(folder_path, filename)
            document = fitz.open(pdf_file_path)
            text = ""
            for page in document:
                text += page.get_text() + "\n"
            text_dict[filename] = text.strip()  
            document.close()
    return text_dict

def retrieve_relevant_context(question, text_dict):
    relevant_context = ""
    question = question.lower()  
    
    for filename, content in text_dict.items():
        if fuzz.partial_ratio(question, content.lower()) > 70:  # 相似度閾值
            relevant_context += f"From {filename}:\n{content}\n\n"
    
    return relevant_context

def get_answer_from_ai(question, context=None):
    prompt = "你是一個善於使用linux系統的大師，請根據以下內容精簡地回答問題的答案就好。"
    
    if context:
        completion=openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": f"{context}\n\n{question}"}
            ],
            max_tokens=128  
        )
        return completion.choices[0].message.content, True  
    else:
        completion=openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": question}
            ],
            max_tokens=128  
        )
        return completion.choices[0].message.content, False  

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        question = request.form['question']
        
        text_dict = extract_text_from_pdf_folder('rag')
        
        context = retrieve_relevant_context(question, text_dict)
        
        answer, from_ppt = get_answer_from_ai(question, context)
        
        return render_template('index.html', answer=answer, from_ppt=from_ppt)
    
    return render_template('index.html', answer=None, from_ppt=None)

if __name__ == '__main__':
    app.run(debug=True)