from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('musicpremium.html')

@app.route("/official-hige-dandism")
def official_hige_dandism():
    return render_template('official_hige_dandism.html')

@app.route("/beenzino")
def beenzino():
    return render_template('beenzino.html')

@app.route("/changmo")
def changmo():
    return render_template('changmo.html')

@app.route("/vaundy")
def vaundy():
    return render_template('vaundy.html')

if __name__ == "__main__":
    app.run(debug=True, port=80)
