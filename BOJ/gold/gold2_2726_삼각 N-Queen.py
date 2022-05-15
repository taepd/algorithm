"""
n이 6인 경우

               (1,1)
            (2,1) (2,2)
         (3,1) (3,2) (3,3)
      (4,1) (4,2) (4,3) (4,4)
   (5,1) (5,2) (5,3) (5,4) (5,5)
(6,1) (6,2) (6,3) (6,4) (6,5) (6,6)

특정 칸에 퀸이 놓여졌을 때, 퀸이 공격할 수 있는 칸(다른 퀸을 놓을 수 없는 칸)의 조건
1. x좌표가 같은 칸
2. y좌표가 같은 칸
3. x좌표와 y좌표가 동시에 +-1 이 되는 칸

"""
"""
brute force 
1) 전체 좌표 리스트에서 임의의 칸에 퀸을 배치
2) 다른 퀸을 놓을 수 없는 칸을 리스트에서 지움
3) 남은 칸 중에 퀸을 배치하고 2)를 실행
4) 놓을 수 있는 퀸의 최대 개수만큼 3)을 반복
5-1) 다 배치하면 출력하고 종료
5-2) 다 배치하는데 실패하면 1)에서 다음 칸에 배치하고 위 과정을 반복
"""


def remove_squeare(chess_board, target, n):
    x, y = map(int, target.split())

    # 1. x좌표가 같은 칸
    for p in range(1, x+1):
        chess_board.discard(f'{x} {p}')  # discard는 O(1)


    # 2. y좌표가 같은 칸
    for p in range(y, n+1):
        chess_board.discard(f'{p} {y}')

    # 3. x좌표와 y좌표가 동시에 +-1 이 되는 칸
    diff = x-y
    for p in range(diff+1, n+1):
        chess_board.discard(f'{p} {p-diff}')


# chess_board = {'1 1', '2 1', '2 2', '3 2', '3 1', '3 3'}
# remove_squeare(chess_board, '3 3', 3)

def solution_1():
    test_case_list = [int(input()) for _ in range(int(input()))]

    for n in test_case_list:
        n_queen = int((2*n+1)/3)  # 놓을 수 있는 퀸의 최대 개수
        print(n_queen)

        # 체스판 생성
        chess_board = set()
        for i in range(1, n+1):
            for j in range(1, i+1):
                chess_board.add(f'{i} {j}')

        # 1) 전체 좌표 리스트에서 임의의 칸에 퀸을 배치
        for square in chess_board:
            answer = [square]
            queen_count = 1
            tmp_board = chess_board.copy()  # 이번 턴에 사용할 체스판 생성
            # 2) 다른 퀸을 놓을 수 없는 칸을 리스트에서 지움
            while queen_count < n_queen and len(tmp_board) >= 0:
                queen_count += 1
                remove_squeare(tmp_board, square, n)
                if len(tmp_board) == 0:
                    break
                # 3) 남은 칸 중에 퀸을 배치하고 2)를 실행
                square = tmp_board.pop()
                answer.append(square)
            if queen_count == n_queen:
                break

        for ans in sorted(answer):
            print(ans)

solution_1()

"""
시간 초과

최대 한 변의 길이가 1000인 삼각형 체스판인 경우에도 빠르게 연산이 되어야 함
한 변의 길이가 1000인 체스판의 사각말판수는 500,500 개이고, 이를 모두 순회하는 것은 1초안에 힘듬
파이썬은 1초에 대략 2천만번 연산이 가능하다고 가정하고 알고리즘을 구현해야 함
remove_square 함수 내부에 for문이 3개 존재하고 전체 구조는 O(N^2)이고 비효율적임
"""