# file related to langGraph


import json

from dotenv import load_dotenv
load_dotenv()

import os
from langchain_groq import ChatGroq
from typing import TypedDict
from langgraph.graph import StateGraph, END
from datetime import datetime

from typing import TypedDict



llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0,
)


def extract_interaction(message: str):

    prompt = f"""
You are an AI assistant for a Healthcare CRM.

Extract the following fields from the conversation.

Return ONLY valid JSON.

{{
"hcp_name":"",
"interaction_type":"",
"date":"",
"time":"",
"attendees":"",
"topics_discussed":"",
"materials_shared":"",
"samples_distributed":"",
"sentiment":"",
"outcomes":"",
"follow_up_actions":"",
"ai_suggestions":""
}}

Conversation:

{message}
"""

    response = llm.invoke(prompt)

    data= json.loads(response.content)
   

    now = datetime.now()

   
    data["date"] = now.strftime("%Y-%m-%d")
    data["time"] = now.strftime("%H:%M")
    return data



# creating a helper fun for edit interaction
def extract_edit_fields(message: str):

    prompt = f"""
You are an AI assistant for a Healthcare CRM.

The user wants to edit an existing interaction.

Extract ONLY the fields that need to be updated.

Return ONLY valid JSON.

Example:

User:
Change sentiment to Neutral and follow up after 2 weeks.

Output:

{{
    "sentiment":"Neutral",
    "follow_up_actions":"Follow up after 2 weeks"
}}

Message:

{message}
"""

    response = llm.invoke(prompt)
    updates = json.loads(response.content)

    field_mapping = {
    "follow_up_date": "follow_up_actions",
    "followup": "follow_up_actions",
    "follow_up": "follow_up_actions",
    }


    normalized = {}

    for key, value in updates.items():
     normalized[field_mapping.get(key, key)] = value

    return normalized




# langGraph state
class GraphState(TypedDict):
    message: str
    tool: str
    interaction: dict
    response: dict

# langGraph node
def log_interaction_node(state: GraphState):

    data = extract_interaction(state["message"])

    return {
        "interaction": data
    } 

def edit_interaction_node(state):

    updates = extract_edit_fields(
        state["message"]
    )

    return {
        "interaction": updates
    }


def latest_interaction_node(state):
    return {
        "response": {
            "tool": "Get Latest Interaction"
        }
    }


def search_interaction_node(state):
    return {
        "response": {
            "tool": "Search Interaction"
        }
    }


def summarize_interaction_node(state):
    return {
        "response": {
            "tool": "Summarize Interaction"
        }
    }

# we are using one single llm instead of multiple for each node like create ,edit, search, summary etc.
#  So we need to route the message to the correct node based on the message content.
#  This is done by the router_node function.
def router_node(state: GraphState):

    message = state["message"].lower()

    if "edit" in message or "change" in message or "update" in message:
        tool = "edit"

    elif "latest" in message:
        tool = "latest"

    elif "search" in message or "find" in message:
        tool = "search"

    elif "summary" in message or "summarize" in message:
        tool = "summary"

    else:
        tool = "log"

    return {
        "tool": tool
    }


# now creating graph
builder = StateGraph(GraphState)

builder.add_node("router", router_node)

builder.add_node("log", log_interaction_node)

builder.add_node("edit", edit_interaction_node)

builder.add_node("latest", latest_interaction_node)

builder.add_node("search", search_interaction_node)

builder.add_node("summary", summarize_interaction_node)


# conditional routing based on the tool selected in the router node
def route(state):

    return state["tool"]

builder.set_entry_point("router")

builder.add_conditional_edges(
    "router",
    route,
    {
        "log": "log",
        "edit": "edit",
        "latest": "latest",
        "search": "search",
        "summary": "summary",
    },
)

builder.add_edge("log", END)

builder.add_edge("edit", END)

builder.add_edge("latest", END)

builder.add_edge("search", END)

builder.add_edge("summary", END)



graph = builder.compile()
