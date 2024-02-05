from openai import OpenAI

import win32com.client

client = OpenAI(api_key="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")

completion = client.chat.completions.create(
  model= "gpt-3.5-turbo",
  messages=[
    {"role" : "system" , "content" : "what is recursion in programming"},


  ],
  temperature=0.7,
  max_tokens=50,
  frequency_penalty=0,
  presence_penalty=0
)

speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Speak(completion.choices[0].message.content)



