# Put, Delete

from flask import Flask, request, jsonify

app = Flask(__name__)

items = [
    {"id": 1, "name": "This is Item 1", "description": "Description Itme1"},
    {"id": 2, "name": "This is Item 2", "description": "Description Itme2"},
]


@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(items)


@app.route("/items/<int:item_id>", methods=["GET"])
def get_specific_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"Error": "No Such Item Found"})
    return jsonify(item)


@app.route("/items", methods=["POST"])
def create():
    if not request.json or not "name" in request.json:
        return jsonify({"Error": "No Name Given or Data Not in Json Format"})
    new_item = {
        "id": items[-1]["id"] + 1 if items else 1,
        "name": request.json["name"],
        "description": request.json["description"],
    }
    items.append(new_item)
    return jsonify(new_item)


@app.route("/items/<int:item_id>", methods=["PUT"])
def update(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"Error": "No Such Item Exists For Updation"})
    item["name"] = request.json.get("name", item["name"])
    item["description"] = request.json.get("description", item["description"])
    return jsonify(item)


@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return jsonify(items)


if __name__ == "__main__":
    app.run(debug=True)
