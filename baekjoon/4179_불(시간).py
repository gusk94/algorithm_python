from collections import deque
def gofire():
    for i in range(len(fires)):
        x, y = fires.popleft()
        for dx, dy in idx:
            if 0 <= x+dx < R and 0 <= y+dy < C and (board[x+dx][y+dy] == '.' or board[x+dx][y+dy] == 'J') and (x+dx, y+dy) not in fires:
                fires.append((x+dx, y+dy))
                board[x+dx][y+dy] = 'F'


def go(a):
    queue = deque()
    queue.append(a)
    cnt = 0
    while queue:
        gofire()
        for i in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in idx:
                if 0 <= x+dx < R and 0 <= y+dy < C and board[x+dx][y+dy] == '.':
                    board[x+dx][y+dy] = 'J'
                    if x+dx == R-1 or y+dy == C-1 or x+dx == 0 or y+dy == 0:
                        return cnt+2
                    queue.append((x+dx, y+dy))
        cnt += 1
    return 'IMPOSSIBLE'


R, C = map(int, input().split())
board = [[i for i in input()] for _ in range(R)]
idx = [(-1, 0), (1, 0), (0, 1), (0, -1)]
fires = deque()
for x in range(R):
    for y in range(C):
        if board[x][y] == 'J':
            people = (x, y)
        if board[x][y] == 'F':
            fires.append((x, y))
if people[0] == 0 or people[0] == R-1 or people[1] == 0 or people[1] == C-1:
    print(1)
else:
    res = go(people)
    print(res)
