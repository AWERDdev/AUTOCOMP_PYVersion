import re
import os
from spellchecker import SpellChecker
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def WelcomeMessage():
    return "<h1>Welcome to the Word COMP PYAPI!</h1>"

@app.route('/word_counter')
def word_counter():
    print("Function called")
    data = request.args.get("data")  # Use request.args.get instead of request.get_json()
    
    if not data:
        return jsonify({"Message": "No data received!", "data": None}), 400

    class WordCounter:
        def count_words(self, text):
            """Returns the total number of words in the given text."""
            words = re.findall(r'\b\w+\b', text)  # Extract words
            word_count = {}
            for word in words:
                word_count[word] = word_count.get(word, 0) + 1  # Count occurrences of each word
            return word_count

    word_counter = WordCounter()
    countedWords = word_counter.count_words(data)
    
    print("Counted words:", countedWords)
    return jsonify({"Message": "Data received successfully", "data": countedWords})

@app.route('/text_corrector')
def text_corrector():
    print("Function called")
    data = request.args.get("text")  # Use request.args.get instead of request.get_json()
    
    if not data:
        return jsonify({"Message": "No text received!", "data": None}), 400

    class TextCorrector:
        def __init__(self):
            self.spellchecker = SpellChecker()

        def fix_typos(self, text):
            """Corrects typos in the given text."""
            words = text.split()  # Split input into words
            corrected_words = [self.spellchecker.correction(word) for word in words]
            return " ".join(corrected_words)  # Return corrected sentence

    spell_checker = TextCorrector()
    correctedText = spell_checker.fix_typos(data)
    
    print("Corrected text:", correctedText)
    return jsonify({"Message": "Data received successfully", "data": correctedText})

if __name__ == "__main__":
    app.run(debug=True)

