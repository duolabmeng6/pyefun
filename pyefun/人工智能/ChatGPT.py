import openai

def 聊天机器人(api_key,聊天内容):
  openai.api_key = api_key
  model_engine = "text-davinci-003"
  # model_engine = "text-davinci-002"
  # engine_name = "davinci-codex"
  response = openai.Completion.create(
    engine=model_engine,
    prompt=聊天内容,
    max_tokens=256,
    temperature=0.9,
    n = 1,
    stop=None,
  )
  print(response)
  message = response.choices[0].text.strip()
  return message
