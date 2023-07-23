from config__application_commander import expert_templates
import main

def test():
    chain = main.create_chain(expert_templates)

    user_test_prompts = [
        "Please make a new spreadsheet",
        "Destroy this document",
        # other prompts, that should NOT be handled by the Commands:
        "what is 2 + 5 divided by 10 ?",
        "Who won the battle of Agincourt, and why was it fought?",
        "What is my favourite color?",
        ]

    for user_prompt in user_test_prompts:
        print("---")
        print(user_prompt)
        # should route to the right 'expert' chain!
        rsp = main.execute_prompt(user_prompt, chain)
        print(rsp)
