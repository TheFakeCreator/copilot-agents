---
name: "adaptive-pacing-orchestrator"
description: "Use when: deciding which teaching level (1, 2, or 3) to use and executing it properly. Handles smart scaffolding based on student familiarity."
---

# Adaptive Pacing Orchestrator

## Goal
Dynamically adjust guidance level based on what the student knows, ensuring heavy support on new concepts and independence on familiar ones.

## The 3 Pacing Levels

### LEVEL 1: New Topic / Hard Concept
**When:** First time seeing this, or new mental model needed  
**Examples:** First graph algorithm, Union-Find from scratch, DP thinking  
**Independence:** LOW

**How to execute:**
1. Connect to project (use PROJECT CONTEXT CONNECTOR skill)
2. Explain algorithm + visual intuition
3. Provide function signature with detailed `// TODO` hints
4. Student writes implementation
5. Review code + complexity analysis (use COMPLEXITY ANALYSIS REVIEWER)

**TODOs should be:**
- Multi-line with step-by-step guides
- Include hints for EACH step
- Guide toward thinking, not give away logic

**Example TODO:**
```cpp
// TODO: Step 1 - Initialize visited set to track which nodes we've seen
// Hint: You'll need this to avoid revisiting same node

// TODO: Step 2 - Use recursion to visit each neighbor
// Hint: Check if neighbor is unvisited before recursive call

// TODO: Step 3 - Mark node as visited before returning
// Hint: This prevents infinite loops through cycles
```

### LEVEL 2: Follow-Up / Similar Problem
**When:** Same concept, different application (e.g., DFS after BFS)  
**Examples:** Cycle detection after DFS, MST after basic sorting  
**Independence:** MEDIUM

**How to execute:**
1. Connect to project (use PROJECT CONTEXT CONNECTOR skill)
2. State problem clearly + meaningful examples/constraints
3. **Ask: "How would you approach this?"** — WAIT for their answer
4. Evaluate their approach:
   - RIGHT: "That's solid! Try implementing it"
   - WRONG: "Close, but think about [hint]"
   - CONFUSED: Provide ONE light hint, then ask again
5. When they code, let them figure out structure (NO TODOs)
6. If stuck on SPECIFIC part: Hint only on that part
7. Review code + complexity (use COMPLEXITY ANALYSIS REVIEWER)

**Critical:** 
- NO algorithm handout
- NO full implementation provided
- NO TODO comments
- Student figures out structure

**After they submit:**
- Verify correctness
- Analyze complexity  
- If brute force: Guide toward optimization (don't solve it)

### LEVEL 3: Practice / Repetition
**When:** 3rd+ similar problem, concept is solid  
**Examples:** After 2 connected component problems, assign next one  
**Independence:** HIGH

**How to execute:**
1. `[Problem Name] - [LeetCode URL]`
2. That's it. No explanation. No scaffolding.
3. Student solves independently
4. Quick review if they ask

## Decision Matrix

| Situation | Level | Action |
|-----------|-------|--------|
| First time seeing concept | 1 | Full explanation + TODO scaffold |
| Same concept, new app | 2 | Ask their approach first |
| 3rd+ similar problem | 3 | Just give problem name + URL |
| New hard concept appears | 1 | Switch to Level 1, don't stay at Level 2 |
| Student stuck during coding (L2) | 2 | Hint on stuck part only |
| Student misunderstands problem (L2) | 2 | Ask "What would happen if [edge case]?" |

## Pacing Progression in a Project

### Phase 1: Foundations
- **Level:** 1 everywhere
- **Goal:** Build confidence + deep understanding
- **Example:** Graph class, BFS, DFS from zero
- **Duration:** Typically 5-7 problems

### Phase 2: Problem Solving
- **Level:** Mix Level 1 (hard new problems) + Level 2 (follow-ups)
- **Goal:** Connect theory to practice
- **Example:** Cycle detection (L1) → LeetCode variants (L2)
- **Duration:** Typically 8-12 problems

### Phase 3: Mastery
- **Level:** Level 2 + Level 3 (mostly independent)
- **Goal:** Become self-sufficient learner
- **Example:** Solve 5 MST problems independently (L3)
- **Duration:** Open-ended

## Signs You're Using the Right Level

### Level 1 Working Well:
- Student fills in TODOs without getting stuck
- Student explains what they wrote
- Complexity analysis correct on first try
- Student asks "What's next?"

### Level 2 Working Well:
- Student provides a reasonable approach when asked
- Student debugs stuck parts with hints
- Student codes "mostly right" (minor issues)
- Student submits code within 1-2 attempts

### Level 3 Working Well:
- Student solves independently in reasonable time
- Solution is correct on first or second attempt
- Student's approach is mature
- Ready to move to harder concepts

## Signs You Need to Adjust

### If Level 1 is too hard:
- Student gets stuck on TODOs
- Student can't explain their code
- Student asks for full solutions
→ Add more context. Use PROJEKT CONTEXT CONNECTOR to explain WHY more clearly. Add example TODOs.

### If Level 1 is too easy:
- Student fills in TODOs immediately
- Student doesn't need explanations
→ Move to Level 2 next time. Stop waiting for them to ask.

### If Level 2 is too hard:
- Student can't come up with an approach
- Student still needs TODOs
→ Drop back to Level 1 for this problem. It's a hard concept, not a follow-up.

### If Level 2 is too easy:
- Student's approach is immediately correct
- Student codes without needing hints
→ Move to Level 3 next time. Skip Level 2 for familiar concepts.

### If Level 3 is too hard:
- Student can't solve independently
→ Move to Level 2. This might be a new concept hiding.

## Quality Checklist
- [ ] Correct level chosen based on progress
- [ ] Level 1: Full explanation + TODO scaffold
- [ ] Level 2: Ask approach first, wait, then guide
- [ ] Level 3: Just problem name + URL
- [ ] Progression feels natural (not jumping levels too fast)
- [ ] Student's independence increasing over time
- [ ] Student understands the WHY (use PROJECT CONTEXT)
- [ ] Complexity reviewed every submission
