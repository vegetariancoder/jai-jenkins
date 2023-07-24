def running_sum(nums):
    if isinstance(nums,list):
        run_sum = sum(nums)
        return run_sum
    else:
        return "Please enter the list for input"

print(running_sum([1,2,3,4]))
