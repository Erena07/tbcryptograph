# ============================================================
# 📍 ServerScript: utils.py
# Fungsi bantu: padding, timing, file I/O
# ============================================================
import time

def read_file(path: str) -> bytes:
    with open(path, 'rb') as f:
        return f.read()

def write_file(path: str, data: bytes):
    with open(path, 'wb') as f:
        f.write(data)

def pad_key(key: str) -> bytes:
    key_bytes = key.encode('utf-8')
    if len(key_bytes) > 32:
        return key_bytes[:32]
    return key_bytes.ljust(32, b'\x00')

def measure_time(func, *args):
    start = time.time()
    result = func(*args)
    duration = time.time() - start
    return result, duration
