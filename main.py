class Square:

    def __init__(self,pos):
        self.n = None
        self.ne = None
        self.e = None
        self.se = None
        self.s = None
        self.sw = None
        self.w = None
        self.nw = None

        self.own = None
        self.pos = pos

class Board:

    def __init__(self):

        order = ['nw','n','ne','w','c','e','sw','s','se']

        self.nw = Square('nw')
        self.n = Square('n')
        self.ne = Square('ne')
        self.w = Square('w')
        self.c = Square('c')
        self.e = Square('e')
        self.sw = Square('sw')
        self.s = Square('s')
        self.se = Square('se')

        self.win = None

        # northwest corner
        self.nw.e = self.n
        self.nw.e.w = self.nw

        self.nw.s = self.w
        self.nw.s.n = self.nw

        self.nw.se = self.c
        self.nw.se.nw = self.nw

        # northeast corner
        self.ne.w = self.n
        self.ne.w.e = self.ne

        self.ne.s = self.e
        self.ne.s.n = self.ne

        self.ne.sw = self.c
        self.ne.sw.ne = self.ne

        # southeast corner
        self.se.w = self.s
        self.se.w.e = self.se

        self.se.n = self.e
        self.se.n.s = self.se

        self.se.nw = self.c
        self.se.nw.se = self.se

        # southwest corner
        self.sw.e = self.s
        self.sw.e.w = self.sw

        self.sw.n = self.w
        self.sw.n.s = self.sw

        self.sw.ne = self.c
        self.sw.ne.sw = self.sw

        # north middle
        self.n.s = self.c
        self.n.s.n = self.n

        # east middle
        self.e.w = self.c
        self.e.w.e = self.e

        # south middle
        self.s.n = self.c
        self.s.n.s = self.s

        # west middle
        self.w.e = self.c
        self.w.e.w = self.w


board = Board()
print(board.nw.se.se.pos)
