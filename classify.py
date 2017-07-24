def classifier():
    file1 = open('clean_data2.txt', 'r')
    stat = open("result.txt", 'w')
    posi = open("positive-co.txt", "r")
    nega = open("negative-co.txt", "r")

    posibuff = 0
    negabuff = 0
    neubuff = 0

    posilist = []
    negalist = []

    for x in posi:
        posilist.append(x.rstrip('\n'))

    for y in nega:
        negalist.append(y.rstrip('\n'))

    for strings in file1:
        sentbuff = 0
        p1 = strings.split()

        for word in p1:
            if word in posilist:
                sentbuff = sentbuff+1

            elif word in negalist:
                sentbuff = sentbuff-1

        if (sentbuff>0):
            #print (strings+"  "+str(sentbuff))
            posibuff = posibuff+1
        elif (sentbuff<0):
            #print(strings + "  " + str(sentbuff))
            negabuff = negabuff+1
        elif (sentbuff==0):
            #print(strings + "  " + str(sentbuff))
            neubuff = neubuff+1

    total = posibuff+negabuff+neubuff
    posiper = (posibuff/total*100)
    negaper = (negabuff/total*100)
    neuper = (neubuff/total*100)
    stat.write(str(posiper)+"\n")
    stat.write(str(negaper)+"\n")
    stat.write(str(neuper))

    file1.close()
    stat.close()
    posi.close()
    nega.close()

#classifier()