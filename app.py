from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/skill", methods=["POST"])
@app.route("/test", methods=["GET"])

def skill():
    print(request.json)
    if str(request.json['userRequest']['utterance']) == "퀵플라이1 응답메세지":
        data ={
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        # "simpleImage": {
                        #     "imageUrl": "https://cf.festa.io/img/2019-11-14/791369de-e762-4cc1-a341-68ce8c4a467f.png",
                        #     "altText": "HUFS 로고"
                        # }
                        "basicCard": {
                            "title": "카드의 제목",
                            "description": "상세 설명",
                            "thumbnail": {
                                "imageUrl":"https://cf.festa.io/img/2019-11-14/791369de-e762-4cc1-a341-68ce8c4a467f.png",
                                "link": {
                                    "mobile": "https://naver.com",
                                    "android": "https:google.com"
                                }
                            },
                            "buttons": [
                                {
                                    # "label": "첫번째 버튼",
                                    # "action": "webLink",
                                    # "webLinkUrl": "https://portal.azure.com"
                                    "label": "010-2500-1925에 전화걸기",
                                    "action": "phone",
                                    "phoneNumber": "010-2054-3247"
                                },
                                {
                                    "label": "공유하기",
                                    "action": "share"
                                }
                            ] 
                        }
                    }
                ]
            }
        }
    else:
        data = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": "사용자 Key: "+ str(request.json['userRequest']['utterance'])
                        }
                    }
                ],
                "quickReplies": [
                    {
                        "label": "퀵플라이1",
                        "action": "message",
                        "messageText": "퀵플라이1 응답메세지"
                    },
                    {
                        "label": "퀵플라이2",
                        "action": "message",
                        "messageText": "퀵플라이2 응답메세지"
                    },
                    {
                        "label": "퀵플라이3",
                        "action": "message",
                        "messageText": "퀵플라이3 응답메세지"
                    }
                ]
                # "outputs": [
                #     {
                #         # "simpleImage": {
                #         #     "imageUrl": "https://cf.festa.io/img/2019-11-14/791369de-e762-4cc1-a341-68ce8c4a467f.png",
                #         #     "altText": "HUFS 로고"
                #         # }
                #         "basicCard": {
                #             "title": "카드의 제목",
                #             "description": "상세 설명",
                #             "thumbnail": {
                #                 "imageUrl":"https://cf.festa.io/img/2019-11-14/791369de-e762-4cc1-a341-68ce8c4a467f.png",
                #                 "link": {
                #                     "mobile": "https://naver.com",
                #                     "android": "https:google.com"
                #                 }
                #             },
                #             "buttons": [
                #                 {
                #                     # "label": "첫번째 버튼",
                #                     # "action": "webLink",
                #                     # "webLinkUrl": "https://portal.azure.com"
                #                     "label": "010-2500-1925에 전화걸기",
                #                     "action": "phone",
                #                     "phoneNumber": "010-2054-3247"
                #                 },
                #                 {
                #                     "label": "공유하기",
                #                     "action": "share"
                #                 }
                #             ] 
                #         }
                #     }
                # ]
            }
        }
    return jsonify(data)

def test():
    data = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "간단한 텍스트 요소입니다."
                    }
                }
            ]
        }
    }
    return jsonify(data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)