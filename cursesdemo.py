from curses import *
from time import sleep
def main(scr):
	upper=\
	{
		(1,1):'myprofile',
		(2,1):'news',
		(3,1):'messages',
		(4,1):'friends'
	}
	cursor=1,1
	scr=initscr()
	scr.border(0)
	scr.refresh()
	curs_set(0)
	for i in upper:
		scr.addstr(*i,upper[i])
		scr.refresh()
	scr.addstr(1,1,upper[(1,1)],A_REVERSE)
	key=0
	while key!=ord('q'):
		key=scr.getch()
		if key==KEY_UP:
			scr.addstr(*cursor,upper[cursor])
			cursor=cursor[0]-1,cursor[1]
			try:scr.addstr(*cursor,upper[cursor],A_REVERSE)
			except:
				cursor=cursor[0]+1,cursor[1]
				scr.addstr(*cursor,upper[cursor],A_REVERSE)
			scr.refresh()
		if key==KEY_DOWN:
			scr.addstr(*cursor,upper[cursor])
			cursor=cursor[0]+1,cursor[1]
			try:scr.addstr(*cursor,upper[cursor],A_REVERSE)	
			except:
				cursor=cursor[0]-1,cursor[1]
				scr.addstr(*cursor,upper[cursor],A_REVERSE)
			scr.refresh()
wrapper(main)
