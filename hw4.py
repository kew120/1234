def rep_char(c,n):
    print(c*n)

def draw_line_string(a):
    rep_char('-',a)
    print(msg1)
    print(msg2)
    rep_char('-',a)

name = input('Input his/her name: ')
msg1 = ' Hello '+name+', '
msg2 = ' Welcome to Seoul. '
nstr = len(msg1) if (len(msg1)>len(msg2)) else len(msg2)
draw_line_string(nstr)
