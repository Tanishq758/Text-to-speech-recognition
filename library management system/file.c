#include <stdio.h>
#define SIZE 3
void input_matrix(int matrix[SIZE][SIZE]) {
    printf("Enter matrix elements: \n");
    for (int i = 0; i < SIZE; i++)
        for (int j = 0; j < SIZE; j++)
            scanf("%d", &matrix[i][j]);
}
void print_matrix(int matrix[SIZE][SIZE]) {
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++)
            printf("%d ", matrix[i][j]);
        printf("\n");
    }
}
void upper_lower_triangular(int matrix[SIZE][SIZE]) {
    printf("Upper triangular matrix:\n");
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            if (i > j) printf("0 ");
            else printf("%d ", matrix[i][j]);
        }
        printf("\n");
    }
    printf("Lower triangular matrix:\n");
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            if (i < j) printf("0 ");
            else printf("%d ", matrix[i][j]);
        }
        printf("\n");
    }
}
void multiply_matrices(int matrix1[SIZE][SIZE], int matrix2[SIZE][SIZE], int result[SIZE][SIZE]) {
    for (int i = 0; i < SIZE; i++)
        for (int j = 0; j < SIZE; j++) {
            result[i][j] = 0;
            for (int k = 0; k < SIZE; k++)
                result[i][j] += matrix1[i][k] * matrix2[k][j];
        }
}
int main() {
    int matrix1[SIZE][SIZE], matrix2[SIZE][SIZE], result[SIZE][SIZE], choice;
    printf("1. Addition\n2. Subtraction\n3. Transpose\n4. Upper/Lower Triangular\n5. Multiplication\nEnter choice: ");
    scanf("%d", &choice);
    input_matrix(matrix1);
    if (choice == 1 || choice == 2 || choice == 5) input_matrix(matrix2);
    switch (choice) {
        case 1:
            for (int i = 0; i < SIZE; i++)
                for (int j = 0; j < SIZE; j++)
                    result[i][j] = matrix1[i][j] + matrix2[i][j];
            break;
        case 2:
            for (int i = 0; i < SIZE; i++)
                for (int j = 0; j < SIZE; j++)
                    result[i][j] = matrix1[i][j] - matrix2[i][j];
            break;
        case 3:
            for (int i = 0; i < SIZE; i++)
                for (int j = 0; j < SIZE; j++)
                    result[j][i] = matrix1[i][j];
            break;
        case 4:
            upper_lower_triangular(matrix1);
            return 0;
        case 5:
            multiply_matrices(matrix1, matrix2, result);
            break;
        default:
            printf("Invalid choice!\n");
            return 1;
    }
    print_matrix(result);
    return 0;
}