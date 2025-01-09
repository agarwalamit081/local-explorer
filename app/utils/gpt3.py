import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the OpenAI client
client = OpenAI(api_key=os.getenv('GPT3_API_KEY'))

def get_activity_suggestion(weather):
    """
    Generate activity suggestions based on the weather using OpenAI's GPT-3.5 Turbo.
    Explicitly request 2 outdoor and 2 indoor activities in a structured format.
    """
    prompt = (
        f"The weather is {weather['description']} with a temperature of {weather['temperature']}°C. "
        "Suggest 2 outdoor activities and 2 indoor activities. "
        "For each activity, provide a name and a brief description. "
        "Format the response as follows:\n"
        "1. Outdoor: [Activity Name] - [Description]\n"
        "2. Outdoor: [Activity Name] - [Description]\n"
        "3. Indoor: [Activity Name] - [Description]\n"
        "4. Indoor: [Activity Name] - [Description]"
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that suggests activities based on the weather."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300,  # Increase token limit for longer responses
        n=1,  # Number of suggestions
        stop=None,  # No specific stop sequence
        temperature=0.7,  # Controls randomness (0 = deterministic, 1 = creative)
    )
    suggestion = response.choices[0].message.content.strip()
    return suggestion
