#!/usr/bin/env python3
"""
Start script for the Main Module GUI.

This launcher starts the main application.

Usage:
  python3 run.py
"""
import os
import sys
import subprocess


def main():
    script = os.path.join(os.path.dirname(__file__), "Main_Module.py")
    if not os.path.exists(script):
        print(f"Error: {script} not found.")
        return 2
    return subprocess.call([sys.executable, script])


if __name__ == "__main__":
    raise SystemExit(main())
