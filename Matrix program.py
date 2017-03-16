#Ismael Garrido
#MatrixProgram.py
#Homework13
#Prof.Natalia Novak

def greetings():
    print('This program tries to open two file with the names provided by the user,\n',
          'and read all the data into a two-dimensional array/list',
    'Then add both matrices, and display the result.')

def processData(data):
    rows = len(data)
    
    print('number of lines is',rows)
    
    A=list()

    cols=0
    for r in range(rows):
        line=data[r].split() # split by white space, store is a list

        if r == 0: # getting the number of elements in each string of the list
            cols=len(line)
            print('number of elements in each line is ',cols)

        if len(line) != cols:
            print('Warning: line %d:'%(cols+1))

            raise ValueError('number of elements in this line is different from the lines above')

        # use list comprehension to convert each element to integer
        line_int=[int(elem) for elem in line]
            
        # appent the list of integers to list A as a next element of list A
        A.append(line_int)
    return A

def display(A):

    cols=len(A[0])
    for i in range(len(A)):
        for j in range(cols):
            print(A[i][j],end=" ")
        print()
        
def matrixAddition(A, B):

    r = []
    for i in range(len(A)):
        temp = []
        for j in range(len(A[0])):
            temp.append(A[i][j] + B[i][j])

        r.append(temp)


    return r


def main():

    greetings()

    while True:

        fmatrix = input('Please, input the name of the file with the first matrix:')
        Smatrix = input('Please, input the name of the file with the second matrix:')
        finalMatrix = input('Please, input the name of the file where you want to store the result:')
        
        try:
            f=open(fmatrix)
            f1=open(Smatrix)
            f2 = open(finalMatrix, 'w')
            break
        except ValueError:
            print('cannot open file',fmatrix, Smatrix)
            

    print('File %s is opened successfully!'%fmatrix)
    print('File %s is opened successfully!'%Smatrix)

    
    data = f.readlines()
    data1 = f1.readlines()
    
  
    A =processData(data)
    B =processData(data1)

    print(A)
    print(B)
    
    print()
    print("This is the first Matrix.\n")
    display(A)
    print()
    print("This is the second Matrix.\n")
    display(B)

    r = matrixAddition(A, B)

    print()
    print("The resulting matrix is as follows")
    display(r)
    
    cols=len(r[0])
    for i in range(len(r)):
        for j in range(cols):
          print(r[i][j],end=" ", file = f2)
        print( file = f2)
        
    f.close()
    f1.close()
    f2.close()

main()    
