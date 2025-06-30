import flask
from flask import request, jsonify
from sheets import updateAttendence

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/hello-world', methods=['GET'])
def hello_world():
    return "Hello World"

@app.route('/zoom', methods=['POST'])
def log_attendance():
    try:
        data = request.get_json(force=True)
        obj = data.get('payload', {}).get('object', {})
        user = obj.get('participant', {})
        topic = obj.get('topic', '')
        sheetName = request.args.get('sheet', 'AttPy')

        event = data.get('event')
        email = user.get('email')

        if not email:
            return "Missing participant email", 400

        if event == 'meeting.participant_joined':
            updateAttendence(email, True, user.get('join_time', ''), topic, sheetName)
            return "Participant joined recorded", 200

        elif event == 'meeting.participant_left':
            updateAttendence(email, False, user.get('leave_time', ''), topic, sheetName)
            return "Participant left recorded", 200

        else:
            return "Event type not handled", 400

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Internal Error", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
