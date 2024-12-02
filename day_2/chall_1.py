from utils import read_input

input_data = read_input(__file__, 1)

lines = input_data.split('\n')
reports = [[int(i) for i in line.split(' ')] for line in lines[:-1]]
valid_reports = 0
for report in reports:
    ascending = None
    error = False
    for i in range(len(report) - 1):
        if ascending is None:
            if report[i] == report[i + 1]:
                error = True
                break
            # end if
            ascending = report[i] < report[i + 1]
        # end if

        if abs(report[i] - report[i + 1]) > 3 \
        or ascending and report[i] >= report[i + 1] \
        or not ascending and report[i] <= report[i + 1]:
            error = True
            break
        # end if
    # end for

    if not error:
        valid_reports += 1
    # end if
# end for

print(valid_reports)