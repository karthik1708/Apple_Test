
s1="This is a sample text but a complicated problem to be solved, so we are adding more text to see that it actually works."
ls=[]
wid=20
def cutStr(s):
    if(len(s)<wid):
        ls.append(s)
        return s
    else:
        for i in range(wid,0,-1):
            if(s[i]==" "):
                ls.append(s[:i])
                break
        return cutStr(s[(i+1):])
cutStr(s1)

array=[]
for l in ls:
    length=len(l)-l.count(' ')
    spl=l.split(" ")
    words=len(l.split(" "))
    spaces=((wid-length)/(words))
    sp=""
    sp += " "*(int(spaces)+1)
    array.append(sp.join(spl))

count=1
for sentence in array:
    print("Array [{}] = \"{}\"".format(count,sentence))
    count += 1

