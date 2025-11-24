import argparse
from workflow.graph import create_graph

def main():
    parser = argparse.ArgumentParser(description="Basic A2A Example: Generator and Critic")
    parser.add_argument("--topic", type=str, default="Artificial Intelligence", help="Topic for the story/joke")
    args = parser.parse_args()
    
    print(f"Starting A2A Workflow with topic: {args.topic}")
    
    app = create_graph()
    
    initial_state = {"topic": args.topic, "iteration_count": 0}
    
    result = app.invoke(initial_state)
    
    print("\n\n================ RESULT ================")
    print(f"TOPIC: {result['topic']}")
    print("\n--- GENERATED CONTENT ---")
    print(result['generated_content'])
    print("\n--- CRITIQUE ---")
    print(result['critique'])
    print("========================================")

if __name__ == "__main__":
    main()
