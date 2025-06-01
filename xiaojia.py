import time
import numpy as np
import requests, json
from PIL import Image
import base64
from io import BytesIO
import os

def base64_to_image(base64_str):
    """将 Base64 编码转换为 PIL 图像"""
    img_data = base64.b64decode(base64_str)
    return Image.open(BytesIO(img_data))

def find_consecutive_pixels(base64_image, y_coord, target_rgb=(192, 192, 192), tolerance=15, min_consecutive=10):
    """在指定 y 坐标行查找至少 min_consecutive 个连续目标颜色的第一个 x 坐标"""
    # 加载图像并转换为 RGB 数组
    image = base64_to_image(base64_image).convert('RGB')
    img_array = np.array(image)
    # 提取指定行的像素
    row_pixels = img_array[y_coord, :, :]  # (width, 3)
    # 计算与目标颜色的欧氏距离
    diff = np.sqrt(np.sum((row_pixels - target_rgb) ** 2, axis=1))
    # 判断每个像素是否在容差范围内
    matches = diff <= tolerance
    # 查找至少 min_consecutive 个连续 True 的位置
    count = 0
    for x, match in enumerate(matches):
        if match:
            count += 1
            if count >= min_consecutive:
                return x - min_consecutive + 1  # 返回连续区域的起始 x 坐标
        else:
            count = 0
    return -1
try:
    print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )
    # requests.get("https://api.day.app/xjRYpUmoXaqbP5kLvfiACT/2024-09-14-808-不合格")
    ##提交post请求
    url = 'http://xg.hieu.edu.cn/index?'
    #打卡界
    url2 = 'http://xg.hieu.edu.cn/content/tabledata/audit/unDo?sEcho=1&iColumns=9&sColumns=%2C%2C%2C%2C%2C%2C%2C%2C&iDisplayStart=0&iDisplayLength=12&mDataProp_0=0&bSortable_0=false&mDataProp_1=1&bSortable_1=false&mDataProp_2=2&bSortable_2=true&mDataProp_3=3&bSortable_3=false&mDataProp_4=FQRXM&bSortable_4=true&mDataProp_5=FQSJ&bSortable_5=true&mDataProp_6=SYHJSHR&bSortable_6=false&mDataProp_7=SYHJBLSJ&bSortable_7=false&mDataProp_8=8&bSortable_8=false&iSortCol_0=5&sSortDir_0=desc&iSortingCols=1&shlc=&type=&bmdm=&dlzh=&xh=&yxb=&zy=&bj=&nj='

    ##登陆url
    url3 ='http://xg.hieu.edu.cn/website/login'

    ##测试验证码结果url
    url4='http://xg.hieu.edu.cn/website/verify/image/result'

    ##获取验证码图片
    url5='http://xg.hieu.edu.cn/website/verify/image'

    #销假url
    url6="http://xg.hieu.edu.cn/content/audit/audit/auditPass?"

    headers2={
    # 'Cookie':'insert_cookie=59063098; JSESSIONID=6301641DEE636034E53A550C09C3F8B7',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
    }
    # # #登录账号
    login = {'uname': '3000021013','pd_mm': os.getenv('PASSWORD')}
    session = requests.session()
    ##先获取一张图片
    data = json.loads(session.get(url5).text)

    #获取y坐标和srcimgd
    src_img = data["SrcImage"]
    y_pos = data["YPosition"]
    x_pos = find_consecutive_pixels(src_img,y_pos+8)
    verify_test= session.post(url4,headers=headers2,data={'moveEnd_X':(x_pos-12),'wbili':'0.9333333333333333'})
    # print(verify_test.text)
    home_page= session.post(url3,headers=headers2,data=login)
    main =session.get(url2)
    info = json.loads(main.text)

    #销假
    count = 0
    for i in info['aaData']:
        if i["LCMC"]== "学生销假审核":
            result = session.post(url6,headers=headers2,data={'operationType': '','shyj':'','pathFile':'','dm':i['DM'],'shzt':'1'})
            if "true" in result.text:
                count=count+1
    requests.get("https://api.day.app/xjRYpUmoXaqbP5kLvfiACT/销假成功，销假"+str(count)+"人?group=ybxj")
except Exception as e:  # 捕获所有异常
    requests.get(f"https://api.day.app/xjRYpUmoXaqbP5kLvfiACT/销假失败，错误?group=ybxj")
    print(f"发生错误: {e}")
