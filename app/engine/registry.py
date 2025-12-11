class ToolRegistry:
    """Simple registry to store callable tools (functions)."""

    def __init__(self):
        self.tools = {}

    def register(self, name: str, func):
        self.tools[name] = func

    def get(self, name: str):
        return self.tools.get(name)

    def register_code_review_tools(self, code_review):
        """Register code review tools."""
        self.register("extract_functions", code_review.extract_functions)
        self.register("check_complexity", code_review.check_complexity)
        self.register("detect_issues", code_review.detect_issues)
        self.register("suggest_improvements", code_review.suggest_improvements)
