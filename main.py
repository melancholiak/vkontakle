import curses
import rootmenu
import submenus
import atoms
def main(scr):
	scr=curses.initscr()
	curses.curs_set(0)
#parent_window-----------------------------------------------------------------
	scr.border(0)
	scr.refresh()
#root_menu---------------------------------------------------------------------
	left=curses.newwin(12,15,0,0)
	left.border(0)
	left.refresh()
	#will be removed in order to give rootmenu and submenus take control
	#over drawing by passing refferance to windows to special class's 
	#method
	for menu_name,position\
	in zip([i for i in dir(submenus) if i.count('_')!=4],range(10)):
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
	scr.getkey()
curses.wrapper(main)
