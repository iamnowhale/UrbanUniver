def introspection_info(obj):

    info = {}

    info["type"] = type(obj).__name__

    info["module"] = getattr(obj, "__module__", None)

    attributes = []
    methods = []

    for attribute_name in dir(obj):
        attribute_value = getattr(obj, attribute_name)
        if callable(attribute_value):
            methods.append(attribute_name)
        else:
            attributes.append(attribute_name)

    info["attributes"] = attributes
    info["methods"] = methods

    doc = getattr(obj, "__doc__", None)
    if doc:
        info["doc"] = doc.strip()

    return info


# Пример использования
if __name__ == "__main__":
    number_info = introspection_info(42)
    print(number_info)
