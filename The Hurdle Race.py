import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
height = map(int, input().strip().split(' '))
m = max(height)
print(m-k if m>k else 0)
