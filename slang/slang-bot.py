import twitter
import codecs
import logging

def main():
    CSECRET = open("../private/consumer-secret.txt").read().strip()
    ATSECRET = open("../private/access-token-secret.txt").read().strip()
    logging.basicConfig(filename="slang.log", level='DEBUG')
    api = twitter.Api(consumer_key='yB4fCtQhEy7tN03YtZRRIMhU4',
            consumer_secret=CSECRET,
            access_token_key='2538303024-JNIEej0MbUw0Xfpdowko5jbvt41apIPxl5Tu1W6',
            access_token_secret=ATSECRET)
    
    infile = codecs.open("queue.txt", "r", encoding="ISO-8859-1")
    postfile = codecs.open("posted.txt", "a", encoding="ISO-8859-1")
    lines = infile.readlines()
    infile.close()

    message = lines[0]
    queue = lines[1:]

    if len(message) > 140:
        logging.error("Message too long")
        too_long = codecs.open("toolong.txt", "a", encoding="ISO-8859-1")
        too_long.write(message)
        too_long.close()
        return

    try:
        api.PostUpdate(message)
        logging.info("Posted new message: %s", message[:30])
    except:
        logging.error("Couldn't post message: %s", message[:30])
        return

    postfile.write(message)
    postfile.close()

    infile = codecs.open("queue.txt", "w", encoding="ISO-8859-1")
    infile.writelines(queue)
    infile.close()


if __name__=="__main__":
    main()
