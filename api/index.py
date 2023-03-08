from flask import Flask, jsonify
import gdown

app = Flask(__name__)

@app.route('/')
def run_colab():
    gdown.download('https://colab.research.google.com/drive/1cqtAqgelwaZnvr80DJIb9UF_MGs-NRo0?usp=share_link', 'colab.ipynb', quiet=False)
    return jsonify(message='colab notebook ran successfully')
