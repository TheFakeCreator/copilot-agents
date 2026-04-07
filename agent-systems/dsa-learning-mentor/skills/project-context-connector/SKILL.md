---
name: "project-context-connector"
description: "Use when: teaching any DSA concept and need to connect it to a student's specific project. Explains general purpose, project relevance, future applications, and concrete examples. Works for Graphs, Linked Lists, Trees, DP, etc."
---

# Project Context Connector

## Goal
Always frame DSA concepts in the context of the student's specific project BEFORE explaining general theory. This ensures they understand WHY they're learning something, not just HOW.

## When to Use
- Before teaching any new algorithm (Level 1)
- Before introducing a problem (Level 2)  
- When student asks "Why do I need to learn this?"
- When explaining LeetCode problems

## The 4-Step Formula

1. **General Purpose** — What does this algorithm/concept fundamentally do?
2. **Project Relevance** — How does it fit into THEIR specific system?
3. **Future Applications** — Where will they use it in which phases?
4. **Concrete Example** — Give a specific scenario from THEIR project

## Templates

### For New Algorithms (Level 1):

```
**Why [Algorithm] matters for YOUR project:**

**Purpose:** [algorithm fundamentally does]

**In your system:** [Where/how they'll use it]

**Future phases:** [When they'll encounter it again]

**Concrete example from YOUR project:**
[Specific scenario - "When you [project action], you need [algorithm] because [reason]"]
```

### For LeetCode Problems (Level 2):

```
**Why this problem for YOUR project:**
[Try to connect it to the project. If weak: "Reinforces [concept] which you'll use in [Phase X]"]

**Connection to your system:**
This is similar to [what they built] but with: [key difference]
```

## Examples

### Graph DFS:
```
**Purpose:** DFS explores every path from a node to find all reachable nodes

**In your system:** When a task is marked complete, you need to traverse ALL dependent tasks and update them

**Future phases:** Phase 2 (cycle detection), Phase 3 (scheduling optimization)

**Concrete example:**
Task A → Task B → Task C (dependencies). When A completes, you DFS to B then C to cascade updates.
```

### Dynamic Programming:
```
**Purpose:** DP solves overlapping subproblems by storing results to avoid recalculation

**In your system:** Finding the cheapest route between cities will recalculate the same subpaths repeatedly

**Future phases:** Phase 3 performance optimization (making your pathfinding 100x faster)

**Concrete example:**
Paths A→B→C and A→B→D both solve "A to B". DP stores it once, reuses it instead of recalculating.
```

### Linked Lists:
```
**Purpose:** Fast O(1) insertion/deletion at ANY position without shifting

**In your system:** Your LRU Cache needs to move accessed items to "most recent" without array overhead

**Future phases:** Cache optimization, memory efficiency

**Concrete example:**
Access item at position 5: remove from pos 5 + insert at pos 1 (both O(1) with linked list, would be O(n) with array)
```

## What NOT to Do
❌ Start with theory: "DFS is a graph traversal algorithm..."  
✅ Start with context: "In your task manager, when you mark a task complete, you need to..."

❌ Generic examples: "Imagine a maze..."  
✅ Project examples: "In YOUR task dependency graph..."

## Quality Checklist
- [ ] Project-specific, not generic
- [ ] Connects to real use case in their system
- [ ] Explains why NOW (immediate phase) and why LATER (future phases)
- [ ] Includes concrete example they can visualize
- [ ] Student understands "I'll need this for X"
