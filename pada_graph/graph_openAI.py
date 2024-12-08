import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain_experimental.tools import PythonAstREPLTool
from langchain_experimental.tools import PythonREPLTool
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import json
import re

#.env파일로드
load_dotenv()
#키 가지고 오기
api_key=os.getenv("OPENAI_API_KEY")

#Langchain 프레임워크에서 openAI 연동
llm = ChatOpenAI(
    model="gpt-4",
    temperature=0.7,
    verbose=False,
    # agent_type="tool-calling",
    # api_key=api_key
)

# 실행 가능한 코드만 추출하는 함수
def extract_code(response_content):
    # "```"로 감싸진 코드 블록을 추출
    code_blocks = re.findall(r"```python\n(.*?)```", response_content, re.DOTALL)
    if code_blocks:
        return code_blocks[0]  # 첫 번째 코드 블록 반환
    return None  # 코드 블록이 없으면 None 반환

#client로 받은 data 가지고 오기
def graph_request(user_request,table_data)->None:

    #테이블 데이터 전처리: 결측값 0으로 처리
    # df=pd.DataFrame(table_data)
    df=pd.read_csv('./output.csv') #test용 csv 파일
    df.fillna(0, inplace=True)
    user_request="코일 ID별 Thickness_mm을 나타내는 그래프를 추천해줘."

    prompt = (
        f"You are a professional data analyst.  "
        f"[Important!]Do not create or overwrite the 'df' variable, as it already contains the data. "
        f"You must use the provided 'df' variable for any analysis or visualization. "
        f"[Important!]fulfill the user's request using only the following libraries:  matplotlib, pandas, json, os"
        f"[Important!]Do not use any other libraries or external tools."
        f"Similarly, use the provided 'plt' module for plotting. "
        f"User has requested: '{user_request}'. "
        f"And here is a preview of the data:\n{df}\n\n" 
        f"Please suggest a specific visualization chart and provide executable Python code. "
        f"The code must generate the requested chart using the 'df' variable and save it as a PNG file. "
    )
    response = llm.invoke(prompt)
    print("\n===============================================================================================\n")
    print("\nGenerated Code:\n")
    print("\n response content data \n ", response.content)   
     # 코드 실행
    # 실행 가능한 코드 추출
    code = extract_code(response.content)
    if code:
        print("\n-------------------------------------------------------------------------\n")
        print("\nExtracted Code:\n")
        print(code)  # 추출된 코드 출력

        # 추출된 코드 실행
        try:
            exec(code, {"df": df, "plt": plt})  # 'df'와 'plt'를 실행 환경에 제공
        except Exception as e:
            print(f"\nError during code execution: {e}")
    else:
        print("\nNo executable code found in the response.")


#test
if __name__ == "__main__":
    with open("./test.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    graph_request(data["user_request"], data["table_data"])


