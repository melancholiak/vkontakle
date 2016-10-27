import curses
import req
import curses
FIELDS = ['photo_id', 'verified', 'sex', 'bdate', 'city', 'country', 'home_town', 
'has_photo', 'photo_50', 'photo_100', 'photo_200_orig', 'photo_200', 'photo_400_orig', 
'photo_max', 'photo_max_orig', 'online', 'lists', 'domain', 'has_mobile', 'contacts', 
'site', 'education', 'universities', 'schools', 'status', 'last_seen', 'followers_count', 
'common_count', 'occupation', 'nickname', 'relatives', 'relation', 'personal', 
'connections', 'exports', 'wall_comments', 'activities', 'interests', 'music', 'movies', 
'tv', 'books', 'games', 'about', 'quotes', 'can_post', 'can_see_all_posts', 
'can_see_audio', 'can_write_private_message', 'can_send_friend_request', 'is_favorite', 
'is_hidden_from_feed', 'timezone', 'screen_name', 'maiden_name', 'crop_photo', 
'is_friend', 'friend_status', 'career', 'military', 'blacklisted', 'blacklisted_by_me']
FIELDS.remove('common_count')
class user:
  def __init__(self,kwargs):
    self.fields={i:kwargs[i] for i in kwargs}
    for i in kwargs:
      setattr(self,i,kwargs[i])
  def display(self,win,globalscr):
    beg=win.getbegyx()
    sz=win.getmaxyx()
    globalscr.setyx(*beg)
    pass
    win.clear()
    win.border(0)
