import math

def nth_root(value, n):
    """
  To  Calculate the nth root of a given value.
    
    Args:
        value (float): The number to extract the root from.
        n (int): The degree of the root.
        
    Returns:
        float: The nth root of the input value.
    
    Raises:
        ValueError: If n is zero because division by zero is undefined.
    """
    if n == 0:
        raise ValueError("The degree of the root (n) cannot be zero.")
    return value ** (1 / n)

def euclidean_distance(point1, point2):
    """
    To Calculate the Euclidean distance between two points in n-dimensional space.
    
    Args:
        point1 (tuple or list of floats): The first point.
        point2 (tuple or list of floats): The second point.
        
    Returns:
        float: The Euclidean distance between the two points.
    
    Raises:
        ValueError: If the input points are not of the same dimensions.
    """
    if len(point1) != len(point2):
        raise ValueError("Both points must have the same dimensions.")

    squared_differences = [(p1 - p2) ** 2 for p1, p2 in zip(point1, point2)]
    return math.sqrt(sum(squared_differences))

# Example usage
if __name__ == "__main__":
    # Testing the nth_root function: The cube root of 27 should be 3.
    value = 27
    degree = 3
    print(f"The {degree}rd root of {value} is {nth_root(value, degree)}")
    
    # Testing the euclidean_distance function: Distance between (1,2) and (4,6).
    p1 = (1, 2)
    p2 = (4, 6)
    print(f"The Euclidean distance between {p1} and {p2} is {euclidean_distance(p1, p2)}")
