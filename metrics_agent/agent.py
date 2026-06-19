from google.adk import Agent

# Define a completely standard Python function. No decorators.
def fetch_user_metrics(user_id: str) -> str:
    """
    Queries the database to retrieve performance metrics, account status, 
    and task logs for a specific employee or user ID.
    
    Args:
        user_id: The unique identifier starting with 'USR-' (e.g., USR-102)
    """
    mock_database = {
        "USR-102": {"name": "Ramkishore", "role": "Data Analyst Intern", "completed_tasks": 42, "status": "Active"},
        "USR-505": {"name": "Aizen", "role": "Captain", "completed_tasks": 900, "status": "Suspended"}
    }
    
    record = mock_database.get(user_id.upper())
    
    if record:
        return (f"Database Match Found: {record['name']} works as a {record['role']}. "
                f"They have completed {record['completed_tasks']} tasks and their account is {record['status']}.")
    else:
        return f"Database Error: User ID '{user_id}' does not exist in the records."

# Pass the raw function straight into the tools list. 
# The ADK engine will inspect the function docstring and parameters automatically.
root_agent = Agent(
    name="metrics_analyst",
    model="gemini-2.5-flash", 
    instruction=(
        "You are a core operations assistant. When asked about user profiles, metrics, "
        "or account statuses, use the fetch_user_metrics tool. Always summarize the "
        "database results professionally for management."
    ),
    tools=[fetch_user_metrics]
)
