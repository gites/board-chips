# -*- coding: utf-8 -*-
__author__ = '123'

# obsługa xmli
from lxml import etree
# obsługa rekurencyjnego kopiowania opiektów
import sys

from os import walk
print len(sys.argv)
if len(sys.argv) != 3:
    print "EXAMPLE: %s res\wb-95\gu white" % sys.argv[0]
    sys.exit("USAGE: %s <path_to_icon_dir> <white or black>" % sys.argv[0])

path = sys.argv[1]
print path
if sys.argv[2] == 'white':
    color = '#ffffff'
elif sys.argv[2] == 'black':
    color = '#000000'
else:
    sys.exit("Chose your destiny... white or black not %s" % sys.argv[2])

idir = sys.argv[2]

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
        if __id == "ICON":
            for icon in element.iter():
                style = icon.get("style")
                src1 = "fill:"+color
                if style:
                    print "Changing DST %s TO %s" % (style, src1)
                    icon.set("style", src1)
        elif __id == "ICON2":
            # """
            for icon in element.iter():
                style = icon.get("style")
                src1 = "fill:"+color
                if style:
                    print "Changing DST %s TO %s" % (style, src1)
                    icon.set("style", src1)
            pass
    b = open(dirpath+"\\"+idir+"\\"+a, "w+")
    b.write(etree.tostring(svg, pretty_print=True))
