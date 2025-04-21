import time

def view_logs(log_file_path="output.log"):
    try:
        with open(log_file_path, "r") as log_file:
            # 让文件从最后一行开始读取，实时显示日志更新
            log_file.seek(0, 2)  # 跳到文件的末尾
            while True:
                line = log_file.readline()
                if not line:
                    time.sleep(0.1)  # 如果没有新行，稍等再试
                    continue
                print(line, end="")
    except Exception as e:
        print(f"Error reading log file: {e}")

if __name__ == "__main__":
    print("输入 1 查看实时日志，输入 q 退出。")
    while True:
        user_input = input("请输入数字: ")
        if user_input == "1":
            print("开始查看实时日志...")
            view_logs("output.log")
        elif user_input.lower() == "q":
            print("退出日志查看.")
            break
        else:
            print("无效输入，输入 1 查看日志，输入 q 退出。")
