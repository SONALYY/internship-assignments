def maxMeetings(start, end):
    n = len(start)
    sm = []
    lt = 0

    for i in range(n):
        if start[i] >= lt:
            sm.append((start[i], end[i]))
            lt = end[i]

    return sm

if __name__ == "__main__":
    start = [1, 3, 0, 5, 8, 5]
    end = [2, 4, 6, 7, 9, 9]
    r = maxMeetings(start, end)
    print("Maximum number of meetings :", r)