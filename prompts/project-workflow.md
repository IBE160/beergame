## Purpose

THe purpose of this workflow is to SIMPLIFY the whole BMAD development process, by creating a predfined workflow that the user should just follow from start to finish.

The output of this workflow should be the following files:

**User input files**
- `@docs/user-input-brainstorming-workflow.md`
- `@docs/user-input-research-workflow.md`
- `@docs/user-input-product-brief-workflow.md`
- `@docs/user-input-prd-workflow.md`
- `@docs/user-input-validate-prd-workflow.md`
- `@docs/user-input-create-design-workflow.md`
- `@docs/user-input-validate-architecture-workflow.md`
- `@docs/user-input-solutioning-gate-check-workflow.md`
- `@docs/user-input-sprint-planning-workflow.md`

The idea with these files is to gather ALL the user input for the project in one place. By answering the questions in these files, the user will have gathered ALL the necessary information for the project.

This means that the user can input the necessary information in forehand, and then run the whole project autonomously (in yolo mode).

**Project workflow file**
And finally a `project-workflow.md` file, which contains EVERYTHING the user needs to do to complete the project.

The idea of this file is to create a set of commands that the user can run to complete the project, where each command takes a user-input file as input, and runs the corresponding workflow.

This way it will be much easier for the user to both now WHAT to do, WHEN to do it, and in what ORDER to do it.





### Variables


### Instructions


### Workflow

#### Step 1: Learn the BMAD framework

Read the `@/bmad` starting from  `C:\IBE160\projects\beergame\bmad\bmm\workflows\workflow-status\paths\method-greenfield.yaml` since this is the project type we are using.

From this file, read ALL the the necessary workflows in `@bmad` to learn about the necessary steps.

#### Step 2: Create the user-input files

For each user-input file, find the corresponding workflow instruction file in `@bmad`. Extract ALL the output text and  questions from the instruction file sent to the user and create a user-input file with the questions.

This files will therefore simulate the exact discussion that the user would have with the agent if he was running the workflow manually.

Your task is to create the FORMAT of this user-input files. REmember its the idea that the user should manually  read this file and make the choices.

There are several different decision types the user needs to make:

Common for all:

**Question N**
{Type the question here you gather from the instruction files, the number N is just the question number, this is needed for branching logic using goto help indicators}
**Answer**
{Input from the user}

We have the following decision types:

1. Only ONE choice from a list of options - make this a radio button list as answer. Use a goto help indicator to guide the user where to go next.
2. SEVERAL possible choices from a list of options - make this a checkbox list as answer. Use goto help indicators to guide the user where to go next.
3. A free text input as answer - type: `Type your answer here`, to tell the user that this is a free text input.

If there are any other types of questions, come up with a suitable format for the user-input file.
