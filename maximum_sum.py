def maximum_sum(arr):
    curr_sum=arr[0]
    global_sum=arr[0]
    for i in arr:
        if curr_sum<0:
            curr_sum=0
        curr_sum+=i
        if curr_sum>global_sum:
            global_sum=curr_sum2
    return global_sum
arr=list(map(int,input().split()))
print(maximum_sum(arr))
