#!/usr/bin/env bash

VENV=.venv
QT_LIB=$VENV/lib/python3.13/site-packages/PySide6/Qt/lib

export LD_LIBRARY_PATH=$QT_LIB

cd src

uv run main.py