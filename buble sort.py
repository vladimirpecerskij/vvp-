def buble_sort(nlist):
    for passnum in
range (len(nlist)-1,0,-1):
    for j in range (passnum):
    if nlist [j] > nlist[j+1]:
    nlist[j], nlist[j+1] = nlist [j+1], nlist[j]
    nlist = [14,46,43,27,57,41,45,21,70]
    buble_sort (nlist)
    print (nlist)
