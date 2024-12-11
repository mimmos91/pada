#프론트와 연계 설정
#flask와 flask-cors 설치
#CORS요청 허용 설정

"""
python flask 서버
작성자: 김유경
작성일: 2024.12.06
버전 : 2 
수정내용: 데이터 받는 곳 변경
"""


from flask import Flask,jsonify,request
from flask_cors import CORS
from graph import process_data
from graph_openAI import graph_request

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Hello, Flask"
#http://127.0.0.1:5000/

# @app.route('/api/graph',methods=['POST'])
# def receive_data():
#     data =request.get_json() #messageId, message, data
#     user_request = data.get("user_request")
#     file_path=data.get("file_path") # 데이터 경로(URL)

#     if not user_request or not file_path:
#         return jsonify({'error':'No data provided'}),400
    
#     try:
#         result=process_data(data)
#         #그래프 요청 처리
#         graph_request(user_request,file_path)
#          #.graph.py로 데이터 전달.
#         result=process_data(user_request,file_path)

#         return jsonify({'result':result})
#     except Exception as e:
#         return jsonify({'error':str(e)}), 500
    
   
if __name__=='__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)


