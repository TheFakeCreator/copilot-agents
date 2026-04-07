---
name: "strivers-dsa-roadmap-reference"
description: "Reference skill containing all DSA topics and their associated LeetCode problems from Striver's A2Z sheet. Use when building learning roadmaps for first-time users."
---

# Striver's DSA Roadmap Reference

## Goal

**The agent dynamically fetches the latest DSA problems from Striver's A2Z Sheet** instead of maintaining a static list that gets outdated.

When building a roadmap for a student, the agent:
1. Fetches current data from https://takeuforward.org/dsa/strivers-a2z-sheet-learn-dsa-a-to-z
2. Extracts all DSA topics and their associated LeetCode problems
3. Organizes problems by difficulty (Easy, Medium, Hard)
4. Distributes across 3 phases (Foundations, Problem Solving, Mastery)
5. Returns fresh, up-to-date problem list for the student's roadmap

---

## HOW THE AGENT FETCHES DATA

### Step 1: Fetch the Striver's Sheet

**The agent calls:**
```
fetch_webpage(
  url: "https://takeuforward.org/dsa/strivers-a2z-sheet-learn-dsa-a-to-z",
  query: "DSA topics, LeetCode problems, problem difficulty, links"
)
```

**Returns:** Complete HTML/content of the sheet with all topics and problems.

---

### Step 2: Parse & Extract Data

**The agent extracts:**

```
For each DSA topic in the sheet:
├─ Topic name (e.g., "Graphs", "Trees", "DP")
├─ Problem list with:
│  ├─ LeetCode problem number
│  ├─ Problem title
│  ├─ Difficulty (Easy, Medium, Hard)
│  ├─ Link to problem
│  └─ Related concept/subtopic
└─ Any category/section info
```

**Example of what gets extracted:**

```
Topic: "Graphs"
  Problems:
    - 1971: Find if Path Exists in Graph (Easy)
    - 200: Number of Islands (Medium)
    - 207: Course Schedule (Medium)
    - 743: Network Delay Time (Hard)
    - ...more problems
```

---

### Step 3: Organize by Phase

**The agent automatically distributes problems:**

```
Phase 1 (Foundations):
  ├─ Easy problems (3-5)
  ├─ Concept introduction problems
  └─ Focus: Understanding basics

Phase 2 (Problem Solving):
  ├─ Mix of Medium problems (5-7)
  ├─ Re-application of concepts
  └─ Focus: Practical application

Phase 3 (Mastery):
  ├─ Hard + some medium problems (5-10)
  ├─ Complex variations
  └─ Focus: Optimization & independence
```

---

## HOW TO USE IN ONBOARDING

### When Student Says: "I want to learn Graphs"

**The agent (using FIRST-TIME USER ONBOARDING):**

1. **Fetch fresh data:**
   ```
   Fetch Striver's sheet → Extract all "Graphs" problems
   ```

2. **Categorize by difficulty:**
   ```
   Easy:   [1971, 200, 1020, ...]
   Medium: [207, 684, 1091, 994, 547, 785, ...]
   Hard:   [743, 1135, 210, 269, 1761, ...]
   ```

3. **Distribute to phases:**
   ```
   Phase 1: Easy problems (3-5)
   Phase 2: Medium + some easy (5-7)
   Phase 3: Hard + medium variants (5-10)
   ```

4. **Build roadmap:**
   ```
   PHASE 1: Foundations (2-3 weeks)
   - LeetCode 1971: Find if Path Exists in Graph
   - LeetCode 200: Number of Islands
   - LeetCode 1020: Number of Enclaves
   
   PHASE 2: Problem Solving (3 weeks)
   - LeetCode 207: Course Schedule
   - LeetCode 684: Redundant Connection
   - ... (5-7 medium problems)
   
   PHASE 3: Mastery (2+ weeks)
   - LeetCode 743: Network Delay Time
   - ... (5-10 hard problems)
   ```

5. **Return to FIRST-TIME USER ONBOARDING** with complete, up-to-date roadmap

---

## DATA EXTRACTION LOGIC

### Pseudo-Code (What Agent Executes)

```python
def get_dsa_roadmap(topic_name):
    # 1. Fetch Striver's sheet
    sheet_content = fetch_webpage(
        url="https://takeuforward.org/dsa/strivers-a2z-sheet-learn-dsa-a-to-z",
        query=f"DSA topic: {topic_name}, LeetCode problems"
    )
    
    # 2. Extract all problems for this topic
    problems = extract_problems_for_topic(sheet_content, topic_name)
    
    # 3. Sort by difficulty
    easy = [p for p in problems if p.difficulty == "Easy"]
    medium = [p for p in problems if p.difficulty == "Medium"]
    hard = [p for p in problems if p.difficulty == "Hard"]
    
    # 4. Distribute across phases
    phase1_problems = easy[0:5] + medium[0:2]  # 3-5 easy, maybe 1-2 medium
    phase2_problems = medium[2:9] + hard[0:2]  # 5-7 medium, 1-2 hard
    phase3_problems = hard[2:] + medium[9:]    # Rest of hard, leftover medium
    
    # 5. Return structured roadmap
    return {
        "topic": topic_name,
        "phase1": phase1_problems,
        "phase2": phase2_problems,
        "phase3": phase3_problems
    }
```

---

## BENEFITS OF THIS APPROACH

✅ **Always Fresh** — No outdated problem lists  
✅ **Single Source of Truth** — Data comes directly from Striver's sheet  
✅ **Automatic Updates** — When Striver adds/removes problems, agent sees them  
✅ **Scalable** — Any DSA topic, not just 15 hardcoded ones  
✅ **No Maintenance** — Don't need to manually update problem lists  
✅ **Current Links** — All LeetCode links are guaranteed current  

---

## FALLBACK (If Fetch Fails)

**If agent can't fetch the URL (network, page changes, etc.):**

Then use this static reference data as backup. The skill will contain a **minimal curated set** of 5-10 most common problems per topic per phase, just for emergencies:

```
Topics covered (fallback only):
- Graphs
- Trees  
- Linked Lists
- Dynamic Programming
- Arrays & Strings
(... minimal set, ~30-50 problems total, not exhaustive)
```

**But primary flow:** Always try to fetch first, use fallback only if needed.

---

## How Agent Uses This Skill

**In FIRST-TIME USER ONBOARDING:**

```python
# When onboarding a new student:
def onboard_student(topic):
    # Step 1: Get fresh roadmap
    roadmap = fetch_striver_roadmap(topic)  # This skill does this
    
    # Step 2: Create project structure
    # (SCAFFOLDING & BOILERPLATE MANAGER)
    
    # Step 3: Assign problems
    phase1 = roadmap.phase1_problems
    → Create problem skeleton files
    → Add them to project/leetcode/
    
    # Step 4: Save to memory
    student_profile.roadmap = roadmap
    
    # Return: Fresh roadmap with latest problems
```

---

## CONFIGURATION

The agent should fetch data:
- **On first-time user onboarding** → Always fetch fresh
- **On roadmap rebuild** → Fetch to update
- **On new phase start** → Fetch to ensure latest problems

**Cache Duration:** Optional (if performance matters)
- Could cache for 24 hours to avoid hammering the website
- But always allow manual refresh option

---

## What The Skill Contains

**NOT:** A hardcoded list of all problems (gets outdated)

**YES:** 
- How to fetch from Striver's sheet
- How to extract topic + problems
- How to categorize by difficulty
- How to distribute across phases
- Fallback static data (optional, for emergencies)

**Result:** Dynamic, always-current problem roadmaps

