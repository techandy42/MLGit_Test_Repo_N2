def cia_dummy_producer_1():
    print("circular_import_a.cia_dummy_producer_1()")

def cia_dummy_consumer_1():
    from circular_import_b import cib_dummy_producer_1
    cib_dummy_producer_1()
    print("circular_import_a.cia_dummy_consumer_1()")

if __name__ == "__main__":
    print("[Running circular_import_a.py]")
    cia_dummy_producer_1()
    cia_dummy_consumer_1()
