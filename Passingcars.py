'''
A non-empty array A consisting of N integers is given. The consecutive elements of array A represent consecutive cars on a road.

Array A contains only 0s and/or 1s:

0 represents a car traveling east,
1 represents a car traveling west.
The goal is to count passing cars. We say that a pair of cars (P, Q), where 0 ≤ P < Q < N, is passing when P is traveling to the east and Q is traveling to the west.

For example, consider array A such that:

  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).

Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the number of pairs of passing cars.

The function should return −1 if the number of pairs of passing cars exceeds 1,000,000,000.

For example, given:

  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
the function should return 5, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer that can have one of the following values: 0, 1.
'''

def solution(A):
    z = 0
    o = 0
    for i in A:
        if i == 0:
            z +=1
        else:
            o+=z
    if o =< 1000000000:
        return b
    else:
        return -1
    
    # GOOD VALUTION. What we do here is that if the value is 01011 the first 1 has only one zero before it and the other has 2 so we add the number of 0 before every 1 and thats's how we solve it
    #100%
    
    
    
'''    
def solution(A):
    b = 0
    for i in range(0,len(A)):
        while A.count(0) != 0:
            z = A.index(0)
            A = A[z:]
            b += A.count(1)
            A.remove(A[0])
        if b < 1000000000:
            return b
        else: 
            return -1
    
solution([1,1,0,1,0,1,1])

# 50% It worked but didn't pass the time tests '''
