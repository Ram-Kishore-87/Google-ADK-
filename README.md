To document this program formally—similar to a computer science lab record or technical project specification—here is the breakdown of your project structured by **Aim, Algorithm, and Result**.

---

## 1. AIM

To design, implement, and deploy an autonomous AI Agent using the **Google Agent Kit (ADK)** framework and the `gemini-2.5-flash` model. The agent must interact with users in natural language, detect queries regarding employee performance metrics, autonomously invoke a local Python backend tool (`fetch_user_metrics`) to retrieve real-time data from a database registry, and synthesize the raw data into a professional management summary.

---

## 2. ALGORITHM

The system operates on an event-driven reasoning loop consisting of the following execution steps:

### Phase A: Initialization

1. Load the Google Agent Kit core `Agent` runtime.
2. Initialize the backend database registry (`mock_database`) mapping unique alphanumeric keys (`user_id`) to data structures containing metadata values (`name`, `role`, `completed_tasks`, `status`).
3. Define the tool signature schema and logic for the lookup function `fetch_user_metrics(user_id)`.
4. Instantiate the AI Agent engine, registering the `gemini-2.5-flash` model, passing the system operations instructions, and injecting the raw reference pointer of the lookup function into the agent's available `tools` array.

### Phase B: The Runtime Reasoning Loop

5. Launch the CLI runtime interactive loop and await string input from the user terminal interface.
6. Upon receiving a natural language prompt, transmit the user input along with the auto-generated JSON schemas of the registered tools to the Gemini backend API.
7. **Model Evaluation:** The LLM processes the user intent against its instructions:
* **IF** the prompt requires external system metrics data, the model generates a structured `FunctionCall` request containing the extracted argument string (e.g., `user_id="USR-102"`).
* **ELSE**, the model directly generates a text response (Skip to Step 11).



### Phase C: Tool Execution & Synthesis

8. **Local Interception:** The ADK framework catches the model's `FunctionCall` request on the client machine and routes execution directly to the local Python function.
9. **Data Processing:** The local function sanitizes the argument using `.upper()`, queries the dictionary catalog using `.get()`, constructs a raw status text block, and returns it to the ADK layer.
10. **Context Injection:** The ADK automatically fires a second payload back to the Gemini API containing the raw text block returned by the Python script.
11. **Final Output:** Gemini interprets the ground-truth data, wraps it in the requested professional persona tone, and streams the final output back to the terminal.

---

## 3. RESULT

The terminal workspace initialized successfully, loaded the credential modules, and established a persistent connection to the model gateway.

When presented with an un-cached, context-dependent production query, the agent completely bypassed hallucination, successfully mapped the entity token to its argument slot, invoked the local environment code, and produced the following verified operational tracking output:

```text
Running agent metrics_analyst, type exit to exit.

[user]: Can you pull up the operational metrics for employee USR-102?

[metrics_analyst]: For employee USR-102, Ramkishore, a Data Analyst Intern, has completed 42 tasks and their account is currently active.

```
