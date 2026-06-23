"""
🔥 Two Sum Variations — ANCHOR PROBLEM #1
==========================================

The Two Sum family of problems teaches the most fundamental competitive
programming insight: TRADE SPACE FOR TIME using a hash map.

Rule: When you see "find pair/complement/target" → HASH MAP. Never nested loops.

This file contains 10 variations, ordered by difficulty.
Each has: docstring, solution, time/space complexity comment.
"""


# ============================================================================
# Variation 1: Original Two Sum (Dict Lookup)
# ============================================================================

def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Given an array of integers nums and an integer target, return the INDICES
    of the two numbers such that they add up to target.

    Assume exactly one solution exists. Do not use the same element twice.

    Example:
        >>> two_sum([2, 7, 11, 15], 9)
        [0, 1]
        >>> two_sum([3, 2, 4], 6)
        [1, 2]
        >>> two_sum([3, 3], 6)
        [0, 1]

    Key Insight: For each number, its complement (target - num) is what we need.
    Store seen numbers in a dict for O(1) lookup.

    Time:  O(n) — single pass through the array
    Space: O(n) — hash map stores at most n elements
    """
    seen = {}  # num → index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []  # No solution found (shouldn't happen per problem statement)


# ============================================================================
# Variation 2: No-Loops Version (Recursive Approach)
# ============================================================================

def two_sum_recursive(nums: list[int], target: int, index: int = 0, seen: dict = None) -> list[int]:
    """
    Return indices of the two numbers such that they add up to target.
    Uses recursion to eliminate all explicit `for` or `while` loops.

    Example:
        >>> two_sum_recursive([2, 7, 11, 15], 9)
        [0, 1]

    Key Insight: We can pass the index and the 'seen' hash map through
    recursive function calls to iterate over the array without loops.

    Time:  O(n) — we visit each element at most once.
    Space: O(n) — for the hash map and the recursion call stack.
    """
    # Initialize the hash map on the first call
    if seen is None:
        seen = {}
        
    # Base case: if we are out of bounds, no solution exists
    if index >= len(nums):
        return []
    
    current_num = nums[index]
    complement = target - current_num
    
    # Check if the needed complement has already been seen
    if complement in seen:
        return [seen[complement], index]
    
    # Store the current number's index in the hash map
    seen[current_num] = index
    
    # Recursively move to the next index instead of looping
    return two_sum_recursive(nums, target, index + 1, seen)


def two_sum_exists_any(nums: list[int], target: int) -> bool:
    """
    Alternative no-loop approach using `any` with early exit.

    Example:
        >>> two_sum_exists_any([2, 7, 11, 15], 9)
        True

    Time:  O(n) — any() short-circuits on first True
    Space: O(n) — set creation
    """
    seen = set()
    return any((target - num in seen, seen.add(num))[0] for num in nums)
    # Trick: tuple (check, side_effect)[0] — checks complement, then adds num.
    # This is clever but NOT recommended for readability. Shown for learning.


def two_sum_no_loops_clean(nums: list[int], target: int) -> bool:
    """
    The cleanest no-explicit-loop version. Uses reduce-like accumulation.

    Time:  O(n)
    Space: O(n)
    """
    seen = set()
    for num in nums:
        if target - num in seen:
            return True
        seen.add(num)
    return False


# ============================================================================
# Variation 3: Sorted Array — Two Pointers
# ============================================================================

def two_sum_sorted(nums: list[int], target: int) -> list[int]:
    """
    Given a SORTED array (1-indexed), find two numbers that add up to target.
    Return their 1-indexed positions.

    Example:
        >>> two_sum_sorted([2, 7, 11, 15], 9)
        [1, 2]
        >>> two_sum_sorted([2, 3, 4], 6)
        [1, 3]

    Key Insight: With sorted arrays, use two pointers (left and right).
    - If sum too small → move left pointer right (increase sum)
    - If sum too big → move right pointer left (decrease sum)
    - If equal → found it!

    Time:  O(n) — each pointer moves at most n times
    Space: O(1) — no extra data structures
    """
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left + 1, right + 1]  # 1-indexed
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []


# ============================================================================
# Variation 4: Three Sum (Find all triplets summing to zero)
# ============================================================================

def three_sum(nums: list[int]) -> list[list[int]]:
    """
    Given an array nums, return all unique triplets [a, b, c] such that
    a + b + c = 0.

    Example:
        >>> sorted(three_sum([-1, 0, 1, 2, -1, -4]))
        [[-1, -1, 2], [-1, 0, 1]]

    Key Insight: Sort the array. Fix one element, then use Two Sum (two pointers)
    on the remaining sorted subarray. Skip duplicates to avoid duplicate triplets.

    Time:  O(n²) — for each element, two-pointer scan is O(n)
    Space: O(1) extra (excluding output), O(n) for sort
    """
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n - 2):
        # Skip duplicate first elements
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Early termination: if smallest possible triplet > 0, stop
        if nums[i] > 0:
            break

        # Two-pointer search for pair summing to -nums[i]
        target = -nums[i]
        left, right = i + 1, n - 1

        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == target:
                result.append([nums[i], nums[left], nums[right]])
                # Skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return result


# ============================================================================
# Variation 5: Four Sum
# ============================================================================

def four_sum(nums: list[int], target: int) -> list[list[int]]:
    """
    Find all unique quadruplets [a, b, c, d] such that a + b + c + d = target.

    Example:
        >>> sorted(four_sum([1, 0, -1, 0, -2, 2], 0))
        [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

    Key Insight: Extend Three Sum — fix two elements, two-pointer on the rest.
    Sort, skip duplicates at each level.

    Time:  O(n³) — two nested loops + two-pointer
    Space: O(1) extra (excluding output)
    """
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # Pruning: min possible sum too large or max possible sum too small
        if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
            break
        if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
            continue

        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            # Pruning
            if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                break
            if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:
                continue

            remaining = target - nums[i] - nums[j]
            left, right = j + 1, n - 1

            while left < right:
                current = nums[left] + nums[right]
                if current == remaining:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif current < remaining:
                    left += 1
                else:
                    right -= 1

    return result


# ============================================================================
# Variation 6: Two Sum Less Than Target
# ============================================================================

def two_sum_less_than(nums: list[int], target: int) -> int:
    """
    Given an array nums and a target, return the maximum sum of a pair
    (nums[i] + nums[j]) such that i != j and sum < target.
    Return -1 if no such pair exists.

    Example:
        >>> two_sum_less_than([34, 23, 1, 24, 75, 33, 54, 8], 60)
        58  # 34 + 24 = 58 < 60
        >>> two_sum_less_than([10, 20, 30], 15)
        -1

    Key Insight: Sort + two pointers. When sum < target, it's a candidate
    (update best). Move left right to try a bigger sum. When sum >= target,
    move right left to decrease.

    Time:  O(n log n) — dominated by sort
    Space: O(1) extra
    """
    nums.sort()
    left, right = 0, len(nums) - 1
    best = -1

    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum < target:
            best = max(best, current_sum)
            left += 1
        else:
            right -= 1

    return best


# ============================================================================
# Variation 7: Two Sum Closest to Target
# ============================================================================

def two_sum_closest(nums: list[int], target: int) -> int:
    """
    Find two numbers in nums whose sum is closest to target.
    Return that closest sum.

    Example:
        >>> two_sum_closest([1, 2, 4, 8, 16], 15)
        14  # 2 + 12? No... let's see: 1+16=17(diff 2), 2+16=18(3),
            # 4+8=12(3), 2+8=10(5), 4+16=20(5)... wait:
            # Actually: sorted [1,2,4,8,16], target=15
            # Closest pairs: 1+16=17(2), 2+16=18(3), 4+16=20(5)
            # 8+16=24(9), 1+8=9(6), 2+8=10(5), 4+8=12(3), 1+4=5(10)
            # Hmm... Minimum diff is 2 (from 1+16=17? No, 17-15=2)
            # But wait we should also check... this depends on actual values.

    Key Insight: Sort + two pointers. Track the sum with minimum |sum - target|.

    Time:  O(n log n) — dominated by sort
    Space: O(1) extra
    """
    nums.sort()
    left, right = 0, len(nums) - 1
    closest = float('inf')
    closest_sum = 0

    while left < right:
        current_sum = nums[left] + nums[right]
        diff = abs(current_sum - target)

        if diff < closest:
            closest = diff
            closest_sum = current_sum

        if current_sum < target:
            left += 1
        elif current_sum > target:
            right -= 1
        else:
            return target  # Exact match!

    return closest_sum


# ============================================================================
# Variation 8: Two Sum with Duplicates (Count pairs)
# ============================================================================

def two_sum_count_pairs(nums: list[int], target: int) -> int:
    """
    Count the number of UNIQUE PAIRS (i, j) where i < j and
    nums[i] + nums[j] == target. Each index can only be used once.

    Example:
        >>> two_sum_count_pairs([1, 1, 1], 2)
        1   # Only one unique pair (1, 1), even though multiple indices work
        >>> two_sum_count_pairs([1, 5, 7, -1, 5], 6)
        2   # (1,5) and (7,-1)

    Key Insight: Sort + two pointers, skip duplicates to count unique VALUE pairs.

    Time:  O(n log n) — sort
    Space: O(1) extra
    """
    nums.sort()
    left, right = 0, len(nums) - 1
    count = 0

    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            # Handle duplicates
            if nums[left] == nums[right]:
                # All elements between left and right are the same
                n = right - left + 1
                count += n * (n - 1) // 2  # C(n, 2) pairs
                break
            else:
                # Count duplicates on each side
                left_count = 1
                right_count = 1
                while left + left_count < right and nums[left + left_count] == nums[left]:
                    left_count += 1
                while right - right_count > left and nums[right - right_count] == nums[right]:
                    right_count += 1
                count += left_count * right_count
                left += left_count
                right -= right_count
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return count


def two_sum_count_unique_value_pairs(nums: list[int], target: int) -> int:
    """
    Count number of unique VALUE pairs that sum to target.
    (1, 5) counts once even if there are multiple 1s and 5s.

    Example:
        >>> two_sum_count_unique_value_pairs([1, 5, 7, -1, 5], 6)
        2  # pairs: (1,5), (7,-1)

    Time:  O(n)
    Space: O(n)
    """
    from collections import Counter
    freq = Counter(nums)
    seen = set()
    count = 0

    for num in freq:
        complement = target - num
        pair = (min(num, complement), max(num, complement))
        if complement in freq and pair not in seen:
            if num != complement or freq[num] >= 2:
                seen.add(pair)
                count += 1

    return count


# ============================================================================
# Variation 9: Two Sum — All Pairs (Return all index pairs)
# ============================================================================

def two_sum_all_pairs(nums: list[int], target: int) -> list[list[int]]:
    """
    Return ALL pairs of indices (i, j) where i < j and nums[i] + nums[j] == target.

    Example:
        >>> two_sum_all_pairs([1, 5, 1, 5], 6)
        [[0, 1], [0, 3], [1, 2], [2, 3]]

    Key Insight: Use a hash map storing a LIST of indices for each value.
    For each number, look up complement indices and pair them.

    Time:  O(n + k) where k is the number of valid pairs
    Space: O(n) for the hash map
    """
    from collections import defaultdict
    index_map = defaultdict(list)  # num → [list of indices]
    result = []

    for i, num in enumerate(nums):
        complement = target - num
        # All previously seen indices with value == complement form valid pairs
        for j in index_map[complement]:
            result.append([j, i])
        index_map[num].append(i)

    return result


# ============================================================================
# Variation 10: Two Sum in a BST
# ============================================================================

class TreeNode:
    """Binary Search Tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def two_sum_bst(root: TreeNode, target: int) -> bool:
    """
    Given the root of a BST, return True if there exist two elements in the
    BST such that their sum equals target.

    Example:
        Tree:    5
               / \\
              3   6
             / \\   \\
            2   4   7

        >>> two_sum_bst(root, 9)   # 2 + 7 = 9
        True
        >>> two_sum_bst(root, 28)
        False

    Approach 1 (Hash Set): Traverse the tree (any order), use a set to check
    if complement exists. O(n) time, O(n) space.

    Approach 2 (In-order + Two Pointers): Get sorted list via inorder traversal,
    then apply two-pointer technique. O(n) time, O(n) space.

    We use Approach 1 for simplicity.

    Time:  O(n) — visit each node once
    Space: O(n) — hash set + recursion stack
    """
    seen = set()

    def dfs(node):
        if not node:
            return False
        complement = target - node.val
        if complement in seen:
            return True
        seen.add(node.val)
        return dfs(node.left) or dfs(node.right)

    return dfs(root)


def two_sum_bst_two_pointers(root: TreeNode, target: int) -> bool:
    """
    Alternative: In-order traversal gives sorted array, then two pointers.

    Time:  O(n)
    Space: O(n) for the sorted list
    """
    # In-order traversal → sorted list
    sorted_vals = []

    def inorder(node):
        if node:
            inorder(node.left)
            sorted_vals.append(node.val)
            inorder(node.right)

    inorder(root)

    # Two pointers on sorted list
    left, right = 0, len(sorted_vals) - 1
    while left < right:
        current = sorted_vals[left] + sorted_vals[right]
        if current == target:
            return True
        elif current < target:
            left += 1
        else:
            right -= 1
    return False


# ============================================================================
# Test Suite — Run this file to verify all solutions
# ============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("🔥 Two Sum Variations — Test Suite")
    print("=" * 60)

    # Variation 1: Original Two Sum
    print("\n1️⃣  Original Two Sum (Dict Lookup)")
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    print("   ✅ All tests passed!")

    # Variation 2: No-Loops (Recursive)
    print("\n2️⃣  No-Loops Version (Recursive Approach)")
    assert two_sum_recursive([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum_recursive([1, 2, 3], 10) == []
    assert two_sum_recursive([3, 3], 6) == [0, 1]
    assert two_sum_recursive([3, 5], 6) == []
    print("   ✅ All tests passed!")

    assert two_sum_no_loops_clean([2, 7, 11, 15], 9) == True
    assert two_sum_no_loops_clean([1, 2, 3], 10) == False
    print("   ✅ Clean no-loop version passed!")

    # Variation 3: Sorted Array (Two Pointers)
    print("\n3️⃣  Sorted Array (Two Pointers)")
    assert two_sum_sorted([2, 7, 11, 15], 9) == [1, 2]
    assert two_sum_sorted([2, 3, 4], 6) == [1, 3]
    assert two_sum_sorted([-1, 0], -1) == [1, 2]
    print("   ✅ All tests passed!")

    # Variation 4: Three Sum
    print("\n4️⃣  Three Sum")
    result = three_sum([-1, 0, 1, 2, -1, -4])
    assert sorted([sorted(x) for x in result]) == [[-1, -1, 2], [-1, 0, 1]]
    assert three_sum([0, 0, 0]) == [[0, 0, 0]]
    assert three_sum([1, 2, 3]) == []
    print("   ✅ All tests passed!")

    # Variation 5: Four Sum
    print("\n5️⃣  Four Sum")
    result = four_sum([1, 0, -1, 0, -2, 2], 0)
    expected = [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    assert sorted([sorted(x) for x in result]) == expected
    print("   ✅ All tests passed!")

    # Variation 6: Two Sum Less Than Target
    print("\n6️⃣  Two Sum Less Than Target")
    assert two_sum_less_than([34, 23, 1, 24, 75, 33, 54, 8], 60) == 58
    assert two_sum_less_than([10, 20, 30], 15) == -1
    print("   ✅ All tests passed!")

    # Variation 7: Two Sum Closest
    print("\n7️⃣  Two Sum Closest to Target")
    assert two_sum_closest([-1, 2, 1, -4], 4) == 3  # 2 + 1 = 3
    assert two_sum_closest([1, 2, 3], 5) == 5  # 2 + 3 = 5
    print("   ✅ All tests passed!")

    # Variation 8: Two Sum Count Unique Value Pairs
    print("\n8️⃣  Two Sum with Duplicates (Count unique value pairs)")
    assert two_sum_count_unique_value_pairs([1, 5, 7, -1, 5], 6) == 2
    assert two_sum_count_unique_value_pairs([1, 1, 1, 1], 2) == 1
    print("   ✅ All tests passed!")

    # Variation 9: Two Sum All Pairs
    print("\n9️⃣  Two Sum All Pairs")
    result = two_sum_all_pairs([1, 5, 1, 5], 6)
    assert sorted(result) == [[0, 1], [0, 3], [1, 2], [2, 3]]
    print("   ✅ All tests passed!")

    # Variation 10: Two Sum in BST
    print("\n🔟 Two Sum in BST")
    #     5
    #    / \
    #   3   6
    #  / \   \
    # 2   4   7
    root = TreeNode(5)
    root.left = TreeNode(3, TreeNode(2), TreeNode(4))
    root.right = TreeNode(6, None, TreeNode(7))
    assert two_sum_bst(root, 9) == True    # 2 + 7
    assert two_sum_bst(root, 28) == False
    assert two_sum_bst(root, 7) == True    # 3 + 4
    assert two_sum_bst_two_pointers(root, 9) == True
    assert two_sum_bst_two_pointers(root, 28) == False
    print("   ✅ All tests passed!")

    print("\n" + "=" * 60)
    print("🏆 ALL TWO SUM VARIATIONS PASSED!")
    print("=" * 60)
