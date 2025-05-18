import sys
import os
abspath = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(abspath)
from outer_module_producer_a import omca_dummy_producer_1
sys.path.remove(abspath)

def imca_dummy_consumer_1():
    omca_dummy_producer_1()
    print("inner_module_consumer_a.imca_dummy_consumer_1()")

if __name__ == "__main__":
    print("[Running inner_module_consumer_a.py]")
    imca_dummy_consumer_1()
