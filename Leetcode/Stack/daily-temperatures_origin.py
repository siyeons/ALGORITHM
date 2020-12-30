def dailyTemperatures(temp):
    answer = [0] * len(temp)
    day = [] 
    for i, currVal in enumerate(temp):
        while day and currVal > temp[day[-1]]:
            lastVal = day.pop()
            answer[lastVal] = abs(i - lastVal)
        day.append(i)
    print(answer)

dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])