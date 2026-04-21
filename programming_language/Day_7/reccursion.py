def loop(n):
    if n==1:
        return 1
    else:
        return n*loop(n-1)
print(loop(4))