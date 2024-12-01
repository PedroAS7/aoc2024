from utils import read_input

input_text = read_input(__file__, 1)
splits = [line.split(" ") for line in input_text.split('\n')]
left_side = sorted([int(n[0]) for n in splits[:-1]])
right_side = sorted([int(n[-1]) for n in splits[:-1]])
nbr_count = {k: k * sum(1 if k == right_side[i] else 0 for i in range(len(right_side))) for k in left_side}
print(sum(nbr_count.values()))