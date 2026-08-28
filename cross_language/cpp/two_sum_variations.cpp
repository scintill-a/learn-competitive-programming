/*
 * 🔥 Two Sum Variations — ANCHOR PROBLEM #1  (C++ Edition)
 * =========================================================
 *
 * The Two Sum family of problems teaches the most fundamental competitive
 * programming insight: TRADE SPACE FOR TIME using a hash map.
 *
 * Rule: When you see "find pair/complement/target" → UNORDERED_MAP. Never nested loops.
 *
 * C++ Key Notes:
 *   - Use unordered_map<int,int> (O(1) avg) not map<int,int> (O(log n))
 *   - Vectors are sorted with std::sort(v.begin(), v.end())
 *   - Comparison: Python `dict` → C++ `unordered_map`
 *                 Python `set`  → C++ `unordered_set`
 *
 * Compile:  g++ -O2 -std=c++17 -o two_sum two_sum_variations.cpp
 * Run:      ./two_sum
 */

#include <bits/stdc++.h>
using namespace std;

// ============================================================================
// Variation 1: Original Two Sum (Hash Map Lookup)
// ============================================================================

/*
 * Given an array of integers and a target, return the INDICES
 * of the two numbers that add up to target.
 *
 * Key Insight: For each number, its complement (target - num) is what we need.
 * Store seen numbers in an unordered_map for O(1) lookup.
 *
 * Time:  O(n) — single pass through the array
 * Space: O(n) — hash map stores at most n elements
 *
 * Python equivalent:
 *   seen = {}
 *   for i, num in enumerate(nums):
 *       complement = target - num
 *       if complement in seen:
 *           return [seen[complement], i]
 *       seen[num] = i
 */
vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> seen; // num → index
    for (int i = 0; i < (int)nums.size(); i++) {
        int complement = target - nums[i];
        if (seen.count(complement)) {           // O(1) lookup
            return {seen[complement], i};
        }
        seen[nums[i]] = i;
    }
    return {}; // No solution
}


// ============================================================================
// Variation 2: Sorted Array — Two Pointers
// ============================================================================

/*
 * Given a SORTED array (1-indexed), find two numbers that add up to target.
 * Return their 1-indexed positions.
 *
 * Key Insight: With sorted arrays, use two pointers (left and right).
 *   - sum too small → move left right  (increase sum)
 *   - sum too big   → move right left  (decrease sum)
 *   - equal         → found it!
 *
 * Time:  O(n) — each pointer moves at most n times
 * Space: O(1) — no extra data structures
 */
vector<int> twoSumSorted(vector<int>& nums, int target) {
    int left = 0, right = (int)nums.size() - 1;
    while (left < right) {
        int currentSum = nums[left] + nums[right];
        if (currentSum == target)
            return {left + 1, right + 1};  // 1-indexed
        else if (currentSum < target)
            left++;
        else
            right--;
    }
    return {};
}


// ============================================================================
// Variation 3: Three Sum (Find all unique triplets summing to zero)
// ============================================================================

/*
 * Given an array nums, return all unique triplets [a, b, c] such that
 * a + b + c = 0. No duplicate triplets.
 *
 * Key Insight: Sort the array. Fix one element, then use Two Sum (two pointers)
 * on the remaining sorted subarray. Skip duplicates to avoid duplicate triplets.
 *
 * Time:  O(n²) — for each element, two-pointer scan is O(n)
 * Space: O(1) extra (excluding output), O(n) for sort
 */
vector<vector<int>> threeSum(vector<int> nums) {
    sort(nums.begin(), nums.end());
    vector<vector<int>> result;
    int n = (int)nums.size();

    for (int i = 0; i < n - 2; i++) {
        // Skip duplicate first elements
        if (i > 0 && nums[i] == nums[i - 1]) continue;
        // Early termination: smallest possible triplet > 0
        if (nums[i] > 0) break;

        int target = -nums[i];
        int left = i + 1, right = n - 1;

        while (left < right) {
            int currentSum = nums[left] + nums[right];
            if (currentSum == target) {
                result.push_back({nums[i], nums[left], nums[right]});
                // Skip duplicates
                while (left < right && nums[left] == nums[left + 1]) left++;
                while (left < right && nums[right] == nums[right - 1]) right--;
                left++;
                right--;
            } else if (currentSum < target) {
                left++;
            } else {
                right--;
            }
        }
    }
    return result;
}


// ============================================================================
// Variation 4: Four Sum
// ============================================================================

/*
 * Find all unique quadruplets [a, b, c, d] such that a + b + c + d = target.
 *
 * Key Insight: Extend Three Sum — fix two elements, two-pointer on the rest.
 * Sort, skip duplicates at each level.
 *
 * Time:  O(n³) — two nested loops + two-pointer
 * Space: O(1) extra (excluding output)
 */
vector<vector<int>> fourSum(vector<int> nums, int target) {
    sort(nums.begin(), nums.end());
    vector<vector<int>> result;
    int n = (int)nums.size();

    for (int i = 0; i < n - 3; i++) {
        if (i > 0 && nums[i] == nums[i - 1]) continue;
        for (int j = i + 1; j < n - 2; j++) {
            if (j > i + 1 && nums[j] == nums[j - 1]) continue;

            long long remaining = (long long)target - nums[i] - nums[j];
            int left = j + 1, right = n - 1;

            while (left < right) {
                long long current = (long long)nums[left] + nums[right];
                if (current == remaining) {
                    result.push_back({nums[i], nums[j], nums[left], nums[right]});
                    while (left < right && nums[left] == nums[left + 1]) left++;
                    while (left < right && nums[right] == nums[right - 1]) right--;
                    left++;
                    right--;
                } else if (current < remaining) {
                    left++;
                } else {
                    right--;
                }
            }
        }
    }
    return result;
}


// ============================================================================
// Variation 5: Two Sum Less Than Target
// ============================================================================

/*
 * Given an array nums and a target, return the maximum sum of a pair
 * such that sum < target. Return -1 if no such pair exists.
 *
 * Key Insight: Sort + two pointers. When sum < target, it's a candidate
 * (update best). Move left right to try a bigger sum. When sum >= target,
 * move right left to decrease.
 *
 * Time:  O(n log n) — dominated by sort
 * Space: O(1) extra
 */
int twoSumLessThan(vector<int> nums, int target) {
    sort(nums.begin(), nums.end());
    int left = 0, right = (int)nums.size() - 1;
    int best = -1;

    while (left < right) {
        int currentSum = nums[left] + nums[right];
        if (currentSum < target) {
            best = max(best, currentSum);
            left++;
        } else {
            right--;
        }
    }
    return best;
}


// ============================================================================
// Variation 6: Two Sum Closest to Target
// ============================================================================

/*
 * Find two numbers in nums whose sum is closest to target.
 * Return that closest sum.
 *
 * Key Insight: Sort + two pointers. Track the sum with minimum |sum - target|.
 *
 * Time:  O(n log n)
 * Space: O(1)
 */
int twoSumClosest(vector<int> nums, int target) {
    sort(nums.begin(), nums.end());
    int left = 0, right = (int)nums.size() - 1;
    int closest = INT_MAX;
    int closestSum = 0;

    while (left < right) {
        int currentSum = nums[left] + nums[right];
        int diff = abs(currentSum - target);

        if (diff < closest) {
            closest = diff;
            closestSum = currentSum;
        }

        if (currentSum < target)      left++;
        else if (currentSum > target) right--;
        else return target;  // Exact match!
    }
    return closestSum;
}


// ============================================================================
// Variation 7: Two Sum Count Unique Value Pairs
// ============================================================================

/*
 * Count the number of UNIQUE VALUE pairs that sum to target.
 * (1, 5) counts once even if there are multiple 1s and 5s.
 *
 * Key Insight: Sort + two pointers, skip duplicates to count unique VALUE pairs.
 *
 * Time:  O(n log n)
 * Space: O(1)
 */
int twoSumCountPairs(vector<int> nums, int target) {
    sort(nums.begin(), nums.end());
    int left = 0, right = (int)nums.size() - 1;
    int count = 0;

    while (left < right) {
        int currentSum = nums[left] + nums[right];
        if (currentSum == target) {
            if (nums[left] == nums[right]) {
                // All elements between left and right are the same
                int n = right - left + 1;
                count += n * (n - 1) / 2;
                break;
            } else {
                int leftCount = 1, rightCount = 1;
                while (left + leftCount < right && nums[left + leftCount] == nums[left])
                    leftCount++;
                while (right - rightCount > left && nums[right - rightCount] == nums[right])
                    rightCount++;
                count += leftCount * rightCount;
                left += leftCount;
                right -= rightCount;
            }
        } else if (currentSum < target) {
            left++;
        } else {
            right--;
        }
    }
    return count;
}


// ============================================================================
// Variation 8: Two Sum All Pairs (Return all index pairs)
// ============================================================================

/*
 * Return ALL pairs of indices (i, j) where i < j and nums[i] + nums[j] == target.
 *
 * Key Insight: Use a hash map storing a VECTOR of indices for each value.
 * For each number, look up complement indices and pair them.
 *
 * Time:  O(n + k) where k is the number of valid pairs
 * Space: O(n) for the hash map
 */
vector<pair<int,int>> twoSumAllPairs(vector<int>& nums, int target) {
    unordered_map<int, vector<int>> indexMap; // num → [list of indices]
    vector<pair<int,int>> result;

    for (int i = 0; i < (int)nums.size(); i++) {
        int complement = target - nums[i];
        if (indexMap.count(complement)) {
            for (int j : indexMap[complement]) {
                result.push_back({j, i});
            }
        }
        indexMap[nums[i]].push_back(i);
    }
    return result;
}


// ============================================================================
// Variation 9: Two Sum in a BST
// ============================================================================

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int v, TreeNode* l = nullptr, TreeNode* r = nullptr)
        : val(v), left(l), right(r) {}
};

/*
 * Given the root of a BST, return true if there exist two elements whose
 * sum equals target.
 *
 * Approach: Traverse the tree with DFS, use a set to check if complement exists.
 *
 * Time:  O(n)
 * Space: O(n) for hash set + recursion stack
 */
bool twoSumBST(TreeNode* root, int target) {
    unordered_set<int> seen;

    function<bool(TreeNode*)> dfs = [&](TreeNode* node) -> bool {
        if (!node) return false;
        int complement = target - node->val;
        if (seen.count(complement)) return true;
        seen.insert(node->val);
        return dfs(node->left) || dfs(node->right);
    };

    return dfs(root);
}

/*
 * Alternative: In-order traversal gives sorted array, then two pointers.
 *
 * Time:  O(n)
 * Space: O(n)
 */
bool twoSumBSTTwoPointers(TreeNode* root, int target) {
    vector<int> sortedVals;

    function<void(TreeNode*)> inorder = [&](TreeNode* node) {
        if (node) {
            inorder(node->left);
            sortedVals.push_back(node->val);
            inorder(node->right);
        }
    };
    inorder(root);

    int left = 0, right = (int)sortedVals.size() - 1;
    while (left < right) {
        int current = sortedVals[left] + sortedVals[right];
        if (current == target) return true;
        else if (current < target) left++;
        else right--;
    }
    return false;
}


// ============================================================================
// Test Suite
// ============================================================================

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cout << string(60, '=') << "\n";
    cout << "🔥 Two Sum Variations — Test Suite (C++)\n";
    cout << string(60, '=') << "\n";

    // --- Variation 1: Original Two Sum ---
    cout << "\n1️⃣  Original Two Sum (Hash Map)\n";
    {
        vector<int> a = {2, 7, 11, 15};
        assert(twoSum(a, 9) == (vector<int>{0, 1}));
        vector<int> b = {3, 2, 4};
        assert(twoSum(b, 6) == (vector<int>{1, 2}));
        vector<int> c = {3, 3};
        assert(twoSum(c, 6) == (vector<int>{0, 1}));
        cout << "   ✅ All tests passed!\n";
    }

    // --- Variation 2: Sorted Array ---
    cout << "\n2️⃣  Sorted Array (Two Pointers)\n";
    {
        vector<int> a = {2, 7, 11, 15};
        assert(twoSumSorted(a, 9) == (vector<int>{1, 2}));
        vector<int> b = {2, 3, 4};
        assert(twoSumSorted(b, 6) == (vector<int>{1, 3}));
        cout << "   ✅ All tests passed!\n";
    }

    // --- Variation 3: Three Sum ---
    cout << "\n3️⃣  Three Sum\n";
    {
        vector<int> a = {-1, 0, 1, 2, -1, -4};
        auto result = threeSum(a);
        // Sort each triplet and then sort the outer vector for comparison
        for (auto& t : result) sort(t.begin(), t.end());
        sort(result.begin(), result.end());
        vector<vector<int>> expected = {{-1, -1, 2}, {-1, 0, 1}};
        assert(result == expected);

        vector<int> b = {0, 0, 0};
        auto r2 = threeSum(b);
        assert(r2 == (vector<vector<int>>{{0, 0, 0}}));
        cout << "   ✅ All tests passed!\n";
    }

    // --- Variation 4: Four Sum ---
    cout << "\n4️⃣  Four Sum\n";
    {
        vector<int> a = {1, 0, -1, 0, -2, 2};
        auto result = fourSum(a, 0);
        for (auto& q : result) sort(q.begin(), q.end());
        sort(result.begin(), result.end());
        vector<vector<int>> expected = {{-2, -1, 1, 2}, {-2, 0, 0, 2}, {-1, 0, 0, 1}};
        assert(result == expected);
        cout << "   ✅ All tests passed!\n";
    }

    // --- Variation 5: Two Sum Less Than Target ---
    cout << "\n5️⃣  Two Sum Less Than Target\n";
    {
        assert(twoSumLessThan({34, 23, 1, 24, 75, 33, 54, 8}, 60) == 58);
        assert(twoSumLessThan({10, 20, 30}, 15) == -1);
        cout << "   ✅ All tests passed!\n";
    }

    // --- Variation 6: Two Sum Closest ---
    cout << "\n6️⃣  Two Sum Closest to Target\n";
    {
        assert(twoSumClosest({-1, 2, 1, -4}, 4) == 3);
        assert(twoSumClosest({1, 2, 3}, 5) == 5);
        cout << "   ✅ All tests passed!\n";
    }

    // --- Variation 7: Count Unique Value Pairs ---
    cout << "\n7️⃣  Two Sum Count Unique Value Pairs\n";
    {
        // Sort + two pointer approach for unique value pairs
        // (1,5) and (7,-1) from [1, 5, 7, -1, 5] → 2 unique pairs
        assert(twoSumCountPairs({1, 5, 7, -1, 5}, 6) == 2);
        assert(twoSumCountPairs({1, 1, 1, 1}, 2) == 6); // C(4,2) = 6 index pairs
        cout << "   ✅ All tests passed!\n";
    }

    // --- Variation 8: All Pairs ---
    cout << "\n8️⃣  Two Sum All Pairs\n";
    {
        vector<int> nums = {1, 5, 1, 5};
        auto result = twoSumAllPairs(nums, 6);
        sort(result.begin(), result.end());
        vector<pair<int,int>> expected = {{0,1},{0,3},{1,2},{2,3}};
        assert(result == expected);
        cout << "   ✅ All tests passed!\n";
    }

    // --- Variation 9: Two Sum in BST ---
    cout << "\n9️⃣  Two Sum in BST\n";
    {
        //     5
        //    / \
        //   3   6
        //  / \   \
        // 2   4   7
        TreeNode* root = new TreeNode(5,
            new TreeNode(3, new TreeNode(2), new TreeNode(4)),
            new TreeNode(6, nullptr, new TreeNode(7))
        );
        assert(twoSumBST(root, 9) == true);   // 2 + 7
        assert(twoSumBST(root, 28) == false);
        assert(twoSumBST(root, 7) == true);   // 3 + 4

        assert(twoSumBSTTwoPointers(root, 9) == true);
        assert(twoSumBSTTwoPointers(root, 28) == false);
        cout << "   ✅ All tests passed!\n";
        // (In a real contest, clean up memory; skipping for brevity)
    }

    cout << "\n" << string(60, '=') << "\n";
    cout << "🏆 ALL TWO SUM VARIATIONS PASSED! (C++)\n";
    cout << string(60, '=') << "\n";

    return 0;
}
