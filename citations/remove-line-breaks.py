import re

def main():
    OPEN_BRACE = re.compile("\[")
    CLOSE_BRACE = re.compile("\]")

    out = open('data/dictionary-clean.txt', 'w+', encoding="ISO-8859-1")

    buf = [] 
    lines = 0
    for line in open('data/dictionary.txt', encoding="ISO-8859-1"):
        lines += 1
        line = line.strip()
        buf += [line]
        if len(line) == 0: # Line Break, finish collecting lines and process buffer
            # Is the line length + next line's first word too long to fit on one line?
            if len(buf) == 1:
                out.write("\n%s" % buf[0] )
                buf = []
                continue

            i = len(buf) - 1

            # Go backwards through each line in buffer to see if it should be connected
            # to previous
            while i > 0:
                join = False
                next_word_len = buf[i].find(" ") if " " in buf[i] else len(buf[i])
                if len(buf[i-1]) + 1 + next_word_len >= 70:
                    # Possible a truncated line
                    if re.match("^[a-z]", buf[i]):
                        # Check if lowercase first character 
                        join = True
                    elif re.match("^[A-Z]", buf[i]) and re.search("[a-z\-]$", buf[i-1]):
                        # If previous line ends with lowercase or hyphen and next line
                        # begins with Capital letter
                        join = True
                    elif "]" in buf[i] and not "[" in buf[i]:
                        join = True
                    elif ")" in buf[i] and not "(" in buf[i]:
                        join = True

                if join:
                        buf[i-1] = "%s %s" % (buf[i-1], buf[i])
                        buf = buf[:i] + buf[i+1:]

                i -= 1

            out.write("\n")
            out.write("\n".join(buf))
            buf = []

    out.close()

if __name__=='__main__':
    main()
