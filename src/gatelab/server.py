"""Gate Lab: Judges every result against walls and the owner's judgments, and turns each judgment into a check.

6 tools, each an action tool over the existing lab functions (26 former tools).
Merged from: weaponlab-mcp (Gate, probe, spec), feellab-mcp.
"""

import importlib

from mcp.server.mcpserver import MCPServer

from .actions import add_action_tool
from .tools import TOOLS

mcp = MCPServer(
    "gatelab",
    instructions="Judges every result against walls and the owner's judgments, and turns each judgment into a check. Each tool takes `action` and that action's `args`; the tool description lists them.",
)


def load(spec):
    return {action: getattr(importlib.import_module(module), fn) for module, fn, action in spec}


for _name, (_summary, _spec) in TOOLS.items():
    add_action_tool(mcp, _name, _summary, load(_spec))


def main():
    mcp.run()


if __name__ == "__main__":
    main()
