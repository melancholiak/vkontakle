import curses
def main(scr):
  scr=curses.initscr()
  curses.curs_set(0)
  scr.getch()
curses.wrapper(main)
