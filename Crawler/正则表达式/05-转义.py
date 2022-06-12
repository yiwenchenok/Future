
import re
#思考题;判断一个文件路径是否存在
print(re.findall('nodejs',"C:\nodejs")) #\n转义成换行符了，所以匹配不到
#[]
print(re.findall('nodejs',r"C:\nodejs")) #todo； r禁止转义
#['nodejs']
#头脑风暴
print(re.findall('\n',"C:\nodejs")) #['\n']
print(re.findall('\\n',"C:\nodejs")) #['\n']
print(re.findall('\\n',r"C:\nodejs")) #[]
print(re.findall('\\\\n',r"C:\nodejs")) #['\\n']
print(re.findall(r'\\n',r"C:\nodejs")) #['\\n']
print('----')




