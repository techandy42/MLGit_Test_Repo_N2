import os
from math import sqrt, floor as fl, pi as PI
from utils import (
    utils_dummy_func_1,
    utils_dummy_func_2 as udf2,
    UtilsDummyClass1,
    UtilsDummyClass2 as UDC2,
)

def external_modules_dummy_func_1():
    print(f"Current working directory: {os.getcwd()}")
    print(f"Square root of 3: {sqrt(fl(PI))}")
    utils_dummy_func_1()
    udf2()
    udc1 = UtilsDummyClass1()
    udc1.instance_method_1()
    # Calling all of the properties and methods of the UtilsDummyClass2 class
    udc2 = UDC2()
    print(UDC2.class_property_1)
    print(udc2.instance_property_1)
    udc2.instance_method_1()
    UDC2.class_method_1()
    UDC2.static_method_1()
    print(str(udc2))
    print(repr(udc2))
    print("external_modules.external_modules_dummy_func_1()")

if __name__ == "__main__":
    print("[Running external_modules.py]")
    external_modules_dummy_func_1()
