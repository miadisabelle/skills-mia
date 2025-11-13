---
name: aistudio-scaffolder
description: This skill helps bootstrap a new Google AI Studio project by generating the initial prompt and specification artifacts from a high-level idea. It should be used when a user wants to start a new application and needs the foundational documents to provide to an implementation agent like the one in AI Studio.  We prototype using terminal agents that will use an MCP tool that drive the web interface of AI Studio to implement the project.
---

# AI Studio Project Scaffolder

This skill guides the user through a process to generate the necessary artifacts for starting a new project in Google AI Studio, ensuring a creative-oriented and structurally sound foundation.

## Workflow

### Step 1: Understand the Desired Outcome

Begin by asking the user for their high-level project idea. Your goal is to understand what they want to *create*.  If there is an intentions already in context, try to find in past conversations, google drive or memories what could that be and make something simple to present the user (no extensive details, just the shapes of it).

**Example Questions:**
- "What is the core purpose of the application you want to build?"
- "What is the primary outcome a user will achieve with this app?"
- "Could you describe the project in a sentence or two?"

### Step 2: Gather Core Requirements

Once you have the high-level vision, gather the essential details needed for the initial prompt.

**Ask about:**
1.  **Technology Stack:** "What technologies are you envisioning? (e.g., React, Next.js, TypeScript, Tailwind CSS)"
2.  **Key Features:** "What are the 3-5 most critical features the application must have?"
3.  **Design Principles:** "Are there any specific design principles or aesthetics to follow? (e.g., minimalist, brutalist, accessible)"
4.  **AI Features:** "Are there any specific AI-powered features you'd like to include? (e.g., chatbot, voice interface, image generation)"

Reference `llms-aistudio-collaboration.md` for a full catalog of potential AI features to suggest if the user is unsure.

### Step 3: Generate the Initial AI Studio Prompt

Using the gathered information, generate a comprehensive initial prompt. This prompt will be the main input for the AI Studio agent.

**Use the `generate_initial_prompt.py` script:**
This script takes the gathered requirements as input and formats them into a structured prompt that aligns with the best practices in `llms-aistudio-collaboration.md`.

```bash
# Example usage (you will call this via the tool)
python3 scripts/generate_initial_prompt.py --name "My New App" --outcome "A tool to visualize data" --stack "React, Tailwind" ...
```

### Step 4: Generate Placeholder RISE Specifications

To ensure the project starts with a strong structural foundation, create placeholder `rispecs` for the core features identified.

**Use the `generate_rise_specs.py` script:**
This script will create a `rispecs` directory and populate it with placeholder `.spec.md` files for each key feature. These files will contain the basic RISE framework structure (Desired Outcome, Current Reality, etc.), ready for further refinement.

```bash
# Example usage
python3 scripts/generate_rise_specs.py --features "User Login,Dashboard,Data Visualization"
```

### Step 5: Package the Artifacts

Combine the generated prompt and the `rispecs` directory into a single, well-organized output for the user.

**Final Output Structure:**
```
/aistudio-project-scaffolding/
├── initial_prompt.md
└── rispecs/
    ├── user-login.spec.md
    ├── dashboard.spec.md
    └── data-visualization.spec.md
```

Present this to the user as the "Project Scaffolding Package," ready to be used in terminal by an agent that will implement it with  AI Studio (the LLM receiving these instructions will NOT IMPLEMENT it but will use AI Studio todo it.
