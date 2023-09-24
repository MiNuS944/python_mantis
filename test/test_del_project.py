from random import randint
from model.project import Project

def test_del_project(app):
    old_list_count = app.mantis.count()
    if old_list_count == 0:
        project_name = str(randint(-1000, 1000))
        add_project = Project(name=project_name,
                           status='разрабатываемый',
                           view_state='общая',
                           description="тесттесттест")
        app.mantis.create_new_project(add_project)
        old_list_count = app.mantis.count()
    app.mantis.delete_project()
    assert old_list_count - 1 == app.mantis.count()
