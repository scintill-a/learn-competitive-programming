"""
🔥 Sliding Window Variations — ANCHOR PROBLEM #2
==================================================

The Longest Substring Without Repeating Characters family.
This EXACT problem appeared as HARD in a past contest.

When you see "longest/shortest substring/subarray with constraint"
→ SLIDING WINDOW + SET/DICT. No exceptions.

This file contains 10 variations of sliding window problems, each with:
- Docstring explaining the problem
- Step-by-step trace comment
- Brute force solution (for understanding)
- Optimal solution (for contests)
- O() complexity annotation

Master these and sliding window problems become automatic.
"""

from collections import Counter, defaultdict


# ============================================================================
# Problem 1: Longest Substring Without Repeating Characters
# THE ANCHOR PROBLEM — 3 implementations
# ============================================================================

def length_of_longest_substring_set(s: str) -> int:
    """
    Given a string s, find the length of the longest substring without
    repeating characters.

    THIS IS THE CONTEST PROBLEM. Memorize this solution.

    Implementation: Set-based sliding window.
    - Expand right pointer every iteration
    - If s[right] already in window set, shrink from left until it's removed
    - Track max window size

    Step-by-step trace for "abcabcbb":
        right=0, char='a': window={a}, left=0, len=1
        right=1, char='b': window={a,b}, left=0, len=2
        right=2, char='c': window={a,b,c}, left=0, len=3
        right=3, char='a': collision! remove 'a', left=1. window={b,c,a}, len=3
        right=4, char='b': collision! remove 'b', left=2. window={c,a,b}, len=3
        right=5, char='c': collision! remove 'c', left=3. window={a,b,c}, len=3
        right=6, char='b': collision! remove 'a',left=4. still collision! remove 'b',left=5. window={c,b}, len=2
        right=7, char='b': collision! remove 'c',left=6. still collision! remove 'b',left=7. window={b}, len=1
        Answer: 3 ("abc")

    Time:  O(n) — each character added/removed from set at most once
    Space: O(min(n, alphabet_size)) — at most 26 for lowercase English

    Examples:
        >>> length_of_longest_substring_set("abcabcbb")
        3
        >>> length_of_longest_substring_set("bbbbb")
        1
        >>> length_of_longest_substring_set("pwwkew")
        3
        >>> length_of_longest_substring_set("")
        0
    """
    window = set()
    left = 0
    length = 0
    for right in range(len(s)):
        while s[right] in window:
            window.remove(s[left])
            left += 1
        window.add(s[right])
        length = max(length, right - left + 1)
    return length


def length_of_longest_substring_dict(s: str) -> int:
    """
    Dict-based implementation — often faster in practice because the left
    pointer JUMPS directly past the duplicate instead of incrementally
    shrinking.

    Key Insight: Store last seen INDEX of each character. When we see a
    duplicate, jump left to (last_seen_index + 1). But only if that index
    is >= current left (i.e., the duplicate is actually in our window).

    Step-by-step trace for "abcabcbb":
        right=0, ch='a': seen={a:0}, left=0, len=1
        right=1, ch='b': seen={a:0,b:1}, left=0, len=2
        right=2, ch='c': seen={a:0,b:1,c:2}, left=0, len=3
        right=3, ch='a': 'a' seen at 0, 0>=left(0) → left=1. seen={a:3,b:1,c:2}, len=3
        right=4, ch='b': 'b' seen at 1, 1>=left(1) → left=2. seen={a:3,b:4,c:2}, len=3
        right=5, ch='c': 'c' seen at 2, 2>=left(2) → left=3. seen={a:3,b:4,c:5}, len=3
        right=6, ch='b': 'b' seen at 4, 4>=left(3) → left=5. seen={a:3,b:6,c:5}, len=2
        right=7, ch='b': 'b' seen at 6, 6>=left(5) → left=7. seen={a:3,b:7,c:5}, len=1
        Answer: 3

    Time:  O(n) — single pass, no inner while loop needed
    Space: O(min(n, alphabet_size))

    Examples:
        >>> length_of_longest_substring_dict("abcabcbb")
        3
        >>> length_of_longest_substring_dict("bbbbb")
        1
        >>> length_of_longest_substring_dict("pwwkew")
        3
    """
    seen = {}
    left = 0
    length = 0
    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        seen[ch] = right
        length = max(length, right - left + 1)
    return length


def length_of_longest_substring_brute(s: str) -> int:
    """
    BRUTE FORCE — O(n³). DO NOT use in contests. Shown for understanding only.

    Check every possible substring, verify if all characters are unique.

    Time:  O(n³) — O(n²) substrings × O(n) uniqueness check
    Space: O(n) — set for uniqueness check

    This WILL get TLE (Time Limit Exceeded) for large inputs.
    """
    n = len(s)
    max_len = 0
    for i in range(n):
        for j in range(i, n):
            substring = s[i:j + 1]
            if len(set(substring)) == len(substring):  # All unique
                max_len = max(max_len, j - i + 1)
    return max_len


# ============================================================================
# Problem 2: Longest Substring with At Most K Distinct Characters
# ============================================================================

def longest_substring_k_distinct(s: str, k: int) -> int:
    """
    Find the length of the longest substring with at most K distinct characters.

    Example:
        >>> longest_substring_k_distinct("eceba", 2)
        3   # "ece" has at most 2 distinct chars
        >>> longest_substring_k_distinct("aa", 1)
        2
        >>> longest_substring_k_distinct("abcadcacacaca", 3)
        11  # "cadcacacaca"

    Key Insight: Sliding window with a dict counting character frequencies.
    When distinct count exceeds k, shrink from left.

    Step-by-step trace for "eceba", k=2:
        right=0, ch='e': freq={e:1}, distinct=1, len=1
        right=1, ch='c': freq={e:1,c:1}, distinct=2, len=2
        right=2, ch='e': freq={e:2,c:1}, distinct=2, len=3  ← max so far
        right=3, ch='b': freq={e:2,c:1,b:1}, distinct=3 > k!
            shrink: remove s[0]='e', freq={e:1,c:1,b:1}, still 3
            shrink: remove s[1]='c', freq={e:1,b:1}, distinct=2, left=2
            len = 3-2+1 = 2
        right=4, ch='a': freq={e:1,b:1,a:1}, distinct=3 > k!
            shrink: remove s[2]='e', freq={b:1,a:1}, distinct=2, left=3
            len = 4-3+1 = 2
        Answer: 3

    Time:  O(n)
    Space: O(k) — dict has at most k+1 entries
    """
    if k == 0:
        return 0

    freq = defaultdict(int)
    left = 0
    max_len = 0

    for right in range(len(s)):
        freq[s[right]] += 1

        # Shrink window until we have at most k distinct characters
        while len(freq) > k:
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                del freq[s[left]]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


# ============================================================================
# Problem 3: Longest Substring with All Unique Characters (Counter version)
# ============================================================================

def longest_substring_all_unique(s: str) -> int:
    """
    Same as Problem 1, but using collections.Counter for demonstration.
    Shows how Counter can be used for sliding window problems.

    Example:
        >>> longest_substring_all_unique("abcabcbb")
        3
        >>> longest_substring_all_unique("pwwkew")
        3

    Key Insight: The window is valid when all counts in Counter are <= 1.
    Equivalently, when len(counter) == window_size (each char appears once).

    Time:  O(n)
    Space: O(min(n, alphabet_size))
    """
    freq = Counter()
    left = 0
    max_len = 0

    for right in range(len(s)):
        freq[s[right]] += 1

        # If any char has count > 1, shrink from left
        while freq[s[right]] > 1:
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                del freq[s[left]]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


# ============================================================================
# Problem 4: Longest Repeating Character Replacement (LeetCode 424)
# ============================================================================

def longest_repeating_char_replacement(s: str, k: int) -> int:
    """
    Given a string s and integer k, find the length of the longest substring
    where you can replace at most k characters to make all characters the same.

    Example:
        >>> longest_repeating_char_replacement("ABAB", 2)
        4   # Replace both 'A's with 'B' or both 'B's with 'A'
        >>> longest_repeating_char_replacement("AABABBA", 1)
        4   # Replace the 'B' at index 3 → "AAAA" (length 4)

    Key Insight: For a window of size W, if the most frequent character appears
    F times, then we need (W - F) replacements. If W - F > k, shrink.

    The trick: We don't need to track the ACTUAL max frequency — we track the
    HISTORICAL max. It only ever increases, and we only care about finding
    the longest valid window, not all valid windows.

    Step-by-step trace for "AABABBA", k=1:
        right=0, 'A': freq={A:1}, max_freq=1, window=1, need=0, len=1
        right=1, 'A': freq={A:2}, max_freq=2, window=2, need=0, len=2
        right=2, 'B': freq={A:2,B:1}, max_freq=2, window=3, need=1, len=3
        right=3, 'A': freq={A:3,B:1}, max_freq=3, window=4, need=1, len=4
        right=4, 'B': freq={A:3,B:2}, max_freq=3, window=5, need=2>k!
            shrink: freq[s[0]]='A' → freq={A:2,B:2}, left=1, window=4, need=2>k!
            shrink: freq[s[1]]='A' → freq={A:1,B:2}, left=2, window=3, need=1, len=4
        right=5, 'B': freq={A:1,B:3}, max_freq=3, window=4, need=1, len=4
        right=6, 'A': freq={A:2,B:3}, max_freq=3, window=5, need=2>k!
            shrink: freq[s[2]]='B' → freq={A:2,B:2}, left=3, window=4, need=2>k!
            shrink: freq[s[3]]='A' → freq={A:1,B:2}, left=4, window=3, need=1, len=4
        Answer: 4

    Time:  O(n)
    Space: O(26) = O(1) — at most 26 different characters
    """
    freq = defaultdict(int)
    left = 0
    max_freq = 0  # Max frequency of any single char in current window
    max_len = 0

    for right in range(len(s)):
        freq[s[right]] += 1
        max_freq = max(max_freq, freq[s[right]])

        # Window size - max_freq = number of replacements needed
        window_size = right - left + 1
        if window_size - max_freq > k:
            freq[s[left]] -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


# ============================================================================
# Problem 5: Minimum Window Substring (LeetCode 76)
# ============================================================================

def min_window_substring(s: str, t: str) -> str:
    """
    Find the minimum window in s that contains all characters of t
    (including duplicates). If no such window exists, return "".

    Example:
        >>> min_window_substring("ADOBECODEBANC", "ABC")
        "BANC"
        >>> min_window_substring("a", "a")
        "a"
        >>> min_window_substring("a", "aa")
        ""

    Key Insight: Use a sliding window with two counters.
    - need: Counter of characters we need from t
    - have: how many character requirements we've satisfied
    - Expand right to satisfy requirements, shrink left to minimize window

    Step-by-step trace for s="ADOBECODEBANC", t="ABC":
        need = {A:1, B:1, C:1}, required=3, have=0
        Expand until have == required, then shrink from left.
        First valid window: "ADOBEC" (indices 0-5)
        Keep shrinking and expanding...
        Final best: "BANC" (indices 9-12)

    Time:  O(|s| + |t|)
    Space: O(|s| + |t|) worst case for the counters
    """
    if not s or not t or len(s) < len(t):
        return ""

    need = Counter(t)
    required = len(need)  # Number of unique chars in t that we need
    have = 0  # How many unique chars we currently satisfy

    window_freq = defaultdict(int)
    left = 0
    min_len = float('inf')
    min_start = 0

    for right in range(len(s)):
        char = s[right]
        window_freq[char] += 1

        # Check if this character's requirement is now satisfied
        if char in need and window_freq[char] == need[char]:
            have += 1

        # Try to shrink from the left while window is still valid
        while have == required:
            # Update minimum window
            window_size = right - left + 1
            if window_size < min_len:
                min_len = window_size
                min_start = left

            # Remove leftmost character
            left_char = s[left]
            window_freq[left_char] -= 1
            if left_char in need and window_freq[left_char] < need[left_char]:
                have -= 1
            left += 1

    return s[min_start:min_start + min_len] if min_len != float('inf') else ""


# ============================================================================
# Problem 6: Find All Anagrams in a String (LeetCode 438) — Fixed window
# ============================================================================

def find_all_anagrams(s: str, p: str) -> list[int]:
    """
    Find all start indices of p's anagrams in s.

    Example:
        >>> find_all_anagrams("cbaebabacd", "abc")
        [0, 6]
        >>> find_all_anagrams("abab", "ab")
        [0, 1, 2]

    Key Insight: FIXED-size sliding window of size len(p).
    Maintain a Counter for the window and compare with Counter(p).

    Optimization: Instead of comparing full counters each time, track how
    many characters match their required frequency.

    Step-by-step trace for s="cbaebabacd", p="abc":
        need = {a:1, b:1, c:1}, window_size=3
        Window "cba" (idx 0-2): matches! → result=[0]
        Slide: remove 'c', add 'e'. Window "bae": no match
        Slide: remove 'b', add 'b'. Window "aeb": no match
        Slide: remove 'a', add 'a'. Window "eba": no match
        Slide: remove 'e', add 'b'. Window "bab": no match
        Slide: remove 'b', add 'a'. Window "aba": no match
        Slide: remove 'b', add 'c'. Window "bac": matches! → result=[0, 6]
        Slide: remove 'a', add 'd'. Window "acd": no match
        Answer: [0, 6]

    Time:  O(n) where n = len(s)
    Space: O(1) — counters have at most 26 entries
    """
    if len(p) > len(s):
        return []

    need = Counter(p)
    window = Counter()
    result = []
    k = len(p)

    for right in range(len(s)):
        # Add new character to window
        window[s[right]] += 1

        # Remove character that's no longer in window (once window is full)
        if right >= k:
            left_char = s[right - k]
            window[left_char] -= 1
            if window[left_char] == 0:
                del window[left_char]

        # Check if current window matches pattern
        if window == need:
            result.append(right - k + 1)

    return result


# ============================================================================
# Problem 7: Permutation in String (LeetCode 567)
# ============================================================================

def permutation_in_string(s1: str, s2: str) -> bool:
    """
    Check if any permutation of s1 is a substring of s2.

    Example:
        >>> permutation_in_string("ab", "eidbaooo")
        True   # "ba" is a permutation of "ab" and is in s2
        >>> permutation_in_string("ab", "eidboaoo")
        False

    Key Insight: Same as "find anagrams" but we just need to know if ANY exist.
    Fixed-size sliding window of size len(s1), compare counters.

    Time:  O(n) where n = len(s2)
    Space: O(1) — 26 chars max
    """
    if len(s1) > len(s2):
        return False

    need = Counter(s1)
    window = Counter(s2[:len(s1)])

    if window == need:
        return True

    for right in range(len(s1), len(s2)):
        # Add new character
        window[s2[right]] += 1
        # Remove old character (left end of previous window)
        old_char = s2[right - len(s1)]
        window[old_char] -= 1
        if window[old_char] == 0:
            del window[old_char]

        if window == need:
            return True

    return False


# ============================================================================
# Problem 8: Maximum Sum Subarray of Size K — Fixed window, sum variant
# ============================================================================

def max_sum_subarray_k(arr: list[int], k: int) -> int:
    """
    Find the maximum sum of any contiguous subarray of size k.

    Example:
        >>> max_sum_subarray_k([2, 1, 5, 1, 3, 2], 3)
        9   # [5, 1, 3]
        >>> max_sum_subarray_k([2, 3, 4, 1, 5], 2)
        7   # [3, 4]

    Key Insight: FIXED-size sliding window. Maintain a running sum.
    When window is full, subtract the element leaving, add the element entering.

    Step-by-step trace for [2, 1, 5, 1, 3, 2], k=3:
        Initial window [2, 1, 5]: sum=8, max=8
        Slide: remove 2, add 1. [1, 5, 1]: sum=7, max=8
        Slide: remove 1, add 3. [5, 1, 3]: sum=9, max=9
        Slide: remove 5, add 2. [1, 3, 2]: sum=6, max=9
        Answer: 9

    BRUTE FORCE (O(n*k)):
        Check all windows of size k, sum each one. Redundant computation.

    OPTIMAL (O(n)):
        Sliding window — add one, remove one, update max.

    Time:  O(n)
    Space: O(1)
    """
    if len(arr) < k:
        return 0

    # Calculate sum of first window
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Slide the window
    for right in range(k, len(arr)):
        window_sum += arr[right] - arr[right - k]
        max_sum = max(max_sum, window_sum)

    return max_sum


# ============================================================================
# Problem 9: Smallest Subarray with Sum ≥ Target — Variable window, sum
# ============================================================================

def smallest_subarray_with_sum(arr: list[int], target: int) -> int:
    """
    Find the length of the smallest contiguous subarray whose sum is ≥ target.
    Return 0 if no such subarray exists.

    Example:
        >>> smallest_subarray_with_sum([2, 3, 1, 2, 4, 3], 7)
        2   # [4, 3]
        >>> smallest_subarray_with_sum([1, 4, 4], 4)
        1   # [4]
        >>> smallest_subarray_with_sum([1, 1, 1, 1, 1, 1], 11)
        0   # No subarray sums to 11

    Key Insight: VARIABLE-size sliding window (like the longest substring problem,
    but now we want the SMALLEST window satisfying a sum condition).

    Pattern:
    - Expand right to increase sum
    - When sum >= target, try to shrink from left (we want minimum!)
    - Track minimum window size when condition is satisfied

    Step-by-step trace for [2, 3, 1, 2, 4, 3], target=7:
        right=0: sum=2 < 7
        right=1: sum=5 < 7
        right=2: sum=6 < 7
        right=3: sum=8 >= 7! min_len=4. Shrink: remove 2, sum=6 < 7, left=1
        right=4: sum=10 >= 7! min_len=4. Shrink: remove 3, sum=7 >= 7! min_len=3.
                 Shrink: remove 1, sum=6 < 7, left=3
        right=5: sum=9 >= 7! min_len=3. Shrink: remove 2, sum=7 >= 7! min_len=2.
                 Shrink: remove 4, sum=3 < 7, left=5
        Answer: 2 (subarray [4, 3])

    BRUTE FORCE (O(n²)):
        Check all subarrays, find shortest with sum >= target.

    OPTIMAL (O(n)):
        Variable sliding window.

    Time:  O(n) — each element added and removed at most once
    Space: O(1)
    """
    n = len(arr)
    left = 0
    current_sum = 0
    min_len = float('inf')

    for right in range(n):
        current_sum += arr[right]

        # Shrink window from left while sum is still >= target
        while current_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_sum -= arr[left]
            left += 1

    return min_len if min_len != float('inf') else 0


# ============================================================================
# Problem 10: Fruit Into Baskets (LeetCode 904)
# ============================================================================

def fruit_into_baskets(fruits: list[int]) -> int:
    """
    You have a row of fruit trees. Each tree produces one type of fruit (integer).
    You have TWO baskets. Each basket can hold only ONE type of fruit.
    You must pick CONTIGUOUS trees. What is the maximum number of fruits you can pick?

    Translation: Find the longest contiguous subarray with at most 2 distinct values.

    This is EXACTLY "Longest Substring with At Most K Distinct Characters" where K=2!
    Contest problems LOVE to disguise sliding window problems like this.

    Example:
        >>> fruit_into_baskets([1, 2, 1])
        3   # All trees: types {1, 2}
        >>> fruit_into_baskets([0, 1, 2, 2])
        3   # Trees [1, 2, 2]: types {1, 2}
        >>> fruit_into_baskets([1, 2, 3, 2, 2])
        4   # Trees [2, 3, 2, 2]: types {2, 3}
        >>> fruit_into_baskets([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4])
        5   # Trees [1, 2, 1, 1, 2]: types {1, 2}

    Step-by-step trace for [1, 2, 3, 2, 2]:
        right=0, fruit=1: baskets={1:1}, distinct=1, len=1
        right=1, fruit=2: baskets={1:1, 2:1}, distinct=2, len=2
        right=2, fruit=3: baskets={1:1, 2:1, 3:1}, distinct=3 > 2!
            shrink: remove fruits[0]=1, baskets={2:1, 3:1}, left=1, len=2
        right=3, fruit=2: baskets={2:2, 3:1}, distinct=2, len=3
        right=4, fruit=2: baskets={2:3, 3:1}, distinct=2, len=4
        Answer: 4

    BRUTE FORCE (O(n²)):
        Check all subarrays, count distinct values in each.

    OPTIMAL (O(n)):
        Sliding window with at most 2 distinct — identical to k_distinct with k=2.

    Time:  O(n)
    Space: O(1) — dict has at most 3 entries before shrinking
    """
    basket = defaultdict(int)
    left = 0
    max_fruits = 0

    for right in range(len(fruits)):
        basket[fruits[right]] += 1

        # Shrink until we have at most 2 types
        while len(basket) > 2:
            basket[fruits[left]] -= 1
            if basket[fruits[left]] == 0:
                del basket[fruits[left]]
            left += 1

        max_fruits = max(max_fruits, right - left + 1)

    return max_fruits


# ============================================================================
# BONUS: The Variable Sliding Window Template (reusable for ALL problems above)
# ============================================================================

def variable_sliding_window_template(arr, condition_check, condition_update):
    """
    TEMPLATE — Adapt this for any variable sliding window problem.

    Pattern:
        left = 0
        state = initial_state
        best = initial_best

        for right in range(len(arr)):
            # 1. Expand: add arr[right] to state
            update_state(arr[right])

            # 2. Shrink: while state violates condition, remove from left
            while state_violates_condition():
                remove_from_state(arr[left])
                left += 1

            # 3. Update answer: window [left, right] is valid
            best = update_best(best, right - left + 1)

        return best
    """
    pass  # This is a template — see the pattern above


# ============================================================================
# Test Suite
# ============================================================================

if __name__ == "__main__":
    print("=" * 65)
    print("🔥 Sliding Window Variations — Test Suite")
    print("=" * 65)

    # Problem 1: Longest Substring Without Repeating Characters
    print("\n1️⃣  Longest Substring Without Repeating Characters")

    print("   Set-based version:")
    assert length_of_longest_substring_set("abcabcbb") == 3
    assert length_of_longest_substring_set("bbbbb") == 1
    assert length_of_longest_substring_set("pwwkew") == 3
    assert length_of_longest_substring_set("") == 0
    assert length_of_longest_substring_set(" ") == 1
    assert length_of_longest_substring_set("dvdf") == 3
    assert length_of_longest_substring_set("abcdef") == 6
    print("   ✅ Passed!")

    print("   Dict-based version:")
    assert length_of_longest_substring_dict("abcabcbb") == 3
    assert length_of_longest_substring_dict("bbbbb") == 1
    assert length_of_longest_substring_dict("pwwkew") == 3
    assert length_of_longest_substring_dict("") == 0
    assert length_of_longest_substring_dict("dvdf") == 3
    print("   ✅ Passed!")

    print("   Brute force version (correctness check):")
    assert length_of_longest_substring_brute("abcabcbb") == 3
    assert length_of_longest_substring_brute("bbbbb") == 1
    assert length_of_longest_substring_brute("pwwkew") == 3
    print("   ✅ Passed!")

    # Problem 2: Longest Substring with K Distinct
    print("\n2️⃣  Longest Substring with At Most K Distinct Characters")
    assert longest_substring_k_distinct("eceba", 2) == 3
    assert longest_substring_k_distinct("aa", 1) == 2
    assert longest_substring_k_distinct("abcadcacacaca", 3) == 11
    assert longest_substring_k_distinct("a", 0) == 0
    print("   ✅ Passed!")

    # Problem 3: Longest Substring All Unique (Counter)
    print("\n3️⃣  Longest Substring All Unique (Counter version)")
    assert longest_substring_all_unique("abcabcbb") == 3
    assert longest_substring_all_unique("bbbbb") == 1
    assert longest_substring_all_unique("pwwkew") == 3
    print("   ✅ Passed!")

    # Problem 4: Longest Repeating Character Replacement
    print("\n4️⃣  Longest Repeating Character Replacement")
    assert longest_repeating_char_replacement("ABAB", 2) == 4
    assert longest_repeating_char_replacement("AABABBA", 1) == 4
    print("   ✅ Passed!")

    # Problem 5: Minimum Window Substring
    print("\n5️⃣  Minimum Window Substring")
    assert min_window_substring("ADOBECODEBANC", "ABC") == "BANC"
    assert min_window_substring("a", "a") == "a"
    assert min_window_substring("a", "aa") == ""
    print("   ✅ Passed!")

    # Problem 6: Find All Anagrams
    print("\n6️⃣  Find All Anagrams in a String")
    assert find_all_anagrams("cbaebabacd", "abc") == [0, 6]
    assert find_all_anagrams("abab", "ab") == [0, 1, 2]
    print("   ✅ Passed!")

    # Problem 7: Permutation in String
    print("\n7️⃣  Permutation in String")
    assert permutation_in_string("ab", "eidbaooo") == True
    assert permutation_in_string("ab", "eidboaoo") == False
    print("   ✅ Passed!")

    # Problem 8: Max Sum Subarray of Size K
    print("\n8️⃣  Maximum Sum Subarray of Size K")
    assert max_sum_subarray_k([2, 1, 5, 1, 3, 2], 3) == 9
    assert max_sum_subarray_k([2, 3, 4, 1, 5], 2) == 7
    print("   ✅ Passed!")

    # Problem 9: Smallest Subarray with Sum >= Target
    print("\n9️⃣  Smallest Subarray with Sum ≥ Target")
    assert smallest_subarray_with_sum([2, 3, 1, 2, 4, 3], 7) == 2
    assert smallest_subarray_with_sum([1, 4, 4], 4) == 1
    assert smallest_subarray_with_sum([1, 1, 1, 1, 1, 1], 11) == 0
    print("   ✅ Passed!")

    # Problem 10: Fruit Into Baskets
    print("\n🔟 Fruit Into Baskets")
    assert fruit_into_baskets([1, 2, 1]) == 3
    assert fruit_into_baskets([0, 1, 2, 2]) == 3
    assert fruit_into_baskets([1, 2, 3, 2, 2]) == 4
    assert fruit_into_baskets([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]) == 5
    print("   ✅ Passed!")

    print("\n" + "=" * 65)
    print("🏆 ALL SLIDING WINDOW VARIATIONS PASSED!")
    print("=" * 65)
