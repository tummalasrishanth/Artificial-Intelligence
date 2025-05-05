import random

environment = {
    'A': random.choice(['Dirty', 'Clean']),
    'B': random.choice(['Dirty', 'Clean'])
}

vacuum_location = random.choice(['A', 'B'])

def vacuum_agent(location, env):
    actions = []
    if env[location] == 'Dirty':
        actions.append(f"Location {location} is Dirty. Action: Suck.")
        env[location] = 'Clean'
    if location == 'A':
        actions.append("Move Right to B.")
        location = 'B'
    else:
        actions.append("Move Left to A.")
        location = 'A'
    return location, actions

print(f"Initial Environment: {environment}")
for _ in range(4):
    vacuum_location, performed_actions = vacuum_agent(vacuum_location, environment)
    for action in performed_actions:
        print(action)
    print(f"Environment Now: {environment}")