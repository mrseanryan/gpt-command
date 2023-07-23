from config__application_commander import expert_templates
import core

def test():
    chain = core.create_chain(expert_templates)

    user_test_prompts = [
        "Please make a new spreadsheet",
        "I'm working on a new budget",
        "I need a new text document",
        "I need a new paper",
        "Destroy this document",
        "I don't need this document anymore",
        "Will my project perform OK?",
        "Check the speed of my project",
        "Check the speed of my spread sheet",
        # other prompts, that should NOT be handled by the Commands:
        "what is 2 + 5 divided by 10 ?",
        "Who won the battle of Agincourt, and why was it fought?",
        "What is my favourite color?",
        ]

    for user_prompt in user_test_prompts:
        print("---")
        print(f">> {user_prompt}")
        # should route to the right 'expert' chain!
        rsp = core.execute_prompt(user_prompt, chain)
        print(rsp)
