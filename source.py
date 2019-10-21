#百度通用翻译API,不包含词典、tts语音合成等资源，如有相关需求请联系translate_api@baidu.com
# coding=utf-8

# TranslateFunction
def printError(qq):
    import http.client
    import hashlib
    from urllib import parse
    import random
    import json
    appid = ''  # 填写你的appid
    secretKey = ''  # 填写你的密钥
    httpClient = None
    myurl = '/api/trans/vip/translate'

    fromLang = 'auto'   #原文语种
    toLang = 'zh'   #译文语种
    salt = random.randint(32768, 65536)
    q=str(qq)
    sign = appid + str(q) + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    #myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign
    myurl = myurl + '?appid=' + appid + '&q=' + parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign

    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)

        # response是HTTPResponse对象
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)
        # print(type(result))
        #print (result)
        #
        # print (type(result['trans_result']))
        print ('Error:'+result['trans_result'][0]['src'],end=': ')
        print (result['trans_result'][0]['dst'])

    except Exception as e:
        print (e)
    finally:
        if httpClient:
            httpClient.close()

# 例子:
try:
    5/0

except Exception as e:
    #print(e)
    printError(e)
    pass
