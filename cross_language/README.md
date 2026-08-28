# Cross-Language Competitive Programming Examples

This folder contains C++ equivalents of the Python problems covered in the main notebooks and `practice_problems/` folder.

## Why C++ Alongside Python?

| Concern                  | Python                       | C++                              |
|--------------------------|------------------------------|----------------------------------|
| Contest Speed            | Slow I/O, GIL                | ⚡ Fastest — use this in ICPC    |
| Robotics / Embedded      | Not typical                  | ✅ Primary language              |
| Interview whiteboard     | ✅ Very readable              | ✅ Acceptable everywhere         |
| Standard library         | `list`, `dict`, `heapq`      | `vector`, `unordered_map`, `pq`  |
| Type system              | Dynamic (with hints)         | Static, manual memory            |

## Folder Structure

```
cross_language/
├── README.md                         ← You are here
└── cpp/
    ├── two_sum_variations.cpp        ← 10 Two Sum problems in C++
    ├── sliding_window_variations.cpp ← 10 Sliding Window problems in C++
    └── contest_template.cpp          ← Boilerplate + all key templates in C++
```

## How to Run

```bash
# Compile a single file
g++ -O2 -std=c++17 -o two_sum cpp/two_sum_variations.cpp && ./two_sum

# Compile all at once
for f in cpp/*.cpp; do
    g++ -O2 -std=c++17 -o "${f%.cpp}" "$f" && echo "✅ $f compiled"
done
```

## Key Language Mapping — Python → C++

| Python                                    | C++ Equivalent                                    |
|-------------------------------------------|---------------------------------------------------|
| `dict` / `Counter`                        | `unordered_map<K,V>` (O(1) avg)                  |
| `set`                                     | `unordered_set<T>`                                |
| `list`                                    | `vector<T>`                                       |
| `collections.deque`                       | `deque<T>` or `queue<T>`                          |
| `heapq` (min-heap)                        | `priority_queue<T, vector<T>, greater<T>>`        |
| `@lru_cache`                              | `unordered_map<K,V>` memo / flat `dp[]` array     |
| `float('inf')`                            | `INT_MAX` / `LLONG_MAX` / `1e18`                  |
| `enumerate(arr)`                          | `for (int i = 0; i < n; i++)`                    |
| `[f(x) for x in arr]`                    | manual loop or `transform(...)`                   |
| `if key in dict:`                         | `if (map.count(key))`                             |
| `del dict[key]`                           | `map.erase(key)`                                  |

## ⚠️ Critical C++ Gotcha: `priority_queue` is a MAX-HEAP

```cpp
// Python heapq is a MIN-HEAP — smallest element at top.
// C++ priority_queue is a MAX-HEAP by default — largest element at top!

priority_queue<int> maxHeap;                              // MAX-heap (default)
priority_queue<int, vector<int>, greater<int>> minHeap;  // MIN-heap (Dijkstra, etc.)

// MIN-heap of pairs (dist, node) — the Dijkstra pattern:
priority_queue<pair<int,int>,
               vector<pair<int,int>>,
               greater<>> pq;
```
