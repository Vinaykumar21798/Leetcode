def twosum(arr,target):
    dici={}
    for i,num in enumerate(arr):
        complement=target-num
        if complement in dici:
            return [dici[complement],i]
        dici[num]=i
    return []
arr=list(map(int,input().split()))
target=int(input())
print(twosum(arr,target))
