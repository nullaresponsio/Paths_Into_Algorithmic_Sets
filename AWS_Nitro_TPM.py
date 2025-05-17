digraph TPM_AWS {
    rankdir=LR;
    bgcolor="#1e1e1e";
    node [shape=box fontname=Helvetica color="#eeeeee" fontcolor="#ffffff" style=filled fillcolor="#3c3c3c"];
    edge [fontname=Helvetica color="#bbbbbb" fontcolor="#bbbbbb"];

    "AWS Nitro TPM" [shape=ellipse fillcolor="#006699"];

    RSA2048                       -> "AWS Nitro TPM" [label="supported [1,2]"];
    RSA3072                       -> "AWS Nitro TPM" [label="supported [2]"];
    "ECC P-256"                   -> "AWS Nitro TPM" [label="supported [2]"];
    "ECC P-384"                   -> "AWS Nitro TPM" [label="supported [2]"];
    "SHA-1"                       -> "AWS Nitro TPM" [label="supported [2]"];
    "SHA-256"                     -> "AWS Nitro TPM" [label="supported [1,2]"];
    "SHA-384"                     -> "AWS Nitro TPM" [label="supported [2]"];
    "AES-128"                     -> "AWS Nitro TPM" [label="supported [2]"];
    "AES-256"                     -> "AWS Nitro TPM" [label="supported [2]"];
    HMAC                          -> "AWS Nitro TPM" [label="supported [2]"];

    "CRYSTALS-Kyber (ML-KEM)"     -> "AWS Nitro TPM" [label="potential [3]"];
    "CRYSTALS-Dilithium (ML-DSA)" -> "AWS Nitro TPM" [label="potential [4]"];
    Falcon                        -> "AWS Nitro TPM" [label="potential [3]"];
    "SPHINCS+"                    -> "AWS Nitro TPM" [label="potential [4]"];

    subgraph cluster_legend {
        label="Citations";
        Legend [shape=note fillcolor="#3c3c3c" label="[1] AWS NitroTPM docs (2025)\n[2] TCG TPM 2.0 Library Spec\n[3] NIST FIPS-203 ML-KEM (2024)\n[4] NIST FIPS-204 ML-DSA (2024)"];
    }
}
