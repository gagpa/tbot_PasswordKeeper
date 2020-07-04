from . import api


@api.route('/')
def hello_new_user():
    return 'Hi new user'
