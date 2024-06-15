import urllib.request
import wmi
def read_text_from_url(url):#定义read_text_from_url函数 通过网络文本获取文本内容
    response = urllib.request.urlopen(url)
    content = response.read().decode('utf-8')#utf-8 也就意味着支持中文
    return content
url = "https://gitcode.net/bnamc/testreadurl/-/raw/master/Version"#这里改成你的URL
text_content = read_text_from_url(url)
wmii = wmi.WMI()
def CPU_USER_NUMBER():#获取CPU硬件
    cpu_uuid = ""
    for cpu in wmii.Win32_Processor():
        cpu_uuid += cpu.ProcessorId.strip()
    return cpu_uuid
user_uuid = CPU_USER_NUMBER()
if user_uuid in text_content:
    print("您已通过验证")
else:
    print("您未通过验证 您的UUID为:",user_uuid)

#By Lysss 2024.6.15 23:35