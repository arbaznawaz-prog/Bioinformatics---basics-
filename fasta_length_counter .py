def fasta_length(fasta_text):
    lines = fasta_text.strip().split("\n")
    seq = "".join(line for line in lines if not line.startswith(">"))
    return len(seq)

fasta = """>test_protein
MKTIIALSYIFCLVFADYKDDDDK"""
print("Protein length:", fasta_length(fasta))
