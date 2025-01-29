def greeting_by_name(name):
    return f"Hello name!"


def get_symbol_position(text, symbol):
    return text.find(symbol)


def merge(dict1, dict2):
    dict1.update(dict2)
    return dict1

# a = {"name":"Roman", "age":"25"}
# b = {"position": "manager", "salary": "11200"}
# c = merge(a, b)
# print(a)
# #print(len(d.items()))