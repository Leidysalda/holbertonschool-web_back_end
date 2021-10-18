#!/usr/bin/env python3
"""
Basic Flask app
"""
from flask import Flask, jsonify, request, abort, redirect
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    """
    Basic Flask app
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """
    User end point
    """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        new_user = AUTH.register_user(email, password)
        dt = {"email": "{}".format(new_user.email), "message": "user created"}
        return jsonify(dt)
    except ValueError:
        return jsonify({'message': 'email already registered'}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def sessions():
    """
    sessions method
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if not AUTH.valid_login(email, password):
        abort(401)
    dt = {"email": email, "message": "logged in"}
    resp = jsonify(dt)
    session_id = AUTH.create_session(email)
    resp.set_cookie('session_id', session_id)
    return resp


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """
    logout method
    """
    cookie_session = request.cookies.get('session_id')
    get_user = AUTH.get_user_from_session_id(cookie_session)
    if get_user is None:
        abort(403)
    AUTH.destroy_session(get_user.id)
    return redirect('/')


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    """
    Profile method
    """
    cookie_session = request.cookies.get('session_id')
    get_user = AUTH.get_user_from_session_id(cookie_session)
    if get_user:
        return jsonify({"email": get_user.email}), 200
    abort(403)


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token():
    """
    Reset password method
    """
    email = request.form.get('email')
    if email is None:
        abort(403)
    try:
        token = AUTH.get_reset_password_token(email)
    except ValueError:
        abort(403)
    return jsonify({"email": email, "reset_token": token}), 200


@app.route('/reset_password', methods=['PUT'], strict_slashes=False)
def update_password():
    """
    Update password methos
    """
    email = request.form.get('email')
    new_password = request.form.get('new_password')
    reset_token = request.form.get('reset_token')
    try:
        AUTH.update_password(reset_token, new_password)
    except ValueError:
        abort(403)
    return jsonify({'email': email, 'message': 'Password updated'}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
