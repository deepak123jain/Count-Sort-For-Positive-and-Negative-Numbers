# Counting sort which takes negative and positive numbers.

def sort(arr):
    f = []
    m1 = max(arr)
    m2 = abs(min(arr))

    # List having all 0's (for positive integers)
    t1 = [0]*(m1+1)

    # List having all 0's (for negative integers)
    t2 = [0]*(m2)

    for i in arr:
        if i>=0:
            t1[i] += 1
        else:
            i=abs(i)
            t2[i-1] += 1

    # sort the negative numbers
    for i in range(m2-1,-1,-1):
        while t2[i] >0:
            f.append(-(i+1))
            t2[i]-=1

    # sort the positive numbers 
    for i in range(0,m1+1):
        while t1[i]>0:
            f.append(i)
            t1[i]-=1
    return f

# Let's Try the Code
arr=[-10,-9,2,4,-9,5,2,13,-13,0,3]
p=sort(arr)
for i in p:
    print(i,end=' ')
