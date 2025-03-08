#OpenAi libraries for text generation and audio to text
import openai

# Set your OpenAI and ElevenLabs API key
openai.api_key = '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'


# Function to send a prompt to the AI and get a response
def ask_ai(question):
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an amicable assistant that provides short and summarized answers unless told otherwise."},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content

print(ask_ai("How many elephants would fit inside a cube with volume of 1000 cubic meters?"))

