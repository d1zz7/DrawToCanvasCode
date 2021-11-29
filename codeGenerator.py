def paint(x1, y1, x2, y2, color, width):
    return 'wn.create_oval({x1}, {y1}, {x2}, {y2}, fill="{color}", outline="{color}", width={width})\n'.format(x1=x1, y1=y1, x2=x2, y2=y2, color=color, width=width)


def circle(x, y, color, width):
    return 'wn.create_oval({x}, {y}, {x} + {width}, {y} + {width}, width={width}, fill="{color}", outline="{color}")\n'.format(x=x, y=y, color=color, width=width)



def square(x, y, color, width):
    return 'wn.create_rectangle({x}, {y}, {x} + 30, {y} + 30, width={width}, fill="{color}", outline="{color}")\n'.format(x=x, y=y, color=color, width=width)

def triangle(x,y, color, width):
    return 'wn.create_polygon({x}, {y}, {x} - ({width}*2/2), {y} + {width}*2, {x} + ({width}*2/2), {y} + {width}*2, fill="{color}", outline="{color}", width=5)\n'.format(x=x, y=y, color=color, width=width)


def line(x1, y1, x2, y2, width, color):
    return 'wn.create_line({lineStartX}, {lineStartY}, {x}, {y}, width={width}, fill="{color}")\n'.format(lineStartX=x1, lineStartY=y1, x=x2, y=y2, color=color, width=width)
