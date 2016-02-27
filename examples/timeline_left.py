"""
Translation of basic_left.py to use the Timeline object.

"""

from labella.scale import LinearScale
from labella.timeline import TimelineSVG, TimelineTex
from labella.utils import COLOR_10

def main():
    items = [
            {'time': 1, 'width': 50},
            {'time': 2, 'width': 50},
            {'time': 3, 'width': 50},
            {'time': 3, 'width': 50},
            {'time': 3, 'width': 50},
            {'time': 304, 'width': 50},
            {'time': 454, 'width': 50},
            {'time': 454, 'width': 50},
            {'time': 454, 'width': 50},
            {'time': 804, 'width': 50},
            {'time': 804, 'width': 70},
            {'time': 804, 'width': 50},
            {'time': 804, 'width': 50},
            {'time': 854, 'width': 50},
            {'time': 854, 'width': 50}]

    options = {
        'initialWidth': 112,
        'initialHeight': 1000,
        'scale': LinearScale(),
        'direction': 'left',
        'dotColor': '#000000',
        'labelBgColor': COLOR_10,
        'linkColor': COLOR_10,
        'labelPadding': {'left': 0, 'right': 0, 'top': 0, 'bottom': 0},
        'labella': {
            'minPos': 0,
            'maxPos': 960,
            'nodeHeight': 12,
            },
        'showTicks': False
        }

    tl = TimelineSVG(items, options=options)
    tl.export('timeline_left.svg')

    tl = TimelineTex(items, options=options)
    tl.export('timeline_left.tex')

if __name__ == '__main__':
    main()
