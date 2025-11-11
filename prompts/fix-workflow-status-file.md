# Purpose

The `@docs/bmm-workflow-status.yaml` file is either corrupted, outdated or missing. Your task is to fix it.

## Workflow

### Step 1 Find the existing workflow status file

- First check if there an existing workflow status file in the `@docs`: It can be named `bmm-workflow-status.yaml` or `bmm-workflow-status.md`.

- If it exists, read it to understand where the workflow is at.\, and what has been done so far.

### Step 2 Run workflow-init

The workflow status file format has been update, so you need to create a new one. We will use the old one to fill in the new file.

Now create a new workflow status file by following the instructions in the the following files: `@/bmad/bmm/workflows/workflow-status/init/instructions.md`

IMPORTANT: YOU NEED to RUN THIS INSTRUCTION WITHOUT ASKING THE USER TO DO ANYTHING - COMPLETELY YOLO MODE. USE THE EXISTING WORKFLOW STATUS FILE TO CREATE THE NEW ONE. THERE IS ALSO A BREAKING CHANGE IN THE NEW FORMAT. HERE IS THE CHANGELOG OF BMAD:

```markdown
Variable Renames:

project_level → project_track in PRD and all planning workflows
Removed target_scale variable (no longer needed with 3-track system)
Workflow Path Files:

Removed 9 level-based workflow paths (brownfield-level-0, greenfield-level-3, etc.)
Added 6 new track-based workflow paths (quick-flow-greenfield, method-brownfield, enterprise-greenfield, etc.)
```

The CORRECT selected_track = method 

The correct path is: method-greenfield found here: `@\bmad\bmm\workflows\workflow-status\paths\method-greenfield.yaml`

The output from this step is a correctly initiated workflow status file. Do NOT save it yet, since we will now update it by running workflow-status.

### Step 3 Run workflow-status

- Run the workflow-status workflow:
`@/bmad/bmm/workflows/workflow-status/instructions.md`
- Use the old workflow status file to fill in the new one
- ITS MANDATORY to fill in the current state of what have been done and what is the next step. 


### Step 4 Delete the old workflow status file and save the new one

- Delete the old workflow status file if it existed
- Save the new workflow status file

### Step 5 Verify the correct workflow status

Verify that the new workflow status file is correct by checking that the necessary output files from the earlier steps exist.


### Step 5 Report completion

- Report completion to the user
- Write a detailed step-by step report of what you did and save it as `@docs/fix-workflow-status-file-report.md`