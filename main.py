import spacy
from spacy import displacy
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
NER = spacy.load("en_core_web_sm")

raw_text = "The Indian Space Research Organisation or is the national space agency of India, headquartered in Bengaluru. It operates under Department of Space which is directly overseen by the Prime Minister of India while Chairman of ISRO acts as executive of DOS as well."


@app.route('/', methods=["GET", "POST"])
def ner():
    if request.method == "POST":
        text1 = request.form.get("text")
        text2 = NER(text1)
        dict1 = dict()
        for word in text2.ents:
            new_key = word.text
            new_value = word.label_
            dict1[new_key] = new_value

        return dict1
    return render_template("form.html")


if __name__ == "__main__":
    app.run(debug=True)