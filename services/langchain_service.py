from langchain_groq import ChatGroq
from utils.constants import LLM_KEY
from utils.persona import Persona
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory


class LangChainService:

    def __init__(self):
        self.llm_instance = ChatGroq(
            model="llama3-8b-8192",
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=3,
            api_key=LLM_KEY,
        )
        self.system_persona = " ".join(
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
        self.__initializeMemory()
        self.__initializeChatPersona()

    def __initializeMemory(self):
        self.memory = self.memory = ConversationBufferMemory()
        self.prompt_template = PromptTemplate(
            input_variables=["user_input"], template="User: {user_input}"
        )
        self.llm_chain = LLMChain(
            llm=self.llm_instance, prompt=self.prompt_template, memory=self.memory
        )

    def __initializeChatPersona(self):
        self.llm_chain.run(user_input=self.system_persona)

    def processDefinitions(definitions: list[str]):

        return " ".join(definitions)

    def updateSystemPersona(self, input: list[str], is_redefined=True):
        definition = self.processDefinitions(input)
        self.system_persona = (
            definition if is_redefined else self.system_persona + definition
        )

    def promptLLMResponse(self, human_input: str):
        message = [
            ("system", self.system_persona),
            ("human", human_input),
        ]

        # return self.llm_instance.invoke(message)
        return self.llm_chain.run(user_input=message)
