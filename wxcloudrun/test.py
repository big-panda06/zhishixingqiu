import requests
import json

API_KEY = "APgfOUoFE2yfp0LovCKq0lRR"
SECRET_KEY = "DCEBc5je7FmPmfovOU7IRxOp7v6144SC"


def main():
    # access_token = get_access_token()
    # print('access_token:', access_token)
    access_token = "24.d6620d6a5f2ee3c49385d07b43669376.2592000.1705502699.282335-42777740"
    content = "算法工程师没有算法能力怎么办？"


    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/bloomz_7b1?access_token=" + access_token

    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": content
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.json()['result'])


def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))


if __name__ == '__main__':
    main()
