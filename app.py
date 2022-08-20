from flask import Flask
from flask import render_template, request

app = Flask(__name__)

def calc(credit, percent, attended, held, compensated, cancelled):
    hours=0
    if(credit==5):
        hours=105
    else:
        hours = 75
    x = int(round((1 - percent/100)*(hours - cancelled)) - held + attended + compensated)
    return x

@app.route("/", methods=['GET', 'POST'])
def home():
    x=0
    percent = 0
    if request.method == 'POST':
        if(type(request.form.get('credits')) is str):
            credit = int(request.form.get('credits'))
        else:
            credit = 4

        if(request.form.get('t_sessions')!=""):
            t_sessions = int(request.form.get('t_sessions'))
        else:
            t_sessions = 0

        if(request.form.get('sessions')!=""):
            sessions = int(request.form.get('sessions'))
        else:
            sessions = 0

        if(request.form.get('percentage')!=""):
            criteria = int(request.form.get('percentage'))
        else:
            criteria = 80

        if(request.form.get('compensated')!="" ):
            compensated = int(request.form.get('compensated'))
        else:
            compensated = 0
        
        if(request.form.get('cancelled')!="" ):
            cancelled = int(request.form.get('cancelled'))
        else:
            cancelled = 0

        print(credit, criteria, sessions, t_sessions, compensated, cancelled)
        x = calc(credit, criteria, sessions, t_sessions, compensated, cancelled)
        if(t_sessions!=0):
            percent = int(((sessions+compensated)/t_sessions) * 100)
    return render_template("home.html", x=x, percent = percent)
