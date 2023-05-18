import openai as ai
import openai as ai2

ai.api_key = "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"
ai2.api_key = "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"

History = ""

prompt = """Be my Dungeon Master in a Dungeons and Dragons game that’s based on Conan the Barbarian. 
Assume the role of an expert on the works and literary style of Robert E. Howard. 
The adventure takes place in a port city on the Black coast. Give a narrative description of everything that follows, based on my actions, in the style of a Robert E. Howard novel, and without taking control of me or my character. 
Also provide suitable names for other characters and places. I arrive in the port city on the Black Coast. What is the city’s name and what do I see as I arrive?"""
model = "text-davinci-002"
temperature = 0.5
max_tokens = 100

response = ai.Completion.create(
    engine=model,
    prompt=prompt,
    temperature=temperature,
    max_tokens=max_tokens
)
History += response.choices[0].text
print(response.choices[0].text.replace(".", ".\n"))
summary = ""

summary = ai2.ChatCompletion.create(
    model="gpt-3.5-turbo",
    max_tokens=100,
    temperature=0.7,
    top_p=0.5,
    frequency_penalty=0.5,
    messages=[
        {
          "role": "system",
          "content": "You are a helpful assistant for text summarization.",
        },
        {
          "role": "user",
          "content": f"Summarize this : {History}",
        },
    ],
)

for x in range(10):
  prompt = input(">>")
  History += prompt

  response = ai.Completion.create(
    engine=model,
    prompt=summary.choices[0].message.content + " " + prompt,
    temperature=temperature,
    max_tokens=max_tokens
  ) 
  print(response.choices[0].text)
  History += response.choices[0].text
  summary = ai2.ChatCompletion.create(
    model="gpt-3.5-turbo",
    max_tokens=100,
    temperature=0.7,
    top_p=0.5,
    frequency_penalty=0.5,
    messages=[
        {
          "role": "system",
          "content": "You are a helpful assistant for text summarization.",
        },
        {
          "role": "user",
          "content": f"Summarize this : {History}"
        },
    ],
  )
