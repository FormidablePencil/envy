import datetime

class CodeGenerator:
    def generate_code(self, parsed_prompt):
        # Generate the corresponding code based on the parsed prompt information
        code = ""

        if parsed_prompt['functionality'] == 'todo_list':
            code = self.generate_todo_list_code(parsed_prompt)
        elif parsed_prompt['functionality'] == 'calculator':
            code = self.generate_calculator_code(parsed_prompt)
        else:
            code = self.generate_default_code(parsed_prompt)

        return code

    def generate_todo_list_code(self, parsed_prompt):
        code = f"""
import datetime

class TodoList:
    def __init__(self, title):
        self.title = title
        self.items = []
        self.created_at = datetime.datetime.now()

    def add_item(self, item):
        self.items.append(item)

    def __str__(self):
        output = f"{{self.title}} (created {datetime.datetime.now().strftime('%Y-%m-%d')})"
        for todo_item in self.items:
            output += f"\n- {todo_item}"
        return output

todo_list = TodoList('{parsed_prompt["title"]}')
{', '.join([f"todo_list.add_item('{item}')" for item in parsed_prompt['items']])}
print(todo_list)
"""
        return code

    def generate_calculator_code(self, parsed_prompt):
        code = f"""
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

calculator = Calculator()
print(calculator.add({parsed_prompt['a']}, {parsed_prompt['b']}))
print(calculator.subtract({parsed_prompt['a']}, {parsed_prompt['b']}))
print(calculator.multiply({parsed_prompt['a']}, {parsed_prompt['b']}))
print(calculator.divide({parsed_prompt['a']}, {parsed_prompt['b']}))
"""
        return code

    def generate_default_code(self, parsed_prompt):
        # Generate a default code structure if the functionality is not recognized
        code = f"""
# Generated code for functionality: {parsed_prompt['functionality']}
print("This is a default code structure.")
"""
        return code