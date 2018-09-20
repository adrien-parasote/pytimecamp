#!/usr/bin/python
# coding: utf-8
from datetime import date, datetime

from pytimecamp.structtime import StructTime

API_BASE_URL = 'https://www.timecamp.com/third_party/api'

ALLOWED_RESPONSE_FORMAT = ['xml', 'json', 'csv', 'rawxml', 'jsonp', 'serialized', 'php', 'html']
ALLOWED_APIS = {
    'account': ['list'],
    'currency': ['list'],
    'tax': ['list'],
    'users': ['list', 'get_current'],
    'group': ['list', 'get_settings', 'set_settings', 'add', 'update', 'delete'],
    'tasks': ['list', 'filter', 'add', 'update'],
    'entries': ['filter', 'add', 'update'],
    'entries_changes': ['filter'],
    'timer_running': ['list'],
    'timer': [],  # TODO : start, get, stop
    'activity': ['filter'],  # TODO : post
    'application': ['filter'],
    'window_title': ['filter'],
    'client': ['list', 'add', 'update'],
    'invoice': ['list', 'add', 'update'],
    'attendance': ['filter'],
    'away_time': ['filter']
}

QUERY_FIELDS = {
    'window_title': {
        'optional': {},
        'mandatory': {
            'window_title_ids': (list,),
        }
    },
    'activity': {
        'optional': {
            'user_id': (int, str)
        },
        'mandatory': {
            'date': (date, datetime),
        }
    },
    'application': {
        'optional': {},
        'mandatory': {
            'application_ids': (list,),
        }
    },
    'tasks': {
        'optional': {
            'exclude_archived': (int, bool),
            'task_id': (int, str),
            'external_task_id': (int, str)
        },
        'mandatory': {}
    },
    'entries': {
        'optional': {
            'task_ids': (list,),
            'with_subtasks': (int,),
            'user_ids': (list,)
        },
        'mandatory': {
            'date_from': (date, datetime),
            'date_to': (date, datetime)
        }
    },
    'entries_changes': {
        'optional': {
            'limit': (int,),
            'task_ids': (list,),
            'user_ids': (list,)
        },
        'mandatory': {
            'date_from': (date, datetime),
            'date_to': (date, datetime)
        }
    },
    'attendance': {
        'optional': {
            'user_ids': (list,)
        },
        'mandatory': {
            'date_from': (date, datetime),
            'date_to': (date, datetime)
        }
    },
    'away_time': {
        'optional': {
            'user_ids': (list,)
        },
        'mandatory': {
            'date_from': (date, datetime),
            'date_to': (date, datetime)
        }
    }
}

POST_DATA = {
    'tasks': {
        'optional': {
            'tags': (str, list),
            'parent_id': (str, int),
            'external_task_id': (str, int),
            'external_parent_id': (str, int),
            'budgeted': (int,),
            'note': (str,),
            'archived': (int,),  # (optional, 0 = no, 1 = yes)
            'billable': (int,),  # (optional, 0 = no, 1 = yes)
            'budget_unit': (str,),
            'user_ids': (list,),
            'role': (int,)  # (optional, by default 1, 1 = manager, 3 = regular user)
        },
        'mandatory': {
            'name': (str,)
        }
    },
    'group': {
        'optional': {
            'name': (str,)  # default: "" - empty string
        },
        'mandatory': {
            'parent_id': (int,)
        }
    },
    'invoice': {
        'optional': {
            'invoiceNumber': (int,),
            'currencyId': (int,),
            'status': (int,),
            'description': (str,),
            'issueDate': (date, datetime),
            'noteToClient': (str,),
            'poNumber': (int,),
            'dueDate': (date, datetime),
            'quote': (bool,),
            'entries': (list,),
        },
        'mandatory': {
            'clientId': (int,)
        }
    },
    'client': {
        'optional': {
            'firstName': (str,),
            'lastName': (str,),
            'address': (str,),
            'email': (str,),
            'currencyId': (int,),
        },
        'mandatory': {
            'organizationName': (str,)
        }
    },
    'entries': {
        'optional': {
            'note': (str,),
            'start_time': (StructTime,),
            'end_time': (StructTime,),
            'billable': (bool,),
            'task_id': (int, str)
        },
        'mandatory': {
            'date': (date, datetime),
            'duration': (int,)  # in seconds
        }
    },
}
PUT_DATA = {
    'tasks': {
        'optional': {
            'name': (str,),
            'tags': (str, list),
            'parent_id': (str, int),
            'external_task_id': (str, int),
            'external_parent_id': (str, int),
            'budgeted': (int,),
            'note': (str,),
            'archived': (int,),  # (optional, 0 = no, 1 = yes)
            'billable': (int,),  # (optional, 0 = no, 1 = yes)
            'budget_unit': (str,),  # (optional, hours / fee)
            'user_ids': (list,),  # (optional, comma separated)
            'role': (int,)  # (optional, by default 1, 1 = manager, 3 = regular user)
        },
        'mandatory': {
            'task_id': (str, int)
        }
    },
    'group': {
        'optional': {
            'name': (str,),
            'parent_id': (int,)
        },
        'mandatory': {
            'group_id': (int,)
        }
    },
    'invoice': {
        'optional': {
            'clientId': (int,),
            'invoiceNumber': (int,),
            'currencyId': (int,),
            'status': (int,),
            'description': (str,),
            'issueDate': (date, datetime),
            'noteToClient': (str,),
            'poNumber': (int,),
            'dueDate': (date, datetime),
            'quote': (bool,),
            'entries': (list,),
        },
        'mandatory': {
            'invoiceId': (int,)
        }
    },
    'client': {
        'optional': {
            'firstName': (str,),
            'lastName': (str,),
            'address': (str,),
            'email': (str,),
            'currencyId': (int,),
            'organizationName': (str,)
        },
        'mandatory': {
            'clientId': (int,)
        }
    },
    'entries': {
        'optional': {
            'note': (str,),
            'start_time': (StructTime,),
            'end_time': (StructTime,),
            'billable': (bool,),
            'task_id': (int, str),
            'date': (date, datetime),
            'duration': (int,)  # in seconds
        },
        'mandatory': {
            'id': (int,)
        }
    },
}

GROUP_SETTINGS = {
    'tt_prevent_editing_hours': [True, False, 0, 1],
    'tt_remove_distracting': [True, False, 0, 1],
    'tt_prevent_tracking_to_tasks_with_level': [-1, 1, 2, 3, 4],
    'tt_prevent_tracking_to_tasks_with_level_on': [True, False, 0, 1],
    'changeBillingFlag': [True, False, 0, 1],
    'tt_prevent_overlapping_entries': [True, False, 0, 1],
    'reportTimeRounding': [60, 300, 360, 600, 900, 1800, 3600],
    'reportTimeRoundingType': ['round', 'ceil', 'floor'],
    'tt_full_taskpicker_visibility': [True, False, 0, 1]
}
