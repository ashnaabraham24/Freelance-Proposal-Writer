from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

from proposal_writer.tools.timeline_validator import TimelineValidator


@CrewBase
class ProposalWriter():

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def project_analyzer(self):

        return Agent(
            config=self.agents_config["project_analyzer"],
            verbose=True
        )

    @agent
    def proposal_writer(self):

        return Agent(
            config=self.agents_config["proposal_writer"],
            verbose=True,
            tools=[TimelineValidator()]
        )

    @agent
    def pricing_strategist(self):

        return Agent(
            config=self.agents_config["pricing_strategist"],
            verbose=True
        )

    @task
    def analyze_project(self):

        return Task(
            config=self.tasks_config["analyze_project"]
        )

    @task
    def write_proposal(self):

        return Task(
            config=self.tasks_config["write_proposal"]
        )

    @task
    def create_pricing(self):

        return Task(
            config=self.tasks_config["create_pricing"],
            # output_file="output/proposal.md"
        )

    @crew
    def crew(self):

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )