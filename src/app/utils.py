def utils_dummy_func_1():
    print("utils.utils_dummy_func_1()")

def utils_dummy_func_2():
    print("utils.utils_dummy_func_2()")

class UtilsDummyClass1:
    class_property_1 = "utils.UtilsDummyClass1.class_property_1"

    def __init__(self):
        self.instance_property_1 = "utils.UtilsDummyClass1.instance_property_1"

    def instance_method_1(self):
        print("utils.UtilsDummyClass1.instance_method_1()")

    @classmethod
    def class_method_1(cls):
        print("utils.UtilsDummyClass1.class_method_1()")

    @staticmethod
    def static_method_1():
        print("utils.UtilsDummyClass1.static_method_1()")

    def __str__(self):
        return "utils.UtilsDummyClass1()"

    def __repr__(self):
        return "utils.UtilsDummyClass1()"

class UtilsDummyClass2:
    class_property_1 = "utils.UtilsDummyClass2.class_property_1"

    def __init__(self):
        self.instance_property_1 = "utils.UtilsDummyClass2.instance_property_1"

    def instance_method_1(self):
        print("utils.UtilsDummyClass2.instance_method_1()")

    @classmethod
    def class_method_1(cls):
        print("utils.UtilsDummyClass2.class_method_1()")

    @staticmethod
    def static_method_1():
        print("utils.UtilsDummyClass2.static_method_1()")

    def __str__(self):
        return "utils.UtilsDummyClass2()"

    def __repr__(self):
        return "utils.UtilsDummyClass2()"
