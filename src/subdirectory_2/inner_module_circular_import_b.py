def imcib_dummy_producer_1():
    print("inner_module_circular_import_a.imcib_dummy_producer_1()")

def imcib_dummy_consumer_1():
    from inner_module_circular_import_a import imcia_dummy_producer_1
    imcia_dummy_producer_1()
    print("inner_module_circular_import_a.imcib_dummy_consumer_1()")

if __name__ == "__main__":
    print("[Running inner_module_circular_import_b.py]")
    imcib_dummy_producer_1()
    imcib_dummy_consumer_1()
