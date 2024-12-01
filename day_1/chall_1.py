from utils import read_input

input_text = read_input(__file__, 1)
splits = [line.split(" ") for line in input_text.split('\n')]
left_side = sorted([int(n[0]) for n in splits[:-1]])
right_side = sorted([int(n[-1]) for n in splits[:-1]])
dists = [abs(left_side[i] - right_side[i]) for i in range(len(left_side))]
print(sum(dists))