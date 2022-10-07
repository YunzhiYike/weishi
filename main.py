import json

import requests

cookie='你的微视小程序cookie'
headers = {
    'content-type': 'application/json',
    'cookie': cookie,
}


# 获取推荐视频列表
def getFeedList():
    url = 'https://api.weishi.qq.com/trpc.weishi.weishi_h5_proxy.weishi_h5_proxy/WxminiGetFeedList'
    data = {
        "req_body": {
            "requestType": 16,
            "isrefresh": 1,
            "isfirst": 1,
            "attachInfo": "",
            "scene_id": 22,
            "requestExt": {
                "mini_openid": "oWGa05LWmxEyaWWoBET2-Ic7dA6M",
                "notLogin-personid": "1645376201698315"
            }
        },
        "req_header": {
            "mapExt": "{\"imageSize\":\"480\",\"adaptScene\":\"PicHDWebpLimitScene\"}"
        }
    }
    res = requests.post(url, data=json.dumps(data), headers=headers).json()
    print(res)


def like(feed_id='79IobAKp71OzSX3uW', is_like=1):
    url = 'https://api.weishi.qq.com/trpc.weishi.weishi_h5_proxy.weishi_h5_proxy/WxMiniPostFeedDing'
    data = {
        "req_body": {
            "feed_id": feed_id,
            "dingAction": is_like
        },
        "req_header": {}
    }
    res = requests.post(url, data=json.dumps(data), headers=headers).json()
    print(res)


def comment(feed_id='79IobAKp71OzSX3uW', comment_text='关注➕我', poster_id='1645376201698315'):
    url = 'https://api.weishi.qq.com/trpc.weishi.weishi_h5_proxy.weishi_h5_proxy/WxminiPostFeedComment'
    data = {
        "req_body": {
            "feed_id": feed_id,
            "comment": {
                "wording": comment_text,
                "poster_id": poster_id,
                "receiver_id": ""
            },
            "platform": "wx"
        },
        "req_header": {}
    }
    res = requests.post(url, data=json.dumps(data), headers=headers).json()
    print(res)


# person_id被关注人ID   is_follow 1关注 2取消关注
def follow(person_id='1562596639401693', is_follow=1):
    url = 'https://api.weishi.qq.com/trpc.weishi.weishi_h5_proxy.weishi_h5_proxy/WxMiniFollow'
    data = {
        "req_body": {
            "person_id": person_id,
            "type": is_follow,
            "mainSceneID": 3
        },
        "req_header": {}
    }
    res = requests.post(url, data=json.dumps(data), headers=headers).json()
    print(res)
    return res


# 获取用户信息 personID目标用户ID
def userInfo(personID='1562596639401693'):
    url = 'https://api.weishi.qq.com/trpc.weishi.weishi_h5_proxy.weishi_h5_proxy/WxminiGetPersonalHomePage'
    data = {
        "req_body": {
            "personID": personID,
            "type": 2
        },
        "req_header": {
            "channelId": 1
        }
    }
    res = requests.post(url, data=json.dumps(data), headers=headers).json()
    print(res)
    return res

# 获取用户下所有作品 personID目标用户ID
def getPersonalFeedList(personID='1562596639401693'):
    url = 'https://api.weishi.qq.com/trpc.weishi.weishi_h5_proxy.weishi_h5_proxy/WxminiGetPersonalFeedList'
    data = {
        "req_body": {
            "personID": personID,
            "type": 1,
            "attachInfo": "",
            "pageCount": 4
        },
        "req_header": {
            "channelId": 1,
            "mapExt": "{\"imageSize\":\"480\",\"adaptScene\":\"PicHDWebpLimitScene\"}"
        }
    }
    res = requests.post(url, data=json.dumps(data), headers=headers).json()
    print(res)
    return res


if __name__ == '__main__':
    # getFeedList()
    comment()
