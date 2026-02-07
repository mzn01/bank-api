import sys
import os

print("--- DIAGNOSTIC REPORT ---")
print(f"1. Python Executable: {sys.executable}")

try:
    import google.generativeai as genai
    print(f"2. GenAI Library Version: {genai.__version__}")
except AttributeError:
    print("2. GenAI Library Version: <Unknown - extremely old>")
except ImportError:
    print("2. GenAI Library Version: NOT INSTALLED")

print("-------------------------")