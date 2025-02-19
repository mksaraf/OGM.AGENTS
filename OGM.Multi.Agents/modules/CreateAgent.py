
class Agent:
    def __init__(self, role, goal, backstory, verbose, allow_delegation, tools):
        self.role = role
        self.goal = goal
        self.backstory = backstory
        self.verbose = verbose
        self.allow_delegation = allow_delegation
        self.tools = tools

def create_agent(role, goal, backstory, verbose=True, allow_delegation=True, tools=[]):
    return Agent(role, goal, backstory, verbose, allow_delegation, tools)



