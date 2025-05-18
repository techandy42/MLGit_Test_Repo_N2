from src.subdirectory_1.inner_module_producer_a import impa_dummy_producer_1

def omca_dummy_consumer_1():
    impa_dummy_producer_1()
    print("outer_module_consumer_a.omca_dummy_consumer_1()")

if __name__ == "__main__":
    print("[Running outer_module_consumer_a.py]")
    omca_dummy_consumer_1()
