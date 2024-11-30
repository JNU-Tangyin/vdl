#!/usr/bin/env python3
import os
import platform
import shutil
import subprocess
import sys
from pathlib import Path

def run_command(cmd, cwd=None):
    """Run a command and return its output"""
    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        sys.exit(1)
    return result.stdout

def setup_venv():
    """Set up virtual environment and install dependencies"""
    if platform.system() == "Windows":
        python = "python"
        venv_path = "venv\\Scripts"
        pip = os.path.join(venv_path, "pip.exe")
    else:
        python = "python3"
        venv_path = "venv/bin"
        pip = os.path.join(venv_path, "pip")

    # Create virtual environment
    if not os.path.exists("venv"):
        run_command([python, "-m", "venv", "venv"])

    # Install dependencies
    run_command([pip, "install", "-r", "requirements.txt"])
    run_command([pip, "install", "pyinstaller"])

def build_executable():
    """Build the executable for the current platform"""
    system = platform.system()
    if system == "Windows":
        pyinstaller = "venv\\Scripts\\pyinstaller.exe"
    else:
        pyinstaller = "venv/bin/pyinstaller"

    # Clean previous builds
    for path in ["build", "dist"]:
        if os.path.exists(path):
            shutil.rmtree(path)

    # Build executable
    run_command([pyinstaller, "vdl.spec", "--clean"])

    # Create macOS DMG if on macOS
    if system == "Darwin":
        run_command([
            "hdiutil", "create",
            "-volname", "VDL",
            "-srcfolder", "dist",
            "-ov",
            "-format", "UDZO",
            "dist/VDL.dmg"
        ])

def main():
    """Main build function"""
    setup_venv()
    build_executable()
    
    system = platform.system()
    exe_path = "dist/vdl.exe" if system == "Windows" else "dist/vdl"
    
    if os.path.exists(exe_path):
        print(f"\nBuild successful! Executable created at: {exe_path}")
        if system == "Darwin":
            print("DMG installer created at: dist/VDL.dmg")
        print("\nYou can now run the executable directly without installation.")
    else:
        print("Build failed: Executable not found")
        sys.exit(1)

if __name__ == "__main__":
    main()
