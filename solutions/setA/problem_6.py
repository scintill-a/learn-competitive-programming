nums = list(map(int, input("").split()))
target = int(input(""))


def two_sum(nums, target, counter = 0, seen = None):
    # fix for mutable default arguments, initialize inside the function
    if seen is None:
        seen = {}
    
    if counter >= len(nums):
        return "No Two Sum"

    curr_val = nums[counter]

    complement = target - curr_val

    if complement in seen:
        return [seen[complement], counter]

    seen[curr_val] = counter 



    return two_sum(nums, target, counter + 1, seen)

print(two_sum(nums, target))