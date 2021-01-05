from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
    {
        "name": "My Gorgeous Store",
        "items": [
            {
                "name": "Apple",
                "price": 1.99
            }
        ]
    }
]


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/store/<string:name>", methods=['GET'])
def get_store(name):
    for store in stores:
        if name == store["name"]:
            return jsonify(store)
    return jsonify({"massage": f"Store {name} is not found"})


@app.route("/store", methods=['GET'])
def list_store():
    return jsonify(stores)


@app.route("/store", methods=['POST'])
def create_store():
    json_data = request.get_json()
    new_store = {
        "name": json_data["name"],
        "items": []
    }
    stores.append(new_store)
    return jsonify(new_store)


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item(name):
    json_data = request.get_json()
    for store in stores:
        if name == store["name"]:
            new_item = {"name": json_data["name"], "price": json_data["price"]}
            store["items"].append(new_item)
            return jsonify(new_item)
    return jsonify({"message": f"Store {name} is not found"})


if __name__ == '__main__':
    app.run(port=5000)
