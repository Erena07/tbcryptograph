# ============================================================
# 📍 ServerScript: gost.py
# Implementasi algoritma GOST 28147-89 (Feistel cipher)
# ============================================================

S_BOX = [
    [4,10,9,2,13,8,0,14,6,11,1,12,7,15,5,3],
    [14,11,4,12,6,13,15,10,2,3,8,1,0,7,5,9],
    [5,8,1,13,10,3,4,2,14,15,12,7,6,0,9,11],
    [7,13,10,1,0,8,9,15,14,4,6,12,11,2,5,3],
    [6,12,7,1,5,15,13,8,4,10,9,14,0,3,11,2],
    [4,11,10,0,7,2,1,13,3,6,8,5,9,12,15,14],
    [13,11,4,1,3,15,5,9,0,10,14,7,6,8,2,12],
    [1,15,13,0,5,7,10,4,9,2,3,14,6,11,8,12]
]

# -----------------------------
# 🔸 Fungsi substitusi (S-Box)
# -----------------------------
def sbox_substitute(value: int) -> int:
    output = 0
    for i in range(8):
        nibble = (value >> (4 * i)) & 0xF
        output |= S_BOX[i][nibble] << (4 * i)
    return output

# -----------------------------
# 🔸 Pembangkitan Subkey (8 subkey, 32-bit)
# -----------------------------
def generate_subkeys(key_bytes: bytes):
    if len(key_bytes) != 32:
        raise ValueError("Kunci harus 256-bit (32 byte)")
    return [key_bytes[i:i+4] for i in range(0, 32, 4)]

# -----------------------------
# 🔸 Fungsi Round Feistel
# -----------------------------
def feistel_round(L: int, R: int, subkey: int):
    temp = (R + subkey) % (2**32)
    temp = sbox_substitute(temp)
    temp = ((temp << 11) | (temp >> (32 - 11))) & 0xFFFFFFFF
    return R, L ^ temp

# -----------------------------
# 🔸 Enkripsi satu blok (8 byte)
# -----------------------------
def encrypt_block(block: bytes, subkeys: list[bytes]) -> bytes:
    L, R = block[:4], block[4:]
    L, R = int.from_bytes(L, 'big'), int.from_bytes(R, 'big')
    for i in range(32):
        subkey = int.from_bytes(subkeys[i % 8], 'big')
        L, R = feistel_round(L, R, subkey)
    return (R.to_bytes(4, 'big') + L.to_bytes(4, 'big'))

# -----------------------------
# 🔸 Dekripsi satu blok (8 byte)
# -----------------------------
def decrypt_block(block: bytes, subkeys: list[bytes]) -> bytes:
    L, R = block[:4], block[4:]
    L, R = int.from_bytes(L, 'big'), int.from_bytes(R, 'big')
    for i in range(32):
        subkey = int.from_bytes(subkeys[7 - (i % 8)], 'big')
        L, R = feistel_round(L, R, subkey)
    return (R.to_bytes(4, 'big') + L.to_bytes(4, 'big'))

# -----------------------------
# 🔸 Enkripsi/Dekripsi data panjang
# -----------------------------
def gost_encrypt(data: bytes, key: bytes) -> bytes:
    subkeys = generate_subkeys(key)
    # padding agar kelipatan 8 byte
    while len(data) % 8 != 0:
        data += b'\x00'
    result = b''
    for i in range(0, len(data), 8):
        result += encrypt_block(data[i:i+8], subkeys)
    return result

def gost_decrypt(data: bytes, key: bytes) -> bytes:
    subkeys = generate_subkeys(key)
    result = b''
    for i in range(0, len(data), 8):
        result += decrypt_block(data[i:i+8], subkeys)
    return result.rstrip(b'\x00')
