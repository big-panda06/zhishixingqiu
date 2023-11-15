import requests
import json

def get_llm(content):
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/eb-instant?access_token=24.7a649d915fe0b59c319416b9d55b65e8.2592000.1702655299.282335-42777740"

    payload = json.dumps({"messages": [{"role": "user", "content": content}]})
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json()['result']


if __name__ == '__main__':
    print(get_llm("介绍一下自己"))