import lmstudio as lms

class Agent:

    def __init__(self):
        self.api_host = lms.Client.find_default_local_api_host() or "http://127.0.0.1:4000"
        lms.configure_default_client(self.api_host)
        self.model = lms.llm()
        self.message = lms.Chat("You are a helpful assistant.")


    def chat(self, message):
        
        self.message.add_user_message(message)
        response = self.model.respond(self.message)
        print(response)

agent = Agent()   
agent.chat("Hello, how are you?")