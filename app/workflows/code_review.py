def extract_functions(state):
    """Mock function to extract functions from code."""
    code = state.get("code", "")
    functions = ["func1", "func2"]
    return {"functions": functions, "num_functions": len(functions)}

def check_complexity(state):
    """Calculate a fake complexity score."""
    complexity = 10 * state["num_functions"]
    return {"complexity": complexity}

def detect_issues(state):
    """Simulate detecting issues."""
    issues = max(0, 5 - state["complexity"] // 10)
    return {"issues": issues}

def suggest_improvements(state):
    """Suggest improvements until quality >= 80."""
    quality = state.get("quality_score", 50) + (5 - state["issues"]) * 5
    stop = quality >= 80
    return {"quality_score": quality, "stop": stop}
