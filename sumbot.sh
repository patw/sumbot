#!/bin/bash
python3 -m uvicorn main:app --host 0.0.0.0 --port 3002 --reload