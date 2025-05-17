// [1] Apple introduces M4 Pro and M4 Max :contentReference[oaicite:0]{index=0}
// [2] Apple-silicon GoFetch vulnerability :contentReference[oaicite:1]{index=1}
// [3] Titan H1D3 Secure µC crypto library PDF :contentReference[oaicite:2]{index=2}
// [4] Titan Cryptographic Library — NIST CAVP :contentReference[oaicite:3]{index=3}
// [5] Evaluating Apple Silicon M-Series for HPC Perf. :contentReference[oaicite:4]{index=4}

digraph CryptoM4Titan {
  rankdir=LR;
  bgcolor="#1e2127";
  node [shape=box, style=filled, fillcolor="#2b2f36", fontcolor=white, fontname="Monaco"];
  edge [color=white, fontcolor=white, fontname="Monaco"];

  M4   [label="M4 Max SoC\nCryptographic Engine"];
  Titan[label="Titan Library"];

  AES    [label="AES-256-GCM"];
  SHA2   [label="SHA-2 256/512"];
  SHA3   [label="SHA-3"];
  ChaCha [label="ChaCha20-Poly1305"];
  Curve  [label="Curve25519"];
  ECDSA  [label="ECDSA"];
  RSA    [label="RSA-4096"];

  /* implementation paths */
  M4    -> AES    [label="[1]"];
  M4    -> SHA2   [label="[1]"];
  M4    -> ChaCha [label="[1]"];
  M4    -> Curve  [label="[1]"];

  Titan -> AES    [label="[3]"];
  Titan -> SHA2   [label="[3]"];
  Titan -> ECDSA  [label="[3]"];
  Titan -> RSA    [label="[4]"];

  /* known vulnerability */
  M4    -> AES    [style=dotted, color=red,   label="GoFetch [2]"];

  /* proposed optimizations */
  M4    -> SHA3   [style=dashed, color=blue,  label="AMX accel [5]"];
  M4    -> ECDSA  [style=dashed, color=blue,  label="Mem-tagging [5]"];
}
