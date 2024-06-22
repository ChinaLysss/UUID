import urllib.request
import wmi
User_Version = "beta2024.6.22"#填写你的软件版本号 用于下面的验证
def Read_Version(url):#定义Read_Version函数 获取软件版本
    response = urllib.request.urlopen(url)
    content = response.read().decode('utf-8')#utf-8 也就意味着支持中文
    return content
Version_URL = "https://gitcode.net/bnamc/testreadurl/-/raw/master/Version"  #这里改成你的URL！！！
Version = Read_Version(Version_URL)
def Read_UUID(url):#定义Read_UUIDl函数 从你的验证库中获取UUID
    response = urllib.request.urlopen(url)
    content = response.read().decode('utf-8')# utf-8 也就意味着支持中文
    return content
UUID_URL = "https://gitcode.net/bnamc/testreadurl/-/raw/master/UUID"  #这里改成你的URL！！！
UUID = Read_UUID(UUID_URL)
wmii = wmi.WMI()
def CPU_USER_NUMBER(): #获取CPU硬件
    cpu_uuid = ""
    for cpu in wmii.Win32_Processor():
        cpu_uuid += cpu.ProcessorId.strip()
    return cpu_uuid
user_uuid = CPU_USER_NUMBER()
if User_Version in Version:
    if user_uuid in UUID:
        print("您已通过验证") #可自行更改
    else:
        print("您未通过验证 您的UUID",user_uuid)  #可自行更改
else:
    print("您不是最新版本 请到官网进行更新！")  #可自行更改
    print("您的版本号:",User_Version)  #可自行更改
    print("最新版本",Version)  #可自行更改

#By Lysss 2024.6.15 23:35

"""
更新日志：

2024.6.22 17:34
[New]Version检测
[Fix]UUID换行问题
[Next]计划在下一次更新中更换UUID算法

2024.6.15 23:35
[New]UUID验证
"""