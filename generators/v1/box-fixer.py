# -*- coding: utf-8 -*-
__author__ = '123'

# max rozmiar: 744.09448819 1052.3622047
# max 12 w wierszu, z czego avers i revers, więc tylko 6 żetonów.
# zaczynamy od +30 jako margines

# obsługa xmli
from lxml import etree
# obsługa rekurencyjnego kopiowania opiektów
import sys

from os import walk


path = sys.argv[1]

sys.exit("Do not use if you don't know what are you doing!")
f = []
for (dirpath, dirnames, filenames) in walk(path):
    f.extend(filenames)
    break
for a in f:
    print dirpath+"\\"+a
    b = open(dirpath+"\\"+a)
    svg = etree.XML(b.read())
    b.close()
    for element in svg[3].iter():
        __id = element.get("id")
        if __id == "DIV_BOX":
            # changing DIV_BOX size and x
            """element.set("height", "15")
            element.set("width", "22")
            x = float(element.get("x"))
            print x
            x -= 2.5
            print x
            element.set("x", x.__str__())
            """
            # adding white border to black DIV_BOX
            # element.set("style","fill:#000000;fill-opacity:1;stroke:#ffffff;stroke-width:0.30000001")
        elif __id == "ATTACK_BOX":
            # element.set("style", "fill:#b00000")
            # element.set("id", "ATTACK_BOX")
            pass
        elif __id == "DEF_BOX":
            # element.set("style", "fill:#008000")
            pass
        elif __id == "MOVE_BOX":
            # element.set("style", "fill:#008080")
            pass
        elif __id == "ATACK":
            element.set("id", "ATTACK")
            pass
    b = open(dirpath+"\\"+a, "w+")
    b.write(etree.tostring(svg, pretty_print=True))
