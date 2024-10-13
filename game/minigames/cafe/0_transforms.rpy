transform alpha(a):
    alpha a
transform rotate(r):
    rotate_pad False
    rotate r
transform zoom(z, n=False):
    nearest n
    zoom z
transform flip(x=1, y=1, n=False):
    nearest n
    xzoom x yzoom y
transform additive(a):
    additive a

# spin

# positions
init -10:
    $ left= Position(yalign=1.0,xalign=0.1)
    $ right= Position(yalign=1.0,xalign=0.9)
    $ midleft= Position(yalign=1.0,xalign=0.3)
    $ midright= Position(yalign=1.0,xalign=0.7)
    $ center= Position(yalign=1.0,xalign=0.5)






