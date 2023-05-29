<p align="center">
  <img width="18%" align="center" src="https://raw.githubusercontent.com/zhiyiYo/PyQt-Fluent-Widgets/master/docs/source/_static/logo.png" alt="logo">
</p>
  <h1 align="center">
  PySide2-Fluent-Widgets
</h1>
<p align="center">
  基于 PySide2 的 Fluent Design 风格组件库
</p>

<p align="center">
  <a style="text-decoration:none">
    <img src="https://img.shields.io/badge/Platform-Win32%20|%20Linux%20|%20macOS-blue?color=#4ec820" alt="Platform Win32 | Linux | macOS"/>
  </a>

  <a style="text-decoration:none">
    <img src="https://static.pepy.tech/personalized-badge/pyqt-fluent-widgets?period=total&units=international_system&left_color=grey&right_color=brightgreen&left_text=Downloads" alt="Download"/>
  </a>

  <a style="text-decoration:none">
    <img src="https://img.shields.io/badge/License-GPLv3-blue?color=#4ec820" alt="GPLv3"/>
  </a>
</p>

<p align="center">
<a href="../README.md">English</a> | 简体中文
</p>

![Interface](https://raw.githubusercontent.com/zhiyiYo/PyQt-Fluent-Widgets/master/docs/source/_static/Interface.jpg)


## 安装📥
安装轻量版 (`AcrylicLabel` 不可用)：
```shell
pip install PySide2-Fluent-Widgets -i https://pypi.org/simple/
```
安装完整版：
```shell
pip install "PySide2-Fluent-Widgets[full]" -i https://pypi.org/simple/
```

> **Warning**
> 请勿同时安装 PyQt-Fluent-Widgets、PyQt6-Fluent-Widgets、PySide2-Fluent-Widgets 和 PySide2-Fluent-Widgets，因为他们的包名都是 `qfluentwidgets`


## 运行示例▶️
使用 pip 安装好 PySide2-Fluent-Widgets 包并下载好此仓库的代码之后，就可以运行 examples 目录下的任意示例程序，比如：
```python
cd examples/gallery
python demo.py
```

如果遇到 `ImportError: cannot import name 'XXX' from 'qfluentwidgets'`，这表明安装的包版本过低。可以按照上面的安装指令将 pypi 源替换为 https://pypi.org/simple 并重新安装.

## 在线文档📕
想要了解 PySide2-Fluent-Widgets 的正确使用姿势？请仔细阅读 [帮助文档](https://pyqt-fluent-widgets.readthedocs.io/zh_CN/latest/) 👈

## 支持💖
如果这个组件库帮助了您，或者是想支持作者继续开发和维护这个组件库，可以在 [爱发电](https://afdian.net/a/zhiyiYo) 或者 [ko-fi](https://ko-fi.com/zhiyiYo) 上请作者喝一杯奶茶。非常感谢您的支持与鼓励 🥰。

## 演示视频📽️
请查收哔哩哔哩上的 [视频合集](https://www.bilibili.com/video/BV12c411L73q)，它展示了 PySide2-Fluent-Widgets 的全部组件和特性 🎉

## 搭配 QtDesigner🚀
切换到 PyQt5 分支（PySide2 无法使用插件），运行 `python ./tools/designer.py` 启动安装了 PyQt-Fluent-Widgets 插件的 QtDesigner。如果操作成功，QtDesigner 的侧边栏中将会显示 PyQt-Fluent-Widgets 的组件。对于旧项目的改造，推荐使用 [视频教程](https://www.bilibili.com/video/BV1na4y1V7jH) 中介绍的 `提升为...`。

> **Note**
> 推荐在虚拟环境中安装 pyqt5-tools 和 PyQt-Fluent-Widgets，并确保 PyQt5-Frameless-Window 的版本号 >= 0.2.7，不然可能出现各种奇怪的问题。

## 加入我们🚩
可以在 [ Discord ](https://discord.gg/mYZME3wraK) 上和我们一起交流探讨，分享自己对这个组件库的新发现和新想法 🚀

## 另见👀
下面是一些使用了 PyQt-Fluent-Widgets 的项目：
* [**zhiyiYo/Groove**: A cross-platform music player based on PyQt5](https://github.com/zhiyiYo/Groove)
* [**zhiyiYo/Alpha-Gobang-Zero**: A gobang robot based on reinforcement learning](https://github.com/zhiyiYo/Alpha-Gobang-Zero)

## 参考
* [**Windows design**: Design guidelines and toolkits for creating native app experiences](https://learn.microsoft.com/zh-cn/windows/apps/design/)
* [**Microsoft/WinUI-Gallery**: An app demonstrates the controls available in WinUI and the Fluent Design System](https://github.com/microsoft/WinUI-Gallery)

## 许可证
PySide2-Fluent-Widgets 使用双许可证。非商业用途使用 [GPLv3](../LICENSE) 许可证进行授权，商用请在 [爱发电](https://afdian.net/item/7f1aa71af2d111ed82045254001e7c00) 或者 [ko-fi](https://ko-fi.com/s/02269112b2) 上进行购买以支持作者的开发。

Copyright © 2021 by zhiyiYo.