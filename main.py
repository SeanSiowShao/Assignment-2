"""
Name:Sean
Date:6 January 2019
Brief Project Description: Assignment 2
GitHub URL: 
"""

from kivy.app import App
from kivy.lang import Builder
from songlist import SongList
from kivy.uix.button import Button
from song import Song
from kivy.properties import StringProperty


class SongsToLearnApp(App):
    song_list = SongList()

    def build(self):
        self.title = "Song Learn 3.0"
        self.root = Builder.load_file('app.kv')
        self.display_list()
        return self.root

    def display_list(self, sur_list=[]):
        self.root.ids.entries_box.clear_widgets()
        store_songs = self.song_list.get_songs('r')
        if sur_list != []:
            store_songs = []
            store_songs = sur_list
        for song in store_songs:

            temp_button = Button(text=Song().print_str(str(song)))
            temp_button.bind(on_release=self.press_entry)
            # add the button to the "entries_box" using add_widget()
            self.root.ids.entries_box.add_widget(temp_button)

    def press_entry(self, arg):
        # print(arg.text)
        if('learned' in arg.text):
            self.root.ids.bottom_text.text = "Song is already learned, plz select another one"
        else:
            self.song_list.add_file(arg.text)
            self.display_list()

    def press_clear(self):
        self.root.ids.add_title.text = ''
        self.root.ids.add_artist.text = ''
        self.root.ids.add_year.text = ''

    def sort(self, text):
        key = 0
        if 'title' in text:
            key = 0
        elif 'artist' in text:
            key = 1
        else:
            key = 2
        new_list = self.song_list.sort(key)
        self.display_list(new_list)

    def add_song(self):
        form_song = self.root.ids.add_title.text + ',' + self.root.ids.add_artist.text + ',' + self.root.ids.add_year.text + ',n\n'
        self.song_list.get_songs('a', form_song)
        self.display_list()



SongsToLearnApp().run()
