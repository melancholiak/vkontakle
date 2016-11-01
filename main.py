import curses
import req
import tree
def main(scr):
  scr=curses.initscr()
  curses.curs_set(0)
  left=curses.newwin(20,20)
  right=curses.newwin(20,20,0,20)
  tree.root.navigate(scr,left,right)
curses.wrapper(main)
