import requests
from db_connect import session, user_model


def log_user(self, username, password):

    data = {'username': username, 'password': password}

    result = requests.post(
        f'{self.running_app.main_api_url}auth/login/', data=data)

    if result.status_code == 200:
        csrf_token = result.cookies['csrftoken']
        auth_token = result.json().get('token')
        loged_username = result.json().get('username')
        django_id = result.json().get('id')

        user = session.query(user_model).filter_by(username=username).first()

        if user:
            user.csrf_token = csrf_token
            user.auth_token = auth_token

        else:
            user = user_model(username=loged_username,
                              django_id=django_id,
                              csrf_token=csrf_token,
                              auth_token=auth_token)
            session.add(user)

        session.commit()
        self.running_app.CURRENT_USER = user
        return True