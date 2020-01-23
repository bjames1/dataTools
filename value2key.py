code_dict = dict(zip(code_index, code_names))

search_code = 'coden30daysubhistyn_genericnames_ends1';
for index, code in code_dict.items():
    if code == search_code:
        print(index)
