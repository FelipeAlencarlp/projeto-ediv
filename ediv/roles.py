from rolepermissions.roles import AbstractUserRole

class Client(AbstractUserRole):
    available_permissions = {
        'submit_video_for_edit': True,
        'view_status_video': True,
    }

class Editor(AbstractUserRole):
    available_permission = {
        'edit_video': True,
        'view_video_for_editing': True,
        'make_budget': True,
    }