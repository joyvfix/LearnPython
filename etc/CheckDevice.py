# import platform


# def check_device_info():
#     system_info = {
#         "System": platform.system(),
#         "Node Name": platform.node(),
#         "Release": platform.release(),
#         "Version": platform.version(),
#         "Machine": platform.machine(),
#         "Processor": platform.processor(),
#     }
#     return system_info


# if __name__ == "__main__":
#     device_info = check_device_info()
#     for key, value in device_info.items():
#         print(f"{key}: {value}")
# {;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;}
import platform
import psutil
import platform


def get_cpu_info():
    cpu_info = {
        "Brand": platform.processor(),
        "Physical Cores": psutil.cpu_count(logical=False),
        "Total Cores": psutil.cpu_count(logical=True),
    }
    return cpu_info


def get_memory_info():
    memory = psutil.virtual_memory()
    memory_info = {
        "Total": f"{get_size(memory.total)}",
        "Available": f"{get_size(memory.available)}",
        "Used": f"{get_size(memory.used)}",
        "Percentage Used": f"{memory.percent}%",
    }
    return memory_info


def get_storage_info():
    partitions = psutil.disk_partitions()
    storage_info = {}
    for partition in partitions:
        partition_name = partition.device.split('/')[-1]
        usage = psutil.disk_usage(partition.mountpoint)
        storage_info[partition_name] = {
            "Total": f"{get_size(usage.total)}",
            "Used": f"{get_size(usage.used)}",
            "Free": f"{get_size(usage.free)}",
            "Percentage Used": f"{usage.percent}%",
        }
    return storage_info


def get_gpu_info():
    try:
        import GPUtil
        gpus = GPUtil.getGPUs()
        gpu_info = []
        for gpu in gpus:
            gpu_info.append({
                "Name": gpu.name,
                "Driver": gpu.driver,
                "Memory Total": f"{gpu.memoryTotal} MB",
                "Memory Free": f"{gpu.memoryFree} MB",
                "Memory Used": f"{gpu.memoryUsed} MB",
                "GPU Load": f"{gpu.load * 100:.2f}%",
            })
        return gpu_info
    except ImportError:
        return None


def get_size(bytes, suffix="B"):
    for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
        if abs(bytes) < 1024.0:
            return "%3.1f %s%s" % (bytes, unit, suffix)
        bytes /= 1024.0
    return "%.1f %s%s" % (bytes, "Yi", suffix)


def check_device_details():
    device_details = {
        "System": platform.system(),
        "Node Name": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": get_cpu_info(),
        "Memory": get_memory_info(),
        "Storage": get_storage_info(),
        "GPU": get_gpu_info(),
    }
    return device_details


if __name__ == "__main__":
    device_details = check_device_details()
    for key, value in device_details.items():
        print(f"{key}: {value}")
