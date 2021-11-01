# https://www.hackerrank.com/challenges/2d-array/problem

def hourglassSum(arr):
    max_i = max_j = 4
    i = 0
    sum = -1

    while i < max_i:
        j = 0
        while j < max_j:
            sum_t = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            if sum < sum_t: sum = sum_t
            j += 1
        i += 1

    return sum

if __name__ == '__main__':
    
    arr = [
        [-9, -9, -9,  1, 1, 1],
        [ 0, -9,  0,  4, 3, 2],
        [-9, -9, -9,  1, 2, 3],
        [ 0,  0,  8,  6, 6, 0],
        [ 0,  0,  0, -2, 0, 0],
        [ 0,  0,  1,  2, 4, 0],
    ]

    print(hourglassSum(arr))