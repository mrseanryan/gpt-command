from config__application_commander import expert_templates
import main

chain = main.create_chain(expert_templates)

input_prompt = "How can I help you with your project? >"
user_prompt = input(input_prompt)
while(user_prompt != None and len(user_prompt) > 0):
    print("---")
    print(f">> {user_prompt}")
    # should route to the right 'expert' chain!
    rsp = main.execute_prompt(user_prompt, chain)
    print(rsp)
    user_prompt = input(input_prompt)
