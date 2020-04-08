#! /usr/bin/env python

def mergeSort(l):
	if (len(l)>1):
	        middle = len(l)/2
		l1 = l[:middle]
		l2 = l[middle:]
		mergeSort(l1)
		mergeSort(l2)
		i1 = i2 = ind = 0
		while i1<len(l1) and i2<len(l2):
			if (l1[i1]<l2[i2]):
				l[ind] = l1[i1]
				i1+=1
			else:
				l[ind] = l2[i2]
				i2+=1
			ind+=1
		for i in range(i1,len(l1)):
			l[ind] = l1[i]
                        ind+=1
                for i in range(i2,len(l2)):
                        l[ind] = l2[i]
                        ind+=1

l = [3,1,7,2,8,5,4]
print l
mergeSort(l)
print l

