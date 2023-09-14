import requests

from tools.decorators import authorization_decorator
from db_connect import session, order_model

@authorization_decorator
def get_user_collections(self, headers):
    data = {'user_id': self.running_app.CURRENT_USER.django_id}
    result = requests.get(f'{self.running_app.main_api_url}collections/', data=data, headers=headers) 
    result = result.json()
    return result

@authorization_decorator
def get_cards_from_collection(self, headers, collection):
    
    data = {'collection_id': collection['id']}
    result = requests.get(f'{self.running_app.main_api_url}cards/', data=data, headers=headers)
    
    cards = result.json()
    
    return collection, cards

@authorization_decorator
def change_card_position(self, headers, word_id=None, replace=None, collection_id=None):
    data = {'word_id': int(word_id),
            'replace': replace,
            'collection_id': collection_id}
    result = requests.post(f'{self.running_app.main_api_url}cards/change_position/', data=data, headers=headers)
    
    result = result.json()
    new_collection = result['new_collection']
    return new_collection
    
    
    
