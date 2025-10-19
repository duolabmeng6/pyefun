import openai
from pyefun import *
from pyefun.模块.文件下载 import *

def 图像生成(api_key,描述,清晰度=256,是否保存图片=False):
  openai.api_key = api_key
  response = openai.Image.create(
    prompt= 描述 ,
    n=1,
    size="{0}x{0}".format(清晰度),
  )
  # print(response)
  image_url = response['data'][0]['url']
  if 是否保存图片 == False:
    return image_url
  print(image_url)
  文件保存地址 = 取运行目录()+"/{0}-{1}.png".format(取现行时间().取时间戳(),文本_取随机字母(4))
  下载文件(image_url,文件保存地址)
  return 文件保存地址

