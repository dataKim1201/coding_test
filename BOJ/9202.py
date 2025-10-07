import sys
from collections import deque
input = sys.stdin.readline
scoring = [
    # 0 ~ 2 -> 0점
    0,0,0,
    # 3 ~ 4 -> 1점
    1, 1, 
    # 5 -> 2점
    2, 
    # 6 -> 3점
    3, 
    # 7 -> 5점
    5,
    # 8 -> 11점 // 8글자는 없다.
    11
    ]

directions = [(-1, -1), (-1, 0), (-1, 1),
                (0, -1),          (0, 1),
                (1, -1),  (1, 0), (1, 1)]
    
def solution(vocabs, boggles):
    # vocabs로 loop돌면서 존재하는지 보기
    for num, boggle in enumerate(boggles):
        score, longest_w, count = 0, None, 0
        # print(f'stage {num}', '*'*100)
        for word in vocabs: # word 되는지 보기
            if is_word_matching(boggle, word):
                if not longest_w:
                    # scoring
                    longest_w = word
                score += scoring[len(word)]
                count += 1
        print(score, longest_w, count)
    return None

def is_word_matching(boggle, word):
    for i in range(4):
        for j in range(4):
            if boggle[i][j] == word[0]:
                if bfs(word, boggle, i,j):
                    return True
    return False

def bfs(word, boggle, x, y):
    queue = deque()
    idx = 1
    queue.append((idx,[(x,y)],x,y))
    # 최종 점수, 가장 긴 단어, cnt
    while queue:
        idx,path,cx,cy  = queue.popleft()
        # print(idx, path, word,cx,cy)
        if idx >= len(word):
            return True
        # 다음 단어인지 확인
        for (dx, dy) in directions:
            nx,ny = cx + dx, cy + dy
            if 0 <= nx < 4 and 0 <= ny < 4 and (nx,ny) not in path and word[idx] == boggle[nx][ny]:
                queue.append((idx + 1, path + [(nx, ny)], nx,ny))
    return False

if __name__ == '__main__':
    w = int(input())
    vocabs = sorted([input().strip() for _ in range(w)], key = lambda x : (-len(x), x ) )
    input().strip()
    b = int(input())
    boggles = []
    for i in range(b):
        boggles.append([input().strip() for _ in range(4)])
        if i == b-1: continue
        input().strip()
    solution(vocabs,boggles)


    