nums = list(map(int, input().split()))

if not nums:
    print("Max Streak: 0")
else:
    max_streak = 1
    curr_streak = 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            curr_streak += 1
            if curr_streak > max_streak:
                max_streak = curr_streak
        else:
            curr_streak = 1
    print(f"Max Streak: {max_streak}")
