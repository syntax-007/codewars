def convert_to_binary(n):
    binary_number = bin(n).replace("0b", "") 
    return list(binary_number).count("1")

print(convert_to_binary(54))