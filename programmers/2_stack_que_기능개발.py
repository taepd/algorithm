progresses = [93, 30, 55]
speeds = [1, 30, 5]


def solution(progresses, speeds):

    answer = []
    while progresses:
        cnt = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        while progresses:
            if progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
                cnt += 1
            else:
                break
        if cnt:
            answer.append(cnt)

    return answer

# def solution(progresses, speeds):
#     Q=[]
#     for p, s in zip(progresses, speeds):
#         if len(Q)==0 or Q[-1][0]<-((p-100)//s):
#             Q.append([-((p-100)//s),1])
#         else:
#             Q[-1][1]+=1
#         print(Q)
#     return [q[1] for q in Q]

print(solution(progresses, speeds))

