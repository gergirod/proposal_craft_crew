from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from crewai_tools import WebsiteSearchTool

# Uncomment the following line to use an example of a custom tool
# from deal_carft.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class DealCarftCrew():
	"""DealCarft crew"""

	@agent
	def technical_researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['technical_researcher'],
			tools=[WebsiteSearchTool()],
			verbose=True
		)

	@agent
	def solution_architect(self) -> Agent:
		return Agent(
			config=self.agents_config['solution_architect'],
			tools=[SerperDevTool()],
			verbose=True
		)
	
	@agent
	def financial_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['financial_analyst'],
			tools=[SerperDevTool()],
			verbose=True
		)
	
	@agent
	def proposal_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['proposal_writer'],
			tools=[SerperDevTool()],
			verbose=True
		)
	

	@task
	def client_industry_research_task(self) -> Task:
		return Task(
			config=self.tasks_config['client_industry_research_task'],
			agent=self.technical_researcher()
		)

	@task
	def solution_design_task(self) -> Task:
		return Task(
			config=self.tasks_config['solution_design_task'],
			agent=self.solution_architect()
		)
	
	@task
	def cost_roi_analysis_task(self) -> Task:
		return Task(
			config=self.tasks_config['cost_roi_analysis_task'],
			agent=self.financial_analyst()
		)
	
	@task
	def proposal_draft_task(self) -> Task:
		return Task(
			config=self.tasks_config['proposal_draft_task'],
			agent=self.proposal_writer()
		)
	

	@crew
	def crew(self) -> Crew:
		"""Creates the DealCarft crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)