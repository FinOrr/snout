#!/bin/bash

# Compile approval program
python3 contracts/approval.py

# Compile clear state program
python3 contracts/clear.py

echo "TEAL compilation complete!"