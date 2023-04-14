def euclidean_algorithm(a, b):
    return a if b == 0 else euclidean_algorithm(b, a % b)


if __name__ == "__main__":
    assert euclidean_algorithm(45, 15) == 15
    assert euclidean_algorithm(45, 10) == 5
    assert euclidean_algorithm(13, 11) == 1
    assert euclidean_algorithm(18, 4) == 2
    print("all tests successful")
