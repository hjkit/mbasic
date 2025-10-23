#!/bin/bash

cd "$(dirname "$0")"

echo "======================================"
echo "Running with mbasic.py"
echo "======================================"
python3 ../mbasic.py prtusing.bas

echo ""
echo ""
echo "======================================"
echo "Running with mbasic521"
echo "======================================"
../utils/mbasic521 prtusing.bas

echo ""
echo "======================================"
echo "Comparison complete"
echo "======================================"
