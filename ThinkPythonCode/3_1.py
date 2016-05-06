def right_justify(str1):
    totalLen = 70
    len1 = len(str1) 
    #if (len1 > totalLen)
        #print ()    
    frontLen = totalLen - len1
    newStr = " "*frontLen+str1
    print(newStr)
    
right_justify("dfjskahlfdasj")