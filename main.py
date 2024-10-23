from flask import Flask, render_template, request, redirect, send_from_directory
import socketio
import eventlet

app = Flask(__name__)
sio = socketio.Server(cors_allowed_origins='*', logger=False, max_http_buffer_size=5_000_000_000_000)


import firebase_management.firebase_manager
import k8_management.k8_manager

user_auth = firebase_management.firebase_manager.authentication()
k8_control = k8_management.k8_manager.manager()







@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup")
def index():
    uid = user_auth.create_user("test@test.net", "test1", "test", "fafds123!")
    k8_control.create_namespace(uid)

@app.route("/login")
def index():
    return render_template("login.html")

@app.route("/logout")
def index():
    return render_template("logout.html")




@app.route("/signup", methods=['POST'])
def index():
    return render_template("signup.html")

@app.route("/login", methods=['POST'])
def index():
    return render_template("login.html")

@app.route("/logout", methods=['POST'])
def index():
    return render_template("logout.html")






#@app.route('/get_payloads/<path:filename>')
#def get_payloads(filename):
#    return send_from_directory('payloads', filename, as_attachment=True)


if __name__ == "__main__":
    flaskApp = socketio.Middleware(sio, app)
    eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 5000)), flaskApp)