def findRockSample(ranges,n, r, arr):
    a = []
 
# Iterate over the ranges
    for i in range(r):
        c = 0
        l, h = ranges[i][0], ranges[i][1]
        for val in arr:
            print(l,h)
            if l <= val <= h:
                c =c+ 1
                print(c)
            
           
        a.append(c)
    return a
 
 
# Driver Code
if __name__ == "__main__":
    n = 5
    r = 2
    arr = [400, 567, 890, 765, 987]
    ranges = [[300, 380], [800, 1000]]
 
# Function Call
    print(*findRockSample(ranges, n, r, arr))