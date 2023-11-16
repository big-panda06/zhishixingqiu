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

    # return test_result(content)

    result = get_llm(content)

    # result = result.strip() + "\n\n" + "↓立即前往，NLP快车道↓\n<a href=\"https://u2496n442z.feishu.cn/mindnotes/OMUobgt6jmtdDJnhoz6cGM1enOf?from=from_copylink\">提前1年学好NLP</a>"
    result = result.strip() + "\n\n" + "↓↓↓\n<a href=\"https://u2496n442z.feishu.cn/mindnotes/OMUobgt6jmtdDJnhoz6cGM1enOf?from=from_copylink\">NLP快车道，提前1年学好NLP</a>"

    print('logger -> result:', result)

    return make_succ_response({"result": result})


def test_result(content):
    result = ''
    if '1' == content.strip():
        return make_succ_response({"result": result})
    if '2' == content.strip():
        # 测试无换行
        result = "测试无换行"
        return make_succ_response({"result": result})
    if '3' == content.strip():
        # 测试有换行
        result = "测试无\n换行"
        return make_succ_response({"result": result})
    if '4' == content.strip():
        # 测试长文本无换行
        result = "算法工程师没有工程能力，可以通过以下方式来提升：nnnn1. 学习基础知识：算法工程师需要具备一定的计算机科学基础知识，包括编程语言、数据结构、算法、操作系统、数据库等。可以通过自学或者参加基础课程来提升这些能力。nn2. 实践经验：实践经验对于提升工程能力非常重要。可以尝试参与一些开源项目，或者自己编写一些小项目，以此来积累实际经验。nn3. 学习和掌握编程语言：算法工程师通常需要使用一种或多种编程语言来实现算法。如果没有特定的编程语言技能，可以通过学习并掌握一种编程语言开始。nn4. 了解行业趋势：了解当前人工智能和机器学习领域的趋势和新技术，可以帮助算法工程师更好地适应工作环境，并提升工程能力。nn5. 参与团队项目：参与团队项目可以帮助算法工程师更好地理解团队协作的重要性，同时也可以通过实际操作来提升工程能力。nn6. 寻求反馈：如果需要改进自己的工程能力，可以寻求同事或导师的反馈，并积极改进自己的工作方式和方法。nn7. 持续学习和改进：算法工程师的工程能力是可以通过持续学习和改进来不断提升的。可以通过阅读相关书籍、参加培训课程、与同行交流等方式来提升自己的工程能力。nnnn总之，算法工程师可以通过学习基础知识、实践经验、掌握编程语言、了解行业趋势、参与团队项目、寻求反馈和持续学习等方式来提升自己的工程能力。"
        return make_succ_response({"result": result})
    if '5' == content.strip():
        result = "算法工程师没有工程能力，可以通过以下方式来提升：\n1. 学习基础知识：算法工程师需要具备一定的计算机科学基础知识，包括编程语言、数据结构、算法、操作系统、数据库等。可以通过自学或者参加基础课程来提升这些能力。nn2. 实践经验：实践经验对于提升工程能力非常重要。可以尝试参与一些开源项目，或者自己编写一些小项目，以此来积累实际经验。nn3. 学习和掌握编程语言：算法工程师通常需要使用一种或多种编程语言来实现算法。如果没有特定的编程语言技能，可以通过学习并掌握一种编程语言开始。nn4. 了解行业趋势：了解当前人工智能和机器学习领域的趋势和新技术，可以帮助算法工程师更好地适应工作环境，并提升工程能力。nn5. 参与团队项目：参与团队项目可以帮助算法工程师更好地理解团队协作的重要性，同时也可以通过实际操作来提升工程能力。nn6. 寻求反馈：如果需要改进自己的工程能力，可以寻求同事或导师的反馈，并积极改进自己的工作方式和方法。nn7. 持续学习和改进：算法工程师的工程能力是可以通过持续学习和改进来不断提升的。可以通过阅读相关书籍、参加培训课程、与同行交流等方式来提升自己的工程能力。nnnn总之，算法工程师可以通过学习基础知识、实践经验、掌握编程语言、了解行业趋势、参与团队项目、寻求反馈和持续学习等方式来提升自己的工程能力。"
        return make_succ_response({"result": result})

    return make_succ_response({"result": '测试'})


def get_llm(content):
    access_token = "24.6bb3f73d0f53beb79d78471e75fd7230.2592000.1702697625.282335-42777740"
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

    return response.json()['result']
