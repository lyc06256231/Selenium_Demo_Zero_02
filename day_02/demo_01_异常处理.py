# coding=utf-8

file = None
try: # 当程序中有不可控因素可能导致程序停止，可以使用try来捕获异常
    file = open("悯农1.txt", encoding="utf-8")
    print(file.read())
    file.seek(28)
    print(file.read())
# except FileNotFoundError as e: # 当try中的程序出现异常时，except中的代码会执行
#     print(f"文件打开失败{e}")
# except UnicodeDecodeError as e1:
#     print(f"文件读写失败{e1}")
except Exception as e:
    print(e)
finally:
    if file: # bool(None) -> False
        file.close()
        print("句柄关闭成功")