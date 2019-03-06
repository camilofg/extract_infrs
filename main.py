import sys
import re

if len(sys.argv) > 1 is not None:
    route_file = sys.argv[1]
else:
    route_file = input('insert the file route')

with open(route_file) as csv_file:
    with open('C:\CF\Delta_Canalizaciones\generated_extract.csv', 'w+') as file_out:
        line = csv_file.readline()
        counter = 0
        while line:
            if counter > 0:
                sp = line.split(';')
                if sp.__len__() > 0:
                    if sp[1] == 'MT' and sp[5] != 'unset':
                        try:
                            sp_infr = sp[5].split('-')
                            if sp_infr.__len__() > 1:
                                infr_i = ''.join(re.findall('[\d*]', str(sp_infr[0])))#.split(':')[1]
                                infr_f = ''.join(re.findall('[\d*]', str(sp_infr[1])))#str(sp_infr[1]).split(':')[1]
                                ctos = '-'.join(set(re.findall('[A-Z]+[\d]+', sp[5])))
                                new_line = '{};{};{};{}'.format(line, infr_i, infr_f, ctos)
                        except Exception as error:
                            print(line)
                            print('line: ' + str(counter))
                            print('line: ' + sp[5])
                            print(error)
                            #print('infr_i: {} - infr_f: {} - cto: {}'.format(infr_i, infr_f, ctos))
            else:
                new_line = line+';INFR_I;INFR_F;CTOS'
            file_out.writelines(new_line.replace('\n', '')+'\n')
            counter += 1
            line = csv_file.readline()
