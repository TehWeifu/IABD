import numpy as np

# Load the wine.csv file
wine_data = np.genfromtxt('wine.csv', delimiter=',')


# Define the function imprimir_datos
def imprimir_datos(matrix):
    # Separate features (x) and wine types (y)
    x = matrix[:, :-1]  # All rows, all columns except the last
    y = matrix[:, -1]  # All rows, only the last column

    # Print the number of features for each type of wine
    print(f"Number of features for each type of wine: {x.shape[1]}")

    # Print the number of wine samples
    print(f"Number of wine samples: {x.shape[0]}")

    # Print the number of distinct types of wine and what they are
    unique_wines = np.unique(y)
    print(f"Number of distinct types of wine: {len(unique_wines)}")
    print(f"Distinct types of wine: {unique_wines}")

    # Print max and min values for each feature
    print("Max values of each feature:", np.max(x, axis=0))
    print("Min values of each feature:", np.min(x, axis=0))

    # Return the feature matrix and wine types array
    return x, y


# Call the function with the wine data
x, y = imprimir_datos(wine_data)
