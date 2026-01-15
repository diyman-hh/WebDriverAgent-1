import wda
import time
import subprocess
import threading
import sys

def start_wda(bundle_id="com.facebook.WebDriverAgentRunner.xctrunner"):
    """
    使用 tidevice 启动 WDA
    """
    print("正在使用 tidevice 启动 WDA...")
    # tidevice xctest -B <bundle_id>
    # 注意：这里假设你只有一台设备连接，或者 tidevice 能自动识别
    # 如果有多台设备，需要指定 -u <udid>
    cmd = ["tidevice", "xctest", "-B", bundle_id]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return process

def run_automation():
    # 等待 WDA 启动
    print("等待 WDA 启动 (约 10 秒)...")
    time.sleep(10)

    try:
        # 连接 WDA，默认端口 8100
        # tidevice 会将设备端口映射到本地
        c = wda.Client('http://localhost:8100')
        
        print("WDA 连接成功！")
        print(f"设备信息: {c.info}")
        
        # 模拟操作
        s = c.session()
        
        # 获取屏幕尺寸
        w, h = s.window_size()
        print(f"屏幕尺寸: {w}x{h}")
        
        # 模拟滑动 (从下往上滑，例如刷视频)
        print("模拟滑动...")
        s.swipe(w/2, h*0.8, w/2, h*0.2, duration=0.5)
        time.sleep(2)
        
        # 模拟点击 (点击屏幕中心)
        print("模拟点击...")
        s.click(w/2, h/2)
        time.sleep(2)
        
        print("自动化测试完成。")

    except Exception as e:
        print(f"发生错误: {e}")
        print("请检查：\n1. 手机是否连接\n2. WDA 是否成功安装并信任\n3. tidevice 是否已安装")

if __name__ == "__main__":
    # 启动 WDA 进程
    wda_process = start_wda()
    
    try:
        run_automation()
    finally:
        # 清理进程
        print("正在停止 WDA...")
        wda_process.terminate()
