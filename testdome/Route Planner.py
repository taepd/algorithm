# https://www.testdome.com/questions/python/route-planner/48626?visibility=1&skillId=9

def route_exists(from_row, from_column, to_row, to_column, map_matrix):
    visited = [[False for i in range(len(map_matrix[0]))] for j in range(len(map_matrix))]
    def temp(from_row, from_column, to_row, to_column, map_matrix):
        if  from_row < 0 or from_column < 0 or from_row >= len(map_matrix) or from_column >= len(map_matrix[0]) or visited[from_row][from_column]:
            return False
        if map_matrix[from_row][from_column]:
            visited[from_row][from_column] = True
            if from_row == to_row and from_column == to_column:
                return True
            return (temp(from_row, from_column+1, to_row, to_column, map_matrix) or
                    temp(from_row, from_column-1, to_row, to_column, map_matrix) or
                    temp(from_row-1, from_column, to_row, to_column, map_matrix) or
                    temp(from_row+1, from_column, to_row, to_column, map_matrix))
    return temp(from_row, from_column, to_row, to_column, map_matrix)

if __name__ == '__main__':
    map_matrix = [
        [True, False, False],
        [True, True, False],
        [False, True, True]
    ];
    print(route_exists(0, 0, 2, 2, map_matrix))