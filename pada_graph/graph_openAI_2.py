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
import seaborn as sns

"""
데이터 분석 LLM
작성자: 김유경
작성일: 2024.12.08
버전 : 1
"""

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

#client로 받은 data 가지고 오기
def graph_request(message,data):

    ##messageId, message, data

    if not isinstance(data, pd.DataFrame):
        return
    # Chat LLM 쪽으로 어떻게 줄 지 아니면
    # return은 서버쪽으로 줘야 할 지 고민

    #테이블 데이터 전처리: 결측값 0으로 처리
    # data=pd.DataFrame(table_data)
    # data=pd.read_csv('./output.csv') #test용 csv 파일
    # data=pd.read_csv(data)
    data.fillna(0, inplace=True)
    # message="숫자형으로 된 모든 수치의 평균을 나타내는 바 그래프 그릴 방법을 추천해줘."

    #prompt 중간: data.head().tostring -> data.head()로 나타남
    prompt = (
    f"You are a professional data analyst. Your task is to analyze the given data and user's request "
    f"to recommend the most suitable visualization chart. Your response must include: "
    f"1. A recommended graph type (e.g., 'bar', 'line', 'scatter').\n"
    f"2. The x-axis labels (column names to use for the x-axis). If multiple columns are suitable, include all of them as a list.\n"
    f"3. The y-axis label (column name to use for the y-axis).\n\n"
    f"4. A suitable title for the graph written in **Korean (한글)**.\n\n"
    f"5. Provide the reason for recommending this type of graph, considering the data and user request."
    f"User request: '{message}'\n\n"
    f"Here is the preview of the data:\n{data.head()}\n\n"
    f"Respond with a JSON object containing the following keys: "
    f"'graph_type', 'x_label', 'y_label'. Ensure your response is strictly in JSON format. For example:\n"
    f"{{\n"
    f"  \"graph_type\": \"bar\",\n"
    f"  \"x_labels\": [\"Column1\", \"Column2\"],\n"
    f"  \"y_label\": \"Column2\"\n"
    f"  \"title\": \"그래프 제목 예시 (한글)\"\n"
    f" \"reason\": Bar chart는 카테고리별로 데이터를 비교하기 적합하며, 주어진 데이터에서 'Column1'과 'Column2'는 서로 연관성이 있어 보입니다."
    f"}}\n"
)
    response = llm.invoke(prompt)
    responseLLM = response.content
    print("\n response content data \n ", response.content)
    return responseLLM, data
    
def graphVisualization(responseLLM,data):
    responseLLM = json.loads(responseLLM)
    # data=pd.read_csv('./output.csv')
    # 시각화에 사용할 데이터 계산 (선택한 열의 평균)
    selected_columns = responseLLM["x_labels"]
    filtered_data = data[selected_columns]

    if '평균' in responseLLM["title"] or 'average' in responseLLM["title"]:
        filtered_data  = filtered_data.mean()
    

    # 데이터 프레임 생성
    plot_data = pd.DataFrame({
        "x_labels": selected_columns,
        "y_values": filtered_data
    })

    
    plt.figure(figsize=(12, 8))

    if data["graph_type"] == "bar":
        sns.barplot(x="x_labels", y="y_values", data=plot_data )
    elif data["graph_type"] == "line":
        sns.lineplot(x="x_labels", y="y_values", data=plot_data )
    elif data["graph_type"] == "scatter":
        plt.scatter(plot_data["x_labels"], plot_data["y_values"])
    else:
        raise ValueError(f"Unsupported graph type: {data['graph_type']}")
    
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()
    # plt.savefig('data')
    return 

    
# #test
# if __name__ == "__main__":
#     with open("./test.json", "r", encoding="utf-8") as file:
#         data = json.load(file)
#     graph_info = graph_request(data["message"], data["table_data"])
#     graphVisualization(graph_info)

    


