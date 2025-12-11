from pydantic import BaseModel
from typing import Dict, Any, List, Optional  # added Optional

class GraphDefinition(BaseModel):
    nodes: Dict[str, str]   # {node_name: tool_name}
    edges: Dict[str, Optional[str]]   # {node_name: next_node_name or None}
    start_node: str

class RunRequest(BaseModel):
    graph_id: str
    initial_state: Dict[str, Any]

class RunResult(BaseModel):
    final_state: Dict[str, Any]
    log: List[Dict[str, Any]]
