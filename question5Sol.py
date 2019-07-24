
def max_num_in_list(ar):
    m = ar[0]
    for x in ar:
        if m > x:
            m=x

    return m
arr=[1,-10,-35,20,-15,45,30,-35,2,3,4,-1,-36,5,6,-5,7,8,9]

print(max_num_in_list(arr))
