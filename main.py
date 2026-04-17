#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Douyin Title Generator Skill Main File
"""

import os
import sys
import subprocess

def main():
    """Skill main entry point"""
    original_script = "/root/.openclaw/workspace/douyin_title_generator.py"
    
    if not os.path.exists(original_script):
        print("Error: Douyin title generator script not found")
        print(f"Please ensure script exists at: {original_script}")
        return 1
    
    if len(sys.argv) > 1:
        cmd = [sys.executable, original_script] + sys.argv[1:]
        result = subprocess.run(cmd)
        return result.returncode
    else:
        print("🎯 Douyin Title Generator Skill")
        print("=" * 50)
        print("Usage:")
        print("  douyin-title-generator product_type [keywords] [count]")
        print("  douyin-title-generator bedding sheets,cotton 10")
        print("")
        print("Features:")
        print("  • Generate viral Douyin titles")
        print("  • Support custom product types and keywords")
        print("  • Automatic emoji and emotional word addition")
        print("=" * 50)
        return 0

if __name__ == "__main__":
    sys.exit(main())