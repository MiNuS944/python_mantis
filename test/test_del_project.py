from model.project import Project
import random

def test_del_project(app):
    old_list_projects = app.soap.get_projects_list()
    if not old_list_projects:
        project_name = str(random.randint(-1000, 1000))
        add_project = Project(name=project_name,
                           status='разрабатываемый',
                           view_state='общая',
                           description="тесттесттест")
        app.mantis.create_new_project(add_project)
        old_list_projects = app.soap.get_projects_list()
    project = random.choice(old_list_projects)
    app.mantis.delete_project_by_name(project)
    new_list_projects = app.soap.get_projects_list()
    assert len(old_list_projects) - 1 == len(new_list_projects)
    assert sorted(old_list_projects, key=Project.name_or_max) == sorted(new_list_projects, key=Project.name_or_max)
