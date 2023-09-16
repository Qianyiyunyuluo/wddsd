
import time
import os

def countdown(minutes):
    seconds = minutes * 60
    while seconds > 0:
        os.system('clear')  # 清屏命令，适用于Mac和Linux系统，Windows系统请使用os.system('cls')
        print("倒计时：%02d:%02d" % (seconds // 60, seconds % 60))
        time.sleep(1)
        seconds -= 1
    os.system('clear')
    print("时间到！")
/111111/
def main():
    minutes = int(input("请输入专注时长（分钟）："))
    countdown(minutes)

if __name__ == "__main__":
    main()
```

这段代码会要求用户输入专注时长（以分钟为单位），然后开始倒计时。在倒计时过程中，每秒钟清屏并打印剩余时间，直到时间到达后输出"时间到！"。请注意，在不同的操作系统中，清屏命令可能不同，所以请根据自己的操作系统做相应的修改。
