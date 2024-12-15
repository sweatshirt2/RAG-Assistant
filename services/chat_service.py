class ChatService:

    def __init__(self):
        self.input_history = []

    def newPrompt(self, human_text):
        self.input_history.append(human_text)

    def restartConversation(self):
        self.input_history = []
