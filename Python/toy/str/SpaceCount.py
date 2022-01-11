def spaceCount(ch, strIn):
    tmp = strIn
    space = 0
    chStr = ""
    for i in tmp:
        if i == ch:
            space = space + 1  
    for i in range(1,space+1):
        chStr += str(i)
    return strIn.replace(space*ch, chStr)