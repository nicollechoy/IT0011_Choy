# Define sets based on the Venn diagram
A = {"a", "b", "c", "d", "f", "g"}
B = {"b", "c", "d", "f", "h", "l", "m", "o"}
C = {"c", "d", "f", "h", "i", "j", "k"}

# (a) Elements in A ∪ B (Union)
union_AB = A | B
print("A ∪ B:", union_AB, "Count:", len(union_AB))

# (b) Elements in B that are not in A or C
B_only = B - (A | C)
print("B - (A ∪ C):", B_only, "Count:", len(B_only))

# (c) Using set operations to find specific elements

# (i) Elements in C but not in A
print("i. Elements in C but not in A:", C - A)

# (ii) Elements common to A, B, and C (Intersection)
print("ii. Elements common to A, B, and C:", A & B & C)

# (iii) Elements in both A and B, plus "h"
print("iii. Elements in both A and B, plus h:", (A & B) | {"h"})

# (iv) Elements common to A and C
print("iv. Elements common to A and C:", A & C)

# (v) Only "c"
print("v. Only c:", {"c"})

# (vi) Elements in B that are not in A or C
print("vi. Elements only in B:", B - (A | C))