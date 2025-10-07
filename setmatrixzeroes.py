matrix=[[1,1,1],[1,0,1],[1,1,1]]
rows=len(matrix)
cols=len(matrix[0])
fi_row=False
fi_col=False
for i in range(rows):
    if matrix[i][0]==0:
        fi_row=True
for i in range(cols):
    if matrix[0][i]==0:
        fi_col=True
for i in range(1,rows):
    for j in range(1,cols):
        if matrix[i][j]==0:
            matrix[i][0]=0
            matrix[0][j]=0
for i in range(1,rows):
    for j in range(1,cols):
        if matrix[i][0]==0 or matrix[j][0]==0:
            matrix[i][j]=0
if fi_row:
    for i in range(rows):
        matrix[i][0]=0
if fi_row:
    for j in range(cols):
        matrix[0][j]=0
print(matrix)