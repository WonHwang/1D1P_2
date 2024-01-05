def solution(n, slicer, num_list):
    return [num_list[i] for i in range(([0, 0, slicer[0], slicer[0], slicer[0]])[n], [0, slicer[1]+1, len(num_list), slicer[1]+1, slicer[1]+1][n], [1, 1, 1, 1, slicer[2]][n])]
