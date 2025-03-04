import sys
from main import cal

def run_tests():
    score = 0
    total_tests = 4

    # Test Case 1: Addition
    if cal("+", 5, 3) == 8:
        score += 1
        print("Test 1 Passed")
    else:
        print("Test 1 Failed")

    # Test Case 2: Addition with negatives
    if cal("+", -2, 4) == 2:
        score += 1
        print("Test 2 Passed")
    else:
        print("Test 2 Failed")

    # Test Case 3: Subtraction
    if cal("-", 10, 4) == 6:
        score += 1
        print("Test 3 Passed")
    else:
        print("Test 3 Failed")

    # Test Case 4: Subtraction with negatives
    if cal("-", -5, -3) == -2:
        score += 1
        print("Test 4 Passed")
    else:
        print("Test 4 Failed")

    print(f"Final Score: {score}/{total_tests}")

    # Exit with non-zero status if tests fail (for GitHub Autograder)
    if score == total_tests:
        sys.exit(0)  # Success
    else:
        sys.exit(1)  # Failure

if __name__ == "__main__":
    run_tests()
