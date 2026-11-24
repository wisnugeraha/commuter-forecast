#!/usr/bin/env python3
"""Nowhere Weather — make.fun entry (u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)"""
import os

ENTRY_LINE = "Nowhere, tomorrow: 80% motivation, sleet by lunch, a patch of sun that lands on the puddle at exactly the right angle."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w") as f:
    f.write(ENTRY_LINE + "\n")
