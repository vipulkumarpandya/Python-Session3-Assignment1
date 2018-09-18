def longestWord(a=[]):
    index = 0
    longLen = 0
    ctr=0

    for i in a:
       if len(i) > longLen:
            longLen = len(i)
            index = ctr
       ctr+=1
    return a[index]


a = input ("Enter a sentense :")
lst = a.split(" ")
print(longestWord(lst))




