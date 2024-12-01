# VDL (Video Downloader) | 视频下载器

A powerful command-line tool for downloading videos from multiple platforms including YouTube and Bilibili.
一个功能强大的命令行视频下载工具，支持包括 YouTube 和 Bilibili 在内的多个平台。

## Quick Start (Portable Executables) | 快速开始（便携版）

Latest Release | 最新版本：[v0.2.0](https://github.com/JNU-Tangyin/vdl/releases/tag/v0.2.0)

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
vdl.exe https://www.youtube.com/watch?v=VIDEO_ID
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
./vdl https://www.youtube.com/watch?v=VIDEO_ID
```

Note: On macOS, you might need to allow the executable in System Settings > Security & Privacy the first time you run it.
注意：在 macOS 上首次运行时，可能需要在系统设置 > 安全性与隐私中允许运行此应用程序。

## Usage | 使用方法

### Basic Commands | 基本命令

1. Download a video (default action) | 下载视频（默认操作）
```bash
vdl <url>
# Example: vdl https://www.youtube.com/watch?v=VIDEO_ID
```

2. List available video formats | 列出可用的视频格式
```bash
vdl formats <url>
# Example: vdl formats https://www.youtube.com/watch?v=VIDEO_ID
```

3. Show supported platforms | 显示支持的平台
```bash
vdl supported
```

### Options | 选项

- `--quality`: Select video quality (e.g., 1080p, 720p)
  选择视频质量（如 1080p、720p）
```bash
vdl --quality 1080p <url>
```

- `--output` or `-o`: Custom output filename
  自定义输出文件名
```bash
vdl -o "video.mp4" <url>
```

- `--subtitle/--no-subtitle`: Download subtitles if available
  下载字幕（如果可用）
```bash
vdl --subtitle <url>
```

- `--playlist/--no-playlist`: Download as playlist
  下载为播放列表
```bash
vdl --playlist <url>
```

## Features | 功能特点

- 🌐 Multi-platform support (YouTube, Bilibili)
  多平台支持（YouTube、Bilibili）
- 🎥 Flexible quality selection
  灵活的质量选择
- 📝 Subtitle download support
  支持下载字幕
- 📋 Playlist download support
  支持下载播放列表
- 🔒 Browser cookie authentication
  浏览器 cookie 认证
- 📊 Progress tracking
  进度跟踪
- 🎨 Beautiful terminal output
  美观的终端输出

## Development | 开发

### Requirements | 依赖要求

- Python 3.11+
- pip (Python package manager)

### Setup | 设置

1. Clone the repository | 克隆仓库
```bash
git clone https://github.com/yourusername/vdl.git
cd vdl
```

2. Install dependencies | 安装依赖
```bash
pip install -r requirements.txt
```

### Build | 构建

Run the build script to create standalone executables:
运行构建脚本创建独立可执行文件：

```bash
python build.py
```

This will create:
这将创建：

- `dist/vdl`: Standalone executable (macOS/Linux)
  独立可执行文件（macOS/Linux）
- `dist/VDL.dmg`: macOS installer
  macOS 安装包

## Credits | 致谢

Built with:
基于以下项目构建：

- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
  For video downloading | 提供视频下载功能

- [Click](https://click.palletsprojects.com/)
  For CLI interface | 提供命令行界面

- [Rich](https://rich.readthedocs.io/)
  For terminal formatting | 提供终端格式化

## License | 许可证

MIT License

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
