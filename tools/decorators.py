def authorization_decorator(func):
    def inner(self, *args, **kwargs):
        headers = {'Authorization': f'Token {self.running_app.CURRENT_USER.auth_token}'}
        result = func(self, headers, *args, **kwargs)
        return result
    return inner