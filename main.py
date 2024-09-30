# Functions
def get_matrix_size(): # For both Matrix A and B
    rows = int(input("Insert the number of rows for both Matrix A and B: "))
    columns = int(input("Insert the number of columns for both Matrix A and B: "))
    return rows, columns

def get_matrix_size_A(): # Individual for Matrix A
    rows = int(input("Insert the number of rows for Matrix A: "))
    columns = int(input("Insert the number of columns for Matrix A: "))
    return rows, columns

def get_matrix_size_B(): # Individual for Matrix B
    rows = int(input("Insert the number of rows for Matrix B: "))
    columns = int(input("Insert the number of columns for Matrix B: "))
    return rows, columns

def get_matrix_size_identity(): # For Identity Matrix
    rows = int(input("Insert the number of rows for Matrix: "))
    columns = int(input("Insert the number of columns for Matrix: "))
    return rows, columns

def get_matrix_input(rows, columns, label):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(int(input(f"{label} [{i}][{j}] - Insert a value: ")))
        matrix.append(row)
    return matrix

def add_matrices(matrixA, matrixB):
    rows = len(matrixA)
    columns = len(matrixA[0])
    result = [[matrixA[i][j] + matrixB[i][j] for j in range(columns)] for i in range(rows)]
    return result

def subtract_matrices(matrixA, matrixB):
    rows = len(matrixA)
    columns = len(matrixA[0])
    result = [[matrixA[i][j] - matrixB[i][j] for j in range(columns)] for i in range(rows)]
    return result

def identity_matrix(rows, columns):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(columns):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    return matrix

def multiply_matrix(matrixA, matrixB):
    rows_A = len(matrixA)
    columns_A = len(matrixA[0])
    rows_B = len(matrixB)
    columns_B = len(matrixB[0])
    if columns_A != rows_B:
        print("Invalid input. Number of columns in Matrix A must be equal to the number of rows in Matrix B.")
        return None
    result = [[0 for _ in range(columns_B)] for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(columns_B):
            for k in range(columns_A):
                result[i][j] += matrixA[i][k] * matrixB[k][j]
    return result

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(str(element) for element in row))
    print()

def menu():
    while True:
        print()
        print(("*" * 10),"MATRIX CALCULATOR", ("*" * 10))
        print("1 - Add matrices\n2 - Subtract matrices\n3 - Multiply matrices\n4 - Identity matrix\n5 - Exit")
        print("*" * 39)
        menu_choice = int(input("Choose here: "))
        print()
        while menu_choice not in [1, 2, 3, 4, 5]:
            menu_choice = int(input("Invalid input - Choose here: "))
        if menu_choice == 1:
            rows, columns = get_matrix_size()
            matrixA = get_matrix_input(rows, columns, "Matrix A")
            matrixB = get_matrix_input(rows, columns, "Matrix B")
            result = add_matrices(matrixA, matrixB)
            print("\nResult:")
            print_matrix(result)
        elif menu_choice == 2:
            rows, columns = get_matrix_size()
            matrixA = get_matrix_input(rows, columns, "Matrix A")
            matrixB = get_matrix_input(rows, columns, "Matrix B")
            result = subtract_matrices(matrixA, matrixB)
            print("\nResult:")
            print_matrix(result)
        elif menu_choice == 3:
            rows, columns = get_matrix_size_A()
            matrixA = get_matrix_input(rows, columns, "Matrix A")
            rows, columns = get_matrix_size_B()
            matrixB = get_matrix_input(rows, columns, "Matrix B")
            result = multiply_matrix(matrixA, matrixB)
            if result:
                print("\nResult:")
                print_matrix(result)
        elif menu_choice == 4:
            rows, columns = get_matrix_size_identity()
            result = identity_matrix(rows, columns)
            print("\nResult:")
            print_matrix(result)
        else:
            print("The program has been closed. Thanks for using Matrix Calculator by Tuchanski")
            print()
            break

if __name__ == "__main__":
    menu()
