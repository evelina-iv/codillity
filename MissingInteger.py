'''This is a demo task.

Write a function:

def solution(A)
that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].'''

def solution(A):
    m = min(A)
    if m > 1:
        return 1
    elif m < 1 and A.count(1) == 0:
        return 1
    A.sort()
    A = list(dict.fromkeys(A))
    for i in range(0,len(A)-1):
     if ((A[i+1]-A[i] )!= 1 and (A[i]+1) > 0):        
         return A[i]+1
    return A[-1]+1
#100! ON YOUR OWN GOOD JOB
    