from todoist_service.db import DB
from todoist_service.todoist_wrapper.todoist_api_wrapper import TodoistAPIWrapper


def register_user(db: DB, access_token: str):
    doist = TodoistAPIWrapper(access_token)
    user_id = hash(access_token)
    user_name = "John Doe"

    db.add_user(user_id=user_id, token=access_token, full_name=user_name)
    return access_token, user_id
