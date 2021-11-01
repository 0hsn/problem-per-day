# https://www.hackerrank.com/challenges/repeated-string/problem

from pprint import pprint

def repeatedString(s, n):
    if len(s) == 1:
        return n if s == 'a' else 0
    if 'a' not in s:
        return 0

    rpt = int(n / len(s)) if (n % len(s) == 0) else int(n / len(s)) + 1

    ss = s * rpt
    ss = ss[:n]

    cnt = 0
    for c in ss:
        if c == 'a': cnt+=1

    return cnt



if __name__ == '__main__':
    print(repeatedString('b', 10000000000000000000000))
