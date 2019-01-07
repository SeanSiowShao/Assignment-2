# create your Song class in this file


class Song:
    def __init__(self):
        pass

    def format_list(self, line):
        tmp_list = []
        tmp_str = ''
        for w in line:
            if w == ',':
                tmp_list.append(tmp_str)
                tmp_str = ''
            else:
                tmp_str += w
        tmp_list.append(tmp_str)
        return tmp_list

    def print_str(self, line):
        return_str = ''
        print(line)
        learned = ''
        tmp_str = ''
        for w in line:
            if w == ',' or w == '[' or w == ']' or w == "'":
                return_str = return_str + tmp_str
                tmp_str = ''
            else:
                tmp_str += w
        return_str += tmp_str
        print(return_str[-3:-2])
        if 'n' in return_str[-3:-2]:
            return return_str[:-3]
        else:
            return (return_str[:-3] + '(learned)')



