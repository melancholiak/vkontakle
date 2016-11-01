import curses
import req
import curses
class tree(object):
  def __init__(self,name=None,children=[]):
    self.name = name
    self.children = children
  def __le__(self,child):
    self.children.append(child)
  def __str__(self):
    return str(self.name)
  def show(self,win,line=-1):
    win.erase()
    win.border(0)
    y,x=1,1
    for i in self.children:
      win.addstr(y,x,str(i),line==y and curses.A_REVERSE)
      y+=1
      if y == win.getmaxyx()[0]:pass
    win.refresh()
  def navigate(self,parent,win,other_win):
    miny,maxy=win.getbegyx()[0]+1,win.getmaxyx()[0]+1
    y,x=win.getbegyx();y+=1;x+=1
    m={i:j for i,j in zip(range(y,y+len(self.children)),self.children)}
    self.show(win,y)
    m[y].show(other_win)
    while 1:
      win.refresh()
      key=parent.getch()
      if key == curses.KEY_UP and y!=miny and y!=0: y-=1
      if key == curses.KEY_DOWN and y!=maxy and y!=len(m): y+=1
      if key == curses.KEY_RIGHT: m[y].navigate(parent,win,other_win)
      if key == curses.KEY_LEFT: return
      self.show(win,y)
      m[y].show(other_win)
class entity:
  def __init__(self,name,val):
    self.name = name
    self.val = val
  def __str__(self):
    return '{}: {}'.format(str(self.name),str(self.val))
  def show(self,win):
    win.erase()
    win.border(0)
    win.addstr(1,1,str(self.val))
    win.refresh()
  def navigate(self,parent,win,other_win):
    self.show(other_win)
root = tree(name='root')
root <= tree('profile',[entity(i,j) for i,j in {'name':'Vasya','online':1}.items()])
root <= tree('profile',[entity(i,j) for i,j in {'name':'Vasyaa','online':2}.items()])
root <= tree('profile',[entity(i,j) for i,j in {'name':'Vasyaaa','online':3}.items()])
root <= tree('profile',[entity(i,j) for i,j in {'name':'Vasyaaaa','online':4}.items()])
