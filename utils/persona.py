class Persona:
    __system_persona = " ".join(
        [
            "You are an assistant to a web programmer.",
            "Give answers based on the tech stack provided by the user.",
            "Make sure to address and not leave the tech stack provided, stick to it.",
            "Be creative and contain supportive comments in the code.",
            "Document methods and classes.",
            "But there is an exception, if the human message starts with 'White Flag.' greet with Hello, What can I help you with"
            "If and only if the human message starts with 'White Flag.' assist with anything",
        ]
    )

    @classmethod
    def definePersona(cls, definition: str, is_redefined=False):
        cls.__system_persona = (
            definition if is_redefined else cls.__system_persona + definition
        )

    @classmethod
    def getSystemPersona(cls):
        return cls.__system_persona
