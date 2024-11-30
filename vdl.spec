# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['vdl/cli.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[
        'rich.console',
        'rich.table',
        'rich.progress',
        'browser_cookie3',
        'yt_dlp.utils',
        'yt_dlp.cookies',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='vdl',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=True,  # Enable argument passing on macOS
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    onefile=True,  # Create a single file executable
)
