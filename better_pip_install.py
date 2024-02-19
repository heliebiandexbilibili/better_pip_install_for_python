import os
jingxiang = input("选择镜像源:[1]清华大学镜像源 [2]阿里云镜像源 [3]中科大镜像源 [4]腾讯云镜像源 [5]关闭默认镜像:")
pack = input("要下载的包:")
print("开始下载:"
      ""
      ""
      "")
match jingxiang:
    case "1":
        os.system(f"pip install {pack.lower()} -i https://pypi.tuna.tsinghua.edu.cn/simple/")
    case "2":
        os.system(f"pip install {pack.lower()} -i https://mirrors.aliyun.com/pypi/simple/")
    case "3":
        os.system(f"pip install {pack.lower()} -i https://pypi.mirrors.ustc.edu.cn/simple/")
    case "4":
        os.system(f"pip install {pack.lower()} -i https://mirrors.cloud.tencent.com/pypi/simple/")
    case _:
        os.system(f"pip install {pack.lower()}")
print("安装完成")
input("按回车键以退出...")