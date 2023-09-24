from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from model.project import Project


class ProjectHelper:
    project_cache = None

    def __init__(self, app):
        self.app = app
        

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/mantisbt-1.2.20/")) or not \
                (wd.current_url.endswith("/mantisbt-1.2.20/my_view_page.php")):
            wd.find_element(By.CSS_SELECTOR, "img[alt='MantisBT']").click()

    def manage(self):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element(By.LINK_TEXT, "управление").click()

    def manage_projects(self):
        wd = self.app.wd
        self.manage()
        wd.find_element(By.LINK_TEXT, "Управление проектами").click()

    def create_new_project(self, projects):
        wd = self.app.wd
        self.manage_projects()
        wd.find_element(By.CSS_SELECTOR, 'input[value="создать новый проект"]').click()
        self.fill_in_form_project(Project(name=projects.name, status=projects.status,
                                           inherit_global=projects.inherit_global, view_state=projects.view_state,
                                           description=projects.description))
        wd.find_element(By.CSS_SELECTOR, 'input[value="Добавить проект"]').click()
        self.open_home_page()
        self.project_cache = None

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None and field_name != 'inherit_global':
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)
        elif field_name == 'inherit_global':
            pass

    def fill_in_form_project(self, projects):
        self.change_field_value("name", projects.name)
        self.select_by_name("status", projects.status)
        self.change_field_value("inherit_global", projects.inherit_global)
        self.select_by_name("view_state", projects.view_state)
        self.change_field_value("description", projects.description)

    def select_by_name(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            Select(wd.find_element(By.NAME, field_name)).select_by_value('10')

    def get_project_list(self):
        wd = self.app.wd
        if self.project_cache is None:
            self.manage_projects()
            self.project_cache = []
            table_project = wd.find_element(By.XPATH, '/html/body/table[3]')
            elements = table_project.find_elements(By.CSS_SELECTOR, "tr.row-1, tr.row-2")
            for element in elements:
                cells = element.find_elements(By.CSS_SELECTOR, "td")
                name = cells[0].text
                status = cells[1].text
                enabled = cells[2].text
                view_state = cells[3].text
                description = cells[4].text
                self.project_cache.append(Project(name=name, status=status, enabled=enabled,
                                                   view_state=view_state, description=description))
        return list(filter(None, self.project_cache))

    def open_first_project_from_row(self):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, "tr.row-1 a").click()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        self.manage_projects()
        table_project = wd.find_element(By.XPATH, '/html/body/table[3]')
        return len(table_project.find_elements(By.CSS_SELECTOR, "tr.row-1, tr.row-2"))

    def delete_project(self):
        wd = self.app.wd
        self.open_home_page()
        self.manage_projects()
        self.open_first_project_from_row()
        wd.find_element(By.CSS_SELECTOR, '[value="Удалить проект"]').click()
        wd.find_element(By.CSS_SELECTOR, '[value="Удалить проект"]').click()