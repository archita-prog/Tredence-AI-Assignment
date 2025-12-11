import asyncio

class WorkflowEngine:
    """Executes nodes step-by-step according to edges."""

    def __init__(self, graph: dict, registry):
        self.nodes = graph["nodes"]
        self.edges = graph["edges"]
        self.start_node = graph["start_node"]
        self.registry = registry

    async def run(self, state: dict):
        current = self.start_node
        log = []

        while current:
            tool_name = self.nodes[current]
            tool = self.registry.get(tool_name)
            if tool is None:
                raise ValueError(f"Tool '{tool_name}' not found in registry")

            # run sync or async tools
            result = await tool(state) if asyncio.iscoroutinefunction(tool) else tool(state)
            state.update(result)
            log.append({"node": current, "state": dict(state)})

            # stop condition
            if state.get("stop", False):
                break

            next_node = self.edges.get(current)
            if not next_node or next_node == "STOP":
                break
            current = next_node


        return state, log
