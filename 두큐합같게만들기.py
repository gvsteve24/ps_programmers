from collections import deque

def solution(queue1, queue2):
    queue1.reverse()
    queue2.reverse()
    L, R = sum(queue1), sum(queue2)
    q = queue1+queue2
    l = len(queue1)-1
    r = len(q) - 1
    diff = R - L, R-L
    if diff == 0:   return 0
    cnt = 0
    while True:
        if diff > 0:
            diff -= 2*q[r]
            r -= 1
        else:
            diff += 2*q[l]
            l -= 1
        if l < 0:
            l += len(q)
        if r < 0:
            r += len(q)
        cnt += 1
        if diff == 0:
            break
        if cnt == 4*len(queue1):
            return -1
        
    return cnt