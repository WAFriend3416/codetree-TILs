class Agent:
    def __init__(self,codeName="-",score=0):
        self.codeName = codeName
        self.score = score

Agents = [
    tuple(map(str,input().split()))
    for _ in range(5)
]

Agent_result = Agent()
result = 100
for i in range(5):
    if result >= int(Agents[i][1]):
        result = int(Agents[i][1])
        Agent_result.codeName,Agent_result.score = (Agents[i][0],Agents[i][1])

print(Agent_result.codeName,Agent_result.score)