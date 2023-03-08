from flask import Flask, jsonify
import gdown

app = Flask(__name__)

@app.route('/')
def run_colab():
    gdown.download('https://drive.google.com/drive/folders/1xQFZ5IPjVvz1qMBZGchYWQ6qyxLKetLj', 'colab.ipynb', quiet=False)
    return jsonify(message='colab notebook ran successfully')
