# Cryptographic Edge List (Snapdragon 8 SM8750-AB / Samsung S25 Ultra)

# Hardware-accelerated edges ─────────────────────────────────────────────
CE -> AES-CBC                [1] :contentReference[oaicite:0]{index=0}
CE -> AES-CTR                [1] :contentReference[oaicite:1]{index=1}
CE -> AES-XTS                [1] :contentReference[oaicite:2]{index=2}
CE -> AES-CCM                [1] :contentReference[oaicite:3]{index=3}
CE -> AES-CMAC               [1] :contentReference[oaicite:4]{index=4}
CE -> HMAC-SHA-1/256/384/512 [1] :contentReference[oaicite:5]{index=5}
CE -> SHA-1/256/384/512      [1] :contentReference[oaicite:6]{index=6}
CE -> DES / 3DES             [1] :contentReference[oaicite:7]{index=7}
CE -> SM4                    [1] :contentReference[oaicite:8]{index=8}
ICE -> AES-XTS-128/256        [2] :contentReference[oaicite:9]{index=9}
SPU -> RSA-2048/4096         [3] :contentReference[oaicite:10]{index=10}
SPU -> ECDSA-P256/P384       [3] :contentReference[oaicite:11]{index=11}
SPU -> ECDH-P256/P384        [3] :contentReference[oaicite:12]{index=12}
TME -> DICE Key-Provisioning [4] :contentReference[oaicite:13]{index=13}

# Compositional edges ────────────────────────────────────────────────────
AES-CCM -> HMAC-SHA-256       [1] :contentReference[oaicite:14]{index=14}   # AEAD
HMAC-SHA-256 -> SHA-256       [1] :contentReference[oaicite:15]{index=15}

# Proposed (future) edges ────────────────────────────────────────────────
CE  -> SHA3-256              [*]   # extend hash set
NPU -> Kyber-768             [*]   # PQC off-load
NPU -> Dilithium-3           [*]   # PQC off-load

# Source keys ────────────────────────────────────────────────────────────
[1] Qualcomm Crypto Engine Core FIPS 140-3 SP (2024)  
[2] Qualcomm Inline Crypto Engine overview           
[3] Qualcomm Secure Processing Unit FIPS policy      
[4] Snapdragon 8 Elite ( SM8750-AB ) Product Brief    
