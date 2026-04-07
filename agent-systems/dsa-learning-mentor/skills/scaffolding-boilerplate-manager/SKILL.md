---
name: "scaffolding-boilerplate-manager"
description: "Use when: setting up files, creating function signatures, managing C++ boilerplate. Agent handles infrastructure, student writes algorithm logic only."
---

# Scaffolding & Boilerplate Manager

## Core Principle
**Agent handles INFRASTRUCTURE. Student writes ALGORITHM LOGIC.**

This means:
- ✅ Agent creates files
- ✅ Agent writes includes, namespaces, function signatures
- ✅ Agent structures TODOs and hints
- ❌ Agent does NOT write the algorithm logic
- ❌ Student does NOT need to set up files or boilerplate

## Responsibility Allocation

### AGENT CREATES
- [ ] File structure (`.cpp`, `.h` if needed)
- [ ] `#include` statements
- [ ] `using namespace std;` setup
- [ ] Function signatures with correct parameters/return
- [ ] Class structure (if needed)
- [ ] Main/test harness skeleton
- [ ] TODO comments as hints (if Level 1)
- [ ] Comments explaining what the function should do

### STUDENT WRITES
- [ ] Algorithm logic inside function body
- [ ] Variable declarations needed for logic
- [ ] Loop structures and control flow
- [ ] Recursion or the core idea
- [ ] Testing/edge case handling (for Level 3)

### CONCRETE EXAMPLE: Graph DFS

**Agent creates this:**
```cpp
#include <vector>
#include <unordered_set>
using namespace std;

// DFS to find all nodes reachable from 'start' in graph 'adj'
void dfs(int node, vector<vector<int>>& adj, unordered_set<int>& visited) {
    // TODO: Mark current node as visited
    
    // TODO: Loop through all neighbors of current node
    
    // TODO: If neighbor is unvisited, recursively call dfs on it
}

int main() {
    vector<vector<int>> adj = {{1, 2}, {0, 3}, {0}, {1}};
    unordered_set<int> visited;
    
    dfs(0, adj, visited);
    
    // Print all visited nodes
    for (int node : visited) {
        cout << node << " ";
    }
    return 0;
}
```

**Student fills in this:**
```cpp
void dfs(int node, vector<vector<int>>& adj, unordered_set<int>& visited) {
    visited.insert(node);  // Student writes this
    
    for (int neighbor : adj[node]) {  // Student writes this
        if (visited.find(neighbor) == visited.end()) {  // Student writes this
            dfs(neighbor, adj, visited);  // Student writes this
        }
    }
}
```

**What agent did NOT do:**
- Student didn't write the #include lines
- Student didn't set up the main function
- Student didn't think about data structures (agent chose unordered_set)
- Student didn't write function signature

**What student DID do:**
- Logic for marking visited
- Loop through neighbors
- Recursion pattern
- Edge case handling (check if visited)

## File Organization Patterns

### Pattern 1: Single Function (Most Common)
**When:** Simple algorithm or one problem at a time  
**Structure:**
```cpp
#include <needed>
using namespace std;

// Function signature + TODOs or skeleton
void/int algorithmName(/* params */) {
    // Student implementation
}

int main() {
    // Test harness
}
```

### Pattern 2: Class-Based (When Reasonable)
**When:** Multiple operations on same structure (Graph class, BST)  
**Structure:**
```cpp
#include <vector>
using namespace std;

class Graph {
private:
    vector<vector<int>> adj;
    int vertices;
    
public:
    Graph(int v) : vertices(v), adj(v) {}
    
    void addEdge(int u, int v);  // TODO: Implementation
    void dfs(int start);  // TODO: Implementation  
    // ... other methods
};

int main() {
    Graph g(4);
    g.addEdge(0, 1);
    g.dfs(0);
    return 0;
}
```

### Pattern 3: Multiple Files (When Needed)
**When:** Project reaches complexity - separate concerns  
**Structure:**
```
project/
├── graph.h      // Class definition (Agent writes)
├── graph.cpp    // Implementation (Student fills TODOs)
├── main.cpp     // Test harness (Agent writes)
└── README.md
```

## TODOs: Infrastructure vs Logic

### TODOs Agent LEAVES (Appropriate)
```cpp
// TODO: Check if two nodes are adjacent
if (/* condition to check neighbors */) {
```

### TODOs Agent SHOULD NOT LEAVE (Implementation)
```cpp
// WRONG: Student shouldn't need to write this
// TODO: Use binary search to find element
// TODO: Loop through unordered_map
```

## Complexity Decisions Made by Agent

**Agent chooses data structures based on:**
1. Problem requirements (what must be fast?)
2. Common practice (what do professionals do?)
3. Teaching value (what helps student understand?)

**Example decisions:**
- DFS → `unordered_set` for visited (fast lookup)
- BFS → `queue<int>` (canonical choice)
- Shortest path → `priority_queue` (shows Dijkstra pattern)
- DP → `vector<vector<int>>` (2D array is standard)

**Agent explains these choices:**
```cpp
// Using unordered_set for O(1) lookups on visited nodes
unordered_set<int> visited;

// Could also use vector<bool> - what's the tradeoff?
// (guides student thinking without giving algorithm away)
```

## Include Strategy

### Minimal Pattern (Starts Bare)
```cpp
#include <vector>
#include <unordered_set>
#include <iostream>
using namespace std;
```

### Teaching Pattern (When Learning C++)
```cpp
#include <vector>      // For adj list
#include <unordered_set>  // For visited tracking
#include <queue>       // For BFS
#include <iostream>
using namespace std;
```

### Full Pattern (When Complete Toolbox Needed)
```cpp
#include <vector>
#include <unordered_set>
#include <unordered_map>
#include <queue>
#include <stack>
#include <algorithm>
#include <iostream>
using namespace std;
```

## Test Harness Strategy

### Level 1: Provided Test Cases
```cpp
int main() {
    // Test Case 1: Simple graph
    vector<vector<int>> adj = {{1, 2}, {0, 3}, {0}, {1}};
    unordered_set<int> visited;
    dfs(0, adj, visited);
    
    cout << "Visited: ";
    for (int node : visited) cout << node << " ";
    cout << endl;
    
    // Expected: 0 1 3 2 (or similar valid order)
    
    return 0;
}
```

### Level 2: Partial Test Cases
```cpp
int main() {
    // Test Case 1
    vector<vector<int>> adj = {{1}, {0, 2}, {1}};
    unordered_set<int> visited;
    dfs(0, adj, visited);
    // Check if all 3 nodes visited
    
    // TODO: You add more test cases below
    
    return 0;
}
```

### Level 3: Student Writes Tests
```cpp
int main() {
    // Student designs AND writes test cases
    // No scaffolding provided
    return 0;
}
```

## Common Patterns to Reuse

### Graph Setup Pattern
```cpp
// Adjacency list representation
vector<vector<int>> adj = {{/* neighbors of 0 */}, 
                            {/* neighbors of 1 */}};
int numVertices = adj.size();
```

### Visited Tracking Pattern
```cpp
// Choose ONE:
unordered_set<int> visited;              // Fast lookup, clean
vector<bool> visited(n, false);          // Simple, explicit
vector<int> visited(n, -1);              // Can store extra info (like parent)
```

### DP Table Pattern
```cpp
// 1D DP
vector<int> dp(n, 0);
dp[0] = 1;  // base case

// 2D DP
vector<vector<int>> dp(m, vector<int>(n, 0));
dp[0][0] = 1;  // base case
```

### Recursion Pattern
```cpp
// Base case first
if (/* termination condition */) {
    return /* base answer */;
}

// Recursive case
return /* recursive calculation */;
```

## Anti-Patterns to Avoid

### ❌ Student Sets Up Own Files
```cpp
// WRONG: Student had to create and structure this
#include <vector>
using namespace std;
void dfs( ... ) { ... }
```
**Why wrong:** Agent didn't reduce friction. Student wasted time on infrastructure.  
**Fix:** Agent provides ready-to-edit file.

### ❌ Agent Doesn't Explain Data Structure Choice
```cpp
unordered_set<int> visited;  // No explanation
```
**Why wrong:** Student doesn't understand why unordered_set vs vector<bool>  
**Fix:** Add comment: `// unordered_set for O(1) lookup vs O(n) with vector<bool>`

### ❌ TODOs are Too Vague
```cpp
// TODO: Implement DFS
```
**Why wrong:** Student doesn't know where to start  
**Fix:** Break into steps: Mark visited → Loop neighbors → Recursion

### ❌ Agent Writes Algorithm Logic
```cpp
// WRONG: Agent did the thinking
for (int neighbor : adj[node]) {  // This is ALGORITHM, not boilerplate
    if (visited.find(neighbor) == visited.end()) {
        dfs(neighbor, adj, visited);
    }
}
```
**Fix:** Leave as TODO. Let student write the logic.

### ❌ Missing Test Harness
```cpp
void dfs( ... ) {
    // ... implementation
}
// No main() function to test
```
**Why wrong:** Student doesn't know how to run/test their code  
**Fix:** Always include working test harness.

## Quality Checklist
- [ ] File is ready to edit immediately (no "set up first")
- [ ] All includes present and explained
- [ ] Function signatures are correct
- [ ] TODOs guide toward algorithm, not infrastructure
- [ ] Test harness works (student can immediately run)
- [ ] No algorithm logic in agent-provided code
- [ ] Data structure choices are explained
- [ ] Code is readable and well-formatted
- [ ] Comments explain WHAT we're doing, not HOW
