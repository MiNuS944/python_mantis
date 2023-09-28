from random import randint
from model.project import Project
import time


def test_add_project(app):
    project_name = str(randint(0, 1000))
    add_project = Project(name=project_name,
                           status='разрабатываемый',
                           view_state='общая',
                           description="тесттесттест")
    old_list_projects = app.soap.get_projects_list()
    app.mantis.create_new_project(add_project)
    new_list_projects = app.soap.get_projects_list()
    assert len(old_list_projects) + 1 == len(new_list_projects)
    old_list_projects.append(add_project)
    assert sorted(old_list_projects, key=Project.name_or_max) == sorted(new_list_projects, key=Project.name_or_max)