import requests, json
from PIL import Image
from io import BytesIO
import time
import ddddocr


def find_consecutive_pixels(image2):
    """在指定 y 坐标行查找至少 min_consecutive 个连续目标颜色的第一个 x 坐标"""
    # 加载图像并转换为 RGB 数组
    image = Image.open(BytesIO(image2))
    ocr = ddddocr.DdddOcr(show_ad=False)
    result = ocr.classification(image2)
    print(result)
    return result
# requests.get("https://api.day.app/xjRYpUmoXaqbP5kLvfiACT/2024-09-14-808-不合格")
##提交post请求
try:
    url = 'http://xg.hieu.edu.cn/gygl/index?'
    # 获取不合格
    url2 = 'http://xg.hieu.edu.cn/gygl/content/tabledata/dormManage/hygiene/hygieneRectify?iSortingCols=1&identity=fdy&status=0'
    ##登陆url
    url3 = 'http://xg.hieu.edu.cn/gygl/website/login'

    ##测试验证码结果url
    # url4 = 'http://xg.hieu.edu.cn/gygl/website/verify/image/result'

    ##获取验证码图片
    url5 = 'http://xg.hieu.edu.cn/gygl/website/servlet/generatevalidatecode?'

    headers2={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
    }
    #登录账号

    #a1167ae78fbb1770d6c080d8f6791a1e
    session = requests.session()
    ##先获取一张图片
    data =session.get(url5)
    otp = find_consecutive_pixels(data.content)
    login = {'uname': '3000021013', 'pd_mm': '949c5aa96fbaaccbf2beeee610d0da8a', 'randnumber': otp}
    home_page= session.post(url3,headers=headers2,data=login)
    query =session.get(url2).text
    # {"sEcho":1,"iDisplayStart":0,"iDisplayLength":10,"iSortColList":[],"sSortDirList":[],"iTotalRecords":6,"iTotalDisplayRecords":6,"aaData":[{"REDFLAG":"1","DF":30,"FJ":"509","ZGRQ":"2025-03-09","HAS_FILE":"1","SSXX":"南3栋 第5层 509","DJ":"基本合格","SS_M":"16462092582113791635","DM":"17414187336306342077","XQ_M":"2","LBMC":"宿舍卫生","ZG_M":"17414989550141115440","DY":null,"XN":"2024","LB":"wsjc","LC":"第5层","SSLMC":"南3栋","JCRQ":"2025-03-08"},{"REDFLAG":"1","DF":30,"FJ":"510","ZGRQ":"2025-03-15","HAS_FILE":"1","SSXX":"南3栋 第5层 510","DJ":"基本合格","SS_M":"16462092582115442920","DM":"17419166670838404489","XQ_M":"2","LBMC":"宿舍卫生","ZG_M":"17420154380643088348","DY":null,"XN":"2024","LB":"wsjc","LC":"第5层","SSLMC":"南3栋","JCRQ":"2025-03-14"},{"REDFLAG":"1","DF":1,"FJ":"505","ZGRQ":"2025-03-06","HAS_FILE":"1","SSXX":"南3栋 第5层 505","DJ":"不合格","SS_M":"16462092582118861691","DM":"17412284372754623937","XQ_M":"2","LBMC":"宿舍卫生","ZG_M":"17413126706619398205","DY":null,"XN":"2024","LB":"wsjc","LC":"第5层","SSLMC":"南3栋","JCRQ":"2025-03-06"},{"REDFLAG":"1","DF":30,"FJ":"511","ZGRQ":"2025-03-09","HAS_FILE":"1","SSXX":"南3栋 第5层 511","DJ":"基本合格","SS_M":"16462092582119386484","DM":"17414187670152718980","XQ_M":"2","LBMC":"宿舍卫生","ZG_M":"17414988516756801701","DY":null,"XN":"2024","LB":"wsjc","LC":"第5层","SSLMC":"南3栋","JCRQ":"2025-03-08"},{"REDFLAG":"1","DF":30,"FJ":"512","ZGRQ":"2025-03-14","HAS_FILE":"1","SSXX":"南3栋 第5层 512","DJ":"基本合格","SS_M":"16462092582126904901","DM":"17419168639655548748","XQ_M":"2","LBMC":"宿舍卫生","ZG_M":"17419193887579002542","DY":null,"XN":"2024","LB":"wsjc","LC":"第5层","SSLMC":"南3栋","JCRQ":"2025-03-14"},{"REDFLAG":"1","DF":30,"FJ":"512","ZGRQ":"2025-03-06","HAS_FILE":"1","SSXX":"南3栋 第5层 512","DJ":"基本合格","SS_M":"16462092582126904901","DM":"17412285466642407747","XQ_M":"2","LBMC":"宿舍卫生","ZG_M":"17412431258607299710","DY":null,"XN":"2024","LB":"wsjc","LC":"第5层","SSLMC":"南3栋","JCRQ":"2025-03-06"}]}'''
    result = json.loads(query)
    if result["aaData"]:
        bhgss = ""
        for i in result['aaData']:
            print(i)
            if i["REDFLAG"]=="0":
                print(i["SSXX"],i["DJ"],i["JCRQ"])
                bhgss +=str(i["SSXX"])+str(i["DJ"])+str(i["JCRQ"])+"\r"
        requests.get(f"https://api.day.app/xjRYpUmoXaqbP5kLvfiACT/{bhgss}?group=ssbhg")
    else:
        requests.get(f"https://api.day.app/xjRYpUmoXaqbP5kLvfiACT/无不合格宿舍?group=ssbhg")
except Exception as e:  # 捕获所有异常
    requests.get("https://api.day.app/xjRYpUmoXaqbP5kLvfiACT/查询错误，错误:?group=ssbhg")
    print(e)
