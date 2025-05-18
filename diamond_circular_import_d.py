def did_dummy_consumer_1():
    from diamond_circular_import_a import dia_dummy_producer_1
    from diamond_circular_import_b import dib_dummy_producer_1
    from diamond_circular_import_c import dic_dummy_producer_1
    dia_dummy_producer_1()
    dib_dummy_producer_1()
    dic_dummy_producer_1()
    print("didmond_circular_import_a.did_dummy_consumer_1()")

if __name__ == "__main__":
    print("[Running didmond_circular_import_d.py]")
    did_dummy_producer_1()
    did_dummy_consumer_1()
