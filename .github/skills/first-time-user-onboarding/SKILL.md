---
name: "first-time-user-onboarding"
description: "Use when: a new student is using the agent for the first time. Extract their DSA interest, suggest a matching project, create a phased roadmap, and set up memory/context for future sessions."
reference-skills: ["strivers-dsa-roadmap-reference", "scaffolding-boilerplate-manager"]
---

# First-Time User Onboarding

## Goal
Convert a student's vague DSA interest ("I want to learn graphs") into a **complete learning environment** with:
- Project folder structure
- Starter code files
- Documentation
- 3-phase roadmap with LeetCode problems
- Memory profile for future sessions

**Result:** Student starts mentorship immediately. Everything is pre-set-up.

**Key Resources:** 
- **STRIVER'S DSA ROADMAP REFERENCE** for LeetCode problems
- **SCAFFOLDING & BOILERPLATE MANAGER** for file/folder setup

## The Onboarding Workflow

### Step 1: Discover Their DSA Interest

**Your job:** Understand what DSA concept(s) they want to learn.

**How to ask:**
```
What DSA topic interests you most? (Examples: Graphs, Trees, Dynamic Programming, 
Linked Lists, Heaps, Sorting algorithms, etc.)

Also: Why does it interest you? (Curiosity, job prep, specific problem, etc.)
```

**What to listen for:**
- Primary topic (e.g., "Graphs")
- Secondary topics they mention (e.g., "and maybe searching")
- Motivation (learning for fun vs. interview prep vs. real project)
- Experience level (completely new vs. "I know the theory but can't code it")

### Step 2: Understand Their Project Context

**Your job:** Decide if they have an existing project or need a suggested one.

**Two scenarios:**

#### Scenario A: They Have a Real Project
```
Great! Tell me about your project:
- What does it do?
- Where would this DSA concept fit in?
- Example: "I'm building a task scheduler. I need graphs for task dependencies."
```
→ Use THEIR project as the learning context.

#### Scenario B: They Don't Have a Project Yet
```
No problem! I'll suggest a project to make this concrete and fun.
Based on [DSA topic] and [motivation], here's what I'm thinking:

[Project Concept] — [Why this specific project]

**Why this works:**
- Teaches [DSA topic] naturally
- Fun to build (visual/interactive/useful)
- Can extend later into a real system

Does this sound good? Want to adjust?
```

### Step 3: Design Their Roadmap

**Your job:** Create a phased plan to go from 0 → mastery using **STRIVER'S DSA ROADMAP REFERENCE skill**.

**The 3-phase structure (with actual LeetCode problems):**

**Reference:** Look up the student's DSA topic in STRIVER'S DSA ROADMAP REFERENCE to get all relevant LeetCode problems for each phase.

#### PHASE 1: Foundations (2-3 weeks)
**Goal:** Understand the data structure + implement basic operations  
**What they build:** Core data structure + 1-2 basic algorithms + 3-5 LeetCode problems

**Example for Graphs:**
```
PHASE 1: Graph Foundations
- Graph class + adjacency list representation
- BFS + DFS implementations (with TODOs in your project)
- LeetCode problems:
  * 1971: Find if Path Exists in Graph
  * 200: Number of Islands
  * 1020: Number of Enclaves
```

**Example for Linked Lists:**
```
PHASE 1: Linked List Foundations
- Node class + basic insertion/deletion
- Traversal + reversal
- Cycle detection
- LeetCode problems:
  * 206: Reverse Linked List
  * 141: Linked List Cycle
  * 83: Remove Duplicates from Sorted List
```

#### PHASE 2: Problem Solving (3-4 weeks)
**Goal:** Apply the concept to LeetCode problems + project features  
**What they do:** Mix project work + LeetCode for reinforcement (5-7 problems)

**Example for Graphs:**
```
PHASE 2: Real Applications
- Cycle detection (project feature + algorithm)
- Shortest path algorithms
- LeetCode problems:
  * 207: Course Schedule
  * 684: Redundant Connection
  * 1091: Shortest Path in Binary Matrix
  * 994: Rotting Oranges
  * 547: Number of Provinces
  * 785: Is Graph Bipartite?
```

#### PHASE 3: Mastery (2+ weeks)
**Goal:** Independent problem-solving + optimization  
**What they do:** Mostly independent LeetCode (5-10 problems) + advanced project features

**Example for Graphs:**
```
PHASE 3: Advanced & Optimization
- Dijkstra's algorithm, MST algorithms, Topological sorting
- LeetCode problems:
  * 743: Network Delay Time
  * 1135: Connecting Cities With Minimum Cost
  * 210: Course Schedule II
  * 269: Alien Dictionary
  * 1761: Minimum Degree of a Connected Trio in a Graph
  * (+ more hard problems for extended practice)
```

### Step 4: Establish Learning Style Preferences

**Your job:** Understand how THEY learn best.

**Ask:**
```
Quick preferences to personalize your experience:

1. **Project style?** (Data structure library, Game/sim, Web app, etc.)
2. **Explanation style?** (Visual/diagrams, Math/theory, Analogies, Code-first)
3. **Pace?** (Aggressive/fast track, Steady/regular, Flexible/whenever)
4. **LeetCode?** (Yes for streaks, No focus just on project, Mix of both)
```

**Record their answers** for future sessions (ADAPTIVE PACING ORCHESTRATOR uses this).

### Step 5: Create Their Memory Profile

**Your job:** Store everything for cross-session continuity.

**Memory should capture:**
```
## Profile: [Student Name]
**DSA Topic:** Graphs
**Project:** Task Dependency Graph
**Motivation:** Learning for job interviews + building a real system
**Phase:** 1 (Foundations)
**Current Level:** 0 (completely new to graphs)

**Preferences:**
- Explanation style: Visual + code examples
- Pace: Steady (1-2x per week)
- LeetCode: Yes, track streaks

**Roadmap:**
- Phase 1 (Foundations): 3 weeks - Graph class, BFS, DFS, connected components
- Phase 2 (Problems): 3 weeks - Cycle detection, shortest paths, LeetCode
- Phase 3 (Mastery): 2+ weeks - MST, advanced algorithms, independent solving

**Starting point:** We'll begin with Level 1 (heavy scaffolding).
```

### Step 6: Create Starter Code

**Your job:** Use SCAFFOLDING & BOILERPLATE MANAGER to set up their first file.

**What to create:**
- Blank C++ project structure
- The core data structure (Graph class, LinkedList node, etc.)
- One simple function with TODOs for them to start with
- Test harness so they can immediately run code

**Example for Graphs:**
```cpp
#include <vector>
#include <unordered_set>
#include <iostream>
using namespace std;

class Graph {
private:
    vector<vector<int>> adj;
    int vertices;
    
public:
    Graph(int v) : vertices(v), adj(v) {}
    
    void addEdge(int u, int v) {
        // TODO: Add edge from u to v (both directions for undirected graph)
    }
    
    void bfs(int start) {
        // TODO: Implement BFS starting from 'start'
    }
};

int main() {
    Graph g(5);
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    // Test your BFS here
    return 0;
}
```

### Step 7: First Project Task Assignment

**Your job:** Give them their first Level 1 problem to start Phase 1.

**Example opening:**
```
**Starting Task:**

**Why for YOUR project:**
In a task dependency system, you need to represent relationships between tasks.
Graphs do exactly this—each task is a node, dependencies are edges.

**What you're building:**
A Graph class with BFS (Breadth-First Search) to find all tasks reachable 
from a starting task.

**Your implementation:**
I've set up a starter file with the Graph class skeleton. Two TODOs:
1. addEdge() - Add a connection between two tasks
2. bfs() - Traverse all reachable tasks

Fill in those TODOs step-by-step. Think about:
- How to store the edge?
- How to traverse level-by-level?

Code it up and show me what you have!
```

**Then:** Use CODE REVIEW CONDUCTOR to review their first submission.

---

## Full Onboarding Example

### User: "I want to learn graphs"

**Agent Response:**

```
Great choice! Graphs are incredibly practical.

**A few quick questions to set you up properly:**

1. **Why graphs?** (Curious, interview prep, specific project, etc.)
2. **Do you have an existing project where you'd use this?**
   - If yes: Tell me about it!
   - If no: I'll suggest one

3. **Quick style check:**
   - Prefer visual explanations or code-first?
   - Want to track LeetCode streaks?
   - What's your usual pace? (1x/week, daily, flexible?)
```

### User: "Interview prep, no existing project, code-first, yes to LeetCode, 2-3x per week"

**Agent Response:**

```
Perfect! Here's your setup:

**Your Project: "Shortest Route Finder"**
Build a social network graph where you:
- Represent people as nodes, friendships as edges
- Find shortest path between two people (BFS)
- Later: Find all mutual friends (advanced traversal)

Why this? Interviews LOVE graph problems, and "social network" is a real-world 
example that makes graph intuition click.

**Your Roadmap:**

📅 **PHASE 1: Graph Foundations (2-3 weeks)**
- Graph class + adjacency list representation
- BFS implementation
- LeetCode problems for practice:
  * 1971: Find if Path Exists in Graph
  * 200: Number of Islands
  * 1020: Number of Enclaves

📅 **PHASE 2: Problem Solving (3 weeks)**
- DFS (depth-first search)
- More path-finding variants
- LeetCode: 6 medium problems
  * 207: Course Schedule
  * 684: Redundant Connection
  * 1091: Shortest Path in Binary Matrix
  * 994: Rotting Oranges
  * 547: Number of Provinces
  * 785: Is Graph Bipartite?

📅 **PHASE 3: Advanced (2+ weeks)**
- Cycle detection, topological sort
- Dijkstra's algorithm (weighted graphs)
- LeetCode: 5+ hard problems
  * 743: Network Delay Time
  * 1135: Connecting Cities With Minimum Cost
  * 210: Course Schedule II
  * 269: Alien Dictionary
  * (+ more from Striver's sheet)

**Starting Point:**
We'll use Level 1 pacing (heavy scaffolding). I'll explain BFS, you code it.
Then we review complexity, and you solve LeetCode variants.

Ready for Task 1?
```

### Agent then creates:
1. ✅ Memory profile (for next session)
2. ✅ Starter code file (ready to edit)
3. ✅ First task (Level 1 BFS with TODOs)
4. ✅ Project context established
5. ✅ Roadmap visible

---

## Project Suggestion Engine

**How to suggest a matching project:**

| DSA Topic | Suggested Project | Why This Project |
|-----------|-------------------|------------------|
| **Graphs** | Social network / routing system | Natural graph relationships |
| **Trees** | File system / org chart | Hierarchical structure |
| **DP** | Game scoring / resource allocation | Optimal subproblem thinking |
| **Linked Lists** | LRU cache / playlist | Sequential, mutable, O(1) insertion |
| **Heaps** | Task scheduler / priority queue | Always-get-max/min nature |
| **Sorting** | Data visualization / leaderboard | Real-world ordering problems |
| **Hash Tables** | URL shortener / caching | Fast lookup essential |
| **Stacks/Queues** | Browser history / print queue | Natural LIFO/FIFO fit |

**After choosing a project:**
1. Use **STRIVER'S DSA ROADMAP REFERENCE** to look up all problems for that topic
2. Distribute problems across Phase 1 (easy), Phase 2 (medium), Phase 3 (hard)
3. Build a specific roadmap with actual LeetCode problem numbers

**Matching algorithm:**
1. **Core DSA topic** → Pick project that uses it naturally
2. **Motivation** → if "interviews", pick classic problem; if "game", pick visual
3. **Complexity** → Starter project should be fun but not overwhelming
4. **Extensibility** → Can grow into Phase 2 and 3 work

---

## Anti-Patterns to Avoid

### ❌ Too Vague Roadmap
```
WRONG: "Week 1: Learn graphs. Week 2: More graphs. Week 3: Projects."
```
**Why wrong:** Student doesn't know what's actually expected  
**Fix:** Specific tasks with clear outputs (e.g., "Build Graph class with addEdge()")

### ❌ Project Doesn't Match Topic
```
WRONG: Learning graphs but project is "Calculator" (not graph-related)
```
**Why wrong:** Disconnect between theory and practice  
**Fix:** Project MUST naturally use the DSA concept

### ❌ No Starter Code Provided
```
WRONG: "Go create a new C++ file and set up a graph"
```
**Why wrong:** Infrastructure friction, student loses focus  
**Fix:** Provide file ready to edit (use SCAFFOLDING & BOILERPLATE MANAGER)

### ❌ Skipping Memory Setup
```
WRONG: User leaves, comes back, agent says "Tell me about your project again?"
```
**Why wrong:** Lost context, student frustrated  
**Fix:** Immediately save full profile to memory

### ❌ Unclear First Task
```
WRONG: "Implement graphs. Go."
```
**Why wrong:** No guidance, student doesn't know where to start  
**Fix:** Use PROJECT CONTEXT CONNECTOR + Level 1 scaffolding with TODOs

---

## Quality Checklist

- [ ] Discovered their DSA topic and motivation
- [ ] Understood if they have existing project or need suggestion
- [ ] Suggested a project that naturally uses their DSA topic
- [ ] Created a 3-phase roadmap with specific milestones
- [ ] Captured learning style preferences (visual, pace, LeetCode, etc.)
- [ ] Saved full profile to memory for future sessions
- [ ] Created starter code file ready to edit
- [ ] Assigned first Level 1 task with clear TODOs
- [ ] Explained project context (WHY this matters)
- [ ] Student knows exactly what to do next
- [ ] Student knows the full roadmap and phases ahead
- [ ] Ready for first code review once they submit

---

## First Session Checklist for Student

After onboarding is complete, student should have:
- [ ] Clear understanding of their DSA topic
- [ ] A real project concept they're excited about
- [ ] A 3-phase roadmap they can see
- [ ] Starter code file with their first task
- [ ] Level 1 scaffolding ready (TODOs with hints)
- [ ] Project context established
- [ ] Knowledge of how next sessions will work
- [ ] First actual task to start coding

---

## 📁 PROJECT STRUCTURE CREATED (Using SCAFFOLDING & BOILERPLATE MANAGER)

**During onboarding, this folder structure is auto-generated:**

```
[ProjectName]/
├── README.md                    # Project overview + WHY this DSA topic
├── ROADMAP.md                   # 3-phase roadmap with LeetCode problems
├── LEARNING_PROGRESS.md         # Track progress (auto-updated by agent)
├── src/
│   ├── phase1/
│   │   ├── main.cpp             # Phase 1 starter code (with TODOs)
│   │   ├── graph.h              # (Example: depends on topic)
│   │   └── graph.cpp
│   ├── phase2/
│   │   └── (empty, ready for next phase)
│   └── phase3/
│       └── (empty, ready for mastery phase)
├── tests/
│   ├── phase1_tests.cpp         # Test harness for Phase 1
│   ├── phase2_tests.cpp
│   └── phase3_tests.cpp
├── leetcode/
│   ├── problem_1971.cpp         # Phase 1 LeetCode problems
│   ├── problem_200.cpp
│   ├── problem_1020.cpp
│   └── (+ Phase 2 & 3 problems)
├── docs/
│   ├── PROJECT_CONTEXT.md       # Why each algorithm matters for THIS project
│   ├── CONCEPTS.md              # Theory + examples
│   └── COMPLEXITY_ANALYSIS.md   # Track complexity of all solutions
├── notes/
│   └── learning_log.md          # Student writes reflections (auto-saved)
└── .agent-memory.json           # Agent's cross-session memory
```

**What's already filled in:**
- All starter code with TODOs (use SCAFFOLDING & BOILERPLATE MANAGER format)
- Phase 1 problem skeletons (Phase 2/3 empty, ready when needed)
- Test harness ready to run
- Complete documentation explaining project context

**What student does:**
- Fill in TODOs in Phase 1 code
- Solve Phase 1 LeetCode problems
- Add notes to `learning_log.md`

**Agent maintains:**
- `LEARNING_PROGRESS.md` (updated after each session with accomplishments)
- `COMPLEXITY_ANALYSIS.md` (auto-populated after code reviews)
- `.agent-memory.json` (cross-session memory, hidden from student)

---

## Memory Entry Template

Use this as a template when saving the onboarded student's profile:

```markdown
## Profile: [Student Name]

**DSA Topic:** [What they want to learn]
**Project:** [Project name and description]
**Motivation:** [Why they're learning this]
**Phase:** 1 (Foundations)
**Current Level:** [0 = brand new, 1 = knows theory, 2 = some practice]

**Learning Preferences:**
- Explanation style: [Visual, Math, Analogies, Code-first, etc.]
- Pace: [Frequency and intensity]
- LeetCode: [Yes/No, tracking streaks or not]
- Project focus: [Frontend, backend, pure algorithms, etc.]

**Roadmap:**
- **Phase 1 (Foundations):** [Duration and key tasks]
- **Phase 2 (Problem Solving):** [Duration and key tasks]
- **Phase 3 (Mastery):** [Duration and key tasks]

**Key Project Context:**
[How DSA topic connects to their specific project]

**Pacing Notes:**
- Start with: Level 1 (heavy scaffolding)
- Transition to Level 2 when: [Signal]
- Move to Level 3 when: [Signal]

**Project Files Created:**
- Starter code at: `[ProjectName]/src/phase1/main.cpp`
- Test harness at: `[ProjectName]/tests/phase1_tests.cpp`
- Project context doc at: `[ProjectName]/docs/PROJECT_CONTEXT.md`
- LeetCode problems at: `[ProjectName]/leetcode/`

**Next Session:**
Recall project context, check progress on Phase 1, assign next task in roadmap.
```
