import numpy as np
from sklearn.metrics import precision_score, recall_score

def main():
    # Read N
    N = int(input("Enter N: "))
    if N <= 0:
        print("Error: N must be a positive integer.")
        return

    # Initialize arrays
    truth = np.zeros(N, dtype=int)
    predicted = np.zeros(N, dtype=int)

    # Read N points
    for i in range(N):
        x = int(input(f"Enter x (ground truth) for point {i+1}: "))
        y = int(input(f"Enter y (predicted) for point {i+1}: "))
        if x not in (0, 1) or y not in (0, 1):
            print("Error: x and y must be 0 or 1.")
            return
        truth[i] = x
        predicted[i] = y

    # Calculate precision and recall
    precision = precision_score(truth, predicted, zero_division=0)
    recall = recall_score(truth, predicted)

    # Output results
    print(f"Precision is: {precision:.2f}")
    print(f"Recall is: {recall:.2f}")

if __name__ == "__main__":
    main()
