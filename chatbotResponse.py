from langchain import PromptTemplate
from langchain.llms import OpenAI
import openai
from langchain.llms import OpenAIChat

from langchain import PromptTemplate
from langchain import HuggingFaceHub, LLMChain

# openai.api_key = open("key.txt", "r").read().strip("\n")


openai.api_key = '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'
# gpt_35 = OpenAIChat(model_name='gpt-3.5-turbo', openai_api_key="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" )






message_history = [
        {"role": "user", "content": f"You are a helpful AI Company HR. Your task is to respond to queries. Your queries include topics related to office location, office employee capacity and team status, What are the services the company mainly focuses on, etc. If you understand, say OK."},
        {"role": "assistant", "content": f"OK"}
        ]

def predict(input):
    # print(message_history)
    message_history.append({"role": "user", "content": f"{input}"})

    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo", #$0.002 per 1k tokens
      messages=message_history
    )
    reply_content = completion.choices[0].message.content   #.replace('```python', '<pre>').replace('```', '</pre>')
    message_history.append({"role": "assistant", "content": f"{reply_content}"}) 
    response = [(message_history[i]["content"], message_history[i+1]["content"]) for i in range(2, len(message_history)-1, 2)]  # convert to tuples of list
    # print(message_history)
    return message_history









def processMessage(msg):

    # print(msg)
    result=predict(msg)


    # print(result)




    return result