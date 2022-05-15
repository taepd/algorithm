import heapq

def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)
    while min(scoville) < K:
        if len(scoville) < 2:
            return -1
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a+(b*2))
        answer += 1
    return answer

scoville, K = [1]*100000, 700
print(solution(scoville, K))