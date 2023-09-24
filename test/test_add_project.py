from random import randint
from model.project import Project


def test_add_project(app):
    project_name = str(randint(0, 1000))
    add_project = Project(name=project_name,
                           status='разрабатываемый',
                           view_state='общая',
                           description="тесттесттест")
    old_list_projects = app.mantis.get_project_list()
    old_list_count = app.mantis.count()
    app.mantis.create_new_project(add_project)
    assert old_list_count + 1 == app.mantis.count()
    new_list_projects = app.mantis.get_project_list()
    old_list_projects.append(add_project)
    print(old_list_projects)
    print(type(old_list_projects))
    print(type(old_list_projects[0]))
    print(type(old_list_projects[0].name))
    print(new_list_projects)
    print(type(new_list_projects))
    print(type(new_list_projects[0]))
    print(type(new_list_projects[0].name))
    assert old_list_projects == new_list_projects
    assert sorted(old_list_projects, key=Project.name_or_max) == sorted(new_list_projects, key=Project.name_or_max)