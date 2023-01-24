#!/usr/bin/env python3

import math
import time
import numpy
import argparse
from curses import wrapper, A_DIM, A_BOLD

def draw_globe( stdscr, m : float, radius : int, steps : int ):

    max_y, max_x = stdscr.getmaxyx()

    stdscr.clear()
    # o is the X-width of the outer circle.
    for o in numpy.arange( 0, (2 * math.pi), math.pi / steps ):
        # i is the X-width of each inner circle.
        for i in numpy.arange( 0, (2 * math.pi), math.pi / steps ):

            # Make stuff on the fringes bright.
            attr = A_BOLD if i + o > 8 else A_DIM

            # Modulate the X width of each inner circle based on sin( m )
            # to create the illusion of spherical depth.
            x = (max_x / 2) + (math.cos( o ) * math.sin( i - m ) * radius)
            y = (max_y / 2) + (math.sin( o ) * radius)

            stdscr.addch( int( y ), int( x ), '.', attr )

    stdscr.refresh()

def main( stdscr ):

    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-r', '--radius', action='store', default=15, type=int )

    parser.add_argument(
        '-s', '--steps', action='store', default=5, type=int )

    args = parser.parse_args()

    m = 0

    while True:
        draw_globe( stdscr, m, args.radius, args.steps )
        m = 0.126 + (m % 0.4)
        time.sleep( 0.1 )


if '__main__' == __name__:
    wrapper( main )

