from binary_search_tree import BinarySearchTree
bst = BinarySearchTree("M")
for row in open("names_1.txt"):
    bst.insert(row.strip())
names = [ row.strip() for row in open("names_2.txt")]
from multiprocessing import Process
duplicates = []
def find_duplicate(i,bst):
    if bst.contains(i):
        duplicates.append(i)
procs = []
for i in names:
    proc = Process(target=find_duplicate, args=(i,bst,))
    procs.append(proc)
    proc.start()
for proc in procs:
    proc.join()

