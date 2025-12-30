import base64
import requests
import os

# Create images directory if it doesn't exist
os.makedirs("images", exist_ok=True)

diagrams = {
    "architecture_overview": """
graph TB
    subgraph Swarm ["Strategic Intelligence Swarm"]
        Monitor["Monitor Agent<br/>(Market Trends)"]
        Analyst["Analyst Agent<br/>(Competitive Intelligence)"]
        Strategist["Strategist Agent<br/>(Board Recommendations)"]
    end
    
    Tools["External Tools<br/>(Market Search, Competitor API)"]
    UX["Executive Dashboard<br/>(Strategic Reports)"]
    
    Monitor --> Tools
    Monitor --> Analyst
    Analyst --> Strategist
    Strategist --> UX
    Strategist --> Monitor
    """,
    "agent_communication": """
sequenceDiagram
    participant M as Monitor Agent
    participant T as External Tools
    participant A as Analyst Agent
    participant S as Strategist Agent
    
    M->>T: Search Market Trends
    T-->>M: Trend Data
    M->>A: Findings & Context
    A->>A: Competitive Analysis
    A->>S: Strategic Insights
    S->>S: Formulate Recommendation
    S-->>M: Loop for Refinement
    """,
    "project_structure_viz": """
graph LR
    Root[Project Root] --> src
    Root --> scripts
    Root --> images
    src --> state.py
    src --> agents.py
    src --> graph.py
    src --> tools.py
    scripts --> publish.py
    scripts --> generate_diagrams.py
    """
}

def generate_diagram(name, code):
    print(f"Generating diagram: {name}...")
    encoded = base64.b64encode(code.encode()).decode()
    url = f"https://mermaid.ink/img/{encoded}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(f"images/{name}_diagram.png", 'wb') as f:
                f.write(response.content)
            print(f"Successfully saved images/{name}_diagram.png")
        else:
            print(f"Failed to generate {name}: {response.status_code}")
    except Exception as e:
        print(f"Error generating {name}: {str(e)}")

if __name__ == "__main__":
    for name, code in diagrams.items():
        generate_diagram(name, code)
