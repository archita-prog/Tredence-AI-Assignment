# ⚙️ AI Workflow Engine  
*A Backend Orchestration System built with FastAPI*

---

### 📌 Overview
This project implements a **minimal workflow (graph) engine**, similar in concept to LangGraph.  
It allows users to define **nodes** (Python functions), connect them via **edges**, maintain a shared **state**, and execute workflows **step-by-step via REST APIs**.

Built as part of the **Tredence AI Engineering Internship Assignment**, this backend demonstrates strong fundamentals in:
- Python design & async programming  
- API structuring with FastAPI  
- State management & modular system logic  

---

## 🧩 Core Features

✅ **Graph Engine**
- Define nodes (functions) and edges (execution order)
- Supports conditional branching and loop-like logic
- Maintains a shared state across nodes  

✅ **Tool Registry**
- Register Python functions as reusable workflow tools

✅ **FastAPI Endpoints**
- `POST /graph/create` → Define and save a workflow graph  
- `POST /graph/run` → Execute workflow with initial state  
- `GET /graph/state/{run_id}` → Retrieve final state and execution logs  

✅ **Example Workflow**
- Implements a **Code Review Mini-Agent** that:
  1. Extracts functions  
  2. Checks code complexity  
  3. Detects issues  
  4. Suggests improvements until a target quality score is achieved  

---

python -m venv venv
.\venv\Scripts\activate     # (Windows)
# or
source venv/bin/activate    # (Mac/Linux)
pip install -r requirements.txt
Sample Input for Graph:
<img width="1855" height="885" alt="image" src="https://github.com/user-attachments/assets/01e2555c-2b19-4779-9b30-6168f1a28df4" />

Sample Output for Graph:
<img width="1832" height="872" alt="image" src="https://github.com/user-attachments/assets/37b694e5-7ff6-4993-9f1f-db57644a7bc2" />
<img width="1878" height="455" alt="image" src="https://github.com/user-attachments/assets/408e692d-9136-4d84-a762-f1dce9562350" />

Sample Input for running the graph:
<img width="1858" height="589" alt="image" src="https://github.com/user-attachments/assets/b6439cbd-a572-4998-9229-85fb5e7766b6" />

Sample Output for running the graph:
<img width="1831" height="869" alt="image" src="https://github.com/user-attachments/assets/9a129dba-92de-49ae-868f-e5e23e6e4c70" />
<img width="1812" height="424" alt="image" src="https://github.com/user-attachments/assets/234070a4-6ee4-44ab-9d56-6f365e55f9ae" />

UI of the Project:
<img width="1870" height="543" alt="image" src="https://github.com/user-attachments/assets/6178dac5-2a5b-4f6e-ad51-de6554d4679b" />
<img width="1888" height="487" alt="image" src="https://github.com/user-attachments/assets/6634305d-c2d3-47e9-a909-64014c4784a1" />








