from flask_restful import Resource, Api
from app.models import ApplicationUser, RoboticProcessAutomation, RobotRunEvent
from app import db
import datetime
import json 
from app.utils import JSON_MIME_TYPE, json_response, check_tokens
import uuid

from flask import (
    url_for, redirect, render_template,
    flash, g, session, jsonify, request
)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class Tables(Resource):
    """ Tables resource contains get method and must be sent with a query param /api/tables?token=<token>"""
    def get(self):
        if check_tokens(request):
            tables = {"table_names": db.engine.table_names()}
            return tables, 200
        else:
            return {"message": "Access Denied!"}, 404

class Users(Resource):
    """
    Users resource contains get and post methods.
    Parameters for query GET : api/users?user=<user>.
    Parameters for POST must be json encoded: {"username":<username>, "password":<password>}"""

    def get(self):

        user_query_param = request.args.get("username")
        if (user_query_param == None):
            error = {'error': 'Missing field/s'}
            return error, 400
        else:
            returned_user = ApplicationUser.query.filter_by(
                username=user_query_param).first()
            if returned_user == None:
                error = {'error': 'Not Found'}
                return error, 404
            else:
                returned_user_d = {
                    "user_id": returned_user.user_id,
                    "username": returned_user.username,
                    "password": returned_user.password
                    }

                return returned_user_d, 200

    def post(self):

        if request.content_type != JSON_MIME_TYPE:
            error = {'error': 'Invalid Content Type'}
            return error, 400

        data = json.loads(request.json)
        if not (('username' in data.keys()) & (('password' in data.keys()))):
            error = {'error': 'Missing field/s'}
            return error, 400

        if (ApplicationUser.query.filter_by(username=data["username"]).first()) != None:
            error = {'error': 'username already exists'}
            return error, 400

        new_user = ApplicationUser(
            user_id=str(uuid.uuid4()),
            username=data["username"],
            password=data["password"]
        )

        new_user_d = {
            "user_id": new_user.user_id,
            "username": new_user.username,
            "password": new_user.password,
        }
        # Add user to database
        db.session.add(new_user)
        # Commit query
        db.session.commit()
        return new_user_d, 201

class RPA(Resource):
    
    def get(self):
        rpa_id = request.args.get("rpa_id")
        if rpa_id == None:
            rpas = [{
                "rpa_id": r.rpa_id,
                "rpa_name": r.rpa_name,
                "creation_date": str(r.creation_date),
                "git_repository": r.git_repository,
                "cron_fmat_schedule": r.cron_fmat_schedule}
                for r in RoboticProcessAutomation.query.all()
                ]
            return rpas, 200
        else:
            returned_rpa = RoboticProcessAutomation.query.filter_by(
                rpa_id=rpa_id).first()
            
            if returned_rpa == None:
                error = {'error': 'Not Found'}
                return error, 404
            else:
                returned_user_d = {
                    "rpa_id": returned_rpa.rpa_id,
                    "rpa_name": returned_rpa.rpa_name,
                    "creation_date": str(returned_rpa.creation_date),
                    "git_repository": returned_rpa.git_repository,
                    "cron_fmat_schedule": returned_rpa.cron_fmat_schedule,
                }

                return returned_user_d, 200
    
    def post(self):
        """ JSON keys for POST must contain ['cron_fmat_schedule', 'git_repository', 'rpa_name'] """
        if request.content_type != JSON_MIME_TYPE:
            error = {'error': 'Invalid Content Type'}
            return error, 400

        data = json.loads(request.json)

        if sorted(data.keys()) != ['cron_fmat_schedule', 'git_repository', 'rpa_name']:
            error = {'error': 'Missing field/s'}
            return error, 400

        if (RoboticProcessAutomation.query.filter_by(rpa_name=data["rpa_name"]).first()) != None:
            error = {'error': 'rpa already exists'}
            return error, 400

        cdate = datetime.datetime.now()
        unique_id = str(uuid.uuid4())
        new_rpa = RoboticProcessAutomation(
            rpa_id=unique_id,
            rpa_name= data["rpa_name"],
            creation_date=cdate,
            git_repository= data["git_repository"],
            cron_fmat_schedule= data["cron_fmat_schedule"],
        )

        new_rpa_dict = {
            "rpa_id": unique_id,
            "rpa_name" : data["rpa_name"],
            "creation_date": str(cdate),
            "git_repository" : data["git_repository"],
            "cron_fmat_schedule" : data["cron_fmat_schedule"],
        }
        # Add user to database
        db.session.add(new_rpa)
        # Commit query
        db.session.commit()
        return new_rpa_dict, 201

class RPAEvent(Resource):

    def get(self):
        rpa_id = request.args.get("rpa_id")
        if rpa_id == None:

            events = [{
                "rpa_id": r.rpa_id,
                "event_id": r.event_id,
                "event_datetime": str(r.event_datetime),
                "tag": r.tag,
                "message": r.message}
                for r in RobotRunEvent.query.all()
            ]
            return events, 202
        else:
            returned_events = RobotRunEvent.query.filter_by(
                rpa_id=rpa_id).all()
            
            if returned_events == []:
                error = {'error': 'Not Found'}
                return error, 404
            else:
                events = [{
                    "rpa_id": r.rpa_id,
                    "event_id": r.event_id,
                    "event_datetime": str(r.event_datetime),
                    "tag": r.tag,
                    "message": r.message}
                    for r in returned_events
                ]

                return events, 200

    def post(self):
        """ JSON keys for POST must contain ['cron_fmat_schedule', 'git_repository', 'rpa_name'] """
        if request.content_type != JSON_MIME_TYPE:
            error = {'error': 'Invalid Content Type'}
            return error, 400

        data = json.loads(request.json)

        if sorted(data.keys()) != ['message', 'rpa_id', 'tag']:
            error = {'error': 'Missing field/s'}
            return error, 400

        cdate = datetime.datetime.now()
        event_id = str(uuid.uuid4())
        new_event = RobotRunEvent(
            event_id= event_id,
            rpa_id= data["rpa_id"],
            event_datetime=str(cdate),
            tag=data["tag"],
            message=data["message"],

        )

        new_event_dict = {
            "event_id": event_id,
            "rpa_id":data["rpa_id"],
            "event_datetime":str(cdate),
            "tag": data["tag"],
            "message":data["message"],

        }

        # Add user to database
        db.session.add(new_event)
        # Commit query
        db.session.commit()
        return new_event_dict, 201
