import uuid
from .workflow import WorkflowEngine

class GraphManager:
    """In-memory storage for graphs and runs."""

    def __init__(self):
        self.graphs = {}
        self.runs = {}

    def save_graph(self, graph: dict) -> str:
        graph_id = str(uuid.uuid4())
        self.graphs[graph_id] = graph
        return graph_id

    async def run_graph(self, graph_id: str, registry, initial_state: dict):
        graph = self.graphs[graph_id]
        engine = WorkflowEngine(graph, registry)
        final_state, log = await engine.run(initial_state)
        run_id = str(uuid.uuid4())
        self.runs[run_id] = {"state": final_state, "log": log}
        return run_id, final_state, log

    def get_state(self, run_id: str):
        return self.runs.get(run_id, {})
