#!/usr/bin/env python3

import sys
import time

def main():
    print("Starting demo Python script for CircleCI...")
    time.sleep(1)

    # Sample logic
    result = 2 + 2
    print(f"Computation result: {result}")

    # Example test condition
    if result == 4:
        print("Test passed! 🎉")
        sys.exit(0)
    else:
        print("Test failed ❌")
        sys.exit(1)

if __name__ == "__main__":
    main()
