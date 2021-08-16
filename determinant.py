
def take_input():
    matrice=[]
    row_len=int (input("Enter rows :"))
    column_len=int (input("Enter columns :"))
    print("Enter elements one by one")
    for i in range(row_len):
        row =[]
        for j in range(column_len):
            row.append(int(input()))
        matrice.append(row)
    return determinant(matrice)
def row_column_ele_rm(indices,matrice):
    second_matrice=[]
    for i in range(len(matrice)):
        row =[]
        if (i!=indices[0]):
            for j in range(len(matrice[0])):
                if (j!=indices[1]):
                    row.append(matrice[i][j])
        if (len(row)!=0):
            second_matrice.append(row)
    return second_matrice
def determinant(matrice):
    if (len(matrice)==1):
        return matrice[0][0]
    else:
        t=0
        sum=0
        for i in range(len(matrice)):
            sum =sum+ ((-1)**t)*matrice[i][0] *( determinant(row_column_ele_rm((i,0),matrice)))
            t+=1
        return sum
print(take_input())