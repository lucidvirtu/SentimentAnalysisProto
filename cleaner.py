import re

def exec_clean():
    #cleanup raw data from hashtag, @ symbol, punctuations and then lowercase all char

    source = open('raw_data.txt', 'r')
    clean = open('clean_data.txt', 'w')

    for text in source:
        raw = text
        cl_text1 = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",raw).split())
        cl_text2 = cl_text1.lower()
        clean.write(cl_text2+"\n")

    clean.close()
    source.close()



def exec_stop():

    stoplist = []
    clean1 = open('clean_data.txt', 'r+')
    clean2 = open('clean_data2.txt', 'w')
    stopdoc = open('stopwmsa.txt', 'r')

    for x in stopdoc:
        stoplist.append(x.rstrip('\n'))


    for text2 in clean1:
        text_p = text2.split()
        resultwords = [word for word in text_p if word not in stoplist]
        result = ' '.join(resultwords)

        clean2.write(result+'\n')

    clean1.close()
    clean2.close()
    stopdoc.close()
