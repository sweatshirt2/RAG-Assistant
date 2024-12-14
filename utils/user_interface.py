from utils.persona import Persona
from services.myllm import getLLM

message = [
    ("system", Persona.getSystemPersona()),
    ("human", "some question"),
]


def getMessage(textInput: str):
    return [
        ("system", Persona.getSystemPersona()),
        ("human", textInput),
    ]


def updateSystemPersona(input: list[str]):
    processedDefinition = processDefinitions(input)
    Persona.definePersona(processedDefinition)


def changeSystemPersona(input: list[str]):
    processDefinitions = processDefinitions(input)
    Persona.definePersona(processDefinitions, True)


def processDefinitions(definitions: list[str]):
    """stringify list of persona definitions

    Parameters:
    definitions (list of string): the list to be parsed into string persona

    Return:
    the string form of the definitions
    """

    return " ".join(definitions)


def interactWithLLM():
    """method to handle user interaction"""

    myLLM = getLLM()

    message = [
        ("system", Persona.getSystemPersona()),
    ]

    print("You can ask your questions here \n Enter 0 to leave")
    while True:
        user_input = input()
        if user_input == "0":
            exit()
        else:
            new_message = message
            new_message.append(("human", user_input))

            print(myLLM.invoke(new_message))
