from flask import Flask

app = Flask(__name__)

DATA_FILE = "/shared/data.txt"

@app.route("/")
def read_data():
    try:
        with open(DATA_FILE, "r") as f:
            content = f.read()
    except:
        content = "No data yet"
    return content

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001)
