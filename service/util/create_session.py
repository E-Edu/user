from service.user import *
from service.util.jwt import *


def create_session(user: User):
    payload = {
        "uuid": user.uuid,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "role": user.role.value,
        "status": user.status.value
    }
    return jwt_encode(payload)
