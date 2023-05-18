import openai as ai
import openai as ai2



History = ""

prompt = """Assume the role of an expert in the characters, scenarios, locations, and plot of the D&D adventure The Lost Mine of Phandelver. As an expert be my Dungeon Master in a roleplaying game based on this adventure. Give a narrative description of everything that follows, based on my actions, in the style of R.A Salvatore, without taking control of me or my character. Also, give suitable names for characters and places. I’m in a tavern meeting with my employer. What does he say to me?"""
model = "text-davinci-003"
temperature = 0.5
max_tokens = 1000

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
