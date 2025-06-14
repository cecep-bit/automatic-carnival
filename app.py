from flask import Flask, render_template, request
from deep_translator import GoogleTranslator
import pykakasi

app = Flask(__name__)
kks = pykakasi.kakasi()

def to_romaji(text):
    result = kks.convert(text)
    return " ".join([item['hepburn'] for item in result])

@app.route("/", methods=["GET", "POST"])
def translate():
    translation = None
    romaji = None
    original = None

    if request.method == "POST":
        original = request.form.get("text")
        japanese = GoogleTranslator(source="auto", target="ja").translate(original)
        romaji = to_romaji(japanese)
        translation = japanese

    return render_template("index.html", original=original, translation=translation, romaji=romaji)

if __name__ == "__main__":
    app.run(debug=True)
