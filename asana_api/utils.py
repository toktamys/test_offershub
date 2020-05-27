import asana
from django.conf import settings


class AsanaApiHelper:
    def __init__(self,):
        self.personal_access_token = settings.PERSONAL_ACCESS_TOKEN
        self.client = asana.Client.access_token(self.personal_access_token)
        self.me = self.client.users.me()
        self.workspace = self.me['workspaces'][0]['gid']

    def add_user(self, user):
        params = {
            'user': user
        }
        return self.client.workspaces.add_user(self.workspace, params)

    def create_project(self, name):
        params = {
            'name': name,
        }
        return self.client.projects.create_in_workspace(self.workspace, params)

    def update_project(self, project_id, name):
        params = {
            'name': name,
        }
        return self.client.projects.update(project_id, params)

    def create_task(self, projects, user_id, name):
        params = {
            'projects': projects,
            'assignee': user_id,
            'name': name
        }
        return self.client.tasks.create_in_workspace(self.workspace, params)

    def update_task(self, task_id, user_id, name):
        params = {
            'assignee': user_id,
            'name': name
        }
        return self.client.tasks.update(task_id, params)
