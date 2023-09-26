from sys import maxsize


class Project:
    def __init__(self, name=None, status=None, inherit_global=None,
                 view_state=None, description=None, enabled=None):
        self.name = name
        self.status = status
        self.inherit_global = inherit_global
        self.view_state = view_state
        self.description = description
        self.enabled = enabled

    def __repr__(self):
        return "%s:%s;%s;%s;%s" % (self.name, self.status, self.inherit_global, 
                                   self.view_state, self.description)

    def __eq__(self, other):
        return (self.name == other.name and self.status == other.status 
                and self.inherit_global == other.inherit_global 
                and self.view_state == other.view_state
                and self.description == other.description)

    def name_or_max(self):
        if self.name:
            return str(self.name)
        else:
            return maxsize