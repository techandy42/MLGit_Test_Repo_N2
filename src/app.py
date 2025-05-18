from definitions import (
    DummyTypeAlias1,
    DummyTypeAlias2,
    DummyTypeAlias3,
)
from external_modules import external_modules_dummy_func_1
from subdirectory_1.inner_module_producer_a import impa_dummy_producer_1

dummy_var_1: DummyTypeAlias1 = {"key": "value"}
dummy_var_2: DummyTypeAlias2 = [1, 2, 3]
dummy_var_3: DummyTypeAlias3 = (1, 2)

def dummy_app():
    print(dummy_var_1)
    print(dummy_var_2)
    print(dummy_var_3)
    external_modules_dummy_func_1()
    impa_dummy_producer_1()
    print("app.dummy_app()")

if __name__ == "__main__":
    print("[Running app.py]")
    dummy_app()
