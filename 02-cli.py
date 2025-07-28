##pip install --upgrade openai

from dotenv import load_dotenv
load_dotenv() #.env 파일이 있다면, 환경변수로서 로딩 



import os 
API_KEY = os.environ["OPEN_API_KEY"]

i = 0 
i += 1
i += 2 

from openai import OpenAI
client = OpenAI(api_key=API_KEY)  # OPENAI_API_KEY 환경변수 지정이 필요

response = client.responses.create(
    model="gpt-4o",
   #  input="Write a one-sentence bedtime story about a unicorn in korean.",
    input = "make python code for factorial"
)

print("usage :", response.usage)
print(response.output_text)