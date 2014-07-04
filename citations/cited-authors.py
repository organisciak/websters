import re
import csv

def main():
    MATCH_ENTRY_TITLE = re.compile('^([A-Z\';]{2,}[- ]?)+$')
    MATCH_END_ATTR = re.compile("[\.\"] (?P<name>(([A-Z][a-z]+).?){1,4})\.$")

    entry = None
    outfile = open("attributions.csv", "w+")
    out = csv.writer(outfile)
    out.writerow(['entry', 'attribution'])

    for line in open('29765-8.txt', encoding="ISO-8859-1"):
        line = line.strip()
        #!print(line)
        a = MATCH_ENTRY_TITLE.search(line)
        if a:
            entry = a.group(0)
            continue

        if not entry:
            continue

        attr = MATCH_END_ATTR.search(line)
        if attr:
            name = attr.group("name")
            #print("{} {}".format(entry, name))
            if name[:3] != "See":
                out.writerow([entry, name])
            #print(line)
            continue

    outfile.close()

if __name__=='__main__':
    main()
