#!/usr/bin/env python3
"""
Test Script for Resume Parser API

This script tests the FastAPI Resume Parser endpoints.
Run the API first with: uvicorn main:app --reload
"""

import requests
import json
from pathlib import Path

# API endpoint
API_BASE_URL = "http://localhost:8000"

def test_root_endpoint():
    """Test the root endpoint."""
    print("\n" + "="*60)
    print("Testing ROOT ENDPOINT: GET /")
    print("="*60)
    
    try:
        response = requests.get(f"{API_BASE_URL}/")
        
        print(f"Status Code: {response.status_code}")
        print(f"Response:\n{json.dumps(response.json(), indent=2)}")
        
        if response.status_code == 200:
            print("\n✓ Root endpoint test PASSED")
            return True
        else:
            print("\n❌ Root endpoint test FAILED")
            return False
    
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to API server!")
        print("   Make sure the API is running: uvicorn main:app --reload")
        return False
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

def test_parse_endpoint_with_pdf():
    """Test the parse endpoint with a PDF file."""
    print("\n" + "="*60)
    print("Testing PARSE ENDPOINT: POST /parse (PDF)")
    print("="*60)
    
    # Try to find a PDF file to test with
    pdf_files = list(Path(".").glob("**/*.pdf"))
    
    if not pdf_files:
        print("⚠️  No PDF files found in the project directory for testing.")
        print("   Create a resume PDF file and run this test again.")
        return None
    
    pdf_path = pdf_files[0]
    print(f"Using test file: {pdf_path}")
    
    try:
        with open(pdf_path, 'rb') as f:
            files = {'file': f}
            response = requests.post(f"{API_BASE_URL}/parse", files=files)
        
        print(f"Status Code: {response.status_code}")
        print(f"Response:\n{json.dumps(response.json(), indent=2)}")
        
        if response.status_code == 200:
            print("\n✓ PDF parsing test PASSED")
            return True
        else:
            print("\n❌ PDF parsing test FAILED")
            return False
    
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to API server!")
        print("   Make sure the API is running: uvicorn main:app --reload")
        return False
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

def test_parse_endpoint_with_docx():
    """Test the parse endpoint with a DOCX file."""
    print("\n" + "="*60)
    print("Testing PARSE ENDPOINT: POST /parse (DOCX)")
    print("="*60)
    
    # Try to find a DOCX file to test with
    docx_files = list(Path(".").glob("**/*.docx"))
    
    if not docx_files:
        print("⚠️  No DOCX files found in the project directory for testing.")
        print("   Create a resume DOCX file and run this test again.")
        return None
    
    docx_path = docx_files[0]
    print(f"Using test file: {docx_path}")
    
    try:
        with open(docx_path, 'rb') as f:
            files = {'file': f}
            response = requests.post(f"{API_BASE_URL}/parse", files=files)
        
        print(f"Status Code: {response.status_code}")
        print(f"Response:\n{json.dumps(response.json(), indent=2)}")
        
        if response.status_code == 200:
            print("\n✓ DOCX parsing test PASSED")
            return True
        else:
            print("\n❌ DOCX parsing test FAILED")
            return False
    
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to API server!")
        print("   Make sure the API is running: uvicorn main:app --reload")
        return False
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

def test_invalid_file():
    """Test the parse endpoint with an invalid file type."""
    print("\n" + "="*60)
    print("Testing ERROR HANDLING: Invalid File Type")
    print("="*60)
    
    try:
        # Create a temporary invalid file
        test_file_path = "test_invalid.txt"
        with open(test_file_path, 'w') as f:
            f.write("This is just a text file, not a resume.")
        
        with open(test_file_path, 'rb') as f:
            files = {'file': f}
            response = requests.post(f"{API_BASE_URL}/parse", files=files)
        
        print(f"Status Code: {response.status_code}")
        print(f"Response:\n{json.dumps(response.json(), indent=2)}")
        
        # Clean up
        Path(test_file_path).unlink()
        
        # Should get a 400 error for unsupported file type
        if response.status_code == 400:
            print("\n✓ Invalid file type error handling test PASSED")
            return True
        else:
            print("\n❌ Invalid file type error handling test FAILED")
            return False
    
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to API server!")
        print("   Make sure the API is running: uvicorn main:app --reload")
        return False
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

def print_summary(results):
    """Print test summary."""
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    
    passed = sum(1 for r in results if r is True)
    failed = sum(1 for r in results if r is False)
    skipped = sum(1 for r in results if r is None)
    
    print(f"\n✓ Passed: {passed}")
    print(f"❌ Failed: {failed}")
    print(f"⚠️  Skipped: {skipped}")
    
    total = len(results)
    print(f"\nTotal: {total} tests")
    
    if failed == 0:
        print("\n✓ All tests passed! API is working correctly.")
    else:
        print(f"\n❌ {failed} test(s) failed. Please check the API setup.")

def main():
    """Run all tests."""
    print("\n" + "="*60)
    print("Resume Parser API - Test Suite")
    print("="*60)
    print("\nMake sure the API is running:")
    print("  uvicorn main:app --reload")
    
    results = []
    
    # Test 1: Root endpoint
    results.append(test_root_endpoint())
    
    # Test 2: Parse with PDF
    results.append(test_parse_endpoint_with_pdf())
    
    # Test 3: Parse with DOCX
    results.append(test_parse_endpoint_with_docx())
    
    # Test 4: Invalid file handling
    results.append(test_invalid_file())
    
    # Print summary
    print_summary(results)
    print()

if __name__ == "__main__":
    main()
