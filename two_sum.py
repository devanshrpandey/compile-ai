
def two_sum_brute_force(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
def two_sum(nums, target):
    diffs = [target - num for num in nums]
    numset = set(nums)
    for i,num in enumerate(diffs):
        if num in numset:
            return [i, nums.index(num)]
    raise ValueError("No two numbers add up to the target")

if __name__ == "__main__":
    nums = [2,4,12,18,3,57,182]
    target = 60
    brute_force_result = two_sum_brute_force(nums, target)
    optimized_result = two_sum(nums, target)
    assert brute_force_result == [4, 5] == optimized_result == [4, 5]
    nums = input("Enter a list of numbers separated by spaces: ").split(" ")
    nums = [int(num) for num in nums]
    target = int(input("Enter the target: "))
    print(f"The indices of the two numbers that add up to {target} are {two_sum(nums, target)}")
    