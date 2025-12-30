from src.graph import create_swarm

def main():
    print("🚀 Initializing Strategic Intelligence Swarm...")
    swarm = create_swarm()
    
    initial_state = {
        "messages": [],
        "focus": "Enterprise Multi-Agent Systems",
        "findings": [],
        "insights": [],
        "report": "",
        "next_step": ""
    }
    
    print(f"🎯 Swarm Mission: Analyze {initial_state['focus']}")
    
    # Run the swarm
    final_state = swarm.invoke(initial_state)
    
    print("\n--- FINAL STRATEGIC REPORT ---")
    print(final_state["report"])
    print("\nSwarm operations completed successfully.")

if __name__ == "__main__":
    main()
