# Project Plan

## Fase 0

- [ ] Brainstorming
  - [ ] /analyst *brainstorm {prompt / user-input-file}
  - [ ] /analyst *brainstorm {prompt / user-input-file}
  - [ ] /analyst *brainstorm {prompt / user-input-file}
- [ ] Research
  - [ ] /analyst *research {prompt / user-input-file}
  - [ ] /analyst *research {prompt / user-input-file}
  - [ ] /analyst *research {prompt / user-input-file}
- [ ] Product Brief
  - [ ] /analyst *product-brief {prompt / user-input-file}

## Fase 1

- [ ] Planning
  - [ ] /run-agent-task pm *prd {prompt / user-input-file}
  - [ ] /run-agent-task pm *validate-prd {prompt / user-input-file}
  - [ ] /run-agent-task ux-designer *create-ux-design {prompt / user-input-file}
  - [ ] /run-agent-task ux-designer *validate-ux-design {prompt / user-input-file}
  - [ ] /run-agent-task tea *framework {prompt / user-input-file}
  - [ ] /run-agent-task tea *ci {prompt / user-input-file}
  - [ ] /run-agent-task tea *test-design {prompt / user-input-file}

## Fase 2

- [ ] Solutioning
  - [ ] /run-agent-task architect *architecture {prompt / user-input-file}
  - [ ] /run-agent-task architect *validate-architecture {prompt / user-input-file}

## Fase 3

- [ ] Implementation
  - [ ] /run-agent-task sm *sprint-planning {prompt / user-input-file}
  - foreach epic in sprint planning:
    - [ ] /run-agent-task sm epic-tech-content {prompt / user-input-file}
    - [ ] /run-agent-task sm validate-epic-tech-content {prompt / user-input-file}
    - foreach story in epic:
      - [ ] /run-agent-task sm *create-story {prompt / user-input-file}
      - [ ] /run-agent-task sm *validate-create-story {prompt / user-input-file}
      - [ ] /run-agent-task sm *story-context {prompt / user-input-file}
      - [ ] /run-agent-task sm *validate-story-context {prompt / user-input-file}
      - [ ] /run-agent-task tea *validate-story-ready {prompt / user-input-file}
      - [ ] /run-agent-task dev *implement-story {prompt / user-input-file}
      - [ ] /run-agent-task dev *validate-story {prompt / user-input-file}
      - [ ] /run-agent-task tea *automate {prompt / user-input-file}
      - [ ] /run-agent-task tea *test-review {prompt / user-input-file}
    - [ ] /run-agent-task sm *retrospective {prompt / user-input-file}
