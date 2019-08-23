# -*- coding: UTF-8 -*-

import json
import urllib

api_url = "http://openapi.tuling123.com/openapi/api/v2"
base_req = {
    "perception":
    {
        "inputText":
        {
            "text": {}
        },

        "selfInfo":
        {
            "location":
            {
                "city": "广州",
                "province": "广东",
                "street": "开创大道"
            }
        }
    },

    "userInfo":
    {
        "apiKey": "868a9779237f4766be62f5266b414d67",
        "userId": "OnlyUseAlphabet"
    }
}

def nlu_reply(new_message):  # make reply
    global base_req, api_url
    base_req['perception']['inputText']['text'] = new_message
    new_req = base_req
    new_req = json.dumps(new_req).encode('utf8')
    http_post = urllib.request.Request(api_url, data=new_req, headers={'content-type': 'application/json'})
    response = urllib.request.urlopen(http_post)
    response_str = response.read().decode('utf8')
    response_dic = json.loads(response_str)

    results_text = response_dic['results'][0]['values']['text']
    replyMsg = results_text
    return replyMsg