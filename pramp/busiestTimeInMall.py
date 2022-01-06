def busiestTimeInMall(data):
    n = len(data)
    counter = 0
    maxCount = 0
    timestamp = None
    
    for i in range(n):
        curTime, visitorCount, entered = data[i]
        if entered:
            counter += visitorCount
        else:
            counter -= visitorCount
        if i < n -1 and curTime == data[i + 1][0]:
            continue
        if counter > maxCount:
            maxCount = counter
            timestamp = curTime
    return timestamp


data = [[1487799425, 14, 1], 
        [1487799425, 4,  0],
        [1487799425, 2,  0],
        [1487800378, 10, 1],
        [1487801478, 18, 0],
        [1487801478, 18, 1],
        [1487901013, 1,  0],
        [1487901211, 7,  1],
        [1487901211, 7,  0]]

print(busiestTimeInMall(data))
