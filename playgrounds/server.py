from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/play/<int:x>")
@app.route("/play/")
@app.route('/play/<int:x>/<color1>')
# def index(x=6,color1='purple'):
    
#     print(x)
#     return render_template("play.html", x=x,color1=color1)

def play(x=8, color1='red'):
    for i in range(0, x):
        return render_template("play.html", x = x, color1 = color1)


if __name__ == "__main__":
    app.run(debug=True)