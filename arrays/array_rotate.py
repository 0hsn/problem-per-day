def rotateArray(d, arr):
    return arr[d:] + arr[:d]

if __name__ == '__main__':
    arr = [1, 4, 3, 2]
    arr_r = rotateArray(2, arr)
    
    import pprint
    pprint.pprint(arr)
    pprint.pprint(arr_r)