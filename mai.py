import subprocess
import time
import yaml

# 启动alist服务
alist_process = subprocess.Popen(['/alist', 'server'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# 等待alist服务启动
time.sleep(5)  # 等待5秒，以确保alist服务有足够的时间启动

# 修改config.yaml文件
config_path = '/alist_batch_add/config.yaml'
with open(config_path, 'r') as f:
    config = yaml.safe_load(f)
    config['auth']['username'] = 'admin'
    config['auth']['password'] = 'NEW_PASSWORD'

with open(config_path, 'w') as f:
    yaml.safe_dump(config, f)

# 执行main.py脚本
main_py_process = subprocess.Popen(['python', '/alist_batch_add/main.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# 等待main.py脚本执行完成
main_py_process.communicate()

# 注意：这里没有等待alist服务停止，如果您需要在完成后停止服务，可以使用alist_process.terminate()
