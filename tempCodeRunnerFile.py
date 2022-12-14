def solution(N):
    N = bin(N)[2:] # 2: is used to remove the first 2 characters as they are 0b
    x = 0
    y = 0
    for k in N:
        if int(k)==0:
            x+=1
        else:
            y = max(x,y)
            x = 0 
    return y

solution(6)