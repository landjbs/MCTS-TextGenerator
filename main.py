from importer import process_text, read_file, process_text_folder
from classes import Node



sample = process_text_folder("sample_texts")
# sample = process_text(read_file("sample_texts/prideandprejudice.txt"))
sample_length = len(sample)
print(sample_length)
n = 4
tree = Node(sample[0:n], sample[n])

for i in range(1,sample_length-(n+1)):
    if i%10000 == 0:
        print(f"{i} | {sample_length}")
    tree.search_add(sample[i:i+n], sample[i+n+1])

# print(sample[500:500+n], tree.nav(sample[500:500+n]))
gen_words = 100
gen_text = []
seed = process_text("pride and prejudice by")

for i in range(gen_words):
    next = tree.nav(seed[-n:])
    seed.append(next)

print(" ".join(seed))
