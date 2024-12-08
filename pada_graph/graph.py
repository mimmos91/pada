import torch
from transformers import AutoModel,AutoModelForCausalLM, AutoTokenizer
from transformers import pipeline
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import re, json

def extract_code(response_content):
    # "```"로 감싸진 코드 블록을 추출
    code_blocks = re.findall(r"```python\n(.*?)```", response_content, re.DOTALL)
    if code_blocks:
        return code_blocks[0]  # 첫 번째 코드 블록 반환
    return None  # 코드 블록이 없으면 None 반환

def process_data(user_request,table_data)->None:
    
    #데이터 준비
    # df=pd.DataFrame(table_data)
    df = pd.read_csv('./output.csv')  # 테스트용 CSV 파일
    df.fillna(0, inplace=True)

    # Transformers 모델 설정
    model_name="EleutherAI/gpt-j-6B"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    # nlp = pipeline(
    #     "text-generation",
    #     model="./gpt-neo-1.3B",  # 사용할 모델
    #     tokenizer="./gpt-neo-1.3B",
    #     # device=0 if torch.cuda.is_available() else -1
    # )

    nlp = pipeline(
         "text-generation",
        model=model,  # 사용할 모델
        tokenizer=tokenizer,
        # device=0 if torch.cuda.is_available() else -1
    )    

    prompt = (
        f"You are a professional data analyst. "
        f"[Important!] Do not create or overwrite the 'df' variable, as it already contains the data. "
        f"You must use the provided 'df' variable for any analysis or visualization. "
        f"[Important!] Fulfill the user's request using only the following libraries: matplotlib, pandas, torch, transformers. "
        f"[Important!] Do not use any other libraries or external tools. "
        f"User has requested: '{user_request}'. "
        f"And here is a preview of the data:\n{df}\n\n"
        f"Please suggest a specific visualization chart and provide executable Python code. "
        f"The code must generate the requested chart using the 'df' variable and save it as a PNG file. "
    )

    response = nlp(prompt, max_length=512)[0]['generated_text']
    print("\n===============================================================================================\n")
    print("\nGenerated Code:\n")
    print("\nResponse content data:\n", response)

    # 실행 가능한 코드 추출
    code = extract_code(response)
    if code:
        print("\n-------------------------------------------------------------------------\n")
        print("\nExtracted Code:\n")
        print(code)  # 추출된 코드 출력

        # 추출된 코드 실행
        try:
            exec(code, {"df": df, "plt": plt, "torch": torch})  # 'df', 'plt', 'torch'를 실행 환경에 제공
        except Exception as e:
            print(f"\nError during code execution: {e}")
    else:
        print("\nNo executable code found in the response.")


# 테스트
if __name__ == "__main__":
    with open("./test.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    process_data(data["user_request"], data["table_data"])