def initial_setup():
    row_init = open("Day18.txt").readlines()[0]
    return row_init

def get_next_row(last_row):
    #patch last row with 2 safe spots
    last_row_buff = '.'+last_row+'.'
    next_row = [0]*len(last_row)
    for i in range(0,len(last_row)):
        if last_row_buff[i] == "^" and last_row_buff[i+1] == "^" and last_row_buff[i+2] == ".":
            next_row[i] = "^"
        elif last_row_buff[i] == "." and last_row_buff[i+1] == "^" and last_row_buff[i+2] == "^":
            next_row[i] = "^"
        elif last_row_buff[i] == "^" and last_row_buff[i+1] == "." and last_row_buff[i+2] == ".":
            next_row[i] = "^"
        elif last_row_buff[i] == "." and last_row_buff[i+1] == "." and last_row_buff[i+2] == "^":
            next_row[i] = "^"
        else:
            next_row[i] = "."
    #print(last_row)
    #print("".join(next_row))
    return "".join(next_row)
    
def get_field():
    field = []
    field.append(initial_setup())
    while len(field) < 40:
        field.append(get_next_row(field[-1]))
    print("The total number of safe tiles on the field of 40 rows amounts to " + str("".join(field).count('.')))
    while len(field) < 400000:
        field.append(get_next_row(field[-1]))
    print("The total number of safe tiles on the field of 400k rows amounts to " + str("".join(field).count('.')))
    
get_field()
