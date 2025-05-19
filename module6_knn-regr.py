import numpy as np

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
    points = []
    for i in range(N):
        x = float(input(f"Enter x value for point {i+1}: "))
        y = float(input(f"Enter y value for point {i+1}: "))
        points.append([x, y])
    
    # Convert to NumPy array
    points = np.array(points)
    
    # Read X
    X = float(input("Enter X to predict: "))
    
    # Calculate k-NN Regression
    distances = np.abs(points[:, 0] - X)
    sorted_indices = np.argsort(distances)
    k_nearest_y = points[sorted_indices[:k], 1]
    y_pred = np.mean(k_nearest_y)
    
    print(f"The predicted Y value is: {y_pred:.2f}")

if __name__ == "__main__":
    main()
