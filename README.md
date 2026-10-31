# gatelab-mcp

Gate Lab: Judges every result against walls and the owner's judgments, and turns each judgment into a check.

6 tools replace 26. Each tool takes `action` and `args`, and calls the existing lab function
unchanged. Merged from: weaponlab-mcp (Gate, probe, spec), feellab-mcp. Plan steps: 5, 7 of
[the labs plan](https://github.com/hpdkhoa/poselab-mcp/blob/main/docs/MEANING_PLAN.md).

| Tool | Actions |
|---|---|
| `gate_cases` | list, metrics, weapons, add |
| `gate_run` | run, verdict, set_baseline |
| `gate_judge` | propose, approve, proposals, evals |
| `probe` | status, plan, run |
| `feel` | list_checklist, list_scenes, list_metrics, check_timeline, judge_folder, gate_rows |
| `project` | info, contract_check, spec_list, spec_read, spec_validate, spec_write |

## Install

```bash
pip install "gatelab-mcp @ git+https://github.com/hpdkhoa/gatelab-mcp.git"
claude mcp add --scope user gatelab -- gatelab-mcp
```

## Test

```bash
pip install -e ".[test]" && pytest
```

MIT license.
