/*
 * 🔥 Sliding Window Variations — ANCHOR PROBLEM #2  (C++ Edition)
 * ================================================================
 *
 * The Longest Substring Without Repeating Characters family.
 * When you see "longest/shortest substring/subarray with constraint"
 * → SLIDING WINDOW + unordered_map/set. No exceptions.
 *
 * C++ Key Notes:
 *   - unordered_map<char,int> ≈ Python Counter / dict
 *   - unordered_set<char>     ≈ Python set
 *   - Use erase/find instead of Python 'del' / 'in'
 *
 * Compile: g++ -O2 -std=c++17 -o sliding_window sliding_window_variations.cpp
 * Run:     ./sliding_window
 */

#include <bits/stdc++.h>
using namespace std;


// ============================================================================
// Problem 1: Longest Substring Without Repeating Characters
// THE ANCHOR PROBLEM — 2 implementations
// ============================================================================

/*
 * Implementation A: Set-based sliding window
 *
 * - Expand right pointer every iteration
 * - If s[right] already in window set, shrink from left until it's removed
 * - Track max window size
 *
 * Time:  O(n), Space: O(min(n, alphabet))
 *
 * Python equivalent:
 *   window = set()
 *   left = 0
 *   for right in range(len(s)):
 *       while s[right] in window:
 *           window.remove(s[left]); left += 1
 *       window.add(s[right])
 *       length = max(length, right - left + 1)
 */
int lengthOfLongestSubstringSet(const string& s) {
    unordered_set<char> window;
    int left = 0, length = 0;

    for (int right = 0; right < (int)s.size(); right++) {
        while (window.count(s[right])) {
            window.erase(s[left]);
            left++;
        }
        window.insert(s[right]);
        length = max(length, right - left + 1);
    }
    return length;
}

/*
 * Implementation B: Map-based (jump version) — often faster in practice
 *
 * Store last seen INDEX of each character. When we see a duplicate, jump
 * left to (last_seen_index + 1). Only if that index is >= current left.
 *
 * Time:  O(n) — single pass, no inner while loop
 * Space: O(min(n, alphabet))
 */
int lengthOfLongestSubstringDict(const string& s) {
    unordered_map<char, int> seen; // char → last seen index
    int left = 0, length = 0;

    for (int right = 0; right < (int)s.size(); right++) {
        char ch = s[right];
        if (seen.count(ch) && seen[ch] >= left) {
            left = seen[ch] + 1;
        }
        seen[ch] = right;
        length = max(length, right - left + 1);
    }
    return length;
}


// ============================================================================
// Problem 2: Longest Substring with At Most K Distinct Characters
// ============================================================================

/*
 * Find the length of the longest substring with at most K distinct characters.
 *
 * Key Insight: Sliding window with a freq map counting character frequencies.
 * When distinct count exceeds k, shrink from left.
 *
 * Time:  O(n), Space: O(k)
 */
int longestSubstringKDistinct(const string& s, int k) {
    if (k == 0) return 0;

    unordered_map<char, int> freq;
    int left = 0, maxLen = 0;

    for (int right = 0; right < (int)s.size(); right++) {
        freq[s[right]]++;

        // Shrink window until we have at most k distinct characters
        while ((int)freq.size() > k) {
            freq[s[left]]--;
            if (freq[s[left]] == 0)
                freq.erase(s[left]);
            left++;
        }

        maxLen = max(maxLen, right - left + 1);
    }
    return maxLen;
}


// ============================================================================
// Problem 3: Longest Repeating Character Replacement (LeetCode 424)
// ============================================================================

/*
 * Given a string s and integer k, find the length of the longest substring
 * where you can replace at most k characters to make all characters the same.
 *
 * Key Insight: For a window of size W, if the most frequent character appears
 * F times, we need (W - F) replacements. If W - F > k, shrink from left.
 *
 * The trick: We track HISTORICAL max_freq. It only ever increases, and we
 * only care about finding the longest valid window.
 *
 * Time:  O(n), Space: O(26) = O(1)
 */
int longestRepeatingCharReplacement(const string& s, int k) {
    unordered_map<char, int> freq;
    int left = 0, maxFreq = 0, maxLen = 0;

    for (int right = 0; right < (int)s.size(); right++) {
        freq[s[right]]++;
        maxFreq = max(maxFreq, freq[s[right]]);

        // Window size - max_freq = number of replacements needed
        int windowSize = right - left + 1;
        if (windowSize - maxFreq > k) {
            freq[s[left]]--;
            left++;
        }

        maxLen = max(maxLen, right - left + 1);
    }
    return maxLen;
}


// ============================================================================
// Problem 4: Minimum Window Substring (LeetCode 76)
// ============================================================================

/*
 * Find the minimum window in s that contains all characters of t
 * (including duplicates). Return "" if no such window exists.
 *
 * Key Insight: Two counters — 'need' for what t requires, 'have' for how
 * many requirements are currently satisfied.
 * Expand right to satisfy requirements, shrink left to minimize window.
 *
 * Time:  O(|s| + |t|), Space: O(|s| + |t|)
 */
string minWindowSubstring(const string& s, const string& t) {
    if (s.empty() || t.empty() || s.size() < t.size()) return "";

    unordered_map<char, int> need;
    for (char c : t) need[c]++;

    int required = (int)need.size();
    int have = 0;
    unordered_map<char, int> windowFreq;

    int left = 0;
    int minLen = INT_MAX, minStart = 0;

    for (int right = 0; right < (int)s.size(); right++) {
        char ch = s[right];
        windowFreq[ch]++;

        // Check if this character's requirement is now satisfied
        if (need.count(ch) && windowFreq[ch] == need[ch])
            have++;

        // Try to shrink from left while window is still valid
        while (have == required) {
            // Update minimum window
            if (right - left + 1 < minLen) {
                minLen = right - left + 1;
                minStart = left;
            }

            // Remove leftmost character
            char leftChar = s[left];
            windowFreq[leftChar]--;
            if (need.count(leftChar) && windowFreq[leftChar] < need[leftChar])
                have--;
            left++;
        }
    }

    return minLen == INT_MAX ? "" : s.substr(minStart, minLen);
}


// ============================================================================
// Problem 5: Find All Anagrams in a String (LeetCode 438) — Fixed window
// ============================================================================

/*
 * Find all start indices of p's anagrams in s.
 *
 * Key Insight: FIXED-size sliding window of size len(p).
 * Maintain a freq map for the window and compare with freq map of p.
 *
 * Time:  O(n), Space: O(1) — at most 26 chars
 */
vector<int> findAllAnagrams(const string& s, const string& p) {
    if (p.size() > s.size()) return {};

    unordered_map<char, int> need, window;
    for (char c : p) need[c]++;

    vector<int> result;
    int k = (int)p.size();

    for (int right = 0; right < (int)s.size(); right++) {
        // Add new character to window
        window[s[right]]++;

        // Remove character no longer in window (once window is full)
        if (right >= k) {
            char leftChar = s[right - k];
            window[leftChar]--;
            if (window[leftChar] == 0)
                window.erase(leftChar);
        }

        // Check if current window matches pattern
        if (window == need)
            result.push_back(right - k + 1);
    }
    return result;
}


// ============================================================================
// Problem 6: Permutation in String (LeetCode 567)
// ============================================================================

/*
 * Check if any permutation of s1 is a substring of s2.
 *
 * Key Insight: Same as "find anagrams" but just return a bool.
 * Fixed-size sliding window of size len(s1).
 *
 * Time:  O(n), Space: O(1)
 */
bool permutationInString(const string& s1, const string& s2) {
    if (s1.size() > s2.size()) return false;

    unordered_map<char, int> need, window;
    for (char c : s1) need[c]++;
    for (int i = 0; i < (int)s1.size(); i++) window[s2[i]]++;

    if (window == need) return true;

    for (int right = (int)s1.size(); right < (int)s2.size(); right++) {
        window[s2[right]]++;
        char oldChar = s2[right - s1.size()];
        window[oldChar]--;
        if (window[oldChar] == 0) window.erase(oldChar);

        if (window == need) return true;
    }
    return false;
}


// ============================================================================
// Problem 7: Maximum Sum Subarray of Size K — Fixed window, sum variant
// ============================================================================

/*
 * Find the maximum sum of any contiguous subarray of size k.
 *
 * Key Insight: FIXED-size sliding window. Running sum = add new, subtract old.
 *
 * Time:  O(n), Space: O(1)
 */
int maxSumSubarrayK(const vector<int>& arr, int k) {
    if ((int)arr.size() < k) return 0;

    int windowSum = 0;
    for (int i = 0; i < k; i++) windowSum += arr[i];
    int maxSum = windowSum;

    for (int right = k; right < (int)arr.size(); right++) {
        windowSum += arr[right] - arr[right - k];
        maxSum = max(maxSum, windowSum);
    }
    return maxSum;
}


// ============================================================================
// Problem 8: Smallest Subarray with Sum ≥ Target — Variable window, sum
// ============================================================================

/*
 * Find the length of the smallest contiguous subarray whose sum is >= target.
 * Return 0 if no such subarray exists.
 *
 * Key Insight: VARIABLE-size sliding window.
 * - Expand right to increase sum
 * - When sum >= target, try to shrink from left (we want minimum!)
 * - Track minimum window size when condition is satisfied
 *
 * Time:  O(n), Space: O(1)
 */
int smallestSubarrayWithSum(const vector<int>& arr, int target) {
    int n = (int)arr.size();
    int left = 0;
    long long currentSum = 0;
    int minLen = INT_MAX;

    for (int right = 0; right < n; right++) {
        currentSum += arr[right];

        // Shrink window from left while sum is still >= target
        while (currentSum >= target) {
            minLen = min(minLen, right - left + 1);
            currentSum -= arr[left];
            left++;
        }
    }
    return minLen == INT_MAX ? 0 : minLen;
}


// ============================================================================
// Problem 9: Fruit Into Baskets (LeetCode 904)
// ============================================================================

/*
 * Two baskets, each holds ONE type of fruit. Find max contiguous trees you can pick.
 * Translation: Longest subarray with at most 2 distinct values.
 *
 * This is exactly longestSubstringKDistinct with k=2!
 * Contest problems LOVE to disguise sliding window problems like this.
 *
 * Time:  O(n), Space: O(1) — map has at most 3 entries before shrinking
 */
int fruitIntoBaskets(const vector<int>& fruits) {
    unordered_map<int, int> basket;
    int left = 0, maxFruits = 0;

    for (int right = 0; right < (int)fruits.size(); right++) {
        basket[fruits[right]]++;

        // Shrink until we have at most 2 types
        while ((int)basket.size() > 2) {
            basket[fruits[left]]--;
            if (basket[fruits[left]] == 0)
                basket.erase(fruits[left]);
            left++;
        }

        maxFruits = max(maxFruits, right - left + 1);
    }
    return maxFruits;
}


// ============================================================================
// Problem 10: Longest Substring with At Most K Distinct (Generalized template)
// ============================================================================

/*
 * TEMPLATE — Adapt this for any variable sliding window problem.
 *
 * Pattern:
 *   left = 0;
 *   state = initial_state;
 *   best = initial_best;
 *
 *   for (int right = 0; right < n; right++) {
 *       // 1. Expand: add arr[right] to state
 *       // 2. Shrink: while state violates condition, remove arr[left], left++
 *       // 3. Update answer: window [left, right] is valid
 *   }
 *
 * Demonstration: Longest subarray with exactly k zeros.
 *
 * Time:  O(n), Space: O(1)
 */
int longestSubarrayWithAtMostKZeros(const vector<int>& nums, int k) {
    int left = 0, zeros = 0, maxLen = 0;

    for (int right = 0; right < (int)nums.size(); right++) {
        if (nums[right] == 0) zeros++;

        while (zeros > k) {
            if (nums[left] == 0) zeros--;
            left++;
        }

        maxLen = max(maxLen, right - left + 1);
    }
    return maxLen;
}


// ============================================================================
// Test Suite
// ============================================================================

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cout << string(65, '=') << "\n";
    cout << "🔥 Sliding Window Variations — Test Suite (C++)\n";
    cout << string(65, '=') << "\n";

    // Problem 1
    cout << "\n1️⃣  Longest Substring Without Repeating Characters\n";
    assert(lengthOfLongestSubstringSet("abcabcbb") == 3);
    assert(lengthOfLongestSubstringSet("bbbbb")    == 1);
    assert(lengthOfLongestSubstringSet("pwwkew")   == 3);
    assert(lengthOfLongestSubstringSet("")         == 0);
    assert(lengthOfLongestSubstringSet("dvdf")     == 3);
    cout << "   Set version: ✅ Passed!\n";

    assert(lengthOfLongestSubstringDict("abcabcbb") == 3);
    assert(lengthOfLongestSubstringDict("bbbbb")    == 1);
    assert(lengthOfLongestSubstringDict("pwwkew")   == 3);
    assert(lengthOfLongestSubstringDict("dvdf")     == 3);
    cout << "   Dict version: ✅ Passed!\n";

    // Problem 2
    cout << "\n2️⃣  Longest Substring with At Most K Distinct\n";
    assert(longestSubstringKDistinct("eceba", 2)        == 3);
    assert(longestSubstringKDistinct("aa", 1)           == 2);
    assert(longestSubstringKDistinct("abcadcacacaca", 3) == 11);
    assert(longestSubstringKDistinct("a", 0)            == 0);
    cout << "   ✅ Passed!\n";

    // Problem 3
    cout << "\n3️⃣  Longest Repeating Character Replacement\n";
    assert(longestRepeatingCharReplacement("ABAB",    2) == 4);
    assert(longestRepeatingCharReplacement("AABABBA", 1) == 4);
    cout << "   ✅ Passed!\n";

    // Problem 4
    cout << "\n4️⃣  Minimum Window Substring\n";
    assert(minWindowSubstring("ADOBECODEBANC", "ABC") == "BANC");
    assert(minWindowSubstring("a", "a")               == "a");
    assert(minWindowSubstring("a", "aa")              == "");
    cout << "   ✅ Passed!\n";

    // Problem 5
    cout << "\n5️⃣  Find All Anagrams\n";
    assert(findAllAnagrams("cbaebabacd", "abc") == (vector<int>{0, 6}));
    assert(findAllAnagrams("abab", "ab")        == (vector<int>{0, 1, 2}));
    cout << "   ✅ Passed!\n";

    // Problem 6
    cout << "\n6️⃣  Permutation in String\n";
    assert(permutationInString("ab", "eidbaooo") == true);
    assert(permutationInString("ab", "eidboaoo") == false);
    cout << "   ✅ Passed!\n";

    // Problem 7
    cout << "\n7️⃣  Maximum Sum Subarray of Size K\n";
    assert(maxSumSubarrayK({2, 1, 5, 1, 3, 2}, 3) == 9);
    assert(maxSumSubarrayK({2, 3, 4, 1, 5}, 2)     == 7);
    cout << "   ✅ Passed!\n";

    // Problem 8
    cout << "\n8️⃣  Smallest Subarray with Sum >= Target\n";
    assert(smallestSubarrayWithSum({2, 3, 1, 2, 4, 3}, 7) == 2);
    assert(smallestSubarrayWithSum({1, 4, 4}, 4)          == 1);
    assert(smallestSubarrayWithSum({1, 1, 1, 1, 1, 1}, 11) == 0);
    cout << "   ✅ Passed!\n";

    // Problem 9
    cout << "\n9️⃣  Fruit Into Baskets\n";
    assert(fruitIntoBaskets({1, 2, 1})                     == 3);
    assert(fruitIntoBaskets({0, 1, 2, 2})                  == 3);
    assert(fruitIntoBaskets({1, 2, 3, 2, 2})               == 4);
    assert(fruitIntoBaskets({3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4}) == 5);
    cout << "   ✅ Passed!\n";

    // Problem 10
    cout << "\n🔟 Longest Subarray with At Most K Zeros (Template demo)\n";
    assert(longestSubarrayWithAtMostKZeros({1, 1, 0, 0, 1, 1, 1, 0, 1}, 1) == 6);
    assert(longestSubarrayWithAtMostKZeros({0, 0, 0}, 2)                    == 2);
    cout << "   ✅ Passed!\n";

    cout << "\n" << string(65, '=') << "\n";
    cout << "🏆 ALL SLIDING WINDOW VARIATIONS PASSED! (C++)\n";
    cout << string(65, '=') << "\n";

    return 0;
}
