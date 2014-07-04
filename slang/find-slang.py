import re
import csv

def main():
    MATCH_ENTRY_TITLE = re.compile('^([A-Z\';]{2,}[- ]?)+$')
    SLANG = re.compile("\[.{0,20}([Ss]lang|[Cc]ollo|[Vv]ulgar).{0,20}\]")

    entry = None
    slang_builder = [] 
    outfile = open("slang.txt", "w+")
    #out = csv.writer(outfile)
    #out.writerow(['entry', 'attribution'])
    # Uses dictionary-clean, which is output by remove-line-breaks.py
    for line in open('data/dictionary-clean.txt', encoding="ISO-8859-1"):
        line = line.strip()
        
        # If slang note was on earlier line, see if it should be continued.
#        if len(slang_builder) > 0:
            #print(slang_builder)
            #if line:
                #slang_builder += [line]
                #continue
            #else:
                #paragraph = " ".join(slang_builder)
                #outfile.write(paragraph)
                #slang_builder = []
                #continue

        a = MATCH_ENTRY_TITLE.search(line)
        if a:
            entry = a.group(0)
            continue

        if not entry:
            continue

        slang = SLANG.search(line)
        if slang:
            s = re.sub("\[.*?\]", "", line)
            outfile.write("%s\t%s:\t%s\n" % (len(s), entry, line))
            #slang_builder = [line]
            continue

    outfile.close()

if __name__=='__main__':
    main()
