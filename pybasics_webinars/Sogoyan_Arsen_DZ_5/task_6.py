# create function that extracts integers from a string
# and returns 0 if no integers found

def extract_int(string):
    try:
        return int(''.join([ch for ch in string if ch.isdigit()]))
    except:
        return 0


# open the file with text to read the lines to a list subj_lines
with open('task_6_file.txt', 'r', encoding='utf-8') as my_file:
    subj_lines = my_file.read().splitlines()

# dict_keys <- list of classes, i.e. dictionary keys
dict_keys = [subj_lines[i].split(': ')[0] for i in range(len(subj_lines))]

# dict_vals_raw <- list of strings with data for each class
dict_vals_raw = [subj_lines[i].split(': ')[1] for i in range(len(subj_lines))]

dict_vals = [] # will contain res_dict values

# dict_vals <- list of sums of class type quantities
for i in range(len(subj_lines)):
     dict_vals.append(sum(list(map(extract_int, dict_vals_raw[i].split()))))

# dictionary generated from dict_keys as keys and dict_vals as values
res_dict = {key: value for key, value in zip(dict_keys, dict_vals)}

print(res_dict)









