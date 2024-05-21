import os
from crewai import Agent, Task, Crew, Process
from langchain_community.tools import DuckDuckGoSearchRun
from crewai_tools.tools import WebsiteSearchTool, SerperDevTool

seper_dev_tool = SerperDevTool()

from dotenv import load_dotenv
from textwrap import dedent
import json 
from langchain_groq import ChatGroq

load_dotenv()
llm = ChatGroq(
            temperature=0, 
            model_name="llama3-8b-8192"
        )


def create_crew(OUTPUT_FOLDER):
  # Load an Excel file into a DataFrame
  #df = pd.read_excel('tasks.xlsx')
  agent_load= json.loads(open("agents.json", "r").read())
  agents={}
  for agent in agent_load: 
    infos = agent_load[agent]
    agents[agent] = Agent(
      role=infos['role'],
      backstory=infos['backstory'],
      goal=infos['goal'],
      allow_delegation=False,
      verbose=True,
      llm=llm
    )

  tasks={}
  tasks_load=json.loads(open("tasks.json", "r").read())
  for task_name in tasks_load:
    infos = tasks_load[task_name]
    tasks[task_name] = Task(
      description=infos['description'],
      agent=agents[infos['agent']],
      memory=True,
      final_answer='Your final answer must well formated and clear',
      expected_output=infos['expected_output'],
      output_file=f"{OUTPUT_FOLDER}/{infos['doc_title']}.txt"
    )

  return agents, tasks 


def crewai_setup(OUTPUT_FOLDER="out"):

  agents, tasks = create_crew(OUTPUT_FOLDER) 
  
  crew = Crew(
      agents=[a for a in agents.values()],
      tasks=[t for t in tasks.values()],
      verbose=True
    )
  # Get your crew to work!
  result = crew.kickoff()

  print("######################")
  return result


if __name__=="__main__":
  crewai_setup()

