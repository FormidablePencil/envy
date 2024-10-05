class CommandPrompt:
    def __init__(self):
        self.registered_commands = {}
        self.registered_prompts = {}

    def register_command(self, command_name, command_function):
        self.registered_commands[command_name] = command_function

    def register_prompt(self, prompt_name, prompt_function):
        self.registered_prompts[prompt_name] = prompt_function

    def execute_command(self, command_name, *args):
        if command_name in self.registered_commands:
            self.registered_commands[command_name](*args)
        else:
            print(f"Command '{command_name}' not found.")

    def get_registered_commands(self):
        """
        Returns a list of the currently registered commands.
        """
        return list(self.registered_commands.keys())

    def get_registered_prompts(self):
        """
        Returns a list of the currently registered prompts.
        """
        return list(self.registered_prompts.keys())

    def _display_commands(self):
        """
        Prints the list of available commands.
        """
        print("Available commands:")
        for command_name in self.registered_commands:
            print(f"- {command_name}")

    def _display_prompts(self):
        """
        Prints the list of available prompts.
        """
        print("Available prompts:")
        for prompt_name in self.registered_prompts:
            print(f"- {prompt_name}")

    def handle_user_input(self):
        """
        Prompts the user for input and executes the corresponding command or prompt.
        If the input matches a registered command, it will execute the command function.
        If the input matches a registered prompt, it will execute the prompt function.
        If the input matches neither a command nor a prompt, it will print an error message.
        """
        user_input = input("Enter command or prompt: ")
        if user_input in self.registered_commands:
            self.execute_command(user_input)
        elif user_input in self.registered_prompts:
            self.registered_prompts[user_input]()
        else:
            print("Invalid command or prompt. Please try again.")