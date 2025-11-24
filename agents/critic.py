from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from config.settings import settings
from workflow.state import AgentState

def critic_node(state: AgentState):
    """
    Critiques the generated content.
    """
    print("--- Critic: Reviewing content ---")
    
    llm = ChatOllama(base_url=settings.OLLAMA_BASE_URL, model=settings.OLLAMA_MODEL)
    
    prompt = ChatPromptTemplate.from_template(
        "You are a constructive critic. Review the following content and provide brief feedback on how to improve it:\n\n{content}"
    )
    
    chain = prompt | llm
    
    response = chain.invoke({"content": state["generated_content"]})
    
    return {"critique": response.content}
