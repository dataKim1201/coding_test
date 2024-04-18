import sys
input = sys.stdin.readline
n,m  = map(int,input().split())
fact_person = list(map(int,input().split()))
if len(fact_person) == 1:
    fact_person = set([])
else:
    fact_person = set(fact_person[1:])
parties = [list(map(int,input().split()))[1:] for _ in range(m)]
visited = [False] * m
answer = 0
flag = False
for idx, party in enumerate(parties):
    for per in party:
        if per not in fact_person:
            flag = True
        else: # 있다면?
            flag = False
            findings = set(party) - fact_person
            if answer > 0 and len(findings) >= 1:
                for i in range(idx-1,-1,-1):
                    if visited[i] and len(findings & set(parties[i])) >= 1:
                        answer -= 1
                        visited[i] = False
                        for item in parties[i]:
                            if item not in fact_person and item not in findings:
                                findings.add(item)
            break
    if flag == True:
        answer += 1
        visited[idx] = True
    else:
        fact_person = fact_person^findings
    # print(fact_person)
print(answer)