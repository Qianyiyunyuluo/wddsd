from datetime import datetime
import pytz

def show_world_time():
    zones = pytz.all_timezones
    print("世界时区列表：")
    for i, zone in enumerate(zones):
        print(f"{i + 1}. {zone}")

    choice = input("请选择一个时区（输入序号）：")
    try:
        choice = int(choice)
        if choice < 1 or choice > len(zones):
            print("无效的选择！")
            return
    except ValueError:
        print("这无效的选择！")
        return

    chosen_zone = pytz.timezone(zones[choice - 1])
    time = datetime.now(chosen_zone)
    print(f"\n{chosen_zone} 的当前时间是：{time.strftime('%Y-%m-%d %H:%M:%S')}")

def main():
    show_world_time()

if __name__ == "__main__":
    main()
