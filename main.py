from services.myllm import getLLM
from utils.user_interface import (
    getMessage,
    updateSystemPersona,
    changeSystemPersona,
    interactWithLLM,
)

myLLM = getLLM()

print("")

ai_mssg = myLLM.invoke(getMessage("who are you"))
print(ai_mssg)

while True:
    text_input = input(
        "Welcome! Enter: \n 1 for a development assistant based on your tech stack \n 2 for other help \n"
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
