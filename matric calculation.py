import numpy as np


print("#"*10,"Matrix Operations Tool","#"*10)
def matric():
    elements=[]
    rows=int(input("Enter number of rows:"))
    cols=int(input("Enter number of columns:"))
    i=1
    while i<=rows:
        values=input(f"Enter {i} row value(use ',')").strip().split(",")
        if len(values)!=cols:
            print("Please enter values with in column range")
            continue
        else:
            values=[int(i) for i in values]
            elements.append(values)
            i=i+1
    return elements


def main(matric): 
    while True:
        try:
            choice = int(input("1. Addition\n2. Substraction\n3. Multiplecation\n4. Transpose\n5. Determinate\n6. Exit\nEnter number to calculation:"))
            if choice==6:
                print("Thank you")
                break
            elif choice in [1,2,3,4,5]:
                print("Etner first matric")
                a=np.array(matric())
                print("Matric 'A'\n",a)
                    
                print("Enter second matrix") 
                b=np.array(matric())
                print("Matric 'B'\n",b)
            
                if choice==1:
                    if a.shape==b.shape:
                        print('Addition of two matrix is:\n',np.add(a,b))
                    else:
                        print("both matix rows and columns are must be equal")
                elif choice==2:
                    if a.shape==b.shape:
                        print('Substraction of two matrix is:\n',np.subtract(a,b))
                    else:
                        print("both matrix rows and columns are must be equal")
                elif choice==3:
                    if a.shape[0]==b.shape[1]:
                        print('Addition of two matrix is:\n',np.dot(a,b))
                    else:
                        print("first matrix colums must be equal to second matrix rows")
                elif choice==4:
                    print("A Transpose\n",a.T)
                    print("B Transpose\n",b.T)
                elif choice==5:  # Determinant
                    if a.shape[0] == a.shape[1]:
                            print(f"\nDeterminant of A: {np.linalg.det(a):.2f}")
                    else:
                        print("Matrix A is not square, determinant not possible.")

                    if b.shape[0] == b.shape[1]:
                        print(f"Determinant of B: {np.linalg.det(b):.2f}")
                    else:
                        print("Matrix B is not square, determinant not possible.")
            else:
                print("you are entered wrong option.")  
        except:
            print("\n########## something went wrong please try again ##############")
    
main(matric)