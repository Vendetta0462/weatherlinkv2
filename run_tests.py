#!/usr/bin/env python3
"""
Test runner script for WeatherLink v2 library

This script provides an easy way to run tests with different configurations.
"""

import sys
import subprocess
import os

def run_tests(coverage=False, verbose=False, specific_test=None):
    """Run the test suite with various options"""
    
    # Base pytest command
    cmd = ["python", "-m", "pytest"]
    
    # Add test directory
    cmd.append("tests/")
    
    # Add options
    if verbose:
        cmd.append("-v")
    
    if coverage:
        cmd.extend(["--cov=weatherlinkv2", "--cov-report=html", "--cov-report=term"])
    
    if specific_test:
        cmd.append(f"tests/{specific_test}")
    
    # Add markers for better test organization
    cmd.extend(["--strict-markers", "--tb=short"])
    
    print(f"Running: {' '.join(cmd)}")
    print("-" * 50)
    
    try:
        result = subprocess.run(cmd, check=True)
        print("\n✅ All tests passed!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Tests failed with exit code: {e.returncode}")
        return False
    except FileNotFoundError:
        print("❌ pytest not found. Install with: pip install pytest")
        return False

def main():
    """Main function to handle command line arguments"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Run WeatherLink v2 tests")
    parser.add_argument("-v", "--verbose", action="store_true", 
                       help="Run tests in verbose mode")
    parser.add_argument("-c", "--coverage", action="store_true",
                       help="Run tests with coverage report")
    parser.add_argument("-t", "--test", type=str,
                       help="Run specific test file (e.g., test_weatherlinkv2.py)")
    parser.add_argument("--install-deps", action="store_true",
                       help="Install test dependencies before running")
    
    args = parser.parse_args()
    
    # Install dependencies if requested
    if args.install_deps:
        print("Installing test dependencies...")
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", "-e", ".[dev]"], 
                         check=True)
            print("✅ Dependencies installed successfully")
        except subprocess.CalledProcessError:
            print("❌ Failed to install dependencies")
            return 1
    
    # Check if we're in the right directory
    if not os.path.exists("tests"):
        print("❌ tests/ directory not found. Run this script from the project root.")
        return 1
    
    # Run tests
    success = run_tests(
        coverage=args.coverage,
        verbose=args.verbose,
        specific_test=args.test
    )
    
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())
