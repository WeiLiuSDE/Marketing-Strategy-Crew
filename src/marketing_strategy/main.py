#!/usr/bin/env python
import sys
import warnings

# Update the import statement to match the new crew class name
from marketing_strategy.crew import MobilePhoneMarketingStrategy

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'Mobile Phone Marketing Strategy for 2024'
    }
    MobilePhoneMarketingStrategy().crew().kickoff(inputs=inputs)

def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "Mobile Phone Marketing Strategy for 2024"
    }
    try:
        MobilePhoneMarketingStrategy().crew().train(
            n_iterations=int(sys.argv[1]), 
            filename=sys.argv[2], 
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        MobilePhoneMarketingStrategy().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "Mobile Phone Marketing Strategy for 2024"
    }
    try:
        MobilePhoneMarketingStrategy().crew().test(
            n_iterations=int(sys.argv[1]), 
            openai_model_name=sys.argv[2], 
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == "__main__":
    run()