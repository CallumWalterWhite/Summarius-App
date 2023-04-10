from flask import Flask, render_template, request
from summarius import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        file_path = "uploads/" + file.filename
        file.save(file_path)
        upload_file(file_path)
        return 'File uploaded successfully'

@app.route('/process_text', methods=['POST'])
def process_text():
    user_input = request.form['user_input']
    summary = get_summary(user_input)
    response_text = f"Summary: {summary}"
    return response_text

if __name__ == '__main__':
    app.run(debug=True)