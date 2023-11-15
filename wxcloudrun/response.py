import json

from flask import Response


def make_succ_empty_response():
    data = json.dumps({'err_code': 0, 'data_list': []})
    return Response(data, mimetype='application/json')


def make_succ_response(data):
    data = json.dumps({'err_code': 0, 'data_list': [data]})
    return Response(data, mimetype='application/json')


def make_err_response(err_msg):
    data = json.dumps({'err_code': -1, 'data_list': [err_msg]})
    return Response(data, mimetype='application/json')


if __name__ == '__main__':
    print(make_succ_response({"param_a": "content_a"}).response)
