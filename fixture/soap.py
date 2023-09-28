from suds.client import Client
from suds import WebFault
from model.project import Project

class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False
        
    def get_projects_list(self):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        projects_list = []
        config = self.app.config['webadmin']
        try:
            projects_list_from_soap = client.service.mc_projects_get_user_accessible(
                username=config["username"], password=config["password"])
            for project in projects_list_from_soap:
                projects_list.append(Project(
                    id=project.id,
                    name=project.name,
                    description=project.description))
            return projects_list
        except WebFault:
            return False
        