import sys


if len(sys.argv) > 1 is not None:
    route_file = sys.argv[1]
else:
    route_file = input('insert the file route')

with open(route_file) as csv_file:
    line = csv_file.readline()
    counter = 0
    while line:
        if counter > 0:
            sp = line.split(';')
            if sp[1] == 'MT':
                sp_infr = sp[5].split('-')
                infr_i = str(sp_infr[0]).split(':')[1]
                infr_f = str(sp_infr[1]).split(':')[1]
        counter += 1
        line = csv_file.readline()
