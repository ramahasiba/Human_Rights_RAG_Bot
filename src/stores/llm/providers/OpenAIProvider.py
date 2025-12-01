from ..LLMInterface import LLMInterface
from ..LLMEnums import OpenAIEnums
from openai import OpenAI
import logging

class OpenAIProvider(LLMInterface):
    def __init__(self, api_key: str, 
                 default_input_max_characters: int, 
                 default_max_output_tokens: int, 
                 default_generation_temperature: float):
        
        self.api_key = api_key
        self.default_input_max_characters = default_input_max_characters
        self.default_max_output_tokens = default_max_output_tokens
        self.default_generation_temperature = default_generation_temperature
        self.generation_model_id = None
        
        self.client = OpenAI(api_key=self.api_key) 

        self.enums = OpenAIEnums 
        self.logger = logging.getLogger(__name__) 
 
    def set_generation_model(self, model_id: str):
        """Sets the ID of the generation model to be used."""
        self.generation_model_id = model_id
      
    def generate_text(self, prompt: str, max_output_token: int=None, temperature: float=None):
        """Generates text based on a prompt using the OpenAI model."""
        if not self.client:
            self.logger.error("OpenAI client is not initialized.")
            return None
        
        if not self.generation_model_id:
            self.logger.error("Generation model ID for openai is not set.")
            return None
        
        max_output_token = max_output_token if max_output_token is not None else self.default_max_output_tokens
        temperature = temperature if temperature is not None else self.default_generation_temperature

        response = self.client.chat.completions.create(
            model=self.generation_model_id,
            messages=[self.construct_prompt(prompt, self.enums.USER.value)],
            max_tokens=max_output_token,
            temperature=temperature
        ) 

        if (
            not response
            or not getattr(response, "choices", None)
            or len(response.choices) == 0
            or not getattr(response.choices[0], "message", None)
            or not getattr(response.choices[0].message, "content", None)
        ):
            self.logger.error("Error while generating summary with OpenAI")
            return None
        
        return response.choices[0].message.content

    def construct_prompt(self, prompt: str, role: str):
        """Constructs a prompt dictionary in the format required by the OpenAI API."""
        return {
            "role": role,
            "content": prompt
        }   