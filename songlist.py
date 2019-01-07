# create your SongList class in this file

from song import Song


class SongList:
    song_cls = Song()
    def get_songs(self, mode, title='fake', artist ='song', year='2000', file_list = []):
        file = open('songs.csv', mode)
        if mode == 'r':
            return list(self.read_file(file))

        elif mode == 'a':
            line = title
            self.add_new_song(line, file)
        elif mode == 'w':
            self.write_to_file(file_list, file)

    def read_file(self, file_obj):
        return_list = []
        for lines in file_obj:
            return_list.append(self.song_cls.format_list(lines))
        return return_list

    def add_new_song(self, line, file):
        file.write(line)

    def write_to_file(self, list_obj, file):
        for lines in list_obj:
            file.writelines(lines)

    def sort(self, sort_key):
        old_list = self.get_songs('r')
        from operator import itemgetter
        new_list = sorted(old_list, key=itemgetter(sort_key))
        return new_list

    def add_file(self, rec_line):
        list = self.get_songs('r')
        flag = 0
        write_lst = []
        for line in list:
            flag = 0
            for w in line:
                if w in rec_line:
                    flag = 1
            if flag == 1:
                write_lst.append(line[0] + ',' + line[1] + ',' + line[2] + ',y\n')
            else:
                write_lst.append(line[0]+','+line[1]+','+line[2]+','+line[3])
        write_file = open('songs.csv', 'w')
        for line_wrt in write_lst:
            write_file.writelines(line_wrt)