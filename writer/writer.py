from flask import Flask
import os

app = Flask(__name__)

DATA_FILE = "/shared/data.txt"

@app.route("/")
def write_data():
    with open(DATA_FILE, "a") as f:
        f.write("New line from writer service\n")
    return "Data written!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
