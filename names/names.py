import time
import asyncio
from concurrent.futures import ThreadPoolExecutor
from binary_search_tree import BinarySearchTree

start_time = time.time()

bst = BinarySearchTree("M")
for row in open("names_1.txt"):
    bst.insert(row.strip())
duplicates = [ row.strip() for row in open("names_2.txt") if bst.contains(row.strip())]

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")


start_time = time.time()

bst = BinarySearchTree("M")
for i in (row.strip() for row in open("names_1.txt")):
    bst.insert(i)

duplicates = [ row.strip() for row in open("names_2.txt") if bst.contains(row.strip())]

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

start_time = time.time()

bst = BinarySearchTree("M")
n1 = set( row.strip() for row in open("names_1.txt"))
duplicates = set((row.strip() for row in open("names_2.txt") if row.strip() in n1))


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
