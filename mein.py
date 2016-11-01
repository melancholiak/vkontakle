import curses
import req
import vkontaCLI
def main(scr):
  scr=curses.initscr()
  win=curses.newwin(40,40)
  curses.curs_set(0)
  u = vkontaCLI.user(req.get_me())
  u.display(win)
curses.wrapper(main)
