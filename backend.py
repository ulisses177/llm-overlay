from langchain_community.llms import Ollama

class ChatBotBackend:
    def __init__(self, log_file="chat_log.txt"):
        self.llm = Ollama(model="llama3")
        self.log_file = log_file
        self.chat_history = self.load_chat_history()

    def load_chat_history(self):
        try:
            with open(self.log_file, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return ""

    def append_to_log(self, message):
        with open(self.log_file, 'a') as file:
            file.write(message + "\n")

    def generate_response(self, user_input):
        self.append_to_log(f"You: {user_input}")
        response = self.llm.invoke(user_input)
        self.append_to_log(f"Assistant: {response}")
        return response