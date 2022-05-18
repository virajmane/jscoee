from flask import Flask, send_file

app = Flask(__name__)
app.config["FILES"] = "/static/"
@app.route("/")
def index():
    return """
<!DOCTYPE html>
<html>
<body>

<h1>Links</h1>

<p><a href="https://jscoee.herokuapp.com/tcp">https://jscoee.herokuapp.com/tcp</a></p>
<p><a href="https://jscoee.herokuapp.com/udp">https://jscoee.herokuapp.com/udp</a></p>
<p><a href="https://jscoee.herokuapp.com/election">https://jscoee.herokuapp.com/election</a></p>
<p><a href="https://jscoee.herokuapp.com/mpi">https://jscoee.herokuapp.com/mpi</a></p>



</body>
</html>

    """

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
