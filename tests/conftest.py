"""
Configuration file for pytest testing
"""

import sys
import os

# Add the package directory to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Test discovery patterns
python_files = ["test_*.py", "*_test.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]

# Test markers
markers = [
    "slow: marks tests as slow (deselect with '-m \"not slow\"')",
    "integration: marks tests as integration tests",
    "unit: marks tests as unit tests",
]

# Coverage settings
addopts = [
    "--strict-markers",
    "--strict-config",
    "--verbose",
]

# Minimum version requirements
minversion = "6.0"

# Test paths
testpaths = ["tests"]
