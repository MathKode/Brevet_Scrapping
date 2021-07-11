#Code pour obtenir les stats entre personnes admis, tres bien, bien, passable
file = open("data_brevet.csv",'r')
ls = file.read().split('\n')
file.close()
del ls[0]
result = []
for i in ls:
    mention = i.split(',')[2]
    i = True
    p = 0
    for r in result:
        if r[0] == mention:
            i = False
            pp = p
        p += 1
    if i:
        result.append([mention,1])
    else:
        r = result[pp]
        r[1] = r[1] + 1
        result[pp] = r

print('\n')
for i in result:
    print(i[0], str(int(i[1]*100/len(ls))),"%")
print('\nSur un total de :',len(ls))

