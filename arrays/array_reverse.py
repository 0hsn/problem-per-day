def reverseArray(a):
    return a[::-1]

if __name__ == '__main__':
    arr = [1, 4, 3, 2]
    arr_r = reverseArray(arr)
    
    import pprint
    pprint.pprint(arr)
    pprint.pprint(arr_r)