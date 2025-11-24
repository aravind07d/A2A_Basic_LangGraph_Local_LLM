from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from config.settings import settings
from workflow.state import AgentState

def generator_node(state: AgentState):
    """
    Generates content based on the topic.
    """
    print(f"--- Generator: Generating content for topic '{state['topic']}' ---")
    
    llm = ChatOllama(base_url=settings.OLLAMA_BASE_URL, model=settings.OLLAMA_MODEL)
    
    prompt = ChatPromptTemplate.from_template(
        "You are a creative writer. Write a short, engaging story or joke about: {topic}. Keep it under 100 words."
    )
    
    chain = prompt | llm
    
    response = chain.invoke({"topic": state["topic"]})
    
    return {"generated_content": response.content, "iteration_count": state.get("iteration_count", 0) + 1}
