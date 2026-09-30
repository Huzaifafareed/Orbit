from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

spacecraft = {
    "mass": 50,
    "power": 100,
    "science": 0
}

components = {
    "camera": {
        "mass": 10,
        "power": 10,
        "science": 20
    },
    "radar": {
        "mass": 25,
        "power": 30,
        "science": 50
    },
    "spectrometer": {
        "mass": 15,
        "power": 20,
        "science": 35
    }
}


@app.route("/status", methods=["GET"])
def get_status():
    return jsonify(spacecraft)


@app.route("/add-component", methods=["POST"])
def add_component():

    data = request.json
    component_name = data["component"]

    if component_name not in components:
        return jsonify({"error": "Component does not exist"}), 400

    component = components[component_name]

    spacecraft["mass"] += component["mass"]
    spacecraft["power"] -= component["power"]
    spacecraft["science"] += component["science"]

    return jsonify(spacecraft)


if __name__ == "__main__":
    app.run(debug=True)