from langchain import PromptTemplate
from langchain.chains import llm
from langchain.chains.summarize import load_summarize_chain
from langchain.llms import OpenAI
import openai
from langchain.llms import OpenAIChat

from langchain import PromptTemplate
from langchain import HuggingFaceHub, LLMChain

# openai.api_key = open("key.txt", "r").read().strip("\n")

from langchain.document_loaders.text import TextLoader
#
# def summarize_text(text_content):
#     loader = TextLoader(text_content)
#     docs = loader.load_and_split()
#     # Assuming you have already initialized and set up the 'llm' language model
#     chain = load_summarize_chain(llm, chain_type="map_reduce")
#     summary = chain.run(docs)
#
#     return summary

message_history = [
            {"role": "user", "content": f"You are a helpful AI Company HR. Your task is to respond to queries. Your queries include topics related to office location, office employee capacity and team status, What are the services the company mainly focuses on, etc. If you understand, say OK."},
            {"role": "assistant", "content": f"OK"}
        ]

openai.api_key = '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'
def summarize_text_my_func(text):
    # Use OpenAI GPT-3.5 model to generate a summary
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=text,
        max_tokens=100,
        temperature=0.7
    )
    summary = response.choices[0].text.strip()

    return summary

def summarize_text(message_history):
    for msg in message_history:
        if 'content' in msg and isinstance(msg['content'], str):
            content = msg['content']
            # print("hA ETAO pailam tooooo")
            # Load the summarization chain and run it on the text content
            summary = summarize_text_my_func(content)
            # print("EIKHANE SHOMOSSHA KORTESE NAKI??")
            msg['content'] = summary

    # print(message_history)
    return message_history

# gpt_35 = OpenAIChat(model_name='gpt-3.5-turbo', openai_api_key="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" )


def predict(input):
    # print(message_history)
    message_history.append({"role": "user", "content": f"{input}"})

    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo", #$0.002 per 1k tokens
      messages=message_history
    )
    reply_content = completion.choices[0].message.content   #.replace('```python', '<pre>').replace('```', '</pre>')
    message_history.append({"role": "assistant", "content": f"{reply_content}"})

    # return message_history
    summarize_history = summarize_text(message_history)
    response = [(message_history[i]["content"], message_history[i+1]["content"]) for i in range(2, len(message_history)-1, 2)]  # convert to tuples of list
    return summarize_history
    # print(summarize_history)
    # return summarize_history

def process_the_message(msg):

    # print(msg)
    result=predict(msg)

    # print(result)

    return result




NON_Summarize_response = [
    {
        "role": "user",
        "content": "You are a helpful AI Company HR. Your task is to respond to queries. Your queries include topics related to office location, office employee capacity and team status, What are the services the company mainly focuses on, etc. If you understand, say OK."
    },
    {
        "role": "assistant",
        "content": "OK"
    },
    {
        "role": "user",
        "content": "Give me an AI hackathon winning Idea"
    },
    {
        "role": "assistant",
        "content": "Sure! An AI hackathon winning idea could be to develop an intelligent virtual assistant for personal finance management. The virtual assistant could use machine learning algorithms to analyze users' spending patterns, provide real-time budgeting suggestions, recommend investment options, and give personalized financial advice. It could also leverage natural language processing to understand users' financial goals and automatically create personalized savings and investment plans. This idea combines the power of AI with the practical need for financial management, making it a strong candidate for a hackathon."
    }
]



Summarize_response =  [
    {
        "role": "user",
        "content": "{\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tLog_Error(\"Start ASIO failed\");\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tm_pASIO->Close();\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tm_pASIO = NULL;"
    },
    {
        "role": "assistant",
        "content": "msg)\n\t\thttp.Error(w, msg, http.StatusBadRequest)\n\t\treturn\n\t}\n\tif item.ID == \"\" {\n\t\titem.ID = id\n\t}\n\tif item.ID != id {\n\t\tmsg := fmt.Sprintf(\"Invalid item id: %s, expected: %s\", item.ID, id)\n\t\tlog.Println(msg)\n\t\thttp.Error("
    },
    {
        "role": "user",
        "content": "The media can have a positive or negative impact on public opinion. It can be used to raise awareness of issues and promote discussion and debate. It can also be used to manipulate public opinion for political or commercial gain.\n\nThe media is not always impartial. It can be biased, either intentionally or unintentionally. This can lead to distorted or incomplete information being presented to the public.\n\nThe media can have a significant impact on our society. It can shape our opinions and beliefs, and"
    },
    {
        "role": "assistant",
        "content": ". Our customers are the focus of everything we do and we strive to offer the best possible service to meet the demands of today’s business environment.\n\nA-Z are an ISO9001 accredited company and are proud to have earned the reputation of being one of the UK’s leading suppliers of office furniture.\n\nWe offer an extensive range of products and services to our customers including:\n\nFree on-site surveys\n\nFree office layouts\n\nA huge range of"
    },
    {
        "role": "user",
        "content": ""
    },
    {
        "role": "assistant",
        "content": "package com.chengdai.cdd.aoptest;\n\nimport android.os.Bundle;\nimport android.support.v7.app.AppCompatActivity;\nimport android.widget.Toast;\n\nimport com.chengdai.cdd.aoptest.aspect.CheckNetAspect;\n\npublic class MainActivity extends AppCompatActivity {\n\n    @Override\n    protected void onCreate(Bundle savedInstance"
    },
    {
        "role": "user",
        "content": "Design a bot that can beat a professional human player at a game such as Go, chess, or poker."
    },
    {
        "role": "assistant",
        "content": ""
    }
]