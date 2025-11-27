genes = ["STAT3", "TP53", "BRCA1", "MAPK1", "FOXO1"]
toxic_target = "STAT3"

filtered = [g for g in genes if g == toxic_target]

print("All genes:", genes)
print("Toxic target gene detected:", filtered)
