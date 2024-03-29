import requests
from db_connect import session, user_model


def log_user(self, username, password):

    data = {'username': username, 'password': password}

    result = requests.post(
        f'{self.running_app.main_api_url}auth/login/', data=data)

    if result.status_code == 200:
        csrf_token: str = result.cookies['csrftoken']
        result: dict = result.json()
        auth_token: str = result.get('token')
        loged_username: str = result.get('username')
        django_id: str = result.get('id')

        user = session.query(user_model).filter_by(username=username).first()

        if user:
            user.csrf_token = csrf_token
            user.auth_token = auth_token
            user.logged = True

        else:
            user = user_model(username=loged_username,
                              django_id=django_id,
                              csrf_token=csrf_token,
                              auth_token=auth_token,
                              logged=True)
            session.add(user)

        session.commit()

        return user
    
def user_registration(self, username, password1, password2, email):
    data = {'username': username,
            'password1': password1,
            'password2': password2,
            'email': email}
    result = requests.post(f'{self.running_app.main_api_url}auth/registration/', data=data)
    return True


def get_logged_user():
    user = session.query(user_model).filter_by(logged=True).first()
    if user:
        return user
    return None

def logout(self):
    self.running_app.CURRENT_USER.csrf_token = None
    self.running_app.CURRENT_USER.auth_token = None
    self.running_app.CURRENT_USER.logged = None
    session.commit()
    result = requests.get(f'{self.running_app.main_api_url}auth/logout/')
    return result