import re
def palin(str1):
    t1 = re.findall(r'([a-z|A-Z]+)',str1)
    #print t1
    t2 = "".join(t1)
    #print t2
    t3 = t2[::-1]
    if (t2.lower() == t3.lower()):
        return True
    else: return False

print palin("man")
print palin("A man, a plan, a canal -- Panama")
print palin("")
