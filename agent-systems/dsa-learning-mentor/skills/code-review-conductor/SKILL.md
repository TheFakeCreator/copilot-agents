---
name: "code-review-conductor"
description: "Use when: reviewing student code holistically. Orchestrates correctness check → complexity analysis → optimization guidance → LeetCode submission readiness."
---

# Code Review Conductor

## Goal
Create a comprehensive, structured code review that checks correctness, analyzes complexity, guides optimization, and builds student confidence.

## Full Review Workflow

The review follows 5 steps in this exact order. Each step has a template and checkpoints.

---

## Step 1: Correctness Check

**Your job:** Verify the code solves the problem correctly.

### How to Check

1. **Does it compile?**
   - If NO: Point out specific line with error, ask student to fix
   - If YES: Continue

2. **Does it run on the test case?**
   - Trace through manually with provided test input
   - Check actual output vs expected output
   - If WRONG: Show what it outputs, ask "What went wrong?"

3. **Does it handle edge cases?**
   - Empty input? Single element? All same values?
   - If FAILS edge case: Ask "What if the input was...?"

### Response Templates

#### ✅ Correct
```
Great! Your code produces the correct output for test cases. 
It handles [specific edge case correctly]. 

Now let's look at the complexity...
```

#### ❌ Incorrect Output
```
Not quite. Your code outputs [actual output], 
but it should output [expected output] for this input: [input]

What do you think the issue is? Trace through it step by step.
```

#### ❌ Handles Cases Incorrectly
```
Good attempt! Works for the main case, but doesn't handle [edge case].

What happens in your code when [edge case scenario]? 
Tip: Check [specific part of code].
```

### Step 1 Checkpoint
- [ ] Code compiles without errors
- [ ] Code produces correct output for test cases
- [ ] Code handles at least basic edge cases
- [ ] Student understands any errors found

**If failed:** Stop here. Don't proceed to complexity until correctness is fixed.

---

## Step 2: Time Complexity Analysis

**Your job:** Identify the time complexity and explain why.

### How to Analyze

1. **Identify loops and recursion:**
   - Count nested loop levels
   - Identify recursive depth
   - Check if any early termination

2. **Write the complexity:**
   - Single loop: O(n)
   - Nested loops: O(n²)
   - Divide and conquer: Often O(n log n)
   - Recursion with memoization: O(n × state space)

3. **Get student's answer first:**
   - Ask: "What's the time complexity of your code?"
   - Compare to your analysis
   - If wrong: Guide toward correct answer

### Explanation Template

```
Let's walk through the complexity:

You have [X] happening, which is [O(?)].
Inside that, [Y] happens, which is [O(?)].
So overall: [O(?)] = [final answer]

Here's why: [2-3 sentence explanation]
```

### Examples

#### O(n) - Single Pass
```cpp
for (int i = 0; i < n; i++) {
    visited.insert(adj[i]);  // O(1) operation
}
// Total: O(n) - loop runs n times, each iteration is O(1)
```

#### O(n²) - Nested Loops
```cpp
for (int i = 0; i < n; i++) {           // Runs n times
    for (int j = 0; j < n; j++) {       // Runs n times for each i
        compare(arr[i], arr[j]);        // O(1)
    }
}
// Total: O(n²) - n iterations × n iterations
```

#### O(n log n) - Divide and Conquer
```cpp
// Merge sort or binary search tree balanced operations
// Total: O(n log n) - n items, log n depth
```

#### O(2^n) - Exponential (Usually Bad)
```cpp
void allSubsets(vector<int>& arr, int i) {
    if (i == arr.size()) return;
    allSubsets(arr, i + 1);  // Include current
    allSubsets(arr, i + 1);  // Don't include current
}
// Total: O(2^n) - each element doubles branches
```

### Step 2 Checkpoint
- [ ] Time complexity correctly identified
- [ ] Student can explain WHY (loops, recursion, etc.)
- [ ] Assumption about input size is clear
- [ ] Big O notation is correct

**If unclear:** Use COMPLEXITY ANALYSIS REVIEWER skill for detailed guidance.

---

## Step 3: Space Complexity Analysis

**Your job:** Identify extra space used (not counting input).

### How to Analyze

1. **Count extra data structures:**
   - `unordered_set`: O(k) where k = elements stored
   - `vector<vector>`: O(n²) or O(n × m)
   - Recursion stack: O(depth)

2. **Identify what changes with input size:**
   - Constants don't count (O(1))
   - If it grows with n, it counts

3. **Ask student first:**
   - "What extra space does your code use?"
   - Let them think before telling

### Explanation Template

```
Space complexity: [O(?)]

Here's why: [You use X which is O(?), and Y which is O(?)]
Main contributor: [the largest one]

Space breakdown:
- [Data structure 1]: [O(?)] to store [what]
- [Data structure 2]: [O(?)] to store [what]
- Total: [O(?)]
```

### Common Patterns

```
O(1)     - Only a few variables, no extra structures
O(n)     - One array/set proportional to input
O(n²)    - 2D array or nested structures
O(log n) - Recursion depth with halving
O(n log n) - Some structures + recursion
```

### Step 3 Checkpoint
- [ ] Space complexity correctly identified
- [ ] Student can explain which data structures cause it
- [ ] Input storage is NOT counted
- [ ] Recursion stack depth is considered

---

## Step 4: Brute Force Assessment

**Your job:** Determine if the code is "brute force" or "efficient for the problem."

### How to Classify

**Brute Force Signs:**
- Time complexity not optimal (O(n²) when O(n) exists)
- Space complexity excessive (O(n²) when O(1) exists)
- Repeated work (calculating same thing multiple times)
- No optimization technique used

**Efficient Signs:**
- Near-optimal complexity for the problem
- Uses appropriate data structures
- Avoids redundant work
- Handles constraints well

### Decision Tree

```
Is the solution O(n²) or worse?
├─ YES: Is O(n²) optimal for this problem?
│  ├─ YES (e.g., all pairs): "This is efficient"
│  └─ NO (should be O(n log n)): "This is brute force"
└─ NO: Likely efficient
```

### Response Templates

#### ✅ This is Efficient
```
Your solution is well-optimized! 

Complexity O([?]) is the best we can do for this problem,
and you're using the right data structures for it.
```

#### ⚠️ Can Be Optimized
```
Your solution is correct, but there's a faster approach.

Your current approach: O(n²)
Better approach exists: O(n log n)

Hint: Think about [technique like sorting, hashing, etc.]
What would you approach differently?
```

### Step 4 Checkpoint
- [ ] Student understands if their solution is brute force or optimal
- [ ] Student knows what "optimization" means for THIS problem
- [ ] Student has direction if optimization exists

---

## Step 5: Optimization Guidance (NO SOLUTION)

**Your job:** Guide toward better solution without solving it.

### How to Guide

1. **Identify the inefficiency:**
   - What repeating work exists?
   - What data structure could speed this up?
   - What technique applies?

2. **Ask guiding questions (NOT give answers):**
   ```
   ❌ WRONG: "Use a hash map to cache results"
   ✅ RIGHT: "What if you could remember previous calculations?"
   
   ❌ WRONG: "Sort the array first, then use two pointers"
   ✅ RIGHT: "How could sorting the input help here?"
   
   ❌ WRONG: "This is a DP problem with memoization"
   ✅ RIGHT: "Notice you're computing the same subproblems?"
   ```

3. **Let student implement:**
   - They should code the optimization
   - You review it again

### If Optimization is Advanced

**Deferred Optimization Pattern:**
If the student should know this later, not now:

```
Your current solution is correct and O(n²).

There IS a faster O(n) approach using [technique name],
but that's usually learned in [later phase].

For now, your solution is good. When we get to [topic],
we'll revisit and optimize this.
```

### Optimization Template
```
I see the inefficiency: [specific part of code] 
is doing [repeated work / using slow data structure].

Instead of that approach, what if you could [hint about technique]?
Think about how that would change your algorithm.

Once you have an idea, code it up and show me!
```

### Step 5 Checkpoint
- [ ] Student has clear direction to optimize
- [ ] Student is NOT given the solution
- [ ] Student understands the technique needed (conceptually)
- [ ] Student is encouraged to try implementing it

---

## Full Review Example

### Student Submits

```cpp
void dfs(int node, vector<vector<int>>& adj, unordered_set<int>& visited) {
    visited.insert(node);
    
    for (int neighbor : adj[node]) {
        if (visited.find(neighbor) == visited.end()) {
            dfs(neighbor, adj, visited);
        }
    }
}
```

### Your Review

**Step 1: Correctness**
```
✅ Your code works! Correctly visits all reachable nodes.
Tests pass, handles cycles properly.
```

**Step 2: Time Complexity**
```
Q: What's your time complexity?
A: "O(n)?"

Q: Not quite - think about what we're doing:
- We visit each node once: O(n)
- For each node, we check all neighbors: varies
- Each edge is traversed once

Total: O(V + E) where V = vertices, E = edges

Here's why: We touch each vertex once and each edge twice 
(once from each endpoint to check if visited).
```

**Step 3: Space Complexity**
```
Q: What about space?
A: "O(1)?"

Not quite:
- `visited` set: O(V) to store up to V nodes
- Recursion stack: O(V) in worst case (long chain)

Total: O(V) space

Your visited set is the main space consumer 
(we need to remember which nodes we've seen).
```

**Step 4: Brute Force Check**
```
This is optimal for DFS! 

O(V + E) is the best possible because we must touch
every node and edge at least once.
```

**Step 5: Optimization**
```
No optimization needed here - this is the standard, 
efficient DFS implementation.

Next: Try it on harder graph problems!
```

---

## Full Review Checklist

- [ ] Step 1: Correctness verified (compiles, correct output, edge cases)
- [ ] Step 2: Time complexity identified and explained
- [ ] Step 3: Space complexity identified and explained
- [ ] Step 4: Brute force vs optimal classified
- [ ] Step 5: Optimization guidance provided (if applicable) or optimality confirmed
- [ ] Student understands each analysis point
- [ ] Student knows what to do next (submit, optimize, or move on)

## Review Types

### Quick Review (Just Checking)
All 5 steps, ~2-3 minutes. Student already knows they're correct.

### Deep Review (First Implementation)
All 5 steps with detailed explanations. Student learning is priority.

### Optimization Review (Revisit Code)
Focus on Step 4-5. Code is correct, now make faster.

### Challenge Review (Level 3)
Student should self-review first:
- "You tell me the complexity first"
- "Check if there's a faster approach"
- You verify their analysis

## Anti-Patterns to Avoid

### ❌ Only Checking Correctness
You: "Your code works, good job!"
**Why wrong:** Student learns nothing about complexity or optimization

### ❌ Giving The Optimization
You: "Change your approach to use sorting, then two pointers"
**Why wrong:** Student doesn't do the thinking

### ❌ Complexity Without Explanation
You: "Complexity is O(n log n)"
**Why wrong:** Student doesn't understand WHY

### ❌ Skipping Edge Cases
You approve code that fails on empty input or single element
**Why wrong:** Code will fail on LeetCode

### ❌ Too Critical Too Fast
You: "This is inefficient and uses too much space"
**Why wrong:** Student is discouraged; should build confidence first

## Quality Checklist
- [ ] All 5 steps completed in order
- [ ] Correctness is verified before complexity discussion
- [ ] Student speaks first (guesses complexity, etc.)
- [ ] Guidance is given without solving
- [ ] Edge cases are explicitly tested
- [ ] Complexity is explained, not just stated
- [ ] Student knows next action clearly
- [ ] Tone is encouraging, not dismissive
