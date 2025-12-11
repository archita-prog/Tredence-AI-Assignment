from fastapi import FastAPI

# Support two execution modes:
# - `python -m app.main` (package mode) where imports like `app.models` work
# - `python app/main.py` (script mode) where the current directory is `app`
# Try package imports first, then fall back to local imports when needed.
try:
    from app.models import GraphDefinition, RunRequest
    from app.engine.registry import ToolRegistry
    from app.engine.graph_manager import GraphManager
    from app.workflows import code_review
except ModuleNotFoundError:
    from models import GraphDefinition, RunRequest
    from engine.registry import ToolRegistry
    from engine.graph_manager import GraphManager
    from workflows import code_review

app = FastAPI(title="AI Workflow Engine")

registry = ToolRegistry()
manager = GraphManager()

# Register available tools
registry.register("extract_functions", code_review.extract_functions)
registry.register("check_complexity", code_review.check_complexity)
registry.register("detect_issues", code_review.detect_issues)
registry.register("suggest_improvements", code_review.suggest_improvements)


@app.post("/graph/create")
async def create_graph(graph: GraphDefinition):
    graph_id = manager.save_graph(graph.dict())
    return {"graph_id": graph_id}


@app.post("/graph/run")
async def run_graph(req: RunRequest):
    try:
        run_id, final_state, log = await manager.run_graph(req.graph_id, registry, req.initial_state)
        return {"run_id": run_id, "final_state": final_state, "log": log}
    except Exception as e:
        import traceback
        traceback.print_exc()
        return {"error": str(e)}


@app.get("/graph/state/{run_id}")
async def get_state(run_id: str):
    return manager.get_state(run_id)
