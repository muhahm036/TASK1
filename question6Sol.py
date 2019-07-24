def secondSmallest(arr):
    n = len(arr)


    for i in range(n):

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                c=arr[j]
                arr[j]= arr[j + 1]
                arr[j + 1]=c

    return arr

def loc(ar):
    for a in range(len(ar)-1):
        if ar[a] < ar[a + 1]:
            break
    return a+1


arrr=[1,-10,-35,20,-15,-36,45,30,-40,-35,-36,2,3,4,-1,-36,5,6,-5,7,8,9]

out=secondSmallest(arrr)
findSecondSmallestLoc=loc(out)
print("Secnd Smallest Element in Array",out[findSecondSmallestLoc])





