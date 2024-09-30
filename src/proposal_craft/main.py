#!/usr/bin/env python
import sys
from deal_carft.crew import DealCarftCrew

# This main file is intended to be a way for your to run your
# crew locally, so refrain from adding necessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'client_needs': "The client is looking to gather information (full name, current job, background experience, past jobs, contact ,linkeding website) about a profile by its full name and company ",
        'solution_details': "The proposed solution is a crew of agents that will search throught the internet using tavily tool and put all the information together, we will also use FirecrawlScrapeTool to scrape information from the link provided by tavily.",
    }
    result = DealCarftCrew().crew().kickoff(inputs=inputs)
    print(result.tasks_output[0])
    print(result.tasks_output[1])
    print(result.tasks_output[2])
    print(result.tasks_output[3])





def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        DealCarftCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        DealCarftCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        DealCarftCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
