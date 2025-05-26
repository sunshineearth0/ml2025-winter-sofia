import numpy as np
from sklearn.neighbors import KNeighborsRegressor

def main():
    # Read N
    N = int(input("Enter N: "))
    if N <= 0:
        print("Error: N must be a positive integer.")
        return

    # Read k
    k = int(input("Enter k: "))
    if k <= 0 or k > N:
        print("Error: k must be a positive integer and not greater than N.")
        return

    # Read N points
    X_train = np.empty((N, 1))
    y_train = np.empty(N)
    for i in range(N):
        x = float(input(f"Enter x for point {i+1}: "))
        y = float(input(f"Enter y for point {i+1}: "))
        X_train[i,0] = x
        y_train[i] = y


    # Calculate variance
    variance = np.var(y_train)
    print(f"\nVariance of labels in training dataset: {variance:.2f}")

    # Read X
    X = float(input("\nEnter X to predict: "))

    # Create and train model
    model = KNeighborsRegressor(n_neighbors=k)
    model.fit(X_train, y_train)

    # Predict and display result
    prediction = model.predict([[X]])
    print(f"\nThe predicted Y value is: {prediction[0]:.2f}")

if __name__ == "__main__":
    main()
