"""
This module provides a function to calculate the running sum of a list of numbers.
"""
def running_sum(nums):
    """
    Calculate the running sum of a list of numbers.

    :param nums: list of nums
    :return: integer
    """
    if isinstance(nums,list):
        run_sum = sum(nums)
        return run_sum
    return "Please enter the list for input"

print(running_sum([1,2,3,4]))
