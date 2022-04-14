# -*- coding: utf-8 -*-
#!/usr/bin/env python
 
import urllib
import json
import urllib.request
import requests
import random
import json
#client_id 为官网获取的AK， client_secret 为官网获取的SK
client_id ='TB4FOwDCqclPDoYXFkQaLIj9'
client_secret ='pKoLOuKWopKEQQ1QlXdh8GNYh0pupgWG'
 
#获取token
def get_token():
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + client_id + '&client_secret=' + client_secret
    request = urllib.request.Request(host)
    request.add_header('Content-Type', 'application/json; charset=UTF-8')
    response = urllib.request.urlopen(request)
    token_content = response.read()
    if token_content:
        token_info = json.loads(token_content)
        token_key = token_info['access_token']
    return token_key

def translate(q):
    token = get_token()
    url = 'https://aip.baidubce.com/rpc/2.0/mt/texttrans/v1?access_token=' + token

    #q = 'بعد إعلان واشنطن مقاطعتها أولمبياد بكين دبلوماسيا.. الصين تلوّح ...'; # example: hello
    # For list of language codes, please refer to `https://ai.baidu.com/ai-doc/MT/4kqryjku9#语种列表`
    from_lang = 'ara'; # example: en
    to_lang = 'zh'; # example: zh
    term_ids = ''; #术语库id，多个逗号隔开


    # Build request
    headers = {'Content-Type': 'application/json'}
    payload = {'q': q, 'from': from_lang, 'to': to_lang, 'termIds' : term_ids}

    # Send request
    r = requests.post(url, params=payload, headers=headers)
    result = r.json()
    return result["result"]['trans_result'][0]['dst']

