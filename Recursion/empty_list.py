import sys

def list_detail(lst):
    print("Capacity:",(sys.getsizeof(lst)))
    print("Capacity:",(lst.__sizeof__()))


marias_last=[1]
list_detail(marias_last)
