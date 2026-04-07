# DSA Learning Mentor System

> Senior DSA mentor helping you learn through building real systems in C++. Smart pacing, project-driven context, and LeetCode integration.

---

## What Is This System?

A complete, production-ready agent system that mentors students learning Data Structures and Algorithms. Instead of isolated algorithm problems, this system connects DSA concepts to real projects—you learn by building.

**Key characteristics:**
- 🎯 **Project-driven:** Every algorithm learned within context of a real application
- 📚 **Adaptive pacing:** Level 1 (heavy scaffolding) → Level 2 (guided) → Level 3 (independent)
- 🧠 **Cross-session memory:** Your progress persists across all conversations
- 🔄 **Integrated LeetCode:** Problem-solving streaks tied to your learning roadmap
- 🛠️ **Automated setup:** First-time users go from "Hi" to coding in 5 minutes

---

## What's Included?

```
dsa-learning-mentor/
├── agents/
│   └── dsa-learning-mentor.agent.md          # Main agent (140 lines, fully modular)
├── skills/                                    # 7 specialized skills
│   ├── first-time-user-onboarding/           # Student discovery + project setup
│   ├── project-context-connector/            # Link DSA concepts to your project
│   ├── adaptive-pacing-orchestrator/         # Choose Level 1, 2, or 3
│   ├── scaffolding-boilerplate-manager/      # Generate project files
│   ├── code-review-conductor/                # Comprehensive 5-step review
│   ├── complexity-analysis-reviewer/         # Time/space complexity focus
│   └── strivers-dsa-roadmap-reference/       # Dynamic LeetCode problems
└── README.md                                  # This file
```

### 7 Core Skills

| Skill | Purpose | When Used |
|-------|---------|-----------|
| **First-Time User Onboarding** | Discover student interest, suggest project, create folder structure, build roadmap | First message from new student |
| **Project Context Connector** | Explain any DSA concept in context of student's specific project | When teaching algorithms (Graphs, Trees, DP, etc.) |
| **Adaptive Pacing Orchestrator** | Decide scaffolding level (1=heavy, 2=guided, 3=independent) based on familiarity | Before each task assignment |
| **Scaffolding Boilerplate Manager** | Auto-generate project folders, function signatures, C++ boilerplate | During project setup and task scaffolding |
| **Code Review Conductor** | 5-step review: correctness → complexity → optimization → refactoring → LeetCode prep | After student submits code |
| **Complexity Analysis Reviewer** | Deep dive into time/space complexity, identify brute force, guide optimization | Every code submission (mandatory) |
| **Striver's DSA Roadmap Reference** | Dynamically fetch relevant LeetCode problems from Striver's A2Z sheet | Building learning roadmaps, assigning practice |

---

## How It Works: The Flow

### First-Time User Journey

```
You: "Hi, I want to learn graphs"
     ↓
Agent: [ONBOARDING SKILL]
  → Discovers you want graph algorithms for a routing system
  → Suggests: "Build a navigation app"
  → Sets up folder: projects/navigation-system/
  → Creates boilerplate files
  → Generates 3-phase roadmap with 20+ LeetCode problems
  → Saves your profile to memory
     ↓
Agent: "Your project is ready! Here's Phase 0..."
     ↓
You: [Solve Level 1 task with heavy scaffolding]
     ↓
Agent: [CODE REVIEW SKILL] → [COMPLEXITY SKILL]
  → Checks correctness
  → Analyzes complexity
  → Suggests optimizations
     ↓
Agent: "Great! Next task..."
     ↓
[Cycle repeats for 3 phases with decreasing scaffolding]
```

### Session 2+: Returning Student

```
You: "Let's continue graphs"
     ↓
Agent: [Loads your profile from memory]
  → "Welcome back! Ready for Phase 1?"
  → Knows your project context, your pace, your progress
     ↓
[Mentorship continues with perfect context]
```

---

## Quick Start

### For Students

1. **Open GitHub Copilot Chat** in VS Code
2. **Type:** `@DSA Learning Mentor` 
3. **Say:** "Hi, I want to learn [topic]" (e.g., "Graphs", "Dynamic Programming", "Binary Search Trees")
4. **Wait:** 5 minutes for complete setup
5. **Start coding:** Follow the Level 1 scaffolding tasks

### For Developers (Customizing This System)

If you want to modify or extend this system:

1. **Agent logic:** Edit [agents/dsa-learning-mentor.agent.md](agents/dsa-learning-mentor.agent.md)
2. **Skills:** Modify specific skills in [skills/](skills/) directory
3. **Adding new skills:** Create a new folder under `skills/` with SKILL.md inside
4. **Testing:** Invoke agent with `@DSA Learning Mentor` and test your changes

---

## 3-Level Pacing System

The system adapts scaffolding based on your familiarity with a topic:

### Level 1: New Concepts (Heavy Scaffolding)
- Complete function signatures provided
- Pseudo-code outline included
- Step-by-step TODO comments
- Multiple hints available
- *Best for:* Learning new algorithms for the first time

### Level 2: Follow-Ups (Guided Discovery)
- Function name + return type provided
- You discover the algorithm approach
- Strategic hints available
- *Best for:* Similar problems after Level 1

### Level 3: Independent (Minimal Scaffolding)
- Problem statement only
- You design the entire solution
- No hints (unless you ask)
- *Best for:* Mastery and LeetCode submissions

---

## Example: Learning Graphs

**Session 1:**
```
You: "I want to learn graphs for a navigation app"

Agent: [ONBOARDING]
→ Sets up: projects/navigation-system/
→ Creates: main.cpp, graph.h, test.cpp
→ Roadmap: BFS basics → DFS basics → Dijkstra → A*
→ 25 LeetCode problems preselected

Agent: "Phase 0: Build your graph data structure"
→ [Level 1: Heavy scaffolding with TODOs]

// graph.h
class Graph {
    // TODO: Implement adjacency list using map + vector
    // Hint: map<int, vector<int>>
    // ...
};

You: [Complete the implementation]

Agent: [CODE REVIEW + COMPLEXITY ANALYSIS]
→ ✅ Correct implementation
→ Time: O(1) add, O(n) traverse
→ Space: O(V + E)
→ Ready for next task!
```

**Session 2:**
```
You: "Let's continue"

Agent: [LOADS MEMORY: "Welcome back! Ready for Phase 1?"]
→ Knows your graph implementation
→ Knows you're learning for navigation
→ Continues with BFS

Agent: "Phase 1: Implement BFS for shortest path"
→ [Level 2: Guided discovery]
→ Provides: `vector<int> bfs(int start, int target);`
→ You discover the algorithm
```

---

## Features & Capabilities

### ✅ What This System Does

- **Full Onboarding:** New students go from cold start to coding in 5 minutes
- **Memory:** Your profiles persist—it remembers your project, progress, pace across sessions
- **Project Context:** Every algorithm taught in context of YOUR project (not generic)
- **Adaptive Difficulty:** Scaffolding adjusts based on your familiarity
- **Code Review:** 5-step structural review after each submission
- **Complexity Analysis:** Mandatory deep-dive into time/space complexity
- **LeetCode Integration:** 25+ problems per DSA topic, properly sequenced
- **All DSA Topics:** Graphs, Trees, DP, Arrays, Heaps, Stacks, Queues, Sorting, Searching, etc.

### ❌ What This System Doesn't Do

- Replace competitive programming coaching (LeetCode coaching is secondary)
- Solve problems for you (scaffolding guides, doesn't auto-complete)
- Support languages other than C++ (by design—full control needed)
- Work without project context (always connected to a real application goal)

---

## Integration Points

### Memory System

This system integrates with persistent memory to store:
- Student profile (name, DSA interests, pace)
- Project information (project name, goal, context)
- Current learning phase (Phase 0, 1, 2)
- Progress tracking (problems completed, complexity mastery)

**Example memory stored:**
```
Student: Sanskar
Interest: Graph algorithms for routing systems
Project: NavigationSystem
Phase: 1 of 3
Pace: Level 1 (moderate scaffolding)
Progress: BFS complete, DFS 50%, ready for Dijkstra
```

### LeetCode Integration

Striver's A2Z DSA Sheet is dynamically fetched (not hardcoded):
- Always up-to-date problem lists
- Problems sequenced by difficulty
- Linked to your roadmap

---

## For System Developers

### Adding a New Agent System

If you want to create another system (e.g., `Writing Coach`, `Design Critic`):

1. Create folder: `agent-systems/[new-system]/`
2. Inside, create:
   ```
   agents/
   ├── [new-system].agent.md
   skills/
   └── [skill-name]/
       └── SKILL.md
   README.md
   ```
3. Follow the modular pattern: Agent coordinates, Skills execute
4. Document the skills and flow in the system README

### Sharing Skills Between Systems

Keep reusable skills in `.github/skills/` if they apply across systems. System-specific skills go in `agent-systems/[system]/skills/`.

---

## Troubleshooting

**Q: The agent doesn't remember me**
- A: First-time? Complete the onboarding process. On return, make sure you're using `@DSA Learning Mentor` agent.

**Q: I'd like different scaffolding level**
- A: Tell the agent "I want Level 3 scaffolding" or "Use Level 1 with more hints"

**Q: How do I customize the learning roadmap?**
- A: After onboarding, ask the agent to modify your roadmap. Changes persist in memory.

**Q: Can I use languages other than C++?**
- A: Not currently. This system is built around C++ for control and performance learning. You're welcome to adapt it!

---

## Philosophy

This system embodies a belief about learning DSA:

> **Don't learn algorithms in isolation. Learn them by building something real.**

When you implement graph algorithms for a routing system, or dynamic programming for a game, the concepts stick. The system scaffolds heavily at first, then gradually removes training wheels as you master concepts.

---

## Next Steps

1. **Jump In:** Open Copilot Chat → `@DSA Learning Mentor` → Start learning
2. **Customize:** Edit skills to match your teaching style
3. **Extend:** Add more evaluation criteria, different pacing models, etc.
4. **Share:** Use this template to create other agent systems!

---

*Last updated: Built as a fully modular, skill-based system for maximum reusability and flexibility.*
