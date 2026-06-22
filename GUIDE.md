# 🏆 The Competitive Programmer's Complete Guide to DSA Mastery in Python

> *"The difference between a good programmer and a contest winner is not intelligence — it's pattern recognition speed."*

---

## 📖 Table of Contents

1. [Introduction: The Competitive Programmer's Mindset](#-introduction-the-competitive-programmers-mindset)
2. [How to Use This Course](#-how-to-use-this-course)
3. [The 5 Core Thinking Patterns](#-the-5-core-thinking-patterns-in-competitive-programming)
4. [THE TWO ANCHOR PATTERNS](#-the-two-anchor-patterns-master-these-first)
5. [Python-Specific Power Moves for Contests](#-python-specific-power-moves-for-contests)
6. [Time & Space Complexity Cheat Sheet](#-time--space-complexity-cheat-sheet)
7. [The Problem-Solving Framework](#-the-problem-solving-framework)
8. [Contest Strategy](#-contest-strategy)
9. [Common Contest Problem Patterns with Recognition Triggers](#-common-contest-problem-patterns-with-recognition-triggers)
10. [Recommended Daily Practice Schedule](#-recommended-daily-practice-schedule)
11. [Resources & Next Steps](#-resources--next-steps)

---

## 🧠 Introduction: The Competitive Programmer's Mindset

Welcome. You're not here to "learn to code." You already know how to code. You're here to become **dangerous** — to look at a problem and *see* the solution structure before your fingers even touch the keyboard.

Competitive programming is a sport. Like any sport, it rewards:

1. **Pattern recognition** — seeing a problem and instantly mapping it to a known technique
2. **Muscle memory** — typing the solution without thinking about syntax
3. **Strategic thinking** — knowing when to fight a problem and when to move on
4. **Deliberate practice** — not just solving problems, but solving them *faster* each time

### The Truth About "Hard" Problems

Here's a secret that separates contest winners from everyone else:

> **There are no hard problems. There are only problems you haven't seen the pattern for yet.**

That "HARD" rated sliding window problem you struggled with? The one asking for the longest substring without repeating characters? Once you've internalized the sliding window + set pattern, it's a **3-minute solve**. It *feels* hard only because the pattern hasn't been burned into your neural pathways yet.

This course exists to burn those patterns in.

### What You'll Build

By the end of this system, you will:

- ✅ See "find a pair with target sum" → **instantly** think Hash Map + complement lookup
- ✅ See "longest substring without repeating" → **instantly** think Sliding Window + Set
- ✅ Solve Two Sum in 30 seconds flat, without a single nested loop
- ✅ Write `length_of_longest_substring(s)` from memory in under 60 seconds
- ✅ Recognize 20+ problem patterns from keywords alone
- ✅ Have battle-tested templates for every major pattern
- ✅ Think in Big-O *before* writing a single line of code
- ✅ Execute at competition speed

Let's go.

---

## 🗺️ How to Use This Course

### Learning Path

This course is designed in three phases:

#### Phase 1: Foundation & Anchor Patterns (Week 1-2)
| Day | Focus | Files |
|-----|-------|-------|
| 1-2 | Mindset, Big-O, Brute Force → Optimize | `00_mindset_and_fundamentals.ipynb` |
| 3-4 | Arrays, Hashing, **Two Sum Family** (Anchor #1) | `01_arrays_and_hashing.ipynb`, `two_sum_variations.py` |
| 5-7 | Two Pointers, **Sliding Window** (Anchor #2) | `02_two_pointers_and_sliding_window.ipynb`, `sliding_window_variations.py` |
| 8-9 | Binary Search mastery | `03_binary_search.ipynb` |
| 10 | Speed drill: Patterns 1-4 | `10_contest_speed_drills.ipynb` (problems 1-10) |

#### Phase 2: Advanced Patterns (Week 3-4)
| Day | Focus | Files |
|-----|-------|-------|
| 11-12 | Recursion & Backtracking | `04_recursion_and_backtracking.ipynb` |
| 13-15 | Dynamic Programming | `05_dynamic_programming.ipynb` |
| 16-18 | Graphs & Trees | `06_graphs_and_trees.ipynb` |
| 19-20 | Sorting, Searching, Heaps | `07_sorting_and_searching.ipynb` |
| 21 | Speed drill: All patterns | `10_contest_speed_drills.ipynb` (problems 11-20) |

#### Phase 3: Mastery & Speed (Week 5+)
| Day | Focus | Files |
|-----|-------|-------|
| 22-23 | Math & Bit Manipulation | `08_math_and_bit_manipulation.ipynb` |
| 24-25 | String Manipulation | `09_string_manipulation.ipynb` |
| 26-27 | Python Contest Toolkit | `11_python_contest_toolkit.ipynb` |
| 28 | Pattern Cheatsheet review | `12_problem_patterns_cheatsheet.ipynb` |
| 29-30 | Full speed drills | `10_contest_speed_drills.ipynb` (all 30) |
| 30+ | Daily practice with contest templates | `contest_templates.py` |

### Daily Routine

```
🌅 Morning (30 min):
   → Review one pattern from the cheatsheet
   → Solve 2 problems from that pattern without looking at solutions
   → Time yourself

🌆 Afternoon (45 min):
   → Work through one notebook section
   → Implement every code cell yourself (don't just read!)
   → Trace through examples by hand on paper

🌙 Evening (30 min):
   → Speed drill: pick 3 random problems, solve under time pressure
   → Review any problems you couldn't solve
   → Update your personal "pattern trigger" notes
```

### The #1 Rule

> **Never read a solution without trying the problem for at least 15 minutes first.**

Your brain builds pattern recognition through *struggle*, not passive reading. The pain of being stuck is literally your neurons forming new connections.

---

## 🔥 The 5 Core Thinking Patterns in Competitive Programming

Every competitive programming problem, no matter how exotic it looks, can be attacked with one of five fundamental thinking patterns. Learn to identify which pattern applies, and the "hard" problem becomes a routine exercise.

### Pattern 1: Brute Force → Optimize 🔨➡️⚡

**The Philosophy:** Start with the dumbest possible solution, then make it smart.

Every problem has a brute force solution. The brute force is your *starting point*, not your answer. But it's critical because:

1. It proves you understand the problem
2. It gives you a correct solution to test against
3. It reveals what's slow, which tells you what to optimize

**The Process:**
```
1. Write the O(n²) or O(n³) brute force
2. Ask: "What work am I repeating?"
3. Find a data structure that eliminates the repetition
4. Rewrite with that data structure → usually O(n) or O(n log n)
```

**Example — Two Sum:**
```python
# Brute Force O(n²) — WRONG for contests (TLE)
def two_sum_brute(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# Optimized O(n) — Hash Map eliminates inner loop
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
```

The repeated work in brute force? **Searching for the complement**. A hash map makes that O(1) instead of O(n).

### Pattern 2: Trade Space for Time 💾➡️⚡

**The Philosophy:** Memory is cheap. Time limits are not.

This is the single most powerful optimization in competitive programming. Almost every O(n²) → O(n) improvement comes from using extra memory:

| Extra Memory | What It Buys You |
|---|---|
| Hash Map/Set | O(1) lookups instead of O(n) scans |
| Memoization table | Avoid recomputing subproblems |
| Prefix sum array | O(1) range queries instead of O(n) sums |
| Visited set | Don't revisit states in BFS/DFS |
| Frequency counter | O(1) count queries |

**The Rule:** If your solution is too slow and you're not using extra space, you're probably missing a hash map, a cache, or a precomputed array.

### Pattern 3: Reduce & Conquer 🔍

**The Philosophy:** Cut the problem in half at every step.

When you see a sorted array, a monotonic function, or a decision boundary, think **binary search**. When you can split a problem into independent halves, think **divide and conquer**.

**Recognition triggers:**
- "Find the minimum/maximum that satisfies..."
- "Sorted array"
- "Find the boundary between yes and no"
- Any problem where you can check if an answer works in O(n) and the answer space is ordered

```python
# Binary search template — memorize this
def binary_search(lo, hi, predicate):
    while lo < hi:
        mid = (lo + hi) // 2
        if predicate(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
```

### Pattern 4: Build Up 🧱

**The Philosophy:** Solve small problems first, then combine them into the big answer.

This pattern covers three major techniques:

1. **Dynamic Programming** — solve subproblems, store results, build up
2. **Prefix Sums** — precompute cumulative data for O(1) range queries
3. **Greedy** — make the locally optimal choice at each step

**DP Recognition:**
- "Count the number of ways..."
- "Find the minimum/maximum..."
- Problem has overlapping subproblems (same inputs computed multiple times)
- You can define a state and a recurrence relation

**Greedy Recognition:**
- "Find the minimum number of X to cover Y"
- Local optimal choice leads to global optimal (prove it!)
- Interval scheduling, activity selection

### Pattern 5: Graph/Relationship Thinking 🕸️

**The Philosophy:** When things are connected, think graphs.

Many problems that don't *look* like graph problems ARE graph problems in disguise:

| Problem Description | Graph Translation |
|---|---|
| "Course prerequisites" | Topological sort on a DAG |
| "Is transformation possible?" | BFS from source to target |
| "Connected components" | Union-Find or DFS |
| "Shortest path" | BFS (unweighted) or Dijkstra (weighted) |
| "Can you reach from A to B?" | DFS/BFS reachability |
| "Grid with obstacles" | Grid is a graph, cells are nodes |

```python
# BFS template — works on any graph
from collections import deque

def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited
```

---

## 🎯 THE TWO ANCHOR PATTERNS (Master These First!)

These two patterns come from **real contest problems you've already encountered**. They are your foundation. Every other pattern builds on the thinking skills these two teach you.

---

### 🔥 ANCHOR PATTERN A: Hash Map Lookup — The Two Sum Family

#### The Problem
> Given an array of integers `nums` and an integer `target`, return indices of the two numbers that add up to `target`.

#### The Contest-Killer Insight

When you see **"find a pair/complement/target in an array"**, your brain should fire:

> **HASH MAP. Store what you've seen. Look up the complement. O(n). Done.**

**NEVER** write a nested loop for this. Ever. In a contest, O(n²) = TLE (Time Limit Exceeded) = zero points.

#### The Complement Trick

The key insight is mathematical:
```
If a + b = target
Then b = target - a
So for each number a, check if (target - a) exists in what we've seen
```

#### Solution 1: Dict Lookup (The Standard)

```python
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

**Why it works:** For each number, we compute what we *need* (the complement) and check if we've already *seen* it. The dict gives us O(1) lookup. Total: O(n).

#### Solution 2: Set Intersection (The No-Loop Mindset)

```python
def two_sum_exists(nums, target):
    num_set = set(nums)
    return any(target - num in num_set for num in nums)

# Or even more Pythonic — set intersection:
def two_sum_exists_v2(nums, target):
    s = set(nums)
    complements = {target - n for n in nums}
    return bool(s & complements)  # set intersection!
```

#### Solution 3: Dict Comprehension

```python
def two_sum_indices(nums, target):
    d = {num: i for i, num in enumerate(nums)}
    return next(([i, d[target - num]] for i, num in enumerate(nums) 
                  if target - num in d and d[target - num] != i), [])
```

#### When to Recognize This Pattern

| You see... | You think... |
|---|---|
| "Two numbers that add up to X" | Hash Map + complement |
| "Find a pair with sum/difference" | Hash Map + complement |
| "Check if complement exists" | Hash Set + lookup |
| "Count pairs with property" | Hash Map + frequency |
| "Find duplicate / seen before" | Hash Set |

---

### 🔥 ANCHOR PATTERN B: Sliding Window — Longest Substring Without Repeating Characters

#### The Problem
> Given a string `s`, find the length of the **longest substring** without repeating characters.

**This exact problem appeared as HARD in a past contest. You WILL see it again.** 

#### The Contest-Killer Insight

When you see **"longest/shortest subarray/substring with constraint"**, your brain should fire:

> **SLIDING WINDOW. Two pointers. A set (or dict) to track the window contents. Expand right, shrink left on violation, track the max.**

#### The Approach: Variable Sliding Window with a Set

```
Initialize: left = 0, window = set(), max_length = 0

For each right pointer (0 to n-1):
    While s[right] is already in window:
        Remove s[left] from window
        Move left forward (left += 1)
    Add s[right] to window
    Update max_length = max(max_length, right - left + 1)

Return max_length
```

#### Step-by-Step Trace: `"abcabcbb"`

| Step | right | s[right] | Action | Window (set) | left | max_len |
|------|-------|----------|--------|-------------|------|---------|
| 0 | 0 | 'a' | Add 'a' | {a} | 0 | 1 |
| 1 | 1 | 'b' | Add 'b' | {a,b} | 0 | 2 |
| 2 | 2 | 'c' | Add 'c' | {a,b,c} | 0 | 3 |
| 3 | 3 | 'a' | 'a' in window! Remove 'a', left=1. Add 'a' | {b,c,a} | 1 | 3 |
| 4 | 4 | 'b' | 'b' in window! Remove 'b', left=2. Add 'b' | {c,a,b} | 2 | 3 |
| 5 | 5 | 'c' | 'c' in window! Remove 'c', left=3. Add 'c' | {a,b,c} | 3 | 3 |
| 6 | 6 | 'b' | 'b' in window! Remove 'a', left=4. 'b' still in window! Remove 'b', left=5. Add 'b' | {c,b} | 5 | 3 |
| 7 | 7 | 'b' | 'b' in window! Remove 'c', left=6. 'b' still in window! Remove 'b', left=7. Add 'b' | {b} | 7 | 3 |

**Result: 3** (the substring "abc")

#### Implementation: Side-by-Side Comparison

**Clean Contest Version (memorize this):**
```python
def length_of_longest_substring(s):
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
```

**Annotated Learning Version:**
```python
def length_of_longest_substring(s):
    window = set()      # Characters currently in our window
    left = 0            # Left boundary of window
    length = 0          # Best answer seen so far
    
    for right in range(len(s)):
        # If s[right] is already in window, we have a duplicate!
        # Shrink window from the left until the duplicate is gone
        while s[right] in window:
            window.remove(s[left])  # Remove leftmost char
            left += 1               # Shrink window
        
        # Now s[right] is safe to add — no duplicates
        window.add(s[right])
        
        # Update our best answer
        # Window size = right - left + 1
        length = max(length, right - left + 1)
    
    return length
```

**Dict Version (fewer iterations — jump left pointer directly):**
```python
def length_of_longest_substring(s):
    seen = {}       # char → last index where it appeared
    left = 0
    length = 0
    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1  # Jump left past the duplicate
        seen[ch] = right
        length = max(length, right - left + 1)
    return length
```

#### Why It's O(n)

Each character is added to the window at most once (when `right` advances) and removed at most once (when `left` advances). Both `left` and `right` only move forward. Total operations: at most 2n. **O(n) time, O(min(n, alphabet_size)) space.**

#### When to Recognize This Pattern

| You see... | You think... |
|---|---|
| "Longest substring without repeating" | Sliding Window + Set |
| "Longest substring with at most K distinct" | Sliding Window + Dict (count) |
| "Shortest subarray with sum ≥ target" | Sliding Window (variable) |
| "Fixed-size window" (sum of K elements) | Sliding Window (fixed) |
| "Find all anagrams / permutation in string" | Sliding Window (fixed) + Counter |
| "Minimum window containing all chars" | Sliding Window + Counter |

---

## ⚡ Python-Specific Power Moves for Contests

Python is slower than C++ and Java. You compensate with **cleaner code, fewer bugs, and Python-specific tricks** that let you write solutions in half the lines.

### Built-ins That Replace Loops

```python
# Instead of manual loops, use these:
nums = [1, 2, 3, 4, 5]

# map — apply a function to every element
squares = list(map(lambda x: x**2, nums))  # [1, 4, 9, 16, 25]

# filter — keep elements matching a condition
evens = list(filter(lambda x: x % 2 == 0, nums))  # [2, 4]

# zip — iterate multiple sequences in parallel
for a, b in zip([1,2,3], ['a','b','c']):
    print(a, b)  # 1 a, 2 b, 3 c

# enumerate — get index + value
for i, val in enumerate(nums):
    print(i, val)

# any / all — short-circuit boolean checks
any(x > 3 for x in nums)  # True (stops at 4)
all(x > 0 for x in nums)  # True

# sum with generator
total = sum(x**2 for x in nums)  # 55

# min/max with key
min(words, key=len)         # shortest word
max(nums, key=lambda x: -x) # smallest (trick for reverse)

# sorted with custom key
sorted(intervals, key=lambda x: x[1])  # sort by end time
```

### collections Module — Your Best Friend

```python
from collections import Counter, defaultdict, deque

# Counter — frequency counting in one line
freq = Counter("abracadabra")  # Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
freq.most_common(2)            # [('a', 5), ('b', 2)]

# defaultdict — no KeyError ever
graph = defaultdict(list)
graph[1].append(2)  # No need to check if key exists
graph[1].append(3)

adj = defaultdict(set)
adj['a'].add('b')

count = defaultdict(int)
for c in "hello":
    count[c] += 1  # No need for if c in count

# deque — O(1) append/pop from both ends (BFS essential!)
q = deque([1, 2, 3])
q.appendleft(0)  # [0, 1, 2, 3]
q.popleft()       # 0, deque is [1, 2, 3]
q.append(4)       # [1, 2, 3, 4]
q.pop()           # 4
```

### itertools — Combinatorial Power

```python
from itertools import combinations, permutations, product, accumulate, chain

# combinations — choose k items (order doesn't matter)
list(combinations([1,2,3], 2))  # [(1,2), (1,3), (2,3)]

# permutations — all orderings
list(permutations([1,2,3]))  # all 6 orderings

# product — Cartesian product (replaces nested loops!)
list(product([0,1], repeat=3))  # all binary strings of length 3

# accumulate — prefix sums!
list(accumulate([1,2,3,4]))  # [1, 3, 6, 10]

# chain — flatten multiple iterables
list(chain([1,2], [3,4], [5]))  # [1, 2, 3, 4, 5]
```

### List Comprehensions vs Generator Expressions

```python
# List comprehension — creates a list (uses memory)
squares = [x**2 for x in range(1000000)]

# Generator expression — lazy evaluation (saves memory)
squares_gen = (x**2 for x in range(1000000))

# Use generators with sum, any, all, min, max:
has_even = any(x % 2 == 0 for x in nums)  # Stops at first True
total = sum(x for x in nums if x > 0)     # Only sums positives

# Nested list comprehension (flatten a 2D list)
matrix = [[1,2], [3,4], [5,6]]
flat = [x for row in matrix for x in row]  # [1, 2, 3, 4, 5, 6]

# Dict comprehension
index_map = {val: i for i, val in enumerate(nums)}

# Set comprehension
unique_lengths = {len(word) for word in words}
```

### One-Liner Tricks That Win Time

```python
# Swap without temp
a, b = b, a

# Multiple assignment
x = y = z = 0

# Conditional expression
result = a if condition else b

# Unpack with *
first, *rest = [1, 2, 3, 4]  # first=1, rest=[2,3,4]
*init, last = [1, 2, 3, 4]   # init=[1,2,3], last=4

# Infinity
INF = float('inf')

# Integer max/min
import sys
sys.maxsize  # largest int-like value for comparisons

# Reverse a string/list
s[::-1]

# Check palindrome
s == s[::-1]

# Flatten 2D list
flat = sum(matrix, [])  # or use itertools.chain.from_iterable

# Count occurrences
"abcabc".count('a')  # 2

# String to list of ints
nums = list(map(int, input().split()))

# Matrix transpose
transposed = list(zip(*matrix))
```

### Input/Output Optimization for Speed Contests

```python
import sys
input = sys.stdin.readline  # 3-5x faster than built-in input()

# Read n integers
n = int(input())
nums = list(map(int, input().split()))

# Read multiple lines
lines = sys.stdin.read().split('\n')

# Fast output
print('\n'.join(map(str, results)))  # Much faster than print() in a loop

# For very large I/O
import sys
data = sys.stdin.buffer.read().decode()  # Even faster
```

---

## 📊 Time & Space Complexity Cheat Sheet

### Big-O Quick Reference

| Complexity | Name | Example | n=10⁶ ops | Verdict |
|---|---|---|---|---|
| O(1) | Constant | Hash map lookup | 1 | ✅ Instant |
| O(log n) | Logarithmic | Binary search | 20 | ✅ Instant |
| O(√n) | Square root | Trial division | 1000 | ✅ Fast |
| O(n) | Linear | Single pass | 10⁶ | ✅ Fine |
| O(n log n) | Linearithmic | Sorting | 2×10⁷ | ✅ Usually OK |
| O(n²) | Quadratic | Nested loops | 10¹² | ❌ TLE for n>10⁴ |
| O(n³) | Cubic | Triple nested | 10¹⁸ | ❌ TLE for n>500 |
| O(2ⁿ) | Exponential | All subsets | 10³⁰⁰⁰⁰⁰ | ❌ TLE for n>20 |
| O(n!) | Factorial | All permutations | ∞ | ❌ TLE for n>10 |

### What Complexity Can I Use?

| n (input size) | Max acceptable complexity |
|---|---|
| n ≤ 10 | O(n!) — brute force everything |
| n ≤ 20 | O(2ⁿ) — bitmask, subset enumeration |
| n ≤ 500 | O(n³) — triple loop, Floyd-Warshall |
| n ≤ 5,000 | O(n²) — double loop, simple DP |
| n ≤ 10⁶ | O(n log n) — sort + process, balanced BST |
| n ≤ 10⁸ | O(n) — single pass, hash map |
| n > 10⁸ | O(log n) or O(1) — math, binary search |

### Python Data Structure Operations

| Operation | list | dict/set | deque | heapq |
|---|---|---|---|---|
| Append | O(1)* | — | O(1) | O(log n) push |
| Pop (end) | O(1) | — | O(1) | O(log n) pop |
| Pop (front) | O(n) ❌ | — | O(1) ✅ | — |
| Access [i] | O(1) | O(1) | O(n) | — |
| Search | O(n) | O(1) ✅ | O(n) | O(n) |
| Insert | O(n) | O(1) | O(1) ends | — |
| Delete | O(n) | O(1) | O(n) | — |
| Sort | O(n log n) | — | — | — |

*amortized

---

## 🧩 The Problem-Solving Framework

Use this 5-step process for EVERY problem. Train it until it's automatic.

### Step 1: 📖 READ (2 minutes)

- Read the problem **twice**
- Circle/highlight: **constraints** (especially n — this tells you what complexity you need)
- Underline: **keywords** (these map to patterns — see the recognition trigger table)
- Identify: input format, output format, edge cases
- Ask: "Have I seen this before? What pattern does it remind me of?"

### Step 2: 🧪 EXAMPLES (2 minutes)

- Trace through the given examples by hand
- Create your own small example
- Think about edge cases: empty input, single element, all same, sorted, reverse sorted

### Step 3: 💭 PLAN (3 minutes)

- State the brute force approach out loud
- Identify what's slow about it (what work is repeated?)
- Apply the pattern you recognized in Step 1
- **State the complexity before coding** — if it doesn't fit the constraints, rethink

### Step 4: 💻 CODE (5-10 minutes)

- Write the solution cleanly
- Use descriptive variable names (even in contests, `left` is better than `l`)
- Don't debug as you write — finish the complete solution first

### Step 5: ✅ VERIFY (2 minutes)

- Trace through your code with the examples
- Check edge cases mentally
- If it's a contest, submit. If practice, run it
- **After solving: Write down the pattern for future reference**

### The Time Budget Rule

In a typical contest with 5 problems and 2-3 hours:

| Problem | Difficulty | Time Budget | Strategy |
|---|---|---|---|
| A | Easy | 5-10 min | Speed solve. If stuck > 5 min, something's wrong |
| B | Easy-Medium | 10-15 min | Pattern recognition. Apply template |
| C | Medium | 15-25 min | Think before coding. Get the approach right |
| D | Medium-Hard | 20-30 min | May need 2+ patterns combined |
| E | Hard | 30-45 min | Skip if no idea after 5 min. Come back if time |

---

## 🏅 Contest Strategy

### Before the Contest

1. **Set up your environment**: Have your template file ready with fast I/O
2. **Warm up**: Solve 2-3 easy problems in the 30 minutes before
3. **Have reference**: Keep `contest_templates.py` and `12_problem_patterns_cheatsheet.ipynb` open

### During the Contest

1. **Read ALL problems first** (3-5 minutes scanning)
   - Sort problems by estimated difficulty for you personally
   - Start with the easiest, not problem A

2. **Speed-solve easy problems** (get points on the board)
   - Don't overthink — if you see the pattern, code it
   - Submit quickly, fix bugs after if needed

3. **The 5-Minute Rule for hard problems**
   - If after 5 minutes you have NO idea → skip it, come back later
   - If you have an idea but aren't sure → spend 2 more minutes thinking, then code
   - Never spend 30 minutes on one problem while ignoring easier ones

4. **Debug efficiently**
   - Print intermediate variables, don't use a debugger in contests
   - Test with small inputs first
   - Check off-by-one errors (most common bug in contests)

5. **Time management**
   - Check the clock after every problem
   - If you're behind, skip to easier problems
   - Save 10 minutes at the end to re-read unsolved problems with fresh eyes

### Common Contest Pitfalls to Avoid

| Pitfall | Solution |
|---|---|
| Spending too long on one problem | 5-minute rule: no idea → skip |
| Not reading constraints | ALWAYS check n — it tells you the complexity |
| Off-by-one errors | Use `range(n)` not `range(n-1)`, double-check boundaries |
| Integer overflow | Python handles big ints natively — one less thing to worry about! |
| Wrong I/O format | Read the output format carefully. "Print each on a new line" vs "space-separated" |
| Not handling edge cases | Empty input, single element, negative numbers, zeros |
| Premature optimization | Get a correct brute force first, then optimize |

---

## 🗂️ Common Contest Problem Patterns with Recognition Triggers

This is the **most important table in this guide**. Memorize it. Print it. Tape it to your wall.

| When You See These Keywords... | Think This Pattern... | Template In... |
|---|---|---|
| "Find pair with target sum" | **Hash Map + complement** | `contest_templates.py` |
| "Longest/shortest substring without repeating" | **Sliding Window + Set** | `contest_templates.py` |
| "Longest substring with at most K distinct" | **Sliding Window + Dict** | `sliding_window_variations.py` |
| "Subarray sum equals K" | **Prefix Sum + Hash Map** | `contest_templates.py` |
| "Sorted array + find target" | **Two Pointers** (from both ends) | `contest_templates.py` |
| "Find position in sorted array" | **Binary Search** | `contest_templates.py` |
| "Minimum/maximum that satisfies condition" | **Binary Search on Answer** | `03_binary_search.ipynb` |
| "All combinations/subsets/permutations" | **Backtracking** | `04_recursion_and_backtracking.ipynb` |
| "Overlapping subproblems" / "Count ways" | **Dynamic Programming** | `contest_templates.py` |
| "Shortest path (unweighted)" | **BFS** | `contest_templates.py` |
| "Shortest path (weighted)" | **Dijkstra's** | `contest_templates.py` |
| "Connected components" | **Union-Find or DFS** | `contest_templates.py` |
| "Prerequisites / ordering" | **Topological Sort** | `contest_templates.py` |
| "Merge intervals / overlapping ranges" | **Sort by start, merge** | `07_sorting_and_searching.ipynb` |
| "K largest/smallest elements" | **Heap (heapq)** | `contest_templates.py` |
| "Palindrome" | **Two Pointers** (from center or ends) | `09_string_manipulation.ipynb` |
| "Grid traversal" | **BFS/DFS on grid** | `06_graphs_and_trees.ipynb` |
| "Tree path/depth/ancestor" | **DFS/BFS on tree** | `06_graphs_and_trees.ipynb` |
| "XOR trick / bit pattern" | **Bit Manipulation** | `08_math_and_bit_manipulation.ipynb` |
| "Frequency / anagram / character count" | **Counter / Hash Map** | `01_arrays_and_hashing.ipynb` |

### The Decision Tree

```
Is the array sorted?
├── Yes → Two Pointers or Binary Search
└── No → 
    ├── Need to find a pair/complement? → Hash Map
    ├── Need longest/shortest subarray? → Sliding Window
    ├── Need all subsets/combinations? → Backtracking
    ├── Need optimal value with subproblems? → DP
    ├── Is it a graph/grid/tree? → BFS/DFS
    └── Need K-th element or top K? → Heap
```

---

## 📅 Recommended Daily Practice Schedule

### Week 1-2: Foundations
```
Day 1:  Read GUIDE.md (this file). Set up environment.
Day 2:  Complete 00_mindset_and_fundamentals.ipynb
Day 3:  Complete 01_arrays_and_hashing.ipynb (first half)
Day 4:  Complete 01_arrays_and_hashing.ipynb (second half)
Day 5:  Solve all two_sum_variations.py problems from memory
Day 6:  Complete 02_two_pointers_and_sliding_window.ipynb (two pointers)
Day 7:  Complete 02_two_pointers_and_sliding_window.ipynb (sliding window)
Day 8:  Solve all sliding_window_variations.py problems from memory
Day 9:  Complete 03_binary_search.ipynb
Day 10: Speed drill — problems 1-10 from 10_contest_speed_drills.ipynb
Day 11: Review weak areas, re-solve problems you struggled with
Day 12: Timed practice: 5 random problems, 1 hour
Day 13: Complete 04_recursion_and_backtracking.ipynb (first half)
Day 14: Complete 04_recursion_and_backtracking.ipynb (second half)
```

### Week 3-4: Advanced Patterns
```
Day 15: Complete 05_dynamic_programming.ipynb (linear DP)
Day 16: Complete 05_dynamic_programming.ipynb (grid + knapsack DP)
Day 17: Complete 05_dynamic_programming.ipynb (string DP + interval DP)
Day 18: Complete 06_graphs_and_trees.ipynb (graphs)
Day 19: Complete 06_graphs_and_trees.ipynb (trees + BST)
Day 20: Complete 07_sorting_and_searching.ipynb
Day 21: Speed drill — problems 11-20 from 10_contest_speed_drills.ipynb
```

### Week 5+: Mastery
```
Day 22: Complete 08_math_and_bit_manipulation.ipynb
Day 23: Complete 09_string_manipulation.ipynb
Day 24: Complete 11_python_contest_toolkit.ipynb
Day 25: Study 12_problem_patterns_cheatsheet.ipynb
Day 26-28: Full speed drill — all 30 problems from 10_contest_speed_drills.ipynb
Day 29-30: Simulated contest (pick 5 random problems, 2 hour time limit)
Day 31+: Daily practice — 3 problems per day, timed, rotating through patterns
```

### The Maintenance Routine (After Initial Learning)

Once you've completed the course, maintain your edge with:

```
🌅 Morning (20 min):
   → 1 random problem from a weak pattern
   → Solve WITHOUT looking at any reference

🌆 Afternoon (30 min):
   → Participate in an online contest (Codeforces, LeetCode contest, AtCoder)
   → OR solve 2 medium problems under time pressure

🌙 Evening (15 min):
   → Review today's problems
   → If you struggled, re-derive the solution from scratch
   → Update your personal pattern notes
```

---

## 📚 Resources & Next Steps

### Online Judges (Practice Platforms)
| Platform | Best For |
|---|---|
| [LeetCode](https://leetcode.com) | Interview prep, pattern practice, weekly contests |
| [Codeforces](https://codeforces.com) | Competitive programming, rated contests |
| [AtCoder](https://atcoder.jp) | Clean problems, beginner-friendly contests |
| [HackerRank](https://hackerrank.com) | Structured tracks, company-specific prep |
| [Project Euler](https://projecteuler.net) | Mathematical problems |

### Recommended Books
| Book | Focus |
|---|---|
| *Competitive Programming* by Steven Halim | Comprehensive CP reference |
| *Cracking the Coding Interview* by Gayle McDowell | Interview-focused DSA |
| *Introduction to Algorithms (CLRS)* | Deep theory understanding |
| *Algorithm Design Manual* by Skiena | Practical problem-solving |

### Video Resources
| Channel | Focus |
|---|---|
| NeetCode | LeetCode solutions with visual explanations |
| Abdul Bari | Algorithm theory with excellent visuals |
| Errichto | Advanced competitive programming |
| William Fiset | Graph algorithms deep dive |

### Recommended Problem Lists
1. **NeetCode 150** — curated list covering all major patterns
2. **LeetCode Top Interview 150** — industry standard
3. **Codeforces Ladder** — problems sorted by rating
4. **CSES Problem Set** — 300 essential CP problems

### Next Steps After This Course

1. **Start rating on Codeforces** — do virtual contests, track your improvement
2. **Join weekly LeetCode contests** — build contest stamina
3. **Study advanced topics**: Segment trees, Fenwick trees, String algorithms (KMP, Z-algorithm), Network flow, Heavy-light decomposition
4. **Teach others** — explaining a pattern solidifies your understanding
5. **Build a personal problem diary** — for each problem you solve, write: pattern recognized, key insight, time taken

---

## 💪 Final Words

Competitive programming mastery is a marathon, not a sprint. But it's a marathon where every kilometer makes you exponentially better. The first 20 patterns you learn will cover 80% of all contest problems you'll ever face.

Start with the two anchor patterns. Master Two Sum and Longest Substring Without Repeating Characters until you can solve them in your sleep. Then expand outward.

See you at the top of the leaderboard. 🏆

---

*Generated for the speed-focused competitive programmer. Every pattern. Every trick. Every template. No fluff.*
