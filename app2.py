from flask import Flask, request
from flask_restful import Resource, Api
import ast
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/WEBCHAT'
db = SQLAlchemy(app)

class MessageBank(db.Model):
    __tablename__ = 'messagebank'
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.Integer)
    previous_msg = db.Column(db.Text)
    response = db.Column(db.Text)

    def __init__(self, session_id, previous_msg, response):
        self.session_id = session_id
        self.previous_msg = previous_msg
        self.response = response


api = Api(app)

class webChat(Resource):
    def post(self):
        # Take the test input. It can be single line or a paragraph
        try:
            data = request.json
            msg = data['msg']
            session_id = data['session_id']

            # Create an instance of the MessageBank model with the received data
            message_bank_entry = MessageBank(session_id=session_id, previous_msg=msg, response="")

            # Add the entry to the database session
            db.session.add(message_bank_entry)

            # Commit the changes to the database
            db.session.commit()

            # Optionally, you can return a response indicating the success
            return {'status': 'success', 'message': 'Data added to MessageBank table'}, 201

        except Exception as e:
            return {'status': 'error', 'message is here ': str(e)}, 500

        # try:
        #     data = MessageBank.query.filter_by(session_id=session_id).order_by(MessageBank.id.desc()).first()
        #
        #     previous_msg = ast.literal_eval(data.previous_msg)
        #     msg_response = ast.literal_eval(data.response)
        #     print(previous_msg)
        #     print(msg_response)
        #     print(type(previous_msg))
        #     print(type(msg_response))
        #
        #     # Call your chatbot response function (processMessage) here and store the result in the "result" variable
        #     # For demonstration purposes, we're using a dummy response
        #     result = {"response": "Hello, you said: " + msg}
        #     return "SECOND TA TE SHOMOSSA"
        # except Exception as e:
        #     result = {"msg": "An exception occurred. Error: " + str(e)}
        #     return {"msg": "An exception occurred. Error: " + str(e)}, 500
        #
        # return result, 200

api.add_resource(webChat, '/web-chat')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
