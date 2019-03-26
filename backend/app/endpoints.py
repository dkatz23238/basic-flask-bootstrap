from app import api
from app.resources import HelloWorld, Tables, Users, RPA, RPAEvent

api.add_resource(HelloWorld, '/')
api.add_resource(Tables, '/api/tables')
api.add_resource(Users, '/api/users')
api.add_resource(RPA, '/api/roboticprocessautomations')
api.add_resource(RPAEvent, '/api/events')
