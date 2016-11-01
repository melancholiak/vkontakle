import requests
ACESS='6c9c5cadb1ebf6aa2fe4865b6efc3a4fc318e7e2175a1c3c7f1eddd2e2bef87c9e6d4997e8d6bb501229d'
UID='246194626'
FIELDS = ['sex', 'bdate', 'city', 'country', 
 'online', 
'activities', 'interests', 
 'quotes']
def _get(method,**kwargs):
  return requests.get('https://api.vk.com/method/{}?{}'.format(method,\
            '&'.join(['{}={}'.format(i,kwargs[i]) for i in kwargs])))
def get(method,**kwargs):
  resp = _get(method,**kwargs).json()
  if not 'error' in resp:return resp['response'][0]
  return resp['error']['error_msg']
def get_me():
  return get('users.get',fields=','.join(FIELDS),user_ids=UID,ACESS_TOKEN=ACESS)
