from circular_import_a import cia_dummy_producer_1

def cib_dummy_producer_1():
    print("circular_import_b.cib_dummy_producer_1()")

def cib_dummy_consumer_1():
    cia_dummy_producer_1()
    print("circular_import_b.cib_dummy_consumer_1()")

if __name__ == "__main__":
    print("[Running circular_import_b.py]")
    cib_dummy_producer_1()
    cib_dummy_consumer_1()
