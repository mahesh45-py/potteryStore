def largestLand(houses):
    d = dict()
    for i in houses:
        d[i[1]]=i[0]
    
    return d[0]



land = [
    [5,2],
    [3,7],
    [1,9],
    [2,0],
    [5,15],
    [4,30]
]
print(largestLand(land))