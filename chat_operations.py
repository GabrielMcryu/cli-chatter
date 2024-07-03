from file_operations import FileOperations
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory, FileChatMessageHistory
from dotenv import load_dotenv

load_dotenv()


class ChatOperations:
    def __init__(self):
        self.prompt = ""
    
    def enter_prompt(self):
        print("""
Message CLI Chatter
    """)
        max_length = 50
        while True:
            prompt = input("> ")
            self.prompt = prompt
            if not prompt:
                print('You have not entered anything. Please enter a prompt')
            else:
                if len(prompt) > max_length:
                    limited_prompt = prompt[:max_length] + '...'
                    return limited_prompt
                else:
                    return prompt
    
    def setup_chat(self):
        prompt = self.enter_prompt()
        file = FileOperations()
        file_name = file.create_chat_details(prompt)
        return file_name
    
    def start_chart(self):
        file = self.setup_chat()
        
        chat = ChatOpenAI()
        
        memory = ConversationBufferMemory(
            chat_memory=FileChatMessageHistory(file),
            memory_key="messages", 
            return_messages=True
        )
        
        prompt = ChatPromptTemplate(
            input_variables=["content", "messages"],
            messages=[
                MessagesPlaceholder(variable_name="messages"),
                HumanMessagePromptTemplate.from_template("{content}")
            ]
        )
        
        chain = LLMChain(
            llm=chat,
            prompt=prompt,
            memory=memory,
        )
        
        result = chain({'content': self.prompt})
            
        print(result['text'])
        
        while True:
            content = input(">> ")
            
            result = chain({'content': content})
            
            print(result['text'])
            
    def existing_chat(self):
        file = FileOperations()
        file.search_all_chats()

    
    
        
    