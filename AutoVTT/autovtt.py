import os.path
import argparse
import codecs
#import re

#reFlags = re.UNICODE

class DialogueLine():
    def __init__(self, inDic={}):
        self.dialogueDic = inDic

parser = argparse.ArgumentParser()
parser.add_argument("INFILE", help = "Input file")
parser.add_argument("OUTFILE", help = "Output file")

args = parser.parse_args()

if not os.path.isfile(args.INFILE):
    raise Exception("Input file must be an existing text file.")

with codecs.open(args.OUTFILE, 'a', encoding='utf-8') as newFile:
    with codecs.open(args.INFILE, 'r', encoding='utf-8') as origFile:
        eventsSection = False
        eventFormatDefined = False
        formatLine = ""
        for line in origFile:
            if u"[Events]" in line and not eventsSection:
                eventsSection = True
            elif eventsSection:
                if line.startswith(u"Format: ") and not eventFormatDefined:
                    formatLine = [word.strip() for word in line.replace(u"Format: ","").split(u",")]
                else:
                    tempLine = line.partition(u":")[2].strip().split(u",", len(formatLine)-1)
                    print tempLine
                    
                    