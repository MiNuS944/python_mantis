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
        return "%s" % (self.name)

    def name_or_max(self):
        if self.name:
            return str(self.name)
        else:
            return maxsize