from flask import Flask, render_template, url_for


app = Flask(__name__)

@app.route("/")
def layout():
    return render_template('layout.html')

if __name__ == '__main__':
    app.run(debug=True)
