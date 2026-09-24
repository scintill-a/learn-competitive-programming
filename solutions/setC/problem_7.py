# peak   =  n[i] > n[i-1]
# valley =  n[i] < n[i-1]
# count each peak
# get the maximum peak value (dont use max)

nums = [*map(int, input().split())]

n_max = sorted(nums)[::-1][0]
n_peaks = 0
n_valleys = 0
amp = 0


# [1,2,3,4,5] len(5), zi_max = 4, range(1,3)=[2,3,4]

l_peaks = []
l_valleys = []

def p7(nums, amp):
    global n_peaks
    global n_valleys

    for i in range(1, len(nums) - 1):
        if (nums[i]> nums[i-1] and nums[i] > nums[i+1]):
            n_peaks += 1
            l_peaks.append(nums[i])
        elif (nums[i] < nums[i-1] and nums[i] < nums[i+1]):
            n_valleys += 1
            l_valleys.append(nums[i])
        else:
            continue

    if (len(l_peaks) <= 0 and len(l_valleys) <= 0): return 0

    return max(l_peaks) - min(l_valleys)

val = p7(nums, amp)

print(f"{n_peaks}, {n_valleys}, Amplitude:{val}")
print(n_max)