point_dict = {'x': [(4, 3), (1, 2), (3, 1)], 'o': [(7, 2), (5, 8), (1, 3)]}

lengths = [(key, len(value)) for key, value in point_dict.items()]
largest_len = max([pair[1] for pair in lengths])
new_lengths = [pair[0] for pair in lengths if pair[1] == largest_len]

print(lengths)
print(largest_len)
print(new_lengths)