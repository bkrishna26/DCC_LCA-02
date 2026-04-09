from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    crop = request.form['crop']
    soil = request.form['soil']

    if crop.lower() == "rice":
        suggestion = "Use nitrogen-rich fertilizer 🌱"
    elif crop.lower() == "wheat":
        suggestion = "Use phosphorus fertilizer 🌾"
    elif soil.lower() == "clay":
        suggestion = "Ensure proper drainage for clay soil"
    else:
        suggestion = "Use organic compost for best results"

    return render_template('index.html', result=suggestion)

if __name__ == '__main__':
    app.run(debug=True)