from flask import Flask, send_file

app = Flask(__name__)
app.config["FILES"] = "/static/"
@app.route("/")
def index():
    return "Hello World!"

@app.route("/udp")
def udp():
    path = "/home/runner/jscoee/static/udp.zip"
    return send_file(path, as_attachment=True)

@app.route("/tcp")
def tcp():
    path = "/home/runner/jscoee/static/tcp.zip"
    return send_file(path, as_attachment=True)

@app.route("/election")
def election():
    path = "/home/runner/jscoee/static/election.zip"
    return send_file(path, as_attachment=True)

@app.route("/mpi")
def mpi():
    path = "/home/runner/jscoee/static/mpi.zip"
    return send_file(path, as_attachment=True)

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)