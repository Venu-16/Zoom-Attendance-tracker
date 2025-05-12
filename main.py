import flask
from flask import request
from sheets import updateAttendence

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/hello-world', methods=['GET'])
def hello_world():
    return "Hello World"


@app.route('/zoom', methods=['GET', 'POST'])
def log_attendence():
    # print(request)
    data = request.json
    obj = data['payload']['object']
    user = obj['participant']
    sheetName = 'AttPy'
    topic = obj['topic']
    if 'sheet' in request.args:
        sheetName = request.args['sheet']

    if data['event'] == 'meeting.participant_left':
        updateAttendence(user['email'], False, user['leave_time'], topic, sheetName)
        return "Update OK"
    if data['event'] == 'meeting.participant_joined':
        updateAttendence(user['email'], True, user['join_time'], topic, sheetName)
        return "Update OK"
    # print(request.args)
    return "EVENT Not Required", 400


@app.errorhandler(Exception)
def all_exception_handler(error):
    return 'Internal Error', 500


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)