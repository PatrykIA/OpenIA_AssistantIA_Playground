import os
from dotenv import load_dotenv
from openai import OpenAI
import time

load_dotenv()

# Load API key and assistant ID from .env file
API_KEY = os.getenv('OPENAI_API_KEY')
ASSISTANT_ID = os.getenv('OPENAI_ASSISTANT_ID')

# Initialize client and assistant
client = OpenAI(api_key=API_KEY)
assistant = client.beta.assistants.retrieve(ASSISTANT_ID)
thread = client.beta.threads.create()

def wait_on_run(run, thread):
    while run.status == "queued" or run.status == "in_progress":
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id,
        )
        time.sleep(0.5)
    return run

def get_assistant_response(user_input):
    # Send user message
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=user_input,
    )

    # Run assistant
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=ASSISTANT_ID,
    )

    # Wait for response
    run = wait_on_run(run, thread)

    # Get response
    messages = client.beta.threads.messages.list(
        thread_id=thread.id, order="asc", after=message.id
    )
    
    return messages.data[0].content[0].text.value

def main():
    print("Welcome to the AI assistant console! (type 'quit' to exit)")
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == 'quit':
            break
            
        response = get_assistant_response(user_input)
        print("\nAssistant:", response)

if __name__ == "__main__":
    main()