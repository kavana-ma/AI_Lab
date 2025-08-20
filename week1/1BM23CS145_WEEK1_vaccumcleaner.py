# Environment: 2 rooms A and B
environment = {
    "A": random.choice(["Clean", "Dirty"]),
    "B": random.choice(["Clean", "Dirty"])
}

# Simple Reflex Agent
def simple_reflex_agent(location, status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Right"
    else:
        return "Left"

# Goal-Based Agent
def goal_based_agent(env):
    actions = []
    for location in ["A", "B"]:
        if env[location] == "Dirty":
            actions.append((location, "toClean"))
            env[location] = "Clean"
    return actions

# Simulation
def run_simulation():
    print("Initial Environment:", environment)

    # Reflex agent
    location = random.choice(["A", "B"])
    action = simple_reflex_agent(location, environment[location])
    print(f"Reflex Agent at {location} sees {environment[location]} -> Action: {action}")

    # Goal-based agent
    actions = goal_based_agent(environment.copy())
    print("Goal-Based Agent Actions:", actions)

run_simulation()
