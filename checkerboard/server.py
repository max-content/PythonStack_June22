from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
@app.route('/<int:x>')
@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def index(x=6,y=6,color1='purple',color2='blue'):
    return render_template("checkerboard.html", x=x,y=y,color1=color1, color2=color2)
#def checkerboard4(x=8, y=8, color1='red', color2='blue'):
#     output = []
#     for i in range(0, x):
#         temp = []
#         for j in range(0, y):
#             temp.append((i +j) %2)
#         output.append(temp)
#     return render_template("checkerboard.html", output = output, color1 = color1, color2 = color2)
@app.route('/<int:x>/<int:y>')
def myversion(x,y,color1='purple',color2='blue'):
    print("did we get here")
    return render_template("checkerboard.html", x=x,y=y,color1=color1,color2=color2)

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def colorpicker(x,y,color1='purple',color2='blue'):
    print("did we get here")
    return render_template("checkerboard.html", x=x,y=y,color1=color1, color2=color2)

if __name__ == "__main__":
    app.run(debug=True)