import flask
from flask import request, Response
from model.extension import ExtensionResult, ExtensionRequest
app = flask.Flask(__name__)
# app.config["DEBUG"] = True


@app.route('/sample', methods=['POST'])
def sample():
    # Get Extension Request from JSON Request Body
    extension_request = ExtensionRequest(request.get_json())

    # Your code here:
    ticket_number = extension_request.intent.ticket.ticketNumber

    # Generate Extension Result to 3Dolphins
    # Format default =>(output, success=True, repeat=False, next_entity=True, agent=False)
    result = ExtensionResult(ticket_number)
    return Response(result.get_value(), mimetype='application/json', status=200)


app.run()
