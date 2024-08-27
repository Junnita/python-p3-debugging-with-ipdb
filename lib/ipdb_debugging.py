#!/usr/bin/env python3

import ipdb

def plus_two(num):
    num = num + 2
    ipdb.set_trace()  # This line sets a breakpoint for debugging
    return num  # The return statement is correctly indented

if __name__ == "__main__":
    # Test the function
    test_num = 3
    result = plus_two(test_num)
    print(f"The result is: {result}")
