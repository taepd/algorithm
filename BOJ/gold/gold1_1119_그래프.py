N = int(input())

matrix = []
edge = 0
for cnt in range(N):
    row = input()
    matrix.append(row)
    for ch in row:
        if ch == 'Y':
            edge += 1/2

if edge < N - 1:
    print(-1)
else:
    block_cnt = 0
    for i in range(N):
        row_str = ""
        for x in range(i):
            row_element = matrix[i][x]
            row_str += row_element
        if len(row_str.replace("N", "")) == 0:
            block_cnt += 1

    print(block_cnt - 1)
