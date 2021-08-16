#!/usr/bin/env python3
""" New view for Session Authentication
"""
from api.v1.views import app_views
from flask import abort, jsonify, request, session, make_response
from models.user import User
from os import getenv
import json


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def sessionLogin() -> str:
    """ POST /api/v1/auth_session/login
         - All routes for the Session authentication.
    """
    email = request.form.get('email')
    if not email:
        return jsonify({"error": "email missing"}), 400
    password = request.form.get('password')
    if not password:
        return jsonify({"error": "password missing"}), 400
    users = User.search({'email': email})
    if len(users) == 0:
        return jsonify({"error": "no user found for this email"}), 404
    for item in users:
        if item.is_valid_password(password):
            from api.v1.app import auth
            respon = jsonify(item.to_json())
            SESSION_NAME = getenv('SESSION_NAME')
            resp.set_cookie(SESSION_NAME, auth.create_session(item.id))
            return respon
    return jsonify({"error": "wrong password"}), 401


@app_views.route(
    '/auth_session/logout', methods=['DELETE'], strict_slashes=False)
def sessionLogout() -> str:
    """ DELETE /api/v1/auth_session/logout
        Logout
    """
    from api.v1.app import auth
    if not auth.destroy_session(request):
        abort(404)
    return jsonify({}), 200
