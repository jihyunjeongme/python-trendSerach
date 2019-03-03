<h1 align="center">
  <br>
  <a href="https://developers.naver.com/docs/datalab/search/#python"><img src="https://user-images.githubusercontent.com/43984584/53692263-e02bc400-3dcf-11e9-983c-0cf6fefc3ac2.png" alt="Markdownify" width=""></a>
  <br>
  
  <br>
</h1>

<h1 align="center"> 네이버 API를 사용하여 검색 트렌드 알아보기
</p>

# Overview

- 대상: 파이썬 기본, HTML 초급, jupyter notebook 기본, 파이썬 외부모듈의 이해, Anaconda(miniconda) 기초를 가지고 있는 분에게 권장합니다.
- 목표: 네이버 API를 활용하여 특정 검색어의 트렌드를 확인해봅니다.

## 네이버 API Overview

<img src="https://user-images.githubusercontent.com/43984584/53692263-e02bc400-3dcf-11e9-983c-0cf6fefc3ac2.png">

## Step

- [NAVER Developers](https://developers.naver.com/products/datalab/) 에 접속 합니다.

  <img src="https://user-images.githubusercontent.com/43984584/53692411-c2139300-3dd2-11e9-81a3-99c7e2f4a8d1.png">

- 오픈 API 이용 신청을 누르고, `애플리케이션 이름`을 작성하고, `WEB 설정`에서 localhost인 `http://127.0.0.1`을 입력한 후 `등록하기`를 클릭합니다.
- `Application` 로 가보면 생성한 Application을 확인 할 수 있습니다.
- `애플리케이션 정보` 에 보면 `Client ID` , `Client Secret`을 확인 한 후 app.py에 입력을 해줍니다.
- `keyword`에 북미정상회담을 넣고 나머지 옵션 부분은 NAVER API Document를 참고하여 설정해줍니다.
- 소스코드를 실행시켜 결과 값을 확인 합니다.
- 해당 결과 값중 필요한 년도와 결과 값만을 `jupyter notebook`을 사용하여 아래와 같이 입력 해 줍니다.
- 확인 한 결과 값을 바탕으로 `jupyter notebook`을 사용해서 그래프를 아래와 같이 그려봅니다.

## 소스코드

```bash
# -*- coding: utf-8 -*-
import os
import sys
import urllib.request
import json
import pprint

client_id = "***Ax_loNWh6muXFz9nVi9B***wsd"
client_secret = "***r0zIdpxwud***wsd"
url = "https://openapi.naver.com/v1/datalab/search"
body = '{"startDate":"2016-01-01","endDate":"2019-02-28","timeUnit":"month","keywordGroups":[{"groupName":"북미정상회담","keywords":["북미정상회담"]}],"device":"","ages":["1","2","3","4","5","6","7","8","9","10","11"],"gender":""}'

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
request.add_header("Content-Type", "application/json")
response = urllib.request.urlopen(request, data=body.encode("utf-8"))
rescode = response.getcode()
if rescode == 200:
    response_body = response.read()
    print(response_body.decode("utf-8"))
else:
    print("Error Code:" + rescode)
```

```bash
import pandas as pd
from matplotlib import pyplot as plt

df = pd.DataFrame([
  {
    "period": "2016-06-01",
    "ratio": 0.00052
  },
  {
    "period": "2017-04-01",
    "ratio": 0.00073
  },
  {
    "period": "2017-05-01",
    "ratio": 0.00811
  },
  {
    "period": "2017-08-01",
    "ratio": 0.00026
  },
  {
    "period": "2018-02-01",
    "ratio": 0.00141
  },
  {
    "period": "2018-03-01",
    "ratio": 10.55092
  },
  {
    "period": "2018-04-01",
    "ratio": 8.06896
  },
  {
    "period": "2018-05-01",
    "ratio": 100
  },
  {
    "period": "2018-06-01",
    "ratio": 91.11174
  },
  {
    "period": "2018-07-01",
    "ratio": 0.92689
  },
  {
    "period": "2018-08-01",
    "ratio": 0.75854
  },
  {
    "period": "2018-09-01",
    "ratio": 1.02529
  },
  {
    "period": "2018-10-01",
    "ratio": 1.33397
  },
  {
    "period": "2018-11-01",
    "ratio": 0.8905
  },
  {
    "period": "2018-12-01",
    "ratio": 0.86725
  },
  {
    "period": "2019-01-01",
    "ratio": 4.14981
  },
  {
    "period": "2019-02-01",
    "ratio": 13.29894
  }
]
)
#   , columns=["period","ratio"])


df.plot.line()

```

## 결과물

```bash
{"startDate":"2016-01-01","endDate":"2019-02-28","timeUnit":"month","results":[{"title":"북미정상회담","keywords":["북미정상회담"],"data":[{"period":"2016-06-01","ratio":0.00052},{"period":"2017-04-01","ratio":0.00073},{"period":"2017-05-01","ratio":0.00811},{"period":"2017-08-01","ratio":0.00026},{"period":"2018-02-01","ratio":0.00141},{"period":"2018-03-01","ratio":10.55092},{"period":"2018-04-01","ratio":8.06896},{"period":"2018-05-01","ratio":100},{"period":"2018-06-01","ratio":91.11174},{"period":"2018-07-01","ratio":0.92689},{"period":"2018-08-01","ratio":0.75854},{"period":"2018-09-01","ratio":1.02529},{"period":"2018-10-01","ratio":1.33397},{"period":"2018-11-01","ratio":0.8905},{"period":"2018-12-01","ratio":0.86725},{"period":"2019-01-01","ratio":4.14981},{"period":"2019-02-01","ratio":27.52107}]}]}
```

<img src="https://user-images.githubusercontent.com/43984584/53606957-1ca8c580-3c00-11e9-9691-29ea729b1e98.png">

## Conclusion

- 데이터를 분석해보면 `{"period":"2018-05-01","ratio":100}` 2018년 5월 가장 검색이 많았으면 확인 할 수 있습니다. 이유는 5월에 북미정상회담에 대한 이슈들이 가장 많았기 때문이라고 추측할 수 있습니다. 또한 최근들어 그래프가 상승하는 이유는 북미정상회담이 2019년 2월 베트남에서 열린것과 연관되어 있다고 볼수 있습니다.
  <img src="https://user-images.githubusercontent.com/43984584/53692557-8201df80-3dd5-11e9-936a-40f1f7a4b560.png">
- 출처 : [2018 북미정상회담,위키백과](https://ko.wikipedia.org/wiki/2018%EB%85%84_%EB%B6%81%EB%AF%B8%EC%A0%95%EC%83%81%ED%9A%8C%EB%8B%B4)

## 기타 문의

- 블로그 : https://stophyun.tistory.com/
- 이메일: stophyuni@gmail.com
- 궁금한 사항은 이메일로 부담없이 보내주세요.
