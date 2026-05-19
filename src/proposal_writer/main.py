import sys
from datetime import datetime

from proposal_writer.crew import ProposalWriter


def run():
    project = input(
        "\nDescribe the client project:\n\n"
    )

    inputs = {
        "project_description": project
    }



    result = (
        ProposalWriter()
        .crew()
        .kickoff(inputs=inputs)
    )

    proposal = result.tasks_output[1].raw
    pricing = result.tasks_output[2].raw

    print("\n" + "=" * 60)
    print("PROPOSAL")
    print("=" * 60)

    print(proposal)

    print("\n" + "=" * 60)
    print("PRICING")
    print("=" * 60)

    print(pricing)


def train():

    inputs = {
        "topic": "Freelancing",
        "current_year": str(
            datetime.now().year
        )
    }

    try:

        ProposalWriter().crew().train(
            n_iterations=int(sys.argv[1]),
            filename=sys.argv[2],
            inputs=inputs
        )

    except Exception as e:

        raise Exception(
            f"Training failed: {e}"
        )


def replay():

    try:

        ProposalWriter().crew().replay(
            task_id=sys.argv[1]
        )

    except Exception as e:

        raise Exception(
            f"Replay failed: {e}"
        )


def test():

    inputs = {
        "topic": "Proposal",
        "current_year": str(
            datetime.now().year
        )
    }

    try:

        ProposalWriter().crew().test(
            n_iterations=int(sys.argv[1]),
            eval_llm=sys.argv[2],
            inputs=inputs
        )

    except Exception as e:

        raise Exception(
            f"Test failed: {e}"
        )


if __name__ == "__main__":
    run()