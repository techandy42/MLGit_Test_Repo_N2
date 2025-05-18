from ...outer_module_producer_a import ompa_dummy_producer_1

def imca_dummy_consumer_1():
    ompa_dummy_producer_1()
    print("inner_module_consumer_a.imca_dummy_consumer_1()")

if __name__ == "__main__":
    print("[Running inner_module_consumer_a.py]")
    imca_dummy_consumer_1()
