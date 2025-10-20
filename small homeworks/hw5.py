input_list = input().split()

unique_elems = list(dict.fromkeys(input_list))
print(' '.join(unique_elems))