from flask import render_template, request
from run import app
from wxcloudrun.response import make_succ_empty_response, make_succ_response, make_err_response
import requests
import json


@app.route('/')
def index():
    """
    :return: 返回index页面
    """
    return render_template('index.html')


@app.route('/api/llm', methods=['GET'])
def llm():
    content = request.values.get('content')
    print('logger -> content:', content)

    result = get_llm(content)
    print('logger -> result:', result)

    return make_succ_response({"result": result})


def get_llm(content):
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/eb-instant?access_token=24.7a649d915fe0b59c319416b9d55b65e8.2592000.1702655299.282335-42777740"

    payload = json.dumps({"messages": [{"role": "user", "content": content}]})
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print('logger -> response.text:', response.text)

    return response.json()['result']
