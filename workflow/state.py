from typing import TypedDict, Optional

class AgentState(TypedDict):
    topic: str
    generated_content: Optional[str]
    critique: Optional[str]
    iteration_count: int
