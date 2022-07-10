from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'spoilers'

@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 1
    else:
        session['count'] += 1
    return render_template("index.html")

@app.route('/add_two', methods=['GET'])
def incremnt_two():
    session['count'] += 1 #this is a plus one because when we redirect it also adds one in the index method
    return redirect('/')

@app.route('/destroy_session', methods=['GET'])
def destroy_session():
    session.clear()
    return redirect('/')

if __name__ =="__main__":
    app.run(debug=True) 