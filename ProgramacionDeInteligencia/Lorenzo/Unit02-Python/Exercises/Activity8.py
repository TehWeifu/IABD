import tabulate

numbers = [
    [1, 0, 0, 0],
    [0, 1, 7, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
]

element_second_row_third_column = numbers[1][2]
third_row = numbers[2]
second_column = [row[1] for row in numbers]

print("The element on the 2nd file and 3rd column is: ", element_second_row_third_column)
print("The elements on the 3rd row are: ", third_row)
print("The elements on the 2rd row are: ", second_column)
print(tabulate.tabulate(numbers, headers=["A", "B", "C", "D"]))
