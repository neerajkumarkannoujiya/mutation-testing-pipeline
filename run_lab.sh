#!/bin/bash

echo "=== Lab Assignment Automation Script ==="
echo "1. Running Unit Tests with Coverage..."
pytest tests/ --cov=src --cov-report=html --cov-report=xml -v

echo -e "\n2. Running Mutation Testing..."
mut.py --target src.calculator --unit-test tests.test_calculator tests.test_calculator_enhanced --runner pytest --report-html mutation_report --colored-output

echo -e "\n3. Generating Reports..."
echo "Coverage report: file://$(pwd)/htmlcov/index.html"
echo "Mutation report: file://$(pwd)/mutation_report/index.html"

echo -e "\n4. Final Test Summary..."
echo "Unit Test Results:"
pytest tests/ --cov=src --cov-report=term-missing

echo -e "\n=== Lab Complete ==="
