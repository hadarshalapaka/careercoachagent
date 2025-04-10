from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.graph import StateGraph, START, END
from typing_extensions import TypedDict
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-001",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)


class State(TypedDict):
    candidate_bg:str
    career_goal:str
    background_analysis:str
    goal_milestones:str
    skills_per_stage:str
    learning_resources:str
    final_plan:str
    
def analyzeBackground(state):
    """To analyze the educational and professional background of the candidate"""

    system_msg = SystemMessage(content="""You are a career coach who thoroughly analyzes the educational and professional background of the candidate.
    Only List key strengths and weaknesses of the candidate to achieve the specified goal. Do not give anything other than the requested list.""")

    human_msg = HumanMessage(content=f"""candidate background:{state["candidate_bg"]}
    career goal:{state["career_goal"]}""")

    messages=[]
    messages.append(system_msg)
    messages.append(human_msg)

    
    response = llm.invoke(messages)
    state["background_analysis"]=response.content
    return state
    
def tool_decision_(state):
    prompt = f"""candidate background:{state["candidate_bg"]}
    career goal:{state["career_goal"]}
    Do you think the career goal is already achieved for the candidate as per their experience, background and career goal? Answer in only one word 'Yes or No')"""

    response = llm.invoke(prompt)
    
    if str(response.content).lower() == "yes":
        return "no_timeline_required"
    else:
        return "breakdown_goal"

def breakdown_goal(state):
    system_msg = SystemMessage(content="""Given the career goal, you have to list major milestones to achieve that goal. Do not give any other information other than the requested list.""")
    prompt = HumanMessage(content=f"""
    The candidate wants to become a {state["career_goal"]}.
    Break down this goal into 4-5 major milestones (logical stages).
    """)
    messages=[]
    messages.append(system_msg)
    messages.append(prompt)
    response = llm.invoke(messages)
    
    state["goal_milestones"] = response.content
    return state

def suggest_skills(state):
    prompt = f"""
    For the following milestones: 
    {state["goal_milestones"]},
    suggest the key skills the user must master at each stage. Do not give extra text.
    """
    response = llm.invoke(prompt)
    state["skills_per_stage"] = response.content
    return state

def suggest_resources(state):
    prompt = f"""
    Suggest top 2 free or paid online courses/resources to learn each of these skills: {state["skills_per_stage"]}.
    """
    response = llm.invoke(prompt)
    state["learning_resources"] = response.content
    return state

def build_timeline(state):
    milestones = state["goal_milestones"]
    skills = state["skills_per_stage"]
    resources = state["learning_resources"]
    prompt = f"""
    Build a 6-month learning timeline using these milestones: {milestones}, skills: {skills}, and resources: {resources}.
    Make it realistic for a working professional.
    """
    response = llm.invoke(prompt)
    state["final_plan"] = response.content
    return state

def no_timeline_required(state):
    state["final_plan"] = "Hurray!, You are on the track and seems goal is achieved"
    return state

def debug_print(state):
    print(state)
    return state


graph = StateGraph(State)

graph.add_node("analyze_background", analyzeBackground)
graph.add_node("breakdown_goal", breakdown_goal)
graph.add_node("debug_print", debug_print)
graph.add_node("suggest_skills", suggest_skills)
graph.add_node("suggest_resources", suggest_resources)
graph.add_node("build_timeline", build_timeline)
graph.add_node("no_timeline_required", no_timeline_required)

graph.add_edge(START, "analyze_background")
graph.add_conditional_edges("analyze_background",tool_decision_)
graph.add_edge("breakdown_goal", "suggest_skills")
graph.add_edge("suggest_skills", "suggest_resources")
graph.add_edge("suggest_resources", "build_timeline")
graph.add_edge("build_timeline", END)
graph.add_edge("no_timeline_required", END)

app = graph.compile()