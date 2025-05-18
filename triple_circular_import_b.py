def tib_dummy_producer_1():
    print("triple_circular_import_a.tib_dummy_producer_1()")

def tib_dummy_consumer_1():
    from triple_circular_import_a import tia_dummy_producer_1
    tia_dummy_producer_1()
    print("triple_circular_import_a.tib_dummy_consumer_1()")

if __name__ == "__main__":
    print("[Running triple_circular_import_b.py]")
    tib_dummy_producer_1()
    tib_dummy_consumer_1()
