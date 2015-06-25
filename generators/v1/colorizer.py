# -*- coding: utf-8 -*-
__author__ = '123'
__version__ = 1
# colorizer.py src.svg dst.svg
# this script takes styles parameters from srv.svg file and sets them in dst.svg
# script requires that src and dst file have grouped path witch id="ICON"
# both need to have the same amount of path
# end file is writen as <dst name>-from-<src name>-colorized.svg

from lxml import etree
import sys


if len(sys.argv) != 3:
    print "USAGE: %s source.svg target.svg" % sys.argv[0]
    sys.exit()


path = '.'



try:
    with open(path + "\\" + sys.argv[1]) as f:
        src = etree.XML(f.read())
    f.close()
except IOError:
    # print "ERROR: No file %s " % (sys.argv[1])
    sys.exit("ERROR: No file %s " % (sys.argv[1]))

try:
    with open(path + "\\" +sys.argv[2]) as f:
        dst = etree.XML(f.read())
    f.close()
except IOError:
    # print "ERROR: No file %s " % (sys.argv[2])
    sys.exit("ERROR: No file %s " % (sys.argv[2]))

src_style = []
src_style2 = []
for element in src[3].iter():
    __id = element.get("id")
    if __id == "ICON":
        for icon in element.iter():
            style = icon.get("style")
            src_style.append(style)
            src_style2.append(style)
        break
        style = src_style.pop(0)

for element in dst[3].iter():
    __id = element.get("id")
    if __id == "ICON":
        for icon in element.iter():
            style = icon.get("style")
            src1 = src_style.pop(0)
            if style:
                print "Changing DST %s TO %s" % (style, src1)
                icon.set("style", src1)
        # break
    elif __id == "ICON2":
        for icon in element.iter():
            style = icon.get("style")
            src1 = src_style2.pop(0)
            if style:
                print "Changing DST %s TO %s" % (style, src1)
                icon.set("style", src1)
        # break
a = sys.argv[1].split('.')
b = sys.argv[2].split('.')

__file = path+ "\\" + b[0]+'-from-'+a[0]+'-colorized.svg'

try:
    with open(__file, 'w+') as f:
        f.write(etree.tostring(dst, pretty_print=True))
    f.close()
    print "INFO: Writen as %s" % __file
except IOError:
    # print "ERROR: Unable to write file %s " % __file
    sys.exit("ERROR: Unable to write file %s " % __file)
