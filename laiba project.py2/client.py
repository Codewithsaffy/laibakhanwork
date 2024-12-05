import openai
from openai import OpenAI
# client = OpenAI()

client = OpenAI(
  api_Key="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",
)
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role":"system","content":"You are a virtual assistant name jarvis skilled in general tasks like alexa and google cloud"},
    {"role":"user","content":"what is coading"},
  ]
)
print(completion.choices[0].message .content)
