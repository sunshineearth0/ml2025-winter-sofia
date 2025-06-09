import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def main():
    # Read training data
    N = int(input("Enter N: "))
    if N <= 0:
        print("Error: N must be a positive integer.")
        return
    
    X_train = np.empty((N, 1))
    y_train = np.empty(N, dtype=int)
    for i in range(N):
        x = float(input(f"Enter x for training point {i+1}: "))
        y = int(input(f"Enter y for training point {i+1}: "))
        X_train[i,0] = x
        y_train[i] = y
    
        
    # Read test data
    M = int(input("\nEnter M: "))
    if M <= 0:
        print("Error: M must be a positive integer.")
        return
    
    X_test = np.empty((M, 1))
    y_test = np.empty(M, dtype=int)
    for i in range(M):
        x = float(input(f"Enter x for test point {i+1}: "))
        y = int(input(f"Enter y for test point {i+1}: "))
        X_test[i, 0] = x
        y_test[i] = y
    
        
    # Initialize variables to track best k and accuracy
    best_k = 0
    best_accuracy = -1.0
    
    # Evaluate k from 1 to 10
    print("\nEvaluating k from 1 to 10:")
    for k in range(1, min(11, N+1)):
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred) * 100
        print(f"k = {k}: Accuracy = {accuracy:.2f}%")
        
        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_k = k
    
    # Output the best k and its accuracy
    print(f"\nThe best k is {best_k} with a test accuracy of {best_accuracy:.2f}%")

if __name__ == "__main__":
    main()
