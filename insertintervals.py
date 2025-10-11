def insertinterval(intervals,newinterval):
    intervals.sort(key=lambda x:x[0])
    merged=[]
    new_start,new_end=newinterval
    for i in range(len(intervals)):
        start,end=intervals[i]
        if end<new_start:
            merged.append([start,end])
        elif start>new_end:
            merged.append([new_start,new_end])
            new_start,new_end=start,end
        else:
            new_start=min(start,new_start)
            new_end=max(end,new_end)
    merged.append([new_start,new_end])
    return merged
intervals=[[1,3],[6,9]]
newinterval=[2,5]
print(insertinterval(intervals,newinterval))