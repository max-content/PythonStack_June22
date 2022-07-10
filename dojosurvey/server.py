from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)

@app.route('/test')
def test():
    return "Sup Nerd"

@app.route('/')
def index():
    return render_template('index.html')

app.route('/results', methods='GET')
def form_results():
    return render_template('results.html')

# @app.route('/process', methods='POST')
def process_form():
    pass

app.run(debug=True)
if __name__ == "__main__":
    app.run(debug=True)