from flask import Blueprint, request, jsonify
from service.usecases.signup import *
from service.usecases.login import *
from service import database
from service.role import *

routes = Blueprint('routes', __name__)


@routes.route('/')
def main():
    return 'Team User-Microservice'


# Create User
@routes.route('/user', methods=['POST'])
def user_register():
    try:
        content = json.loads(request.data)
    except ValueError:
        error = ErrorResponse("JSON expected", 400)
        return error.get_json_value(), error.get_code()

    response = signup(content)
    return response.get_json_value(), response.get_code()


# Login User
@routes.route('/user/login', methods=['POST'])
def user_login():
    try:
        content = json.loads(request.data)
    except ValueError:
        error = ErrorResponse("JSON expected", 400)
        return error.get_json_value(), error.get_code()

    response = login(content)
    return response.get_json_value(), response.get_code()


# Get User Info
@routes.route('/user/<uuid>/info', methods=['GET']) # TODO not REST compliant
def user_info():
    """
    session: JWT as string
    user: optional, mail address of other user you want to get information about


    # TODO: Verify that the request is valid (from session)
    req_body = None

    try:
        req_body = json.loads(request.data)
    except ValueError:
        error = ErrorResponse('JSON expected', 400)
        return jsonify(error.get_description()), error.get_code()

    if not 'session' in req_body:
        error = ErrorResponse('No session provided', 400)
        return jsonify(error.get_description()), error.get_code()

    user_id_to_query = None
    # switch based on wheather the user was provided
    if (not 'user' in req_body) or req_body['user'] == None:
        # return information about owner of this session
        # TODO: where in the JWT is the id stored?
        token_payload = jwt.decode(req_body.session)
        user_id_to_query = token_payload['id']  # TODO put here the correct field name
    else:
        # return informatin about the provided user
        user_to_query = req_body['user']
        if not user_registrar._is_valid_email(user_to_query) or not database.existsUser(user_to_query):
            error = ErrorResponse('No valid user', 400)
            return jsonify(error.get_description()), error.get_code()

        user_id_to_query = database.getUserIdByEmail(user_to_query) # user exists after check above

    infos = database.getUserInfo(user_id)

    # TODO: privileged student + report_spammer
    return {
        'teacher': infos[7] == Role.TEACHER,
        'admin': infos[7] == Role.ADMIN,
        'priviliged_student': False,
        'report_spammer': 0
    }
    """


# Set User Info
@routes.route('/user', methods=['PUT']) # TODO not REST compliant
def user_update():
    return 'and update responses here'


# Verify Email
@routes.route('/user/verify', methods=['PATCH'])
def user_session():
    return 'or some email checks there'


# Check User Session
@routes.route('/user/session', methods=['POST'])
def user_session():
    return 'or some session checks there'



