def dib_dummy_producer_1():
    print("dibmond_circular_import_a.dib_dummy_producer_1()")

def dib_dummy_consumer_1():
    from diamond_circular_import_a import dia_dummy_producer_1
    dia_dummy_producer_1()
    print("dibmond_circular_import_a.dib_dummy_consumer_1()")

if __name__ == "__main__":
    print("[Running dibmond_circular_import_b.py]")
    dib_dummy_producer_1()
    dib_dummy_consumer_1()
