from flask import Flask, render_template, session, request, redirect
import random
app = Flask(__name__)
app.secret_key = "P@ssw0rd"

@app.route("/")
def index():

    if 'totalGold' not in session:
        session['totalGold'] = int(0)
    if 'actLog' not in session:
        session['actLog'] = []
    if 'findGold' not in session:
        session['findGold'] = int(0)

    return render_template("index.html", totalGold = session['totalGold'], findGold = session['findGold'], actLog = session['actLog'])

@app.route("/process_money", methods=['POST','GET'])
def process():
    
    # if 'totalGold' not in session:
    #     session['totalGold'] = int(0)
    # if 'actLog' not in session:
    #     session['actLog'] = []
    # if 'findGold' not in session:
    #     session['findGold'] = int(0)

    try:
        session['totalGold'] = request.form('which_form')
        session['actLog'] = request.form('which_form')
        session['findGold'] = request.form('which_form')
    except:
        pass

    
    if request.form['which_form'] == 'farm':
        session['findGold'] = random.randint(10,20)
        session['totalGold'] += session['findGold']
    elif request.form['which_form'] == 'cave':
        session['findGold'] = random.randint(5,10)
        session['totalGold'] += session['findGold']
    elif request.form['which_form'] == 'house':
        session['findGold'] = random.randint(2,5)
        session['totalGold'] += session['findGold']
    elif request.form['which_form'] == 'casino':
        session['findGold'] = random.randint(-50,50)
        session['totalGold'] += session['findGold']
    
    if session['findGold'] < 0:
        session['actLog'].insert(0,f"<p class='lost'>Lost {session['findGold']} golds in the casino!</p>")
    else:
        session['actLog'].insert(0,f"<p class='earned'>Earned {session['findGold']} golds from the farm!</p>")

    # print(f"totalGold: {session['totalGold']} and farm gold : {session['findGold']} and act: {session['actLog']}")
    
    return redirect("/")

@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)