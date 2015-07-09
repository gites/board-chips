#Requirements for *nix’s
- python 2.7.x (https://www.python.org/downloads/)
- modul lxml  (http://lxml.de/installation.html) 
- Inkscape (https://inkscape.org/en/)
**WARNING:** this project was developed under Windows (unfortunately :) ), and haven’t been tested on Linux. It can happen, that I mistakenly assumed something about path format and script will not work. Fixes welcome. 

#Requirements for Windows
- Microsoft Visual C++ 2008 Redistributable Package(http://www.microsoft.com/downloads/en/details.aspx?FamilyID=9b2da534-3e03-4391-8a4d-074b9f2bc1bf&displaylang=en)
- Inkscape (https://inkscape.org/en/)
- modul lxml  (http://lxml.de/installation.html)  (if you are using Python scripts, not exe)

#How it works
##Definition of counters for WB-95
In order to generate counters You fist need to define what should be on them. You can do this by filling up sheet, whit counters description. When you and done sheet need to be saved as **CSV** file, which then can be processed by script. One line define one counter.
You can set the following fields:
* COUNTRY - define which country is represented by this counter (also this define colours set for counter, and group together counters from one country).
	Colours definitions for each country are set in file colours.ods (colours.csv) - later more about that. If in definition You use country with is not defined, script will stop working.
	For now you can use:
	- RU - Soivet Uninon
	- DE - Germany 
	- DE-SS - Germany - Nazi units (SS)
	- HU - Hungary 
	- BG - Bulgaria
	- JU - Yugoslavia
	- RO - Romania
	- UT - Ustaše (Croats faithing for Germans)
* TYPE - define unit type, You can choose from:
	- HQ - headquarters
	- GU - ground unit
* UNIT NAME - unit name :) Number or something
	RESTRICTIONS!:
	- for HQs max 12 chars or some letters will be outside of counter
	- for GUs max 5 chars (+ eventually dot ".")
* UNIT NAME2 - second line with unit name. Works only for counter templates that have defined correct tag. Ignored for the rest. In general this was intended for soviets panzer and motorized corps.
* ARMY-DIV - division or army number for GUs or army corps for HSs
	RESTRICTIONS!:
	- max 3 digits/letters (for GUs)
	- may be empty, if so then div/army box is removed from counter (for GUs)
* SIZE - size of unit. This field is ignored for HQs. Enter one of:
	- I, II, III, X, XX, XXX
* ICON1 - file name with icon for this counter (you can see icons in res\wb-95 dir, or on indexes)
* ICON2 - file name with icon used on the counter back (only for GUs). If not set, ICON1 is used.
* ATTACK1 - attack strength on counter face.
* ATTACK2 - attack strength on counter back.
* DEFENSE1 - defence strength on counter face. Works only for counter templates that have defined correct tag. Ignored for the rest. In general this was intended for artillery counters. 
* DEFENSE2 - like DEFENSE1 but for counter back.
* MOVMENT1 - movement points for counter face.
* MOVMENT2 - movement points for counter back.
* WHITE STAR - number of white start on counter.
* BLACK STAR - number of black start on counter.
* YELLOW STAR - number of yellow start on counter.
* BLUE STAR - number of blue start on counter.

In general on one counter can be max 4 starts. If there is more, the rest is ignored.

After filling up counter sheet, You need to save it by using "**File->Save a Copy**" and choosing **CSV** format. As encoding use **UTF-8**, other settings without change. 

##Counters colours definition
In file colours.ods (colours.csv) we can define colours for our counters. One line defines colours for one country (type of counters). Colours are described in standard html notation. Some colours picker sites:
 - (http://html-color-codes.info/)
 - (http://www.w3schools.com/tags/ref_colorpicker.asp)
 - (http://www.rapidtables.com/web/color/RGB_Color.htm)
 
 Description for filds:
* COUNTRY - define for with country we are defining colours. This designation is used in counters definition.
* BACKGROUND - background color.
* BORDER - colour for border around the counter and for inscriptions (name, unit size, parameters, etc.)
* DIV_BOX - background colour for box with div or army number.
* DIV_BOX_BORDER - border coloru for DIV_BOX.
* DIV_COLOR - colour for div or army number. You can use here html colour code (in this case every counter for that country will have the same colour for its divs/armys) or **RNG**. In the second case script will use random colours for etch div/army. Because colours are generated randomly, after every run You will get different results - if You don't like some colours, just generate counters once more. **WARNING:** Script distinguishes divs/armys based on its number (ARMY-DIV field), so if You have "1st Panzer Division" and "1st Infantry Division", and You name them in counter sheet as "1", they both ends with the same colour.
* HQ_COLOR - same as DIV_COLOR but for HSs.
* ATTACK_BOX - background colour for attack box.
* DEF_BOX - background colour for defence box.
* MOVE_BOX - background colour for move box.

After filling up colours sheet, You need to save it by using "**File->Save a Copy**" and choosing **CSV** format. As encoding use **UTF-8**, other settings without change. 

#Counters sheets generation 
1. Run CMD
2. Go to dir where you have downloaded scripts
3. Run this command:
	`gen4.exe wb95 example-wb95.csv colours.csv`
4. If there was no errors You will find counter in file named like `<name of CSV file>-counters-sheet-1.svg`. One sheet have 108 counters (face and back). If You have more, then script will crate additional .svg files.
Lazy ones can use batch files `gen-exmaple.bat` (or  `gen-budapeszt1945.bat`)

#What next
Now You can look on generated sheets in web browser (just drag svg file on browser tab). Every current browser should work (Opera, Chrome, FF, IE11). If there are some errors, just correct them in counter sheet and run generation one more time. 

If You want to do some manual changes You can do this in [Inkscape](https://inkscape.org/en/). **WARNING:** If your computer has less than 2GB RAM... be patient.

#Printing
**I DO NOT RECOMEND PRINITNG FROM BROWSER.**  Printing from browser can mess with dimensions and you will ends with to small or to big counters in relativ to hexes on map.

The best way is to print directly from [Inkscape](https://inkscape.org/en/). If you can't do that, I advise to export counters sheet to pdf and print from pdf. Also if you want to share your work with others pdf is better - there is no problem with opening and file size is smaller.

#Other tools
While working on counters sheet generator I also crated some other tools to automatize. They are rough and can be unstable, I advise using them with caution.
##box-fixer.py
This tool is form mass settings change in counters templates. There is only Python version. This tool operate on raw SVG files. To use it, you need to edit code and set what element should be changed and what parameters should be set. It requires some knowledge about Python and SVG. This script operate on all files in directory provided in command argument. **Don't use it if You don't know what are You doing**
Usage: `python box-fixer.py target\dir`
##colorizer.py (colorizer.exe)
This tool if for coping colours pallet from one SVG file to another SVG file. Requires that both files have icon with **ICON** tag and the same amount paths. Colours are copied one to one, so colour of first path is copied to first path, second to second, etc. It is useful if your icons came from different sources, with different colours sets and You want to standardized them (to reduce variegation in the resulting sheets).
Usage: `colorizer.exe <source>.svg <target>.svg`
The resulting file is written as `<target>-from-<source>-colorized.svg`
##gen4.py (gen4.exe)
Main program to generate counters sheets - described above
##icon2bw.py (icon2bw.exe)
This program is for generating white and black icons from colour ones - for those, that like simplicity ;) It requires that icons on counters templates are tagged with **ICON** and/or **ICON2** tag. This script operate on all files in directory provided in argument. 
Usage: `icon2bw.exe <path_to_icon_dir> <white or black>`
The resulting counters templates are written to `<path_to_icon_dir>\white` or `<path_to_icon_dir>\black` depending on the second parameter.
##icon-indexer.py (icon-indexer.exe)
Program for indexing counters templates from specified directory.
Usage: `icon-indexer.exe path\to\templates`
Script generate SVG files containing every counter template from specified directory and it file name. This is useful to generate cheat-shit with available templates.

#Making new counters templates 
Just overall procedure:
- find image that you want to use as icon
- in Inkscape change bitmap to vector  (use 8 path, colours and no smooh)
- copy empty template (xx-blank.svg) and change file name to what you want
- open you newly copied file in Inkscape and copy to it previously vectorized image. Remember about rescaling, and positioning in counter.
- set ICON tag on icon (group all icon paths if they are not group already, open XML Editor (Ctrl+Shift+X), click on image and in ID field set ICON)
- and done :)






























































































