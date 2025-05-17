/* titan_crypto.dot */
digraph TitanCrypto {
  rankdir=LR;
  node [shape=box];

  /* hardware */
  TitanM2      [label="Titan M2"];
  OTBN         [label="OTBN"];
  TensorG4     [label="Tensor G4"];
  TitanKey     [label="Titan Security Key"];

  /* algorithms */
  AES          [label="AES-256"];
  SHA3         [label="SHA-3"];
  RSA          [label="RSA-2048"];
  ECC          [label="ECC P-256"];
  HMAC         [label="HMAC-SHA256"];
  Kyber        [label="Kyber (PQC)"];
  Dilithium    [label="Dilithium (PQC)"];

  /* established edges */
  TitanM2 -> AES        [label="accelerates [1]"];
  TitanM2 -> SHA3       [label="accelerates [1]"];
  TitanM2 -> RSA        [label="accelerates [1]"];
  TitanM2 -> ECC        [label="accelerates [1]"];

  OTBN    -> RSA        [label="optimized [2]"];
  OTBN    -> ECC        [label="optimized [2]"];

  TitanKey-> ECC        [label="FIDO2 [4]"];
  TitanKey-> HMAC       [label="HOTP [4]"];

  TensorG4-> TitanM2    [label="integrates [5]"];

  /* new candidate edges */
  OTBN    -> Kyber      [style=dashed,label="proposed [3]"];
  OTBN    -> Dilithium  [style=dashed,label="proposed [3]"];
  TitanM2 -> Kyber      [style=dashed,label="future accel"];
}

/*
[1] Titan M2 cryptographic accelerators :contentReference[oaicite:0]{index=0}
[2] OTBN wide-integer crypto core for RSA/ECC :contentReference[oaicite:1]{index=1}
[3] Lattice-based PQC for OpenTitan :contentReference[oaicite:2]{index=2}
[4] Titan Security Key protocols :contentReference[oaicite:3]{index=3}
[5] Tensor G4 + Titan M2 integration :contentReference[oaicite:4]{index=4}
*/
