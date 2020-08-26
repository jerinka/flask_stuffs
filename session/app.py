from flask import Flask, session
from flask_session import Session

app = Flask(__name__)
# Check Configuration section for more details
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)

@app.route('/')
def reset():
    session["counter"]=0
    print('session["counter"]',session["counter"])
    return "counter was reset"

@app.route('/inc')
def routeA():
    if not "counter" in session:
        session["counter"]=0

    session["counter"]+=1

    return "counter is {}".format(session["counter"])

@app.route('/dec')
def routeB():
    if not "counter" in session:
        session["counter"] = 0

    session["counter"] -= 1

    return "counter is {}".format(session["counter"])


if __name__ == '__main__':
    app.run()
