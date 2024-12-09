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
def graph_request(user_request,file_path):

    #테이블 데이터 전처리: 결측값 0으로 처리
    # df=pd.DataFrame(table_data)
    # df=pd.read_csv('./output.csv') #test용 csv 파일
    df=pd.read_csv(file_path)
    df.fillna(0, inplace=True)
    # user_request="숫자형으로 된 모든 수치의 평균을 나타내는 바 그래프 그릴 방법을 추천해줘."

    prompt = (
    f"You are a professional data analyst. Your task is to analyze the given data and user's request "
    f"to recommend the most suitable visualization chart. Your response must include: "
    f"1. A recommended graph type (e.g., 'bar', 'line', 'scatter').\n"
    f"2. The x-axis labels (column names to use for the x-axis). If multiple columns are suitable, include all of them as a list.\n"
    f"3. The y-axis label (column name to use for the y-axis).\n\n"
    f"4. A suitable title for the graph written in **Korean (한글)**.\n\n"
    f"5. Provide the reason for recommending this type of graph, considering the data and user request."
    f"User request: '{user_request}'\n\n"
    f"Here is the preview of the data:\n{df.head().to_string()}\n\n"
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
    data = response.content
    print("\n response content data \n ", response.content)
    return data
    
def graphVisualization(data ):
    data = json.loads(data)
    df=pd.read_csv('./output.csv')
    # 시각화에 사용할 데이터 계산 (선택한 열의 평균)
    selected_columns = data["x_labels"]
    filtered_data = df[selected_columns]

    if '평균' in data["title"] or 'average' in data["title"]:
        filtered_data  = filtered_data.mean()
    

    # 데이터 프레임 생성
    plot_data = pd.DataFrame({
        "x_labels": selected_columns,
        "y_values": filtered_data
    })

    # # 평균 계산 함수
    # def calculate_average(df):
    #     return df["y_values"].mean()

    # # 평균 값 계산
    # overall_average = calculate_average(df)
    # print(f"Overall Average: {overall_average:.2f}")

    
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
    # plt.savefig('file_path')
    return 

    
# #test
# if __name__ == "__main__":
#     with open("./test.json", "r", encoding="utf-8") as file:
#         data = json.load(file)
#     graph_info = graph_request(data["user_request"], data["table_data"])
#     graphVisualization(graph_info)

    


