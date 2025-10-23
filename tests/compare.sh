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
timeout 2 tnylpo /home/wohl/cl/mbasic/com/mbasic prtusing.bas 2>&1

echo ""
echo "======================================"
echo "Comparison complete"
echo "======================================"
