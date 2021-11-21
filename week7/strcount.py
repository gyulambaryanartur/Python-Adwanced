def givestr(str1, str2):
    
    step = 0
    while (str1 != str2):
        str1len = len(str1)
        str2len = len(str2)
        if str1len > str2len:
            str1 = str1[(str1len-str2len):]
            step += str1len-str2len

        elif str1len < str2len:
            str2 = str1[(str2len-str1len):]
            step += str2len-str1len

        else:
            str1 = str1[1:]
            str2 = str2[1:]
            step += 2
    return step


print(givestr('aaa', 'bb'))
