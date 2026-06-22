"""
⚡ Contest Templates — Ready-to-Copy Python Templates
=====================================================

Every template you need for competitive programming, ready to paste
into your contest solution file. Tested, optimized, Pythonic.

Usage: Copy the template, adapt the problem-specific logic, submit.
"""

import sys
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
from functools import lru_cache
from itertools import accumulate


# ============================================================================
# 🚀 FAST INPUT TEMPLATE — Always start your contest file with this
# ============================================================================

def fast_input_template():
    """
    Contest submission boilerplate. Paste this at the top of every solution.

    Usage:
        import sys
        input = sys.stdin.readline

        def solve():
            n = int(input())
            nums = list(map(int, input().split()))
            # ... your solution ...
            print(result)

        # For multiple test cases:
        t = int(input())
        for _ in range(t):
            solve()
    """
    pass


CONTEST_BOILERPLATE = """
import sys
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop
from functools import lru_cache
from itertools import accumulate
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    # YOUR SOLUTION HERE
    print(result)

t = int(input())
for _ in range(t):
    solve()
"""


# ============================================================================
# 🔥 SLIDING WINDOW — VARIABLE SIZE (THE MOST IMPORTANT TEMPLATE)
# ============================================================================
# Based on the Longest Substring Without Repeating Characters pattern.
# This is the #1 template from past contest experience.

def sliding_window_variable(arr, is_valid, add_to_window, remove_from_window):
    """
    Variable-size sliding window template.

    Usage pattern:
        left = 0
        # Initialize window state (set, dict, counter, sum, etc.)

        for right in range(len(arr)):
            # 1. Add arr[right] to window state
            # 2. While window is INVALID, shrink from left:
            #        remove arr[left] from state, left += 1
            # 3. Update answer: window [left..right] is the largest valid window
    """
    pass  # See concrete examples below


def length_of_longest_substring(s: str) -> int:
    """
    🔥 THE ANCHOR PROBLEM — Longest Substring Without Repeating Characters.
    Clean contest version. Memorize this.

    Time: O(n), Space: O(min(n, alphabet))
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


def sliding_window_variable_example(arr):
    """
    Generic variable sliding window — find longest subarray satisfying condition.

    Adapt the condition_violated check and state management for your problem.
    """
    left = 0
    state = defaultdict(int)  # or set(), or a running sum, etc.
    best = 0

    for right in range(len(arr)):
        # --- EXPAND: Add arr[right] to window state ---
        state[arr[right]] += 1

        # --- SHRINK: While window violates the condition, remove from left ---
        while condition_violated(state):  # <-- CUSTOMIZE THIS
            state[arr[left]] -= 1
            if state[arr[left]] == 0:
                del state[arr[left]]
            left += 1

        # --- UPDATE: Window [left..right] is valid ---
        best = max(best, right - left + 1)

    return best


def condition_violated(state):
    """Placeholder — replace with your problem's constraint check."""
    return False


# ============================================================================
# 🔥 HASH MAP COMPLEMENT LOOKUP (TWO SUM PATTERN)
# ============================================================================

def two_sum_template(nums: list[int], target: int) -> list[int]:
    """
    🔥 THE ANCHOR PATTERN — Hash Map + Complement Lookup.
    When you see "find pair with target sum" → THIS.

    Time: O(n), Space: O(n)
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


# ============================================================================
# 📌 FIXED SLIDING WINDOW TEMPLATE
# ============================================================================

def sliding_window_fixed(arr, k):
    """
    Fixed-size sliding window of size k.
    Returns the maximum sum of any window of size k.

    For other problems: replace sum with your aggregate function
    (counter comparison, set check, etc.)

    Time: O(n), Space: O(1)
    """
    if len(arr) < k:
        return 0

    window_sum = sum(arr[:k])
    best = window_sum

    for right in range(k, len(arr)):
        window_sum += arr[right] - arr[right - k]
        best = max(best, window_sum)

    return best


# ============================================================================
# 📌 TWO POINTERS TEMPLATE
# ============================================================================

def two_pointers_sorted(arr: list[int], target: int) -> list[int]:
    """
    Two pointers on a SORTED array to find a pair with given sum.

    Time: O(n), Space: O(1)
    """
    left, right = 0, len(arr) - 1
    while left < right:
        current = arr[left] + arr[right]
        if current == target:
            return [left, right]
        elif current < target:
            left += 1
        else:
            right -= 1
    return []


def two_pointers_opposite(arr: list[int]) -> None:
    """
    Template for opposite-direction two pointers.
    Used for: palindrome check, container with most water, trapping rain water.
    """
    left, right = 0, len(arr) - 1
    while left < right:
        # Process arr[left] and arr[right]
        # Move left right or right left based on condition
        if some_condition(arr, left, right):  # noqa: F821
            left += 1
        else:
            right -= 1


# ============================================================================
# 📌 BINARY SEARCH TEMPLATE
# ============================================================================

def binary_search(arr: list[int], target: int) -> int:
    """
    Standard binary search. Returns index of target, or -1 if not found.

    Time: O(log n), Space: O(1)
    """
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def binary_search_leftmost(arr: list[int], target: int) -> int:
    """
    Find the leftmost (first) position where target could be inserted
    to keep array sorted. Equivalent to bisect_left.

    Time: O(log n), Space: O(1)
    """
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo


def binary_search_on_answer(lo: int, hi: int, is_feasible) -> int:
    """
    Binary search on the answer space.
    Find the smallest value x in [lo, hi] such that is_feasible(x) is True.

    The predicate must be MONOTONIC:
        is_feasible(x) = False, False, ..., False, True, True, ..., True

    Usage example (Koko Eating Bananas):
        def can_finish(speed):
            hours = sum(math.ceil(pile / speed) for pile in piles)
            return hours <= h
        answer = binary_search_on_answer(1, max(piles), can_finish)

    Time: O(log(hi-lo) * cost_of_is_feasible)
    """
    while lo < hi:
        mid = (lo + hi) // 2
        if is_feasible(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo


# ============================================================================
# 📌 BFS TEMPLATE (Breadth-First Search)
# ============================================================================

def bfs(graph: dict, start: int) -> dict:
    """
    BFS on an adjacency list graph.
    Returns distances from start to all reachable nodes.

    Time: O(V + E), Space: O(V)
    """
    dist = {start: 0}
    queue = deque([start])

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in dist:
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)

    return dist


def bfs_grid(grid: list[list[int]], start_r: int, start_c: int) -> int:
    """
    BFS on a 2D grid. Returns shortest distance from start to target.
    Adapts for "Number of Islands", "Shortest Path in Grid", etc.

    grid[r][c] = 0 means passable, 1 means wall (customize as needed).

    Time: O(rows * cols), Space: O(rows * cols)
    """
    rows, cols = len(grid), len(grid[0])
    visited = {(start_r, start_c)}
    queue = deque([(start_r, start_c, 0)])  # (row, col, distance)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        r, c, dist = queue.popleft()

        # Check if this is the target (customize condition)
        # if (r, c) == (target_r, target_c):
        #     return dist

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                if grid[nr][nc] == 0:  # passable
                    visited.add((nr, nc))
                    queue.append((nr, nc, dist + 1))

    return -1  # Target not reachable


# ============================================================================
# 📌 DFS TEMPLATE (Depth-First Search)
# ============================================================================

def dfs_recursive(graph: dict, node: int, visited: set) -> None:
    """
    Recursive DFS. Use for: connected components, cycle detection, tree traversal.

    Time: O(V + E), Space: O(V) for visited + O(V) recursion stack
    """
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)


def dfs_iterative(graph: dict, start: int) -> set:
    """
    Iterative DFS using a stack. Avoids recursion limit issues.

    Time: O(V + E), Space: O(V)
    """
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)

    return visited


def dfs_grid(grid: list[list[int]], r: int, c: int, visited: set) -> None:
    """
    DFS on a 2D grid. Mark connected cells as visited.
    Used in: Number of Islands, flood fill, etc.
    """
    rows, cols = len(grid), len(grid[0])
    if r < 0 or r >= rows or c < 0 or c >= cols:
        return
    if (r, c) in visited or grid[r][c] == 0:
        return

    visited.add((r, c))
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        dfs_grid(grid, r + dr, c + dc, visited)


# ============================================================================
# 📌 TOPOLOGICAL SORT (Kahn's Algorithm — BFS-based)
# ============================================================================

def topological_sort(num_nodes: int, edges: list[tuple[int, int]]) -> list[int]:
    """
    Topological sort using BFS (Kahn's algorithm).
    edges: list of (u, v) meaning u → v (u must come before v).

    Returns topological order, or empty list if cycle detected.

    Time: O(V + E), Space: O(V + E)
    """
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    # Build graph
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    # Start with nodes that have no prerequisites
    queue = deque([node for node in range(num_nodes) if in_degree[node] == 0])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If not all nodes are in order, there's a cycle
    return order if len(order) == num_nodes else []


# ============================================================================
# 📌 UNION-FIND (Disjoint Set Union)
# ============================================================================

class UnionFind:
    """
    Union-Find with path compression and union by rank.

    Operations:
        find(x): Find the root of x's component
        union(x, y): Merge components of x and y
        connected(x, y): Check if x and y are in the same component

    Time: O(α(n)) ≈ O(1) amortized per operation
    Space: O(n)
    """

    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n

    def find(self, x: int) -> int:
        """Find root with path compression."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        """
        Union by rank. Returns True if x and y were in different components
        (i.e., a merge actually happened).
        """
        px, py = self.find(x), self.find(y)
        if px == py:
            return False

        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1

        self.components -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        """Check if x and y are in the same component."""
        return self.find(x) == self.find(y)


# ============================================================================
# 📌 SEGMENT TREE (Range Query + Point Update)
# ============================================================================

class SegmentTree:
    """
    Segment tree for range sum queries and point updates.
    Modify the merge function for other operations (min, max, GCD, etc.).

    Build: O(n)
    Query: O(log n)
    Update: O(log n)
    Space: O(n)
    """

    def __init__(self, arr: list[int]):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        if self.n > 0:
            self._build(arr, 1, 0, self.n - 1)

    def _build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self._build(arr, 2 * node, start, mid)
            self._build(arr, 2 * node + 1, mid + 1, end)
            self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def update(self, idx: int, val: int) -> None:
        """Update arr[idx] = val."""
        self._update(1, 0, self.n - 1, idx, val)

    def _update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            if idx <= mid:
                self._update(2 * node, start, mid, idx, val)
            else:
                self._update(2 * node + 1, mid + 1, end, idx, val)
            self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def query(self, l: int, r: int) -> int:
        """Query sum of arr[l..r] (inclusive)."""
        return self._query(1, 0, self.n - 1, l, r)

    def _query(self, node, start, end, l, r):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        left_sum = self._query(2 * node, start, mid, l, r)
        right_sum = self._query(2 * node + 1, mid + 1, end, l, r)
        return left_sum + right_sum


# ============================================================================
# 📌 TRIE (Prefix Tree)
# ============================================================================

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    """
    Trie for prefix-based operations.

    Insert: O(len(word))
    Search: O(len(word))
    StartsWith: O(len(prefix))
    Space: O(total characters across all words)
    """

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        """Returns True if the word is in the trie."""
        node = self._find_node(word)
        return node is not None and node.is_end

    def starts_with(self, prefix: str) -> bool:
        """Returns True if any word in the trie starts with prefix."""
        return self._find_node(prefix) is not None

    def _find_node(self, s: str) -> TrieNode | None:
        node = self.root
        for ch in s:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node


# ============================================================================
# 📌 DIJKSTRA'S ALGORITHM (Shortest Path — Weighted Graph)
# ============================================================================

def dijkstra(graph: dict, start: int, n: int) -> list[int]:
    """
    Dijkstra's shortest path algorithm.
    graph: adjacency list where graph[u] = [(v, weight), ...]

    Returns: list of shortest distances from start to each node (0 to n-1).
    dist[v] = float('inf') if v is unreachable.

    Time: O((V + E) log V) with binary heap
    Space: O(V + E)
    """
    dist = [float('inf')] * n
    dist[start] = 0
    heap = [(0, start)]  # (distance, node)

    while heap:
        d, u = heappop(heap)

        # Skip if we've already found a shorter path
        if d > dist[u]:
            continue

        for v, weight in graph[u]:
            new_dist = dist[u] + weight
            if new_dist < dist[v]:
                dist[v] = new_dist
                heappush(heap, (new_dist, v))

    return dist


# ============================================================================
# 📌 PREFIX SUM
# ============================================================================

def prefix_sum(arr: list[int]) -> list[int]:
    """
    Build prefix sum array. prefix[i] = sum of arr[0..i-1].
    prefix[0] = 0 (empty prefix).

    Range sum query: sum(arr[l..r]) = prefix[r+1] - prefix[l]

    Time: O(n) build, O(1) per query
    Space: O(n)
    """
    n = len(arr)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]
    return prefix


def range_sum(prefix: list[int], l: int, r: int) -> int:
    """Sum of arr[l..r] using prefix sums. O(1)."""
    return prefix[r + 1] - prefix[l]


def prefix_sum_pythonic(arr: list[int]) -> list[int]:
    """Using itertools.accumulate — cleaner in contests."""
    return [0] + list(accumulate(arr))


# Subarray Sum Equals K (classic prefix sum + hash map problem)
def subarray_sum_equals_k(nums: list[int], k: int) -> int:
    """
    Count the number of subarrays whose sum equals k.

    Key Insight: prefix_sum[j] - prefix_sum[i] = k means subarray [i..j-1] sums to k.
    So for each j, we need count of i where prefix_sum[i] = prefix_sum[j] - k.
    Use a hash map to count prefix sums seen so far.

    Time: O(n), Space: O(n)
    """
    count = 0
    current_sum = 0
    prefix_counts = defaultdict(int)
    prefix_counts[0] = 1  # Empty prefix

    for num in nums:
        current_sum += num
        count += prefix_counts[current_sum - k]
        prefix_counts[current_sum] += 1

    return count


# ============================================================================
# 📌 DP MEMOIZATION TEMPLATE
# ============================================================================

def dp_memo_template():
    """
    Template for top-down DP with memoization.

    import sys
    sys.setrecursionlimit(10**6)  # Increase if needed

    from functools import lru_cache

    @lru_cache(maxsize=None)
    def dp(state):
        # Base case
        if base_condition(state):
            return base_value

        # Recursive case — try all transitions
        result = initial_value  # e.g., float('inf') for min, 0 for count
        for next_state in transitions(state):
            result = combine(result, dp(next_state))

        return result

    answer = dp(initial_state)
    dp.cache_clear()  # Free memory after use
    """
    pass


def dp_tabulation_template():
    """
    Template for bottom-up DP with tabulation.

    n = len(input_data)
    dp = [0] * (n + 1)  # or 2D: [[0] * (m+1) for _ in range(n+1)]

    # Base cases
    dp[0] = base_value

    # Fill table
    for i in range(1, n + 1):
        for transition in transitions(i):
            dp[i] = combine(dp[i], dp[prev_state] + cost)

    answer = dp[n]
    """
    pass


# ============================================================================
# 📌 BACKTRACKING TEMPLATE
# ============================================================================

def backtrack_template(candidates, target):
    """
    Generic backtracking template.
    Generates all valid combinations/permutations/subsets.

    Time: varies (often exponential)
    Space: O(depth of recursion)
    """
    result = []

    def backtrack(start, current, remaining):
        # Base case: found a valid solution
        if remaining == 0:
            result.append(current[:])
            return

        # Pruning: invalid state
        if remaining < 0:
            return

        # Try each candidate
        for i in range(start, len(candidates)):
            # Skip duplicates (if candidates is sorted)
            if i > start and candidates[i] == candidates[i - 1]:
                continue

            # Choose
            current.append(candidates[i])

            # Explore (i+1 for combinations, i for reuse)
            backtrack(i + 1, current, remaining - candidates[i])

            # Unchoose (backtrack)
            current.pop()

    candidates.sort()  # Sort for duplicate handling
    backtrack(0, [], target)
    return result


# ============================================================================
# 📌 MONOTONIC STACK
# ============================================================================

def next_greater_element(arr: list[int]) -> list[int]:
    """
    For each element, find the next greater element to its right.
    Returns -1 if no greater element exists.

    Example:
        >>> next_greater_element([4, 5, 2, 25])
        [5, 25, 25, -1]

    Time: O(n), Space: O(n)
    """
    n = len(arr)
    result = [-1] * n
    stack = []  # Stack of indices

    for i in range(n):
        while stack and arr[i] > arr[stack[-1]]:
            result[stack.pop()] = arr[i]
        stack.append(i)

    return result


# ============================================================================
# 📌 INTERVAL MERGE
# ============================================================================

def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    """
    Merge overlapping intervals.

    Example:
        >>> merge_intervals([[1,3],[2,6],[8,10],[15,18]])
        [[1, 6], [8, 10], [15, 18]]

    Time: O(n log n) for sorting
    Space: O(n)
    """
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])

    return merged


# ============================================================================
# Test Suite
# ============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("⚡ Contest Templates — Test Suite")
    print("=" * 60)

    # Two Sum
    print("\n🔸 Two Sum Template")
    assert two_sum_template([2, 7, 11, 15], 9) == [0, 1]
    print("   ✅ Passed!")

    # Sliding Window
    print("\n🔸 Sliding Window (Longest Substring)")
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    print("   ✅ Passed!")

    # Fixed Sliding Window
    print("\n🔸 Fixed Sliding Window")
    assert sliding_window_fixed([2, 1, 5, 1, 3, 2], 3) == 9
    print("   ✅ Passed!")

    # Binary Search
    print("\n🔸 Binary Search")
    assert binary_search([1, 3, 5, 7, 9], 5) == 2
    assert binary_search([1, 3, 5, 7, 9], 4) == -1
    assert binary_search_leftmost([1, 3, 3, 3, 5], 3) == 1
    print("   ✅ Passed!")

    # Binary Search on Answer
    print("\n🔸 Binary Search on Answer")
    # Find smallest x >= 5 in range [1, 10]
    assert binary_search_on_answer(1, 10, lambda x: x >= 5) == 5
    print("   ✅ Passed!")

    # BFS
    print("\n🔸 BFS")
    g = defaultdict(list, {0: [1, 2], 1: [3], 2: [3], 3: []})
    assert bfs(g, 0) == {0: 0, 1: 1, 2: 1, 3: 2}
    print("   ✅ Passed!")

    # Topological Sort
    print("\n🔸 Topological Sort")
    order = topological_sort(4, [(0, 1), (0, 2), (1, 3), (2, 3)])
    assert order[0] == 0 and order[-1] == 3
    print("   ✅ Passed!")

    # Union-Find
    print("\n🔸 Union-Find")
    uf = UnionFind(5)
    uf.union(0, 1)
    uf.union(2, 3)
    assert uf.connected(0, 1) == True
    assert uf.connected(0, 2) == False
    uf.union(1, 3)
    assert uf.connected(0, 3) == True
    assert uf.components == 2
    print("   ✅ Passed!")

    # Segment Tree
    print("\n🔸 Segment Tree")
    st = SegmentTree([1, 3, 5, 7, 9, 11])
    assert st.query(1, 3) == 15  # 3 + 5 + 7
    st.update(2, 10)  # arr becomes [1, 3, 10, 7, 9, 11]
    assert st.query(1, 3) == 20  # 3 + 10 + 7
    print("   ✅ Passed!")

    # Trie
    print("\n🔸 Trie")
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") == True
    assert trie.search("app") == False
    assert trie.starts_with("app") == True
    trie.insert("app")
    assert trie.search("app") == True
    print("   ✅ Passed!")

    # Dijkstra
    print("\n🔸 Dijkstra's Algorithm")
    g = defaultdict(list)
    g[0] = [(1, 4), (2, 1)]
    g[1] = [(3, 1)]
    g[2] = [(1, 2), (3, 5)]
    g[3] = []
    dist = dijkstra(g, 0, 4)
    assert dist == [0, 3, 1, 4]
    print("   ✅ Passed!")

    # Prefix Sum
    print("\n🔸 Prefix Sum")
    ps = prefix_sum([1, 2, 3, 4, 5])
    assert range_sum(ps, 1, 3) == 9  # 2 + 3 + 4
    assert subarray_sum_equals_k([1, 1, 1], 2) == 2
    print("   ✅ Passed!")

    # Next Greater Element
    print("\n🔸 Monotonic Stack (Next Greater Element)")
    assert next_greater_element([4, 5, 2, 25]) == [5, 25, 25, -1]
    print("   ✅ Passed!")

    # Merge Intervals
    print("\n🔸 Merge Intervals")
    assert merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [
        [1, 6], [8, 10], [15, 18]
    ]
    print("   ✅ Passed!")

    print("\n" + "=" * 60)
    print("🏆 ALL CONTEST TEMPLATES PASSED!")
    print("=" * 60)
