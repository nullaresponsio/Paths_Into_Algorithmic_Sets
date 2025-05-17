# Sources: :contentReference[oaicite:0]{index=0}
import networkx as nx
import matplotlib.pyplot as plt

nodes = [
    "RSA-2048", "RSA-3072",
    "ECC-P256", "ECC-P384",
    "SHA-1", "SHA-256", "SHA-384",
    "AES-128", "AES-256", "AES-GCM-128",
    "HMAC-SHA256", "HMAC-SHA384",
    "EK", "PCR Extend", "EncryptDecrypt",
    "Quote", "Sealed Storage", "Attestation"
]

existing_edges = [
    ("RSA-2048", "EK", "PTP v1.05"),
    ("ECC-P256", "EK", "PTP v1.05"),
    ("SHA-1", "PCR Extend", "Dell KB"),
    ("SHA-256", "PCR Extend", "PTP v1.05"),
    ("AES-128", "EncryptDecrypt", "wolfSSL Req"),
    ("AES-256", "EncryptDecrypt", "wolfSSL Opt"),
    ("HMAC-SHA256", "Quote", "Algo Registry"),
    ("EK", "Attestation", "TPM Part1 §31")
]

new_edges = [
    ("RSA-3072", "EK", "Proposed"),
    ("ECC-P384", "EK", "Proposed"),
    ("SHA-384", "PCR Extend", "Proposed"),
    ("AES-GCM-128", "EncryptDecrypt", "Proposed"),
    ("HMAC-SHA384", "Quote", "Proposed")
]

G = nx.DiGraph()
for n in nodes:
    G.add_node(n)

for u, v, lbl in existing_edges:
    G.add_edge(u, v, label=lbl, color='black')

for u, v, lbl in new_edges:
    G.add_edge(u, v, label=lbl, color='red')

pos = nx.spring_layout(G, seed=13900)
edge_colors = [G[u][v]['color'] for u, v in G.edges()]
edge_labels = nx.get_edge_attributes(G, 'label')

nx.draw_networkx_nodes(G, pos,
                       node_color='lightblue',
                       edgecolors='black',
                       node_size=1200)
nx.draw_networkx_labels(G, pos, font_size=8)

nx.draw_networkx_edges(G, pos,
                       edge_color=edge_colors,
                       arrows=True,
                       arrowstyle='-|>',
                       arrowsize=10,
                       width=1.2)

nx.draw_networkx_edge_labels(G, pos,
                             edge_labels=edge_labels,
                             font_size=6)

plt.title("TPM i9-13900H Algorithmic Analysis", fontsize=10)
plt.tight_layout()
plt.savefig("tpm_algorithms_i9_13900h.png", dpi=300)
plt.show()
