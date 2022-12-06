from todoist_service.db import DB
from todoist_service.todoist_wrapper.todoist_api_wrapper import TodoistAPIWrapper

import hashlib

def register_user(db: DB, access_token: str):
    doist = TodoistAPIWrapper(access_token)
    user_id = hashlib.md5(access_token.encode('utf-8')).hexdigest()
    user_name = "John Doe"

    db.add_user(user_id=user_id, token=access_token, full_name=user_name)
    return access_token, user_id
