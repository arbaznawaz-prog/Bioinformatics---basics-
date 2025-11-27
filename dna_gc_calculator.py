def gc_content(seq):
    g = seq.upper().count("G")
    c = seq.upper().count("C")
    gc = ((g + c) / len(seq)) * 100
    return round(gc, 2)

sequence = "ATGCGATACGATACGCGGATTA"
print("Sequence:", sequence)
print("GC Content (%):", gc_content(sequence))
