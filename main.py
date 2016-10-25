import curses
import rootmenu
import submenus
import atoms
import vk
def main(scr):
  scr=curses.initscr()
  curses.curs_set(0)
#parent_window-----------------------------------------------------------------
  #scr.border(0)
  scr.refresh()
  curses.curs_set(1)
  #curses.echo(1)
#root_menu---------------------------------------------------------------------
  left=curses.newwin(12,15,0,0)
  left.border(0)
  left.refresh()
  #will be removed in order to give rootmenu and submenus take control
  #over drawing by passing refferance to windows to special class's 
  #method
  menunames=['{:<12}'.format(i) for i in dir(submenus) if i.count('_')!=4]
  positions = {i:j for i,j in zip(range(10),menunames)}
  for menu_name,position in zip(menunames,range(10)):
    left.addstr(position+1,1,menu_name)
  left.refresh()
#submenu-----------------------------------------------------------------------
  middle=curses.newwin(70,35,0,14)
  middle.border(0)
  middle.refresh()
#atoms------------------------------------------------------------------------
  right=curses.newwin(70,31,0,48)
  right.border(0)
  right.refresh()
#actions----------------------------------------------------------------------
  cur_pos=[1,1]
  left.addstr(*cur_pos,positions[cur_pos[0]-1],curses.A_REVERSE)
  left.refresh()
  while 1:
    key = scr.getch()
    add=0
    if key==curses.KEY_UP and cur_pos[0]!=1:add=-1
    if key==curses.KEY_DOWN and cur_pos[0]!=10: add=1
    if key==curses.KEY_RIGHT and positions[cur_pos[0]-1]=='{:<12}'.format('profile'):
      d=vk.get_p('photo_id','bdate').json()['response'][0]
      for j,i in zip(d,range(len(d))):
        middle.addstr(i+1,1,'{}: {}'.format(j,d[j]))
      middle.refresh()
    if key==curses.KEY_LEFT and positions[cur_pos[0]-1]=='{:<12}'.format('profile'):
      middle.clear()
      middle.border(0)
      middle.refresh()
    left.addstr(*cur_pos,positions[cur_pos[0]-1]);cur_pos[0]+=add
    left.addstr(*cur_pos,positions[cur_pos[0]-1],curses.A_REVERSE)
    left.refresh()
curses.wrapper(main)
