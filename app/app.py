from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

SHIPMENTS = [
    {
        "id": "IA1001",
        "customer": "Acme Retail",
        "origin": "Manchester",
        "destination": "Liverpool",
        "status": "In Transit"
    },
    {
        "id": "IA1002",
        "customer": "NorthWest Supplies",
        "origin": "Birmingham",
        "destination": "Leeds",
        "status": "Delivered"
    },
    {
        "id": "IA1003",
        "customer": "City Wholesale",
        "origin": "Glasgow",
        "destination": "Bristol",
        "status": "Pending Dispatch"
    }
]


@app.route("/")
def home():
    return render_template("index.html", shipments=SHIPMENTS)


@app.route("/shipment")
def shipment_lookup():
    shipment_id = request.args.get("id")
    shipment = next((s for s in SHIPMENTS if s["id"] == shipment_id), None)
    return render_template("shipment.html", shipment=shipment, shipment_id=shipment_id)


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


@app.route("/version")
def version():
    return jsonify({"version": "1.0.0"}), 200


@app.route("/api/shipments")
def get_shipments():
    return jsonify({"shipments": SHIPMENTS}), 200


@app.route("/api/shipments/<shipment_id>")
def get_shipment(shipment_id):
    shipment = next((s for s in SHIPMENTS if s["id"] == shipment_id), None)

    if shipment:
        return jsonify(shipment), 200

    return jsonify({"error": "Shipment not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)