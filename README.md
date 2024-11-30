# VDL (Video Downloader) | 视频下载器

A powerful command-line tool for downloading videos from multiple platforms including YouTube and Bilibili.
一个功能强大的命令行视频下载工具，支持包括 YouTube 和 Bilibili 在内的多个平台。

## Quick Start (Portable Executables) | 快速开始（便携版）

### Windows Users | Windows 用户

1. Download `vdl.exe` from the latest release
   从最新发布版本下载 `vdl.exe`

2. Open Command Prompt or PowerShell
   打开命令提示符或 PowerShell

3. Navigate to the directory containing `vdl.exe`
   导航到包含 `vdl.exe` 的目录

4. Run commands directly:
   直接运行命令：
```batch
vdl.exe download https://www.youtube.com/watch?v=VIDEO_ID
```

### macOS Users | macOS 用户

1. Download `VDL.dmg` from the latest release
   从最新发布版本下载 `VDL.dmg`

2. Mount the DMG file by double-clicking it
   双击打开 DMG 文件

3. Drag the `vdl` executable to a location of your choice (e.g., Downloads)
   将 `vdl` 可执行文件拖到你选择的位置（如下载文件夹）

4. Open Terminal
   打开终端

5. Navigate to the directory containing `vdl`
   导航到包含 `vdl` 的目录

6. Run commands directly:
   直接运行命令：
```bash
./vdl download https://www.youtube.com/watch?v=VIDEO_ID
```

Note: On macOS, you might need to allow the executable in System Settings > Security & Privacy the first time you run it.
注意：在 macOS 上首次运行时，可能需要在系统设置 > 安全性与隐私中允许运行此应用程序。

## Features | 功能特点

- Download videos from multiple platforms (YouTube, Bilibili)
  支持多平台视频下载（YouTube、Bilibili）

- Select video quality (e.g., 1080p, 720p)
  可选择视频质量（如 1080p、720p）

- List available video formats
  列出可用视频格式

- Progress bar with download status
  下载进度条显示

- Browser cookie authentication support
  支持浏览器 cookie 认证

- Custom output filename support
  支持自定义输出文件名

## Usage Examples | 使用示例

1. Download a video in best quality:
   下载最佳质量视频：
```bash
vdl download https://www.youtube.com/watch?v=VIDEO_ID
```

2. Download with specific quality:
   指定质量下载：
```bash
vdl download https://www.youtube.com/watch?v=VIDEO_ID --quality 1080p
```

3. List available formats:
   列出可用格式：
```bash
vdl formats https://www.youtube.com/watch?v=VIDEO_ID
```

4. Show supported platforms:
   显示支持的平台：
```bash
vdl supported
```

### Advanced Options | 高级选项

- Set custom output filename:
  设置自定义输出文件名：
```bash
vdl download URL --output "my_video.mp4"
```

- Download with subtitles:
  下载字幕：
```bash
vdl download URL --subtitle
```

- Download playlist:
  下载播放列表：
```bash
vdl download URL --playlist
```

## Building from Source | 从源码构建

### Prerequisites | 前置要求

- Python 3.11 or higher | Python 3.11 或更高版本
- git

### Steps | 步骤

1. Clone the repository:
   克隆仓库：
```bash
git clone https://github.com/yourusername/vdl.git
cd vdl
```

2. Run the build script:
   运行构建脚本：
```bash
# On Windows | Windows 系统
python build.py

# On macOS | macOS 系统
python3 build.py
```

The build script will:
构建脚本将：

- Set up a virtual environment
  设置虚拟环境

- Install dependencies
  安装依赖

- Create a portable executable
  创建便携式可执行文件

- Create a DMG installer (macOS only)
  创建 DMG 安装程序（仅 macOS）

## Development | 开发

1. Create and activate virtual environment:
   创建并激活虚拟环境：
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows | Windows: venv\Scripts\activate
```

2. Install development dependencies:
   安装开发依赖：
```bash
pip install -r requirements.txt
```

3. Run tests:
   运行测试：
```bash
pytest tests/ -v --cov=vdl
```

## Requirements | 系统要求

- ffmpeg (for video processing)
  ffmpeg（用于视频处理）

- Chrome/Chromium (for cookie authentication)
  Chrome/Chromium（用于 cookie 认证）

## License | 许可证

This project is licensed under the MIT License - see the LICENSE file for details.
本项目采用 MIT 许可证 - 详见 LICENSE 文件。

## Contributing | 贡献

1. Fork the repository
   复刻仓库

2. Create your feature branch
   创建特性分支
```bash
git checkout -b feature/amazing-feature
```

3. Commit your changes
   提交更改
```bash
git commit -m 'Add some amazing feature'
```

4. Push to the branch
   推送到分支
```bash
git push origin feature/amazing-feature
```

5. Open a Pull Request
   创建拉取请求

## Acknowledgments | 致谢

- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
  For video downloading functionality | 提供视频下载功能

- [Click](https://click.palletsprojects.com/)
  For CLI interface | 提供命令行界面

- [Rich](https://rich.readthedocs.io/)
  For terminal formatting | 提供终端格式化
