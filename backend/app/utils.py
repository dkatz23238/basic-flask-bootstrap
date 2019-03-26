from flask import (
    url_for, redirect, render_template,
    flash, g, session, jsonify, request
)
from app.SECRET_TOKENS import SECRET_TOKENS
JSON_MIME_TYPE = 'application/json'

def json_response(data='', status=200, headers=None):
    headers = headers or {}
    if 'Content-Type' not in headers:
        headers['Content-Type'] = JSON_MIME_TYPE
    return make_response(data, status, headers)


def check_tokens(request):
    token = request.args.get('token')
    return token in SECRET_TOKENS
