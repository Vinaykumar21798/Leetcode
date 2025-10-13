def reversepairs(arr):
    def mergesort(arr):
        if len(arr)<=1:
            return arr,0
        mid=len(arr)//2
        left,left_count=mergesort(arr[:mid])
        right,right_count=mergesort(arr[mid:])
        count=left_count+right_count
        j=0
        for i in range(len(left)):
            while j<len(right) and left[i]>2*right[j]:
                j+=1
            count+=j
        merged=[]
        i=j=0
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                merged.append(left[i])
                i+=1
            else:
                merged.append(right[j])
                j+=1
        merged+=left[i:]+right[j:]
        return merged,count
    _,total_count=mergesort(arr)
    return total_count
arr=list(map(int,input().split()))
print(reversepairs(arr))
