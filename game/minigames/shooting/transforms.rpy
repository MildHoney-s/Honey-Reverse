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






