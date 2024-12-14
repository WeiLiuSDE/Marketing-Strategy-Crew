from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class MobilePhoneMarketingStrategy():
    """Mobile Phone Marketing Strategy Crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            verbose=True
        )

    @agent
    def marketing_strategist(self) -> Agent:
        return Agent(
            config=self.agents_config['marketing_strategist'],
            verbose=True
        )

    @agent
    def product_positioning_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['product_positioning_expert'],
            verbose=True
        )

    @task
    def market_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['market_research_task'],
            output_file='market_research_report.md'
        )

    @task
    def strategy_development_task(self) -> Task:
        return Task(
            config=self.tasks_config['strategy_development_task'],
            output_file='marketing_strategy.md'
        )

    @task
    def product_positioning_task(self) -> Task:
        return Task(
            config=self.tasks_config['product_positioning_task'],
            output_file='product_positioning.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Mobile Phone Marketing Strategy crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )