def dic_dummy_producer_1():
    print("dicmond_circular_import_a.dic_dummy_producer_1()")

def dic_dummy_consumer_1():
    from diamond_circular_import_a import dia_dummy_producer_1
    dia_dummy_producer_1()
    print("dicmond_circular_import_a.dic_dummy_consumer_1()")

if __name__ == "__main__":
    print("[Running dicmond_circular_import_c.py]")
    dic_dummy_producer_1()
    dic_dummy_consumer_1()
