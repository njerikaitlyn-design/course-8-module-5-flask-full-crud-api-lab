from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated data
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

# In-memory "database"
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]

# TODO: Task 1 - Define the Problem
# Create a new event from JSON input

@app.route("/events", methods=["GET"])
def get_events():
    return jsonify([event.to_dict() for event in events])

@app.route("/events", methods=["POST"])
def create_event():
    # TODO: Task 2 - Design and Develop the Code
    data = request.get_json()
    if not data or "title" not in data:
        return jsonify({"error": "Invalid input"}), 400

    # TODO: Task 3 - Implement the Loop and Process Each Element
    max_id = 0
    for event in events:
        if event.id > max_id:
            max_id = event.id
    new_id = max_id + 1
    new_event = Event(new_id, data["title"])
    events.append(new_event)

    # TODO: Task 4 - Return and Handle Results
    return jsonify(new_event.to_dict()), 201

# TODO: Task 1 - Define the Problem
# Update the title of an existing event
@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    # TODO: Task 2 - Design and Develop the Code
    data = request.get_json()
    if not data or "title" not in data:
        return jsonify({"error": "Invalid input"}), 400

    # TODO: Task 3 - Implement the Loop and Process Each Element
    Target_event = None
    for event in events:
        if event.id == event_id:
            Target_event = event
            break

    # TODO: Task 4 - Return and Handle Results
    if not Target_event:
        return jsonify({"error": "Event not found"}), 404

    Target_event.title = data["title"]
    return jsonify(Target_event.to_dict()), 200

# TODO: Task 1 - Define the Problem
# Remove an event from the list
@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    # TODO: Task 2 - Design and Develop the Code
    target_index = None

    # TODO: Task 3 - Implement the Loop and Process Each Element
    for index, event in enumerate(events):
        if event.id == event_id:
            target_index = index
            break

    # TODO: Task 4 - Return and Handle Results
    if target_index is None:
        return jsonify({"error": "Event not found"}), 404
    del events[target_index]
    return jsonify({"message": "Event deleted successfully"}), 200

if __name__ == "__main__":
    app.run(debug=True)
