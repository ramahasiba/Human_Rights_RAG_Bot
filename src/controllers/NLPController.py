from .BaseController import BaseController  
from langchain_core.prompts import ChatPromptTemplate 
 
class NLPController(BaseController):
        def __init__(self, generation_client, template_parser):
            super().__init__() 
            self.generation_client = generation_client 
            self.template_parser = template_parser 

        def generate_response(self, page_content: str, max_length, key_highlights_count):
            # Get prompts from the template parser
            system_prompt = self.template_parser.get("answer","system_prompt")
            body_prompt = self.template_parser.get("answer", "answer_prompt", 
                {"page_content": page_content}
            )
            
            # Build a prompt template 
            prompt = ChatPromptTemplate.from_messages([
                ("system", "{system_prompt}"),
                ("user", "{body_prompt}"),
            ])

            # Turn the LLM into a structured-output LLM for SummaryItems
            # implement answer generation code here
  
            return ""