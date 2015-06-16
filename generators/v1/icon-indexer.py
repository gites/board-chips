# -*- coding: utf-8 -*-
__author__ = '123'


import sys
from os import walk
from lxml import etree
from copy import deepcopy

class A4:
    """
    base class representing A4 paper sheet
    """
    def __init__(self):
        self.x_start = 0
        self.y_start = 0
        self.x_end = 0
        self.y_end = 0
        self.num = 0  # current counter on page
        self.xstep = 0  # px X steep for each counter
        self.ystep = 0   # px Y steep
        self.cpr = 0  # cpr = counters per row
        self.cpc = 0  # cpc = counter per column
        self.max = 0  # max counters on a4 page
        self.a4 = False

    def create(self, __type):
        """
        method for creating svg A4 object
        :param __type: used counters type
        :return: True on success, False on error. A4 page is stored as svg in self.a4
        """
        try:
            with open('res\\a4.svg', 'r') as f:
                self.a4 = etree.XML(f.read())
            f.close()
        except IOError:
            sys.exit("ERROR: No res\\a4.svg file!")

        # TODO: hymmmm should this be in A4 class or CounterWB95?
        if __type == 'WB95' or __type == 'WB-95':
            self.x_start = 35
            self.y_start = 35
            self.x_end = 659
            self.y_end = 0
            self.xstep = 53
            self.ystep = self.xstep
            self.cpr = 1  # cpr = counters per row
            self.cpc = 18  # cpc = counter per column
            self.max = self.cpr * self.cpc
        elif __type == 'INDEX':
            self.x_start = 35
            self.y_start = 35
            self.x_end = 659
            self.y_end = 0
            self.xstep = 230
            self.ystep = 53
            self.cpr = 3  # cpr = counters per row
            self.cpc = 18  # cpc = counter per column
            self.max = self.cpr * self.cpc
        else:
            sys.exit("ERROR: Unknown counter type %s" % __type)

        return True

    def add(self, __counter, __name):
        """
        method for adding counters to page
        :param __counter: counter (face and back)
        :return: True on success, False on error.
        """
        if self.num >= self.max:
            return False
        else:
            __x = self.x_start + ((self.num % self.cpr) * self.xstep)
            __y = self.y_start + ((self.num / self.cpr) * self.ystep)
            print __x, __y
            __trans = "translate(%f,%f)" % (__x, __y)
            __counter[0].set("transform", __trans)
            self.a4[3].append(deepcopy(__counter[0]))
            __x += 60
            __y += 30
            # TODO: add file name
            __error = "<g id=\"layer1\">" \
                      "<text x=\"" + str(__x) + "\" y=\"" + str(__y) + "\" id=\"name\" " \
                      "style=\"font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;" \
                      "font-size:15px;line-height:100%;font-family:sans-serif;-inkscape-font-specification:\'" \
                      "sans-serif, Normal\';text-align:left;writing-mode:lr-tb;text-anchor:start\">" \
                      "<tspan id=\"nanana\" x=\"" + str(__x) + "\" y=\"" + str(__y) + "\">" \
                      + __name + "</tspan></text></g>"

            __root = etree.XML(__error)
            self.a4[3].append(deepcopy(__root))
            self.num += 1
            return True
"""
            __x = self.x_end - ((self.num % self.cpr) * self.xstep)
            # __y = self.y_start + ((self.num / self.cpr) * self.ystep)
            __trans = "translate(%f,%f)" % (__x, __y)
            __counter[1].set("transform", __trans)
            self.a4[3].append(deepcopy(__counter[1]))
            self.num += 1
            return True
"""



if len(sys.argv) == 2:
    path = sys.argv[1]
else:
    path = "res/wb-95/gu/"

f = []
for (dirpath, dirnames, filenames) in walk(path):
    # print dirpath, dirnames, filenames
    f.extend(filenames)
    break

sheets = []
page = A4()
page.create('INDEX')

for i in xrange(0, len(f)):
    print dirpath+"\\"+f[i]
    b = open(dirpath+"\\"+f[i])
    svg = etree.XML(b.read())
    b.close()
    if page.add((svg[3], svg[3]), f[i]):
        pass
    else:
        sheets.append(page)
        page = A4()
        page.create('WB95')
        page.add((svg[3], svg[3]), f[i])
        print "INFO: another page created"

sheets.append(page)

for i in xrange(0, len(sheets)):
    page = sheets[i].a4
    name = 'WB95-index-sheet-%d.svg' % (i+1)
    f = open(name, 'w+')
    f.write(etree.tostring(page, pretty_print=True))
    f.close()