> **Note:** This agent system is **still in development** and may break or change as features are added and refined. Use with caution for production writing projects.

# Story Writing & World Building Agent System

A comprehensive multi-agent system designed to support writers in all aspects of story creation, from initial brainstorming through final editing.

## System Overview

This system consists of 11 specialized agents that work together to help writers craft compelling stories and immersive worlds within an Obsidian vault:

### Master Agent
**`master-agent.agent.md`** | User-invocable entry point

The orchestrator and coordinator for the entire system. Routes user requests to appropriate specialists and synthesizes feedback. Start here for most writing tasks. Designed for Obsidian vault organization with awareness of Worldbuilding, Research, and Draft folders.

### Project Setup Agent
**`project-onboarding-agent.agent.md`** | User-invocable

Sets up a complete Obsidian vault structure for new story projects. Creates all folders (Worldbuilding, Research, Draft, Story Planning, etc.), generates starter files, and provides navigation setup. Use this first when starting a fresh story project.

### Specialist Agents (Non-user-invocable, delegated by Master Agent)

1. **Researcher Agent** (`researcher-agent.agent.md`)
   - Historical and cultural research
   - Scientific accuracy and technical details
   - Real-world facts and references
   - Source suggestions and citations

2. **Brainstorming Helper** (`brainstorming-helper.agent.md`)
   - Story concepts and plot ideas
   - Character archetypes and variations
   - World building elements
   - Creative problem-solving

3. **Character Consistency Evaluator** (`character-consistency-evaluator.agent.md`)
   - Character trait verification
   - Motivation alignment
   - Development arc checking
   - Behavioral authenticity

4. **Plot Structure Advisor** (`plot-structure-advisor.agent.md`)
   - Story structure and frameworks
   - Pacing and tension management
   - Plot point mapping
   - Narrative architecture

5. **Worldbuilding Detailer** (`worldbuilding-detailer.agent.md`)
   - Geography and climate
   - Magic/technology systems
   - Cultures and societies
   - History and politics

6. **Dialogue Coach** (`dialogue-coach.agent.md`)
   - Character voice development
   - Dialogue authenticity
   - Subtext and implication
   - Conversation pacing

7. **Continuity Checker** (`continuity-checker.agent.md`)
   - Plot hole detection
   - Timeline verification
   - Consistency checking
   - Logical coherence

8. **Theme & Tone Monitor** (`theme-tone-monitor.agent.md`)
   - Theme identification
   - Tone consistency
   - Emotional resonance
   - Thematic development

9. **Editing & Style Assistant** (`editing-style-assistant.agent.md`)
   - Grammar and style
   - Clarity and readability
   - Prose polish
   - Voice preservation

## How to Use

1. **Start with Master Agent**: Invoke the Master Agent with your writing task
2. **Let it Delegate**: Master Agent will analyze your request and delegate to appropriate specialists
3. **Receive Specialized Help**: Each specialist provides focused expertise on their domain
4. **Synthesize Results**: Master Agent coordinates feedback into actionable guidance

### Example Workflows

- **Starting a new story**: Master Agent → Brainstorming Helper → Plot Structure Advisor
- **Character review**: Master Agent → Character Consistency Evaluator
- **World consistency check**: Master Agent → Worldbuilding Detailer + Continuity Checker
- **Before publication**: Master Agent → Theme & Tone Monitor → Editing & Style Assistant

## Obsidian Vault Structure

This agent system is designed specifically for Obsidian and creates projects with this folder structure:

```
Story Project (Obsidian Vault)/
├── 📋 Index.md (main navigation hub)
├── 📝 Project Brief.md (story overview, genre, audience)
├── 🌍 Worldbuilding/
│   ├── World Overview.md
│   ├── Geography/
│   ├── Cultures & Societies/
│   ├── Magic & Technology/
│   ├── History & Timeline/
│   ├── Events/
│   ├── Characters/ (use "Add New Character" skill to add)
│   ├── Factions/ (use "Add New Faction" skill to add)
│   └── Locations/
├── 🔍 Research/ (for real-world research and references)
├── ✍️ Draft/ (story drafts organized by act/section)
│   ├── Story Outline.md
│   ├── Act 1/
│   ├── Act 2/
│   ├── Act 3/
│   └── Scenes/
├── 📊 Story Planning/
│   ├── Plot Outline.md
│   ├── Character Arcs.md
│   ├── Timeline.md
│   └── Theme & Tone.md
└── 📌 Notes/
```

**Use Project Onboarding Agent to set up this structure automatically for new projects.**

## Skills

Skills provide guided workflows and template creation for specific writing tasks.

### Available Skills

1. **Add New Character** (`add-new-character/SKILL.md`)
   - Creates character folder with template files
   - Generates: Character Profile, Background, Personality, Goals, Relationships, Arc, Appearance, Voice
   - Keeps character documentation organized within Worldbuilding/Characters/
   - **Status**: Scaffold ready (awaiting your exact template specification)

### Planned Skills

- **Project Structure Setup** — Preset Obsidian vault configurations
- **Add New Faction** — Faction folder and documentation templates
- **Create Research Document** — Research entry templates with source tracking
- **Scene Planning** — Guide for outlining scenes with purpose, characters, setting
- **Character Relationship Mapper** — Track character connections and dynamics
- **Timeline Builder** — Create and verify story timeline with events
- **World Bible Generator** — Comprehensive world documentation template
- **Dialogue Scenario Templates** — Common dialogue situations and patterns
- **Writing Prompts Library** — Guided prompts for different story challenges

## Agent Design Principles

Each agent follows these core principles:

1. **Single Focus**: One specialized role with clear boundaries
2. **Minimal Tools**: Only essential tools for their function
3. **Clear Constraints**: Defined what they should NOT do
4. **Keyword-Rich Descriptions**: For effective Master Agent delegation
5. **Specific Output Format**: Consistent, actionable feedback

## Technical Notes

- All agents are `.agent.md` files in the `agents/` directory
- Master Agent can invoke all specialist agents via the `agents` field
- Non-user-invocable agents (except Master) are accessed through Master Agent
- Each agent has focused tool access matching their role
- Descriptions follow the "Use when..." pattern for effective delegation
