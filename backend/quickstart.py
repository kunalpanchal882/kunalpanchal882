#!/usr/bin/env python3
"""
Quick Start Guide for Resume Parser API

This script helps you set up and run the FastAPI Resume Parser.
"""

import os
import sys
import subprocess

def print_section(title):
    """Print a formatted section header."""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}\n")

def check_python_version():
    """Check if Python 3.10+ is installed."""
    print_section("Checking Python Version")
    version = sys.version_info
    print(f"Python Version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 10):
        print("❌ Python 3.10 or higher is required!")
        return False
    print("✓ Python version is compatible!")
    return True

def check_env_file():
    """Check if .env file exists and has API key."""
    print_section("Checking Environment Setup")
    
    if not os.path.exists('.env'):
        print("❌ .env file not found!")
        print("\n  Steps to fix:")
        print("  1. Copy .env.example to .env:")
        print("     cp .env.example .env")
        print("  2. Edit .env and add your GEMINI_API_KEY")
        print("  3. Get your API key from: https://aistudio.google.com/app/apikey")
        return False
    
    with open('.env', 'r') as f:
        env_content = f.read()
    
    if 'your_gemini_api_key_here' in env_content:
        print("⚠️  .env file exists but API key is not set!")
        print("\n  Steps to fix:")
        print("  1. Get your API key from: https://aistudio.google.com/app/apikey")
        print("  2. Edit .env and replace 'your_gemini_api_key_here' with your actual key")
        return False
    
    print("✓ .env file exists and API key is configured!")
    return True

def check_dependencies():
    """Check if required packages are installed."""
    print_section("Checking Dependencies")
    
    required = {
        'fastapi': 'FastAPI',
        'uvicorn': 'Uvicorn',
        'pydantic': 'Pydantic',
        'pdfplumber': 'pdfplumber',
        'docx': 'python-docx',
        'dotenv': 'python-dotenv',
        'google.generativeai': 'google-generativeai'
    }
    
    missing = []
    for module, name in required.items():
        try:
            __import__(module)
            print(f"✓ {name} is installed")
        except ImportError:
            print(f"❌ {name} is NOT installed")
            missing.append(name)
    
    if missing:
        print(f"\n  Install missing packages with:")
        print(f"  pip install -r requirements.txt")
        return False
    
    return True

def run_api():
    """Run the FastAPI application."""
    print_section("Starting FastAPI Server")
    
    print("Starting Uvicorn server...")
    print("API will be available at: http://localhost:8000")
    print("API Documentation: http://localhost:8000/docs")
    print("\nPress Ctrl+C to stop the server\n")
    
    try:
        subprocess.run([sys.executable, '-m', 'uvicorn', 'main:app', '--reload'], 
                      check=False)
    except KeyboardInterrupt:
        print("\n\nServer stopped by user.")

def main():
    """Main setup and run function."""
    print("\n" + "="*60)
    print("  Resume Parser API - Quick Start")
    print("="*60)
    
    checks = [
        ("Python Version", check_python_version),
        ("Environment File", check_env_file),
        ("Dependencies", check_dependencies),
    ]
    
    all_passed = True
    for check_name, check_func in checks:
        if not check_func():
            all_passed = False
    
    if not all_passed:
        print("\n" + "="*60)
        print("  ❌ Setup incomplete. Please fix the issues above.")
        print("="*60 + "\n")
        sys.exit(1)
    
    print("\n" + "="*60)
    print("  ✓ All checks passed! Ready to start the API.")
    print("="*60)
    
    # Ask user if they want to start the server
    response = input("\n▶ Start the FastAPI server now? (y/n): ").strip().lower()
    if response == 'y':
        run_api()
    else:
        print("\n  To start the server manually, run:")
        print("  uvicorn main:app --reload")
        print()

if __name__ == "__main__":
    main()
