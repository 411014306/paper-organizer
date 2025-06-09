#%%
# utils.py
import os

def ensure_directories():
    os.makedirs("./papers", exist_ok=True)
    os.makedirs("./data", exist_ok=True)
