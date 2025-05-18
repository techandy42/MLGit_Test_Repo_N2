def dia_dummy_producer_1():
    print("diamond_circular_import_a.dia_dummy_producer_1()")

def dia_dummy_consumer_1():
    print("diamond_circular_import_a.dia_dummy_consumer_1()")

if __name__ == "__main__":
    print("[Running diamond_circular_import_a.py]")
    dia_dummy_producer_1()
    dia_dummy_consumer_1()
