# My Agents Repository

Hi! I'm TheFakeCreator, a developer, student, writer, story builder, graphic designer, and an active learner. Because I'm always exploring new domains and juggling a variety of creative and technical projects, I frequently need assistance with highly specific and niche tasks.

This repository is my personal playground for experimenting with the AI agent ecosystem. Here, you'll find all sorts of agents, skills, and prompts that I've personally used, tested, and refined to fit my workflow. Some are polished and reliable, while others are experimental ideas I'm still iterating on.

Think of this as my open notebook—a collection of custom tools that help me work smarter across multiple disciplines.

Unlike generic AI agents, **everything here is designed to evolve and improve itself through your feedback**—you're not just using static tools; you're building tools that grow with you.

---

## Quick Start

**TL;DR:** Clone this repo → Pick an agent that matches your needs → Copy it to `.github/agents/` in your project → Start using and personalizing it.

---

## Table of Contents

- [My Agents Repository](#my-agents-repository)
  - [Quick Start](#quick-start)
  - [Table of Contents](#table-of-contents)
  - [What's Inside?](#whats-inside)
  - [Structure](#structure)
  - [Example Agent: DSA Learning Mentor](#example-agent-dsa-learning-mentor)
  - [How I Use This Repo](#how-i-use-this-repo)
  - [How To Use These For Yourself](#how-to-use-these-for-yourself)
    - [Step 1: Take What Resonates](#step-1-take-what-resonates)
    - [Step 2: Fork or Copy \& Customize](#step-2-fork-or-copy--customize)
    - [Step 3: Test in Your Workflow](#step-3-test-in-your-workflow)
    - [Step 4: Iterate \& Refine](#step-4-iterate--refine)
    - [Step 5: Build Your Own Ecosystem](#step-5-build-your-own-ecosystem)
    - [Pro Tips](#pro-tips)
    - [Where to Start](#where-to-start)
  - [How I Actually Use This In Practice](#how-i-actually-use-this-in-practice)
    - [My Workspaces](#my-workspaces)
    - [Why VS Code?](#why-vs-code)
    - [My Setup Pattern](#my-setup-pattern)
    - [My Workflow](#my-workflow)
    - [Example](#example)
  - [Key Lessons Learned](#key-lessons-learned)
    - [There's No One-Size-Fits-All](#theres-no-one-size-fits-all)
    - [Personalization is Key](#personalization-is-key)
    - [The Real Work is in the Details](#the-real-work-is-in-the-details)
  - [Future Plans](#future-plans)
  - [Philosophy](#philosophy)

---

## What's Inside?

- **Agents** (`agents/`) — Autonomous or semi-autonomous assistants tailored for my unique needs—coding, writing, design, learning, and more. Each agent has a specific purpose and personality.
- **Skills** (`skills/`) — Modular capabilities and workflows that enhance agents or can be reused across different tasks. Think of these as power-ups for AI interactions.
- **Prompts** (`prompts/`) — Instruction sets, templates, and prompt engineering assets that I've crafted and tested. Reusable patterns that just work.

---

## Structure

```
agents/
├── .github/
│   ├── agents/              # Agent definitions
│   │   └── dsa-learning-mentor.agent.md
│   ├── skills/              # Skill modules (in development)
│   └── prompts/             # Prompt templates
└── README.md                # This file
```

---

## Example Agent: DSA Learning Mentor

One of my favorite agents is the **DSA Learning Mentor**. Here's what makes it special:

- **Smart Pacing**: Adapts guidance based on whether you're learning something new or reinforcing familiar concepts
- **Project-Driven**: Encourages building real systems rather than solving isolated problems
- **LeetCode Integration**: Solves problems both on your project AND on LeetCode to maintain streaks
- **Focus on Understanding**: Provides hints and guidance, not complete solutions

This agent has been tested extensively and has become a core part of my DSA learning workflow.

---

## How I Use This Repo

1. **Creating New Agents** — When I discover a new workflow that needs automation, I add it as a new agent to `.github/agents/`
2. **Building Skills** — Reusable patterns and workflows go into `.github/skills/` so they can be shared across agents
3. **Sharing Prompts** — Effective prompt templates and instructions go into structured files for future reference
4. **Iterating & Adapting** — Everything here is constantly refined based on real usage and feedback

The key is that every addition is battle-tested before it makes it into this repo.

---

## How To Use These For Yourself

Found something useful here? Great! Here's how to adapt this repository for your own needs:

### Step 1: Take What Resonates
- Browse through the agents and prompts
- Identify which ones align with your workflow or interests
- Don't feel pressured to use everything—be selective

### Step 2: Fork or Copy & Customize
- Copy the agent or prompt that interests you
- Modify it to fit YOUR personal style, preferences, and specific needs
- Change terminology, adjust the tone, update examples—make it yours

### Step 3: Test in Your Workflow
- Use the agent/skill/prompt in a real project or task
- Pay attention to what works and what doesn't
- Document your experience

### Step 4: Iterate & Refine
- Update the agent file with your feedback and learnings
- Notice patterns in how the agent behaves
- Fine-tune the instructions based on real usage
- Create memory notes or agent profiles to track what works for you

### Step 5: Build Your Own Ecosystem
- As you refine agents, start creating your own
- Build skills tailored to YOUR unique combination of interests and projects
- Keep track of what works for documentation
- Share back if you have improvements!

### Pro Tips

- **Start small** — Don't try to use all agents at once. Pick one and master it.
- **Personalize from day one** — Don't wait for perfection. Update agent files with your preferences immediately.
- **Document as you go** — Keep notes on what you learn, what works, and what doesn't.
- **Create feedback loops** — After using an agent, spend 2-3 minutes updating it based on what you learned.
- **Mix and match** — Combine skills from different agents to create new workflows tailored to your needs.

### Where to Start

1. Try the **DSA Learning Mentor** if you're learning programming concepts
2. Explore the agent files to understand the format and structure
3. Pick the agent closest to one of your current projects
4. Fork it, modify it, and make it your own

Remember: The goal isn't to use my agents exactly as they are. The goal is to understand how to build an AI assistant ecosystem that works specifically for you.

---

## How I Actually Use This In Practice

I don't use everything in one place. My workflow is distributed across multiple tools, but the constant is **VS Code**—it's where all the AI magic happens for me.

### My Workspaces

- **Obsidian** — For academics, thoughts, writings, personal notes, and knowledge management
- **VS Code** — For programming, project work, and AI interactions (the nerve center of my setup)
- **Connection** — I use a plugin to open my Obsidian vault in VS Code and switch between both seamlessly

### Why VS Code?

VS Code is where I've anchored this entire ecosystem because:

1. **Top-tier GitHub Copilot Integration** — Built-in access to state-of-the-art models (Claude, OpenAI, etc.)
2. **Agents & Skills Work Best Here** — The `.github/agents/` and `.github/skills/` files integrate naturally with VS Code's capabilities
3. **Free (or nearly free)** — VS Code is free, and GitHub Copilot is free for students (plus affordable for professionals)
4. **Programmer-Friendly** — As a developer, I'm naturally in VS Code most of the time, so this is my natural command center

**Recommendation:** Even if you're not primarily a programmer, I highly recommend VS Code as your AI assistant hub. It's genuinely the best software you can get for free, and with a GitHub Copilot subscription (especially if you're a student), it becomes an unbeatable tool.

### My Setup Pattern

Every new environment I create—whether it's a learning project, a writing space, or an experimental workspace—follows the same pattern:

```
project-name/
├── README.md          # Entry point for understanding the project
├── .github/
│   ├── agents/        # Custom agents for this project
│   ├── skills/        # Reusable skills
│   └── prompts/       # Project-specific prompts
├── [project files]
└── [other structure]
```

This structure is consistent whether the project goes on GitHub or not. The `README.md` and `.github/` folder are always the entry points for agents and skills in VS Code.

### My Workflow

1. **Set up the environment** — Create the `.github/agents/` and `.github/skills/` folders
2. **Add agents and skills** — Place the relevant agents/skills files there
3. **Tell them what I need** — Describe my workflow and ask them to help
4. **Feedback loop** — If an agent or skill isn't working as intended, I tell them explicitly
5. **They improve themselves** — I ask the AI to update its own agent file or skills file accordingly, based on our conversation

This creates a **feedback cycle where the tools literally learn and improve themselves** based on how I'm using them.

### Example

When I set up a new DSA learning project:
- I copy the DSA Learning Mentor agent to `.github/agents/`
- I work through problems with it
- If it's not pacing correctly or giving too many hints, I tell it: "This pacing isn't right for me; update your agent file to match what works better"
- The agent updates itself
- Next time I use it, it remembers and adapts

This self-improving ecosystem is the real power—you're not just using static tools; you're building tools that evolve with you.

---

## Key Lessons Learned

### There's No One-Size-Fits-All

Through extensive tweaking and experimenting, I've learned that there is no magical way to adopt someone else's workflow and expect it to work perfectly for you. Early on, I would ask AI to create agents for me and expect them to magically solve all my problems. That's not how this works.

### Personalization is Key

Everyone has unique interests, tastes, and workflows. For agents, skills, and prompts to truly work for you, you have to:

1. **Tailor them to your preferences** — Don't use agents as-is; adapt them to your style
2. **Give yourself adaptation time** — These tools need time to mesh with your workflow
3. **Keep them updated** — When you teach an agent something new, update its agent file or memory to reflect your learnings
4. **Iterate constantly** — This is how you build an AI ecosystem that genuinely fits you

### The Real Work is in the Details

- Don't expect instant perfection
- Experiment freely but document what works
- Share failures and successes equally
- Let your agents and skills evolve with your growth

---

## Future Plans

- Expand the skills library for more domains (writing, storytelling, design, ML, etc.)
- Add more specialized agent templates for my evolving needs
- Document best practices and detailed case studies from real-world usage
- Create templates for others to build their own personalized agent ecosystems

---

## Philosophy

This repository represents my belief that **AI tools should work for YOU, not the other way around**. It's okay to have an opinionated, personalized setup. In fact, it's necessary. Your workflow, your taste, your agents—build them with intention.

---

**This repository is always evolving as I learn, experiment, and build. If you stumble upon it, feel free to explore, get inspired, or adapt ideas for your own ecosystem!**

---

**Author:** [TheFakeCreator](https://github.com/TheFakeCreator) | [@TheFakeCreator on GitHub](https://github.com/TheFakeCreator)
