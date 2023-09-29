from suds.client import Client
from suds import WebFault
from model.project import Project

class SoapHelper:

    def __init__(self, app):
        self.app = app
    
    def url_client(self):
        base_url = self.app.config['web']['baseUrl']
        client = Client(base_url + "/api/soap/mantisconnect.php?wsdl")
        return client

    def can_login(self, username, password):
        client = self.url_client()
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False
        
    def get_projects_list(self):
        client = self.url_client()
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
        