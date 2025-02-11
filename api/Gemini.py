from google import genai
import os
import random
from dotenv import load_dotenv, dotenv_values

load_dotenv()

class GeminiGateway:
    client = genai.Client(api_key=os.getenv('gemini-key'))
    
    def generate_content(self, input):
        
        response = self.client.models.generate_content(
            model="gemini-1.5-flash",
            contents=input)

    def get_recommendations_based_on_collection(self, collection):
        album_titles = "Here is my collection: "
        collection = random.sample(collection, min(5, len(collection)))
        for item in collection:
            album_titles += item.name + ", "

        album_titles += "What do you recommend?" 
        return self.generate_content("Kom igen nu, ge mig några rekommendationer på plattor! Jag gillar rock")
