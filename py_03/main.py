
from datetime import datetime
import json
import os
import uuid
import random
import time

origin_folder_path = "py_03/origin"
rip_folder_path = "py_03/rip"
error_folder_path = "py_03/errors"
count_folder_path = "py_03/count"


def wrapping_simulate():
    """模拟包装机器
    通过用户输入执行时常，模拟包装机器执行 1个/1s 的任务
    Args:void
    Returns:void
    """
    excecute_time = input("请输入执行时长(单位:分):")
    start_time = time.time()
    end_time = start_time + int(excecute_time) * 60
    wrapper_machines = ["machine_1", "machine_2", "machine_3", "machine_4"]
    error_triggered = False
    flag = True

    while time.time() <= end_time:

        json_files_list = os.listdir(origin_folder_path)
        arrange_results(json_files_list)

        if time.time() > start_time + 5 and not error_triggered:
            error_triggered = True
            error_machine = random.choice(wrapper_machines)
            error_data = {
                "machine_no": error_machine,
                "error_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
            error_path = os.path.join(
                error_folder_path, error_machine + ".json")
            error_file = open(error_path, "w")
            json.dump(error_data, error_file, indent=2)
            print(error_machine + "出现错误")
            user_input = input("按回车继续")
            if user_input == "":
                flag = True

        if flag:
            file_name = datetime.now().strftime("%Y%m%d%H%M%S")
            origin_file_path = os.path.join(
                origin_folder_path, file_name + ".json")
            result = "qualified" if random.random() <= 0.7 else "unqualified"
            data = {
                "id": uuid.uuid4().hex,
                "maker_no": random.choice(wrapper_machines),
                "result": result
            }
            origin_file = open(origin_file_path, "w")
            json.dump(data, origin_file, indent=2)
            time.sleep(1)


def generate_rip_json(path):
    """生成rip文件
    Args:path string origin文件路径
    Returns: void
    """
    rip_file = open(path, "w")
    json.dump({}, rip_file, indent=2)


def record(filename, data, origin_file_path):
    """记录统计数据
    把产品的数据写入count文件夹，并删除原始文件
    Args:filename string 文件名 data 文件数据 origin_file_path string 原始文件路径
    Returns:void
    """
    print(filename)
    counter_path = os.path.join(count_folder_path, filename)
    json_file = open(counter_path, "w")
    json.dump(data, json_file, indent=2)
    os.remove(origin_file_path)


def arrange_results(file_list):
    """整理文件列表
    循环origin文件夹下的json文件，对结果为qualified和unqualified进行分类处理
    Args:file_list list 
    Returns:void
    """
    for file_name in file_list:
        if file_name.endswith(".json"):
            print(file_name)

            file_path = os.path.join(origin_folder_path, file_name)
            json_file = open(file_path, "r")
            if (os.path.getsize(file_path)):
                data = json.load(json_file)
                if data["result"] == "unqualified":
                    generate_rip_json(file_path)
                else:
                    record(file_name, data, origin_file_path=file_path)


wrapping_simulate()
