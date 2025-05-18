def cic_dummy_producer_1():
    print("circular_import_a.cic_dummy_producer_1()")

def cic_dummy_consumer_1():
    from circular_import_d import cid_dummy_producer_1
    cid_dummy_producer_1()
    print("circular_import_a.cic_dummy_consumer_1()")

if __name__ == "__main__":
    print("[Running circular_import_c.py]")
    cic_dummy_producer_1()
    cic_dummy_consumer_1()
