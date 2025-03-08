'''Import the openai library'''
import openai

'''Access the personal API'''
openai.api_key = 'secret-api-key'


'''Ask openai's gpt 4o mini a question and get a response back'''
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

