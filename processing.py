import pickle

with open("filtered_data_list.txt", "r") as f:
    result = f.read()

ans = list(i.split(": ")[-1] for i in result.split(", "))

with open("idset.pickle", "wb") as f:
    pickle.dump(ans, f)