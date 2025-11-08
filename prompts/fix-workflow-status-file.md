# Purpose

The `@docs/bmm-workflow-status.yaml` file is either corrupted, outdated or missing. Your task is to fix it.

## Workflow

### Step 1 Find the existing workflow status file

- First check if there an existing workflow status file in the `@docs`: It can be named `bmm-workflow-status.yaml` or `bmm-workflow-status.md`.

- If it exists, read it to understand where the workflow is at.\, and what has been done so far.

### Step 2 Create correct workflow status file

The workflow status file format has been update, so you need to create a new one. We will use the old one to fill in the new file.

Now create a new workflow status file by following the instructions in the the following file: `@/bmad/bmm/workflows/workflow-status/instructions.md`

IMPORTANT: YOU NEED to RUN THIS INSTRUCTION WITHOUT ASKING THE USER TO DO ANYTHING - COMPLETELY YOLO MODE. USE THE EXISTING WORKFLOW STATUS FILE TO CREATE THE NEW ONE. THERE IS ALSO A BREAKING CHANGE IN THE NEW FORMAT. HERE IS THE CHANGELOG OF BMAD:

```markdown
Variable Renames:

project_level → project_track in PRD and all planning workflows
Removed target_scale variable (no longer needed with 3-track system)
Workflow Path Files:

Removed 9 level-based workflow paths (brownfield-level-0, greenfield-level-3, etc.)
Added 6 new track-based workflow paths (quick-flow-greenfield, method-brownfield, enterprise-greenfield, etc.)
```

The CORRECT project_track value is: method-greenfield found here: `@\bmad\bmm\workflows\workflow-status\paths\method-greenfield.yaml`


### Step 3 Delete the old workflow status file and save the new

- Delete the old workflow status file if it existed
- Save the new workflow status file

### Step 4 Report completion

- Report completion to the user
- Write a detailed step-by step report of what you did and save it as `@docs/fix-workflow-status-file-report.md`