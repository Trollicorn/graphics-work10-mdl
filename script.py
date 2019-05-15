import mdl
from display import *
from matrix import *
from draw import *
from lighting import *
from solid import *
from transform import *
from curve import *

def run(filename):
    """
    This function runs an mdl script
    """
    p = mdl.parseFile(filename)
    if p:
        (commands, symbols) = p
    else:
        print "Parsing failed."
        return
    view = [0,
            0,
            1];
    ambient = [50,
               50,
               50]
    light = [[0.5,
              0.75,
              1],
             [255,
              255,
              255]]
    color = [0, 0, 0]
    areflect = [0.1,
                0.1,
                0.1]
    dreflect = [0.5,
                0.5,
                0.5]
    sreflect = [0.5,
                0.5,
                0.5]
    tmp = new_matrix()
    ident( tmp )
    csystems = [ [x[:] for x in tmp] ]
    screen = new_screen()
    zbuffer = new_zbuffer()
    tmp = []
    step_3d = 100
    consts = ''
    coords = []
    coords1 = []
    symbols['.white'] = ['constants',
                         {'red': [0.2, 0.5, 0.5],
                          'green': [0.2, 0.5, 0.5],
                          'blue': [0.2, 0.5, 0.5]}]
    reflect = '.white'
    transform = {
        "move": translate,
        "rotate": rotate,
        "scale": dilate
    }
    solid = {
        "box": box,
        "sphere": sphere,
        "torus": torus
    }
    print symbols
#    print csystems
    for command in commands:
        op = command['op']
        if op == 'constants':
            pass
        elif op == 'push':
            csystems.append(duplicate(csystems[-1]))
        elif op == 'pop':
            del csystems[-1]
        elif op in transform:
            transform[op](csystems[-1],command['args'])
        elif op in solid:
            solid[op](tmp,command['args'])
            matrix_mult(csystems[-1],tmp)
            print op
            print command
            if command['constants'] is None:
                draw_polygons(tmp,screen,zbuffer,color,view, ambient, light, areflect, dreflect, sreflect)
            else:
                print "USES CONSTANT"
                const = command['constants']
                print symbols[const]
        #        print symbols[command['constants']]
        #        draw_polygons(tmp,screen,zbuffer,color,view, ambient, light, areflect, dreflect, sreflect)
        else:
            pass
        #    print command['op']
        #    print command
