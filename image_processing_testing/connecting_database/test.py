first_list = first_list = ["egg", "chocolateflavour", "newspaper", "mouse", "monitor", "phone", "charger"]
second_list = ["chocolate", "vanilla", "caramel"]

matches = {sub for item in first_list for sub in second_list if sub in item}

print(matches)