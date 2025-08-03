from agents import Agent, Runner #Agent & Runner are classes

agent:Agent = Agent(name="Assistant",instructions="A helpful assistant for flight booking tasks.")

output = Runner.run_sync(starting_agent = agent,input= "Hello, how can I help you.")

print(output.final_output)