#print([i for i in range(20,8,-1)])
#print([i**2 for i in range(1,13)])
#print([ (i*2-1)*(-1)**i for i in range(1,14) ])
#print(   [ i*(i+1)//2 for i in range(1,10) ]   )
#print( [ (i*2-1)*'*' for i in range(1,6) ] )

'''def create_zero_matrix(m,n):
    res = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(0)
        res.append(row)
    return res
print(create_zero_matrix(2,3))'''

'''def create_zero_matrix(m,n):
     return [ [0]*n  for i in range(m)  ]
print(create_zero_matrix(2,3))'''

'''
def plus(A,B):
     return [  [A[i][j] + B[i][j]  for j in range(len(A[0]))] for i in range(len(A))]
print(plus([[1,2],[3,4]],[[5,6],[7,8]]))
'''
'''
def transpose(A):
     return [ [ A[j][i]  for j in range(len(A))] for i in range(len(A[0]))]
print(transpose([[1,2],[3,4],[5,6]]))
'''

def multiply(A,B):
     #return [  [A[i][j] + B[i][j]  for j in range(len(A[0]))] for i in range(len(A))]
    return [ [ sum( A[i][k] * B[k][j] for k in range(len(A[0]))) for j in range(len(B[0]))] for i in range(len(A)) ]
print(multiply([[1,2,3,4,5],[3,4,6,7,8],[5,6,9,10,11]],[[12,23,34,45,56,44],[32,43,46,57,78,33],[51,63,59,80,71,22],[1,2,3,4,5,34],[6,7,8,9,10,99]]))

#result = [ [ sum( A[i][k] * B[k][j] for k in range(len(A[0]))) for j in range(len(B[0]))] for i in range(len(A)) ]

def multiply(A,B):
    res = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            summa = 0
            for k in range(len(A[0])):
                summa += A[i][k] * B[k][j]
            row.append(summa)
        res.append(row)
    return res
print(multiply([[1,2,3,4,5],[3,4,6,7,8],[5,6,9,10,11]],[[12,23,34,45,56,44],[32,43,46,57,78,33],[51,63,59,80,71,22],[1,2,3,4,5,34],[6,7,8,9,10,99]]))





