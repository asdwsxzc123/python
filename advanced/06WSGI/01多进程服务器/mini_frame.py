def login():
    return 'login in'
def register():
    return 'register in'

def application(file_name):
    if (file_name == '/login.py'):
        login()
    elif (file_name == '/register.py'):
        register()
    else: 
        return 'esle'