def tia_dummy_producer_1():
    print("triple_circular_import_a.tia_dummy_producer_1()")

def tia_dummy_consumer_1():
    from triple_circular_import_c import tic_dummy_producer_1
    tic_dummy_producer_1()
    print("triple_circular_import_a.tia_dummy_consumer_1()")

if __name__ == "__main__":
    print("[Running triple_circular_import_a.py]")
    tia_dummy_producer_1()
    tia_dummy_consumer_1()
