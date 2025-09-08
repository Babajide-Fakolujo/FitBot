import openai
import os
from dotenv import load_dotenv

# Load environment variables from config.env file
load_dotenv('config.env')

# Get API key from environment variable
api_key = os.getenv('OPENAI_API_KEY')

if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables. Please check your config.env file.")

client = openai.OpenAI(api_key=api_key)

def chatter(messages):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )
    
    reply = response.choices[0].message.content.strip() if response.choices[0].message.content else "Sorry, I couldn't process that."
    messages=[{"role": "assistant", "content": reply}]
    return reply

if __name__ == "__main__":
    messages = [{"role" : "system", "content": "Your Name is FitBot whenever asked make sure your you say FitBot is you named", "content": "The Person who created NextRep is Babajide Fakolujo he is from Providence Rhode Island and he is very passionate about fitness", "content": "Anytime your promoted about something no fitness related answer but make your answer have some analogy to fitness and in the end ask if they want to contiue talking about fitness because your main goal is to be a fitness bot"}]
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break
        messages.append({"role": "user", "content": user_input})
        response = chatter(messages)
        print("FitBot: ", response)
        