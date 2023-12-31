class Command:
    def __init__(self, name, user_prompts, expert_template, description, action_function = None) -> None:
        self.name = name
        self.user_prompts = user_prompts
        self.expert_template = expert_template
        self.description = description
        # Can remove this?
        self.actionFunction = self.default_action if action_function is None  else action_function

    def default_action(self):
        print(f"Commnd {self.name} triggered")
