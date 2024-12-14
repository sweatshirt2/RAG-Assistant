from services.myllm import getLLM
from utils.user_interface import (
    getMessage,
    updateSystemPersona,
    changeSystemPersona,
    interactWithLLM,
)

prompt_message = "Welcome!"

while True:
    text_input = input(
        f"{prompt_message} Enter: \n 1 for a development assistant based on your tech stack \n 2 for other help \n"
    )

    if text_input == "1":
        loop_count = 1
        print("Enter your tech stack | 0 when you finish \n")
        tech_stack = []
        while True:
            new_input = input(f"\n Tool {loop_count}: ")
            loop_count += 1
            if new_input != "0":
                tech_stack.append(new_input)
            else:
                updateSystemPersona(["This is my stack", *tech_stack])
                break

        interactWithLLM()

    elif text_input == "2":

        prompt_type = "I would like you to assist me with."
        user_assistance_input = input("What would you like me to assist you with? \n")
        model_role = "You are " + input(
            "What role should I take in the assistance process \n"
        )
        changeSystemPersona([prompt_type, user_assistance_input, model_role])

        interactWithLLM()

    else:
        prompt_message = "Wrong Input"
