from django.db import models
from asana_api.utils import AsanaApiHelper


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    asana_id = models.CharField(max_length=255)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.id:
            asana = AsanaApiHelper()
            user = asana.add_user(
                self.email
            )
            self.asana_id = user['gid']
        super(User, self).save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=255, unique=True)
    asana_id = models.CharField(max_length=255)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        asana = AsanaApiHelper()
        if not self.id:
            try:
                project = asana.create_project(self.name)
                self.asana_id = project['gid']
                super(Project, self).save(force_insert, force_update, using, update_fields)
            except Exception as e:
                print("error1" + str(e))
        else:
            try:
                asana.update_project(self.asana_id, self.name)
                super(Project, self).save(force_insert, force_update, using, update_fields)
            except Exception as e:
                print("error2" + str(e))

    def __str__(self):
        return self.name


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    executor = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField()
    asana_id = models.CharField(max_length=255)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        asana = AsanaApiHelper()
        if not self.id:
            try:

                task = asana.create_task(
                    [self.project.asana_id],
                    self.executor.asana_id,
                    self.name
                )
                self.asana_id = task['gid']
                super(Task, self).save(force_insert, force_update, using, update_fields)
            except Exception as e:
                print(str(e))
        else:
            try:
                asana.update_task(
                    self.asana_id,
                    self.executor.asana_id,
                    self.name
                )
                super(Task, self).save(force_insert, force_update, using, update_fields)
            except Exception as e:
                print(str(e))

    def __str__(self):
        return '{} - {} - {}'.format(
            self.project.name,
            self.executor.name,
            self.name
        )
