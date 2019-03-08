import sys
import re

if len(sys.argv) > 1 is not None:
    route_file = sys.argv[1]
else:
    route_file = input('insert the file route')

with open(route_file) as csv_file:
    with open('D:\codensa\generated_extract1.csv', 'w+') as file_out:
        line = csv_file.readline()
        counter = 0
        while line:
            new_line = ''
            if counter > 0:
                sp = line.split(';')
                if sp[0] == '114793':
                    print('punto interrupcion')
                if sp.__len__() > 0:
                    if sp[3] == 'MT' and sp[7] != 'unset':
                        try:
                            sp_infr = sp[7].split('-')
                            if sp_infr.__len__() > 1:
                                infr_i = ''.join(re.findall('[\d*]', str(sp_infr[0])))
                                infr_f = ''.join(re.findall('[\d*]', str(sp_infr[1])))
                                ctos = '-'.join(set(re.findall('[A-Z]+[\d]+', sp[7])))
                                new_line = '{};{};{};{}'.format(line, infr_i, infr_f, ctos)

                            elif sp_infr.__len__() == 1:
                                infr_i = ''.join(re.findall('[\d*]', str(sp_infr[0])))
                                ctos = '-'.join(set(re.findall('[A-Z]+[\d]+', sp[7])))
                                new_line = '{};{};{};{}'.format(line, infr_i, '', ctos)

                            else:
                                new_line = '{};{};{};{}'.format(line, '', '', '')
                                
                        except Exception as error:
                            print(line)
                            print('line: ' + str(counter))
                            print('line: ' + sp[7])
                            print(error)
                    else:
                        new_line = '{};{};{};{}'.format(line, '', '', '')
            else:
                new_line = line+';INFR_I;INFR_F;CTOS'
            file_out.writelines(new_line.replace('\n', '')+'\n')
            counter += 1
            line = csv_file.readline()
