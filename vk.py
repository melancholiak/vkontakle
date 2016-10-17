import requests
ACESS='6c9c5cadb1ebf6aa2fe4865b6efc3a4fc318e7e2175a1c3c7f1eddd2e2bef87c9e6d4997e8d6bb501229d'
USER_ID='246194626'

def get_profile(acess_token,user_id,fields):
	return requests.get('https://api.vk.com/method/users.get?acces_token={0}&user_ids={1}&fields={2}&v=5.57'.format(acess_token,user_id,','.join(fields)))
def get_p(fields):
	return get_profile(ACESS,USER_ID,fields)		

#r = requests.get('https://api.vk.com/method/messages.getDialogs?PARAMETERS&access_token=2e88d23fa0865126f3dd13914c545af4f516141b2ed13f3fa0e5169078ebe7c15abb7c3673a423052eb72&v=V')
