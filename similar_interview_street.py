

def similar(str1):
	l=len(str1)
	i=0
	res=0
	while i<l:
		suf = str1[i:]
		j=0
		while j<len(suf):
			if(suf[j]==str1[j]):
				j= j + 1
			else : break
		res = res + j
		i=i+1
	return res		
N= int(raw_input())
ans1=[]
for i in range(N):
        ans1.append(similar(raw_input()))
for i in range(N):
        print ans1[i]
#print similar("ababaa")
#print similar("aa")
