import requests

def get_user_collections(self):
    data = {'user_id': self.running_app.CURRENT_USER.django_id}
    headers = {'Authorization': f'Token {self.running_app.CURRENT_USER.auth_token}'}
    
    result = requests.get(f'{self.running_app.main_api_url}collections/', data=data, headers=headers)
    
    return result.json()