from langgraph.graph import StateGraph, END
from workflow.state import AgentState
from agents.generator import generator_node
from agents.critic import critic_node

def create_graph():
    workflow = StateGraph(AgentState)
    
    # Add nodes
    workflow.add_node("generator", generator_node)
    workflow.add_node("critic", critic_node)
    
    # Define edges
    workflow.set_entry_point("generator")
    workflow.add_edge("generator", "critic")
    workflow.add_edge("critic", END)
    
    return workflow.compile()
