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

#sys.exit("Do not use if you don't know what are you doing!")
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
            # element.set("id", "ATTACK")
            pass
        elif __id == "DIV_TEXT":
            """
            x = float(element.get("x"))
            print x
            x += 1.5
            print x
            element.set("x", x.__str__())
            # element.set("id", "DIV_TEXT")
            """
            pass
        elif __id == "ARMY" or __id == "DIV":
            """
            x = float(element.get("x"))
            print x
            x += 1.5
            print x
            element.set("x", x.__str__())
            # element.set("id", "DIV")
            """
            pass
        elif __id == "NAME_TEXT" or __id == "NAME_TEXT2" :
            """
            x = float(element.get("x"))
            print x
            x += 1
            print x
            element.set("x", x.__str__())
            #element.set("id", "NAME_TEXT")
            """
            """
            style= "font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;" \
                      "font-size:8.75px;line-height:100%;font-family:sans-serif;-inkscape-font-specification:" \
                      "\'sans-serif, Normal\';text-align:left;writing-mode:lr-tb;text-anchor:start"
            element.set("style", style)
            """
            # element.set("x", "1.5")
            pass
        elif __id == "NAME" or __id == "NAME2":
            # element.set("x", "1.5")
            """
            x = float(element.get("x"))
            print x
            x += 1
            print x
            element.set("x", x.__str__())
            # element.set("id", "NAME_TEXT")
            """
            pass

        elif __id == "ICON":
            # """
            for icon in element.iter():
                style = icon.get("style")
                src1 = "fill:#ffffff"
                if style:
                    print "Changing DST %s TO %s" % (style, src1)
                    icon.set("style", src1)
            # break
            # """
        elif __id == "ICON2":
            # """
            for icon in element.iter():
                style = icon.get("style")
                src1 = "fill:#ffffff"
                if style:
                    print "Changing DST %s TO %s" % (style, src1)
                    icon.set("style", src1)
            # break
            # """
            pass
    b = open(dirpath+"\\white\\"+a, "w+")
    b.write(etree.tostring(svg, pretty_print=True))
