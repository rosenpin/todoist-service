import logging

from todoist_api_python.api import TodoistAPI

import todoist_service.todoist_wrapper.consts as consts
from todoist_service.todoist_wrapper.todoist_wrapper import TodoistWrapper


class TodoistAPIWrapper(TodoistWrapper):
    def __init__(self, token):
        self.api = TodoistAPI(token=token)
        self.sync()

    def get_all_labels(self):
        return self.api.get_labels()

    def get_tasks(self, filt):
        return self.api.get_tasks(filt=filt)

    def get_all_tasks(self):
        return self.api.get_tasks()

    def get_task_by_id(self, item_id):
        return self.api.get_task(item_id)

    def add_label(self, name):
        self.api.add_label(name)
        self.commit()

    def get_label(self, label_id):
        return self.api.get_label(label_id)

    def add_project(self, name):
        self.api.add_project(name)
        self.commit()

    def get_project(self, project_id):
        return self.api.get_project(project_id)

    def get_all_projects(self):
        return self.api.get_projects()

    def sync(self):
        return

    def commit(self):
        return
