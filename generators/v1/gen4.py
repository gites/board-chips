# -*- coding: utf-8 -*-
__author__ = '123'



import csv
import operator
import sys
from lxml import etree
from copy import deepcopy
# ---------------------------------------------------------------------------
class Color:
    # Class for setting counters and borders colors based on country codes
    # reads data from csv file added as third argument to script
    # sets everything in colours2
    colours2 = {}

    def __init__(self, __file):
        try:
            with open(__file) as __csvfile:
                __reader = csv.DictReader(__csvfile)
                __color_list = sorted(__reader, key=operator.itemgetter('COUNTRY'), reverse=True)
        except IOError:
            sys.exit("ERROR: No file %s " % __file)

        for __line in __color_list:
            self.colours2[__line['COUNTRY']] = __line

# ---------------------------------------------------------------------------
class Counter:
    # Base Class for Counters
    def __init__(self):
        self.x = 0
        self.y = 0
        self.backIcon = ""
        self.faceIcon = ""
        self.type = ""
        self.color = ""
        self.borderColor = ""
        self.country = ""
        self.unitName = "Counter"
        self.path = ""

    def create(self, __type, __csvrow):
        if __type == 'WB95' or __type == 'WB-95':
            __counter = CounterWB95(__csvrow)
            return __counter.make_svg()
        else:
            sys.exit("ERROR: Unknown counter type %s" % __type)

    def read_raw_svg(self, __path, __type, __icon):
        # reads svg files witch icons
        try:
            with open(__path.lower()+__type.lower()+'\\'+__icon.lower(), 'r') as __f:
                root = etree.XML(__f.read())
            __f.close()
            return root
        except IOError:
            sys.exit("ERROR: No res file %s in %s%s\\" % (__icon, __path, __type))

    def make_svg_err(self):
        """
        :returns "ER" icon
        """
        __error = "<g id=\"layer1\">" \
                  "<text style=\"font-size:40px;fill:#ff0000;\" x=\"-0.78125\" y=\"39.087105\" id=\"ER\">ER</text>" \
                  "</g>"
        __root = etree.XML(__error)
        return __root, __root

# ---------------------------------------------------------------------------
class CounterWB95(Counter):
    # Counter for WB95 games
    def __init__(self, csvrow):
        Counter.__init__(self)
        self.x = 53.150  # 53.150px -> 15mm on paper
        self.y = 53.150
        self.country = csvrow['COUNTRY'].upper()

        if csvrow['COUNTRY']:
            self.country = csvrow['COUNTRY'].upper()
            self.color = color.colours2[self.country]['BACKGROUND']
            self.borderColor = color.colours2[self.country]['BORDER']
            self.divBoxColor = color.colours2[self.country]['DIV_BOX']
            self.divBoxBorderColor = color.colours2[self.country]['DIV_BOX_BORDER']
            self.attackBoxColor = color.colours2[self.country]['ATTACK_BOX']
            self.defBoxColor = color.colours2[self.country]['DEF_BOX']
            self.moveBoxColor = color.colours2[self.country]['MOVE_BOX']
        else:
            self.quit("country", csvrow['UNIT NAME'], csvrow['ARMY-DIV'])
        # type is handled make_svg
        self.type = csvrow['TYPE'].upper()

        if csvrow['UNIT NAME']:
            self.unitName = csvrow['UNIT NAME']
        else:
            self.warn("name", self.unitName, self.div)
            self.unitName = csvrow['UNIT NAME']
        # army/div is optional
        self.div = csvrow['ARMY-DIV']

        if csvrow['SIZE'] or self.type == 'HQ':
            self.size = csvrow['SIZE']
        else:
            self.warn("size", self.unitName, self.div)
            self.unitName = csvrow['UNIT NAME']

        # face settings
        if csvrow['ICON1']:
            self.faceIcon = csvrow['ICON1']
        else:
            self.warn("face icon", self.unitName, self.div)

        if csvrow['ATTACK1'] or self.type == 'HQ':
            self.faceAttack = csvrow['ATTACK1']
        else:
            self.warn("face attack", self.unitName, self.div)
            self.faceAttack = csvrow['ATTACK1']
        # defence only in artillery
        self.faceDefense = csvrow['DEFENSE1']

        if csvrow['MOVEMENT1'] or self.type == 'HQ':
            self.faceMove = csvrow['MOVEMENT1']
        else:
            self.warn("face movement", self.unitName, self.div)
            self.faceMove = csvrow['MOVEMENT1']
        # back settings
        # back icon only in artillery
        self.backIcon = csvrow['ICON2']

        if csvrow['ATTACK2'] or self.type == 'HQ':
            self.backAttack = csvrow['ATTACK2']
        else:
            self.warn("back attack icon", self.unitName, self.div)
            self.backAttack = csvrow['ATTACK2']

        if csvrow['MOVEMENT2'] or self.type == 'HQ':
            self.backMove = csvrow['MOVEMENT2']
        else:
            self.warn("back movement", self.unitName, self.div)
            self.backMove = csvrow['MOVEMENT2']
        # defence only in artillery
        self.backDefense = csvrow['DEFENSE2']

        # stars - what if on face there are 2 stars, and on back 1....
        # stars are optional, if there is more than for rest are skipped
        self.whiteStar = csvrow['WHITE STAR']
        self.blackStar = csvrow['BLACK STAR']
        self.yellowStar = csvrow['YELLOW STAR']
        self.blueStar = csvrow['BLUE STAR']
        if self.whiteStar:
            self.whiteStar = int(csvrow['WHITE STAR'])
        else:
            self.whiteStar = 0
        if self.blackStar:
            self.blackStar = int(csvrow['BLACK STAR'])
        else:
            self.blackStar = 0
        if self.yellowStar:
            self.yellowStar = int(csvrow['YELLOW STAR'])
        else:
            self.yellowStar = 0
        if csvrow['BLUE STAR']:
            self.blueStar = int(csvrow['BLUE STAR'])
        else:
            self.blueStar = 0
        # TODO: add sanity checks (mandatory fields for etch counter type)
        self.path = 'res\\wb-95\\'

    def warn(self, __why, __name, __army):
        # print "-->WARNING: CSV Line %i. No %s for unit: %s/%s (name/div)" % (csv_line, __why, __name, __army)
        # line numbers are invalid because script operates on csv sorted in memory by country, not raw data from file
        print "-->WARNING: No %s for unit: %s/%s (name/div)" % (__why, __name, __army)

    def quit(self, __why, __name, __army):
        # sys.exit("----->EXIT: CSV Line %i. No %s for unit: %s/%s (name/div)" % (csv_line, __why, __name, __army))
        # line numbers are invalid because script operates on csv sorted in memory by country, not raw data from file
        sys.exit("----->EXIT: No %s for unit: %s/%s (name/div)" % (__why, __name, __army))

    def make_svg(self):
        if self.type == 'HQ':
            return self.make_svg_hq()
        elif self.type == 'GU':
            return self.make_svg_gu()
        # GU works for arty
        # elif self.type == 'ART':
        #    return self.make_svg_art()
        elif self.type == 'AIR':
            return self.make_svg_err()
            #return self.make_svg_air()
        else:
            print "--> WARNING:  CSV Line %i. Unknown type %s" % (csv_line, self.type)
            return self.make_svg_err()

    def make_svg_hq(self):
        """
        makes HQs, based on country, commander name and army or corps number
        source SVG need to have ids "ARMY", "COMMANDER", "BACKGROUND" in correct elements
        to be adjusted by script ex: look on ru-hq.svg or de-hq.svg
        :return: svg code for face and back of a counter without svg "headers",
         need to embedded in to svg document
        """
        face_root = self.read_raw_svg(self.path, self.type, self.faceIcon)
        # set counter specific names, etc based on IDs in svg elements
        for element in face_root[3].iter():
            __id = element.get("id")
            if __id == 'ARMY':
                element.text = self.div
            elif __id == 'NAME':
                element.text = self.unitName
            elif __id == 'BACKGROUND':
                __style = "fill:"+self.color+";fill-opacity:1;stroke:"+self.borderColor+";stroke-width:0.55318326"
                element.set("style", __style)

        print "ADDING: %s/%s" % (self.unitName, self.div)
        return [face_root[3], face_root[3]]

    def make_svg_gu(self):
        """
        makes GU (ground units). if no backIcon is specified faceIcon is used
        """
        __face_root = self.read_raw_svg(self.path, self.type, self.faceIcon)
        # set counter specific names, etc based on IDs in svg elements
        # face
        for element in __face_root[3].iter():
            __id = element.get("id")
            if __id == 'ARMY' or __id == 'DIV':
                element.text = self.div
            elif __id == 'NAME':
                element.text = self.unitName
                __style = "font-size:8.75px;text-anchor: middle;font-family:sans-serif;" \
                          "text-align:right;letter-spacing:0px;fill:"+self.borderColor+";fill-opacity:1;"
                element.set("style", __style)
            elif __id == 'BACKGROUND':
                __style = "fill:"+self.color+";fill-opacity:1;stroke:"+self.borderColor+";stroke-width:0.55318326"
                element.set("style", __style)
            elif __id == 'SIZE':
                element.text = self.size
                __style = "fill:"+self.borderColor+";fill-opacity:1;"
                element.set("style", __style)
            elif __id == 'ATTACK':
                element.text = self.faceAttack
            elif __id == 'DEFENSE':
                element.text = self.faceDefense
            elif __id == 'MOVE':
                element.text = self.faceMove
            elif __id == "ATTACK_BOX":
                element.set("style", "fill:"+self.attackBoxColor)
            elif __id == "DEF_BOX":
                element.set("style", "fill:"+self.defBoxColor)
            elif __id == "MOVE_BOX":
                element.set("style", "fill:"+self.moveBoxColor)
            elif __id == "DIV_BOX":
                element.set("style", "fill:"+self.divBoxColor+";fill-opacity:1;stroke:" \
                            + self.divBoxBorderColor+";stroke-width:0.30000001")
        # back

        if self.backIcon == "":
            self.backIcon = self.faceIcon
        __back_root = self.read_raw_svg(self.path, self.type, self.backIcon)

        for element in __back_root[3].iter():
            __id = element.get("id")
            if __id == 'ARMY' or __id == 'DIV':
                element.text = self.div
            elif __id == 'NAME':
                element.text = self.unitName
                __style = "font-size:8.75px;text-anchor: middle;font-family:sans-serif;" \
                          "text-align:right;letter-spacing:0px;fill:"+self.borderColor+";fill-opacity:1;"
                element.set("style", __style)
            elif __id == 'BACKGROUND':
                __style = "fill:"+self.color+";fill-opacity:1;stroke:"+self.borderColor+";stroke-width:0.55318326"
                element.set("style", __style)
            elif __id == 'SIZE':
                element.text = self.size
                __style = "fill:"+self.borderColor+";fill-opacity:1;"
                element.set("style", __style)
            elif __id == 'ATTACK':
                element.text = self.backAttack
            elif __id == 'DEFENSE':
                element.text = self.backDefense
            elif __id == 'MOVE':
                element.text = self.backMove
            elif __id == "ATTACK_BOX":
                element.set("style", "fill:"+self.attackBoxColor)
            elif __id == "DEF_BOX":
                element.set("style", "fill:"+self.defBoxColor)
            elif __id == "MOVE_BOX":
                element.set("style", "fill:"+self.moveBoxColor)
            elif __id == "DIV_BOX":
                element.set("style", "fill:"+self.divBoxColor+";fill-opacity:1;stroke:" \
                            + self.divBoxBorderColor+";stroke-width:0.30000001")
        # stars

        __stars = self.blackStar + self.whiteStar + self.yellowStar + self.blueStar

        if __stars > 4:
            print "--> WARNING: CSV Line %i. Only 4 stars allowed on counter. Skipping extra stars..." % csv_line
            __stars = 4

        __stars_table = []
        if __stars:
            __star_root = self.read_raw_svg(self.path, "", "star.svg")
            for __element in __star_root[3].iter():
                __id = __element.get("id")
                if __id == 'STAR1':
                    __stars_table.append(__element)
                elif __id == 'STAR2':
                    __stars_table.append(__element)
                elif __id == 'STAR3':
                    __stars_table.append(__element)
                elif __id == 'STAR4':
                    __stars_table.append(__element)

        for __s in xrange(0, __stars):
            if self.blackStar:
                if self.color == "#000000":
                    __style = "fill:#000000;fill-opacity:1;stroke:"+self.borderColor+";stroke-width:0.38"
                    __stars_table[__s].set("style", __style)
                else:
                    __style = "fill:#000000;fill-opacity:1;stroke:#000000;stroke-width:0.38"
                    __stars_table[__s].set("style", __style)
                __face_root[3].append(deepcopy(__stars_table[__s]))
                __back_root[3].append(__stars_table[__s])
                self.blackStar -= 1
            elif self.whiteStar:
                __style = "fill:#ffffff;fill-opacity:1;stroke:#ffffff;stroke-width:0.38"
                __stars_table[__s].set("style", __style)
                __face_root[3].append(deepcopy(__stars_table[__s]))
                __back_root[3].append(__stars_table[__s])
                self.whiteStar -= 1
            elif self.yellowStar:
                __style = "fill:#ffff00;fill-opacity:1;stroke:#ffff00;stroke-width:0.38"
                __stars_table[__s].set("style", __style)
                __face_root[3].append(deepcopy(__stars_table[__s]))
                __back_root[3].append(__stars_table[__s])
                self.yellowStar -= 1
            elif self.blueStar:
                __style = "fill:#0000ff;fill-opacity:1;stroke:#0000ff;stroke-width:0.38"
                __stars_table[__s].set("style", __style)
                __face_root[3].append(deepcopy(__stars_table[__s]))
                __back_root[3].append(__stars_table[__s])
                self.blueStar -= 1
        # TODO: if no army/div is specified then change army_box color to background
        if self.div:
            pass
        else:
            __style = "fill:"+self.color+";"
            for element in __face_root[3].iter():
                __id = element.get("id")
                if __id == 'ARMY_BOX' or __id == 'DIV_BOX':
                    element.set("style", __style)
            for element in __back_root[3].iter():
                __id = element.get("id")
                if __id == 'ARMY_BOX' or __id == 'DIV_BOX':
                    element.set("style", __style)

        print "ADDING: %s/%s" % (self.unitName, self.div)
        return [__face_root[3], __back_root[3]]
    """
    def make_svg_art(self):
        print "-----> ART BUM BUM!"
    """
    """
    def make_svg_air(self):
        print "-----> AIR wziiuuuu tratratara!"
    """

# ---------------------------------------------------------------------------
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
            self.cpr = 6  # cpr = counters per row
            self.cpc = 18  # cpc = counter per column
            self.max = self.cpr * self.cpc
        else:
            sys.exit("ERROR: Unknown counter type %s" % __type)

        return True

    def add(self, __counter):
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
            __trans = "translate(%f,%f)" % (__x, __y)
            __counter[0].set("transform", __trans)
            self.a4[3].append(deepcopy(__counter[0]))

            __x = self.x_end - ((self.num % self.cpr) * self.xstep)
            # __y = self.y_start + ((self.num / self.cpr) * self.ystep)
            __trans = "translate(%f,%f)" % (__x, __y)
            __counter[1].set("transform", __trans)
            self.a4[3].append(deepcopy(__counter[1]))
            self.num += 1
            return True


# /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
if len(sys.argv) != 4:
    print "USAGE: %s <counter type> <counters.csv> <colours.csv>" % sys.argv[0]
    sys.exit()

# TODO: add command line arguments
# TODO: output name based on counters.csv name
svg = []

color = Color(sys.argv[3])

try:
    with open(sys.argv[2]) as csvfile:
        reader = csv.DictReader(csvfile)
        sortedlist = sorted(reader, key=operator.itemgetter('COUNTRY'), reverse=True)
except IOError:
    sys.exit("ERROR: No file %s " % (sys.argv[2]))
csv_line = 1
for row in sortedlist:
    counter = Counter()
    tmpsvg = counter.create(sys.argv[1].upper(), row)
    svg.append(tmpsvg)
    csv_line += 1


sheets = []
page = A4()
page.create(sys.argv[1].upper())
print "INFO: page created"
# Add counters to page
for i in xrange(0, len(svg)):
    if page.add(svg[i]):
        pass
    else:
        sheets.append(page)
        page = A4()
        page.create(sys.argv[1].upper())
        page.add(svg[i])
        print "INFO: another page created"
sheets.append(page)

game = sys.argv[2].split('.')

for i in xrange(0, len(sheets)):
    page = sheets[i].a4
    name = '%s-counters-sheet-%d.svg' % (game[0], i+1)
    f = open(name, 'w+')
    f.write(etree.tostring(page, pretty_print=True))
    f.close()
