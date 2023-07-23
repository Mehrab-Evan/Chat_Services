from flask import Flask, request
from flask_restful import Resource, Api

from chatbotResponse import processMessage

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/WEBCHAT'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/WEBCHAT'
db = SQLAlchemy(app)
migrate = Migrate(app, db)



class MessageBank(db.Model):
    __tablename__='MessageBank'
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.Integer)
    previous_msg = db.Column(db.Text)
    response = db.Column(db.Text)

    def __init__(self, session_id, previous_msg, response):
        self.session_id=session_id
        self.previous_msg=previous_msg
        self.response=response


api = Api(app)


class webChat(Resource):

    # def post(self):
    #     # take the test input. It can be single line or a paragraph
    #     print(request.json)
    #     try:
    #         data = request.json
    #         msg = data['msg']
    #         session_id = data['session_id']
    #
    #         # Create an instance of the MessageBank model
    #         message_bank_entry = MessageBank(session_id=session_id, previous_msg=msg, response="")
    #
    #         # Add the entry to the database session
    #         db.session.add(message_bank_entry)
    #         db.session.commit()
    #
    #         print("THIS IS COMING HERE")
    #         return {'status': 'success', 'message': 'Data added to MessageBank table'}, 201
    #     except Exception as e:
    #         return {'status': 'error', 'message': str(e)}, 500

    def post(self):
        #take the test input. It can be single line or a paragraph
        print(request.json)
        try:
            data = request.json
            msg = data['msg']
            session_id = data['session_id']
        except Exception as e:
            return {"msg": "An exception occurred. Error: "+str(e)}, 400
        try:
            data = MessageBank.query.filter_by(session_id= session_id).order_by(MessageBank.id.desc()).first()


            previous_msg = ast.literal_eval(data.previous_msg)
            msg_response = ast.literal_eval(data.response)
            print(previous_msg)
            print(msg_response)
            print(type(previous_msg))
            print(type(msg_response))


            result = processMessage(msg)
        except Exception as e:
            result={"msg": "An exception occurred. Error: "+str(e)}
            return {"msg": "An exception occurred. Error: "+str(e)}, 500

        # print(result)

        # print(result[:-1])


        # print(result[-1])





        # session_id =data['session_id']
        # previous_msg = str(result[:-1])
        # response = str(result[-1])
        # msg = MessageBank(session_id,previous_msg,response )
        # db.session.add(msg)
        # db.session.commit()
        # return result, 200
    

        # return {"msg": "Service Not Ready."}, 200



api.add_resource(webChat, '/web-chat')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)