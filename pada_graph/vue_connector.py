#프론트와 연계 설정
#flask와 flask-cors 설치
#CORS요청 허용 설정
from flask import Flask,jsonify,request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Hello, Flask"
#http://127.0.0.1:5000/

@app.route('/api/graph',method=['POST'])
def receive_data():
    #vue.js에서 보낸 데이터 받기
    data =request.get_json()
    markdown = data.get('markdown') #vue에서 보낸 데이터 키
    
    #마크다운 형식으로 받을 경우
    if not markdown:
        return jsonify({'error':'No Markdown data provided'}),400
    
    try:
        result = process_markdown(markdown)
        return jsonify({'result':result})
    except Exception as e:
        return jsonify({'error':str(e)}), 500

if __name__=='__main__':
    app.run(debug=True)


