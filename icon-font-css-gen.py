# generate icon font css from glyphmap json

import argparse
import json


'''
example:
  python icon-font-css-gen.py -j Ionicons.json -o ion.css -p ion
  icon-font-to-png --css ion.css --ttf Ionicons.ttf --size 64 person
'''

parser = argparse.ArgumentParser()
parser.add_argument("-j", "--json", help = "Glyphmap Json file path")
parser.add_argument("-p", "--prefix", help = "CSS font class & prefix")
# parser.add_argument("-f", "--font-family", help = "CSS font family name")
parser.add_argument("-o", "--output", help = "Output CSS file name")

args = parser.parse_args()

jsonFile = ""
prefix = "iconfont"
output = "iconfont.css"
# fontFamily = "Icon Font"

if args.json:
    print("Glyphmap Json file: %s" % args.json)
    jsonFile = args.json
else:
    print("Glyphmap Json file is required")
    exit(-1)

if args.prefix:
    print("CSS font class prefix: %s" % args.prefix)
    prefix = args.prefix

# if args.font_family:
#     print("CSS font family: %s" % args.font_family)
#     fontFamily = args.fontFamily

if args.output:
    print("Output CSS file: %s" % args.output)
    output = args.output

with open(jsonFile, 'r', encoding='utf-8') as fp:
    data = json.load(fp)
    with open(output, 'w', encoding='utf-8') as cssfp:
        for k, v in data.items():
            cssfp.write('''.%s-%s:before {
    content: "\%x";
}
''' % (prefix, k, v))

