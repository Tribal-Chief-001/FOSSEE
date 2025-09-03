# 🚀 FOSSEE Python Screening Task 2: AI Debugging Assistant Prompt

![FOSSEE](https://fossee.in/images/logo.png)  

**Author:** Nikhil & SOTA AI Commentary  
**Internship:** FOSSEE Semester Internship — Autumn 2025  
**Task:** Python Screening Task 2 — Write a Prompt for an AI Debugging Assistant  

---

## 📌 Table of Contents

1. [Overview](#overview)  
2. [Project Structure](#project-structure)  
3. [Prompt Details](#prompt-details)  
   - [Role of AI](#role-of-ai)  
   - [Operating Principles](#operating-principles)  
   - [Structured Response Framework](#structured-response-framework)  
   - [Skill-Level Adaptation](#skill-level-adaptation)  
   - [Dual-Format Implementation](#dual-format-implementation)  
4. [White Paper](#white-paper)  
5. [Usage Instructions](#usage-instructions)  
6. [Design Rationale (Summary)](#design-rationale-summary)  
7. [Contact](#contact)  

---

## Overview

This repository contains the **final submission** for **FOSSEE Python Screening Task 2**. The task requires designing a **pedagogically robust AI prompt** that:

- Analyzes a student’s buggy Python code  
- Offers constructive suggestions and hints  
- Avoids revealing the correct solution  
- Adapts to learner skill levels: Beginner, Intermediate, Advanced  

This project includes:

- **Markdown prompt** for human readability  
- **JSON prompt** for machine integration  
- **10-page white paper PDF** detailing the design, pedagogy, and reasoning  

---

## Project Structure

FOSSEE_Task2/
│
├── README.md                                 # Project description & instructions
├── AI_Debugging_Prompt.md                    # Final prompt (Markdown)
├── AI_Debugging_Prompt.json                  # Final prompt (JSON)
└── AI_Debugging_Assistant_WhitePaper.pdf    # 10-page research paper with rationale

## Prompt Details

### Role of AI

The AI acts as a **mentor and guide**, providing reflective hints, diagnostics, and conceptual nudges **without giving direct solutions**. The goal is to **enhance learning while preserving learner autonomy**.

### Operating Principles

- Supportive, encouraging, and non-judgmental tone  
- Avoid providing full code solutions  
- Encourage experimentation and small tests (print statements, test cases)  
- Adapt suggestions according to skill level  

### Structured Response Framework

The AI follows a **six-step framework**:

1. **Goal Identification** → Verify program intent and objectives  
2. **Bug Triage** → Classify error types (syntax, logic, recursion, etc.)  
3. **Guided Checks** → Suggest small diagnostic experiments  
4. **Conceptual Nudges** → Highlight relevant Python concepts  
5. **Probing Questions** → Ask reflective questions  
6. **Next Steps** → Recommend iterative investigation strategies  

### Skill-Level Adaptation

| Skill Level   | Guidance Strategy                                           |
|---------------|------------------------------------------------------------|
| Beginner      | Stepwise hints, concrete examples, incremental reasoning |
| Intermediate  | Guided testing, conceptual nudges, reflective questions  |
| Advanced      | Edge-case exploration, abstract reasoning, strategy tips |

### Dual-Format Implementation

- **Markdown:** Human-readable and review-friendly  
- **JSON:** Structured for AI system integration or automated pipelines  

---

## White Paper

A **10-page PDF** accompanies this repository, covering:

- Prompt design methodology and rationale  
- Pedagogical principles for AI-assisted debugging  
- Beginner, intermediate, and advanced examples  
- Challenges in prompt engineering  
- Ethical considerations  
- References and appendices (Markdown & JSON prompts)  

---

## Usage Instructions

- **Markdown Prompt:** Open `AI_Debugging_Prompt.md` to read and review the prompt.  
- **JSON Prompt:** Use `AI_Debugging_Prompt.json` in AI systems for integration.  
- **White Paper:** Open `WhitePaper.pdf` for detailed design rationale, examples, and evaluation metrics.  

This repository is designed for **educational submission purposes**, demonstrating advanced prompt engineering and AI-assisted pedagogy in Python debugging.

---

## Design Rationale (Summary)

- **Clarity:** Structured guidance ensures precise, pedagogically sound AI responses.  
- **Non-Solution-Oriented:** Guardrails prevent AI from giving solutions; learners remain active participants.  
- **Adaptable:** Tailors prompts to different skill levels.  
- **Dual Format:** Markdown + JSON maximizes usability for both humans and systems.  
- **Pedagogical Alignment:** Six-step framework encourages reflective, iterative problem-solving aligned with educational principles.  


✨ **This submission is comprehensive, structured, and designed to maximize pedagogical impact while aligning with FOSSEE Task 2 guidelines.**
