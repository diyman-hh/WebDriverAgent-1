# WDA 自动化使用说明

## 前置要求 (Windows)

1.  **Python 环境**: 确保安装了 Python 3.x。
2.  **iTunes**: 安装 iTunes (非 Microsoft Store 版本推荐) 以获取必要的驱动，或者安装 Apple Devices 应用。
3.  **连接设备**: 使用 USB 线将 iPhone 连接到电脑。

## 安装步骤

1.  **安装依赖库**:
    打开终端 (Powershell 或 CMD)，运行：
    ```bash
    pip install -r automation/requirements.txt
    ```

2.  **安装 WDA**:
    - 前往 GitHub 仓库的 [Actions 页面](https://github.com/diyman-hh/WebDriverAgent-1/actions)。
    - 下载最新构建的 `WebDriverAgentRunner-IPA`。
    - 使用 [TrollStore](https://github.com/opa334/TrollStore) (推荐) 或其他签名工具 (如 Sideloadly) 将 `.ipa` 安装到您的手机上。
    - **注意**: 如果使用免费开发者账号签名，需要在手机上“设置 -> 通用 -> VPN与设备管理”中信任证书。

## 运行自动化脚本

1.  确保手机已连接电脑。
2.  在终端中运行：
    ```bash
    python automation/run_wda.py
    ```
3.  脚本会自动：
    - 使用 `tidevice` 启动手机上的 WDA 服务。
    - 连接 WDA。
    - 执行简单的滑动和点击测试。

## 常见问题

- **Failed to get system application**: 可能是证书签名问题，或者 WDA 未在手机上启动。尝试手动在手机上打开 WebDriverAgentRunner 应用。
- **Unable to launch**: 确保手机未锁屏，或者已信任电脑。
