def tic_dummy_producer_1():
    print("triple_circular_import_a.tic_dummy_producer_1()")

def tic_dummy_consumer_1():
    from triple_circular_import_b import tib_dummy_producer_1
    tib_dummy_producer_1()
    print("triple_circular_import_a.tic_dummy_consumer_1()")

if __name__ == "__main__":
    print("[Running triple_circular_import_c.py]")
    tic_dummy_producer_1()
    tic_dummy_consumer_1()
