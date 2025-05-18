from ..subdirectory_2.inner_module_circular_import_a import imcia_dummy_producer_1

def impa_dummy_producer_1():
    imcia_dummy_producer_1()
    print("inner_module_producer_a.impa_dummy_producer_1()")

if __name__ == "__main__":
    print("[Running inner_module_producer_a.py]")
    impa_dummy_producer_1()
