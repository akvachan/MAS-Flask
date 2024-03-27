from flask import Flask, render_template, request
import tf_model

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        text = request.form['abstractText']

        sentences = tf_model.sentences(text)
        predictions = tf_model.predict(sentences, model)
        struct_sents = tf_model.structure_sentences(sentences, predictions)

        return render_template('index.html', segmented_abstract=struct_sents, original_text=text)
    else:
        return render_template('index.html', segmented_abstract=None, original_text="")

if __name__ == '__main__':
    model_url = 'https://drive.google.com/uc?export=download&id=1PUVyn7eSzAmtMF36mNHRPRFA0JVgAWY2'
    model_path = 'poseidon_lstm'
    tf_model.download_and_extract_model(model_url, model_path)
    model = tf_model.load_tf_model(model_path)
    app.run(port=os.getenv("PORT", default=5000), debug=True)
