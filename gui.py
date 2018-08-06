import threading
import tkinter

import app
import test_progress_bar

a = app.App()


class MusicPlayer(object):
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("RetroMusicPlayer")
        self.play_button = tkinter.Button(self.root, command=a.play_or_unpause, text="播放")
        self.pause_button = tkinter.Button(self.root, command=a.pause_music, text="暂停")
        self.stop_button = tkinter.Button(self.root, command=a.stop_music, text="停止")
        self.pre_music_button = tkinter.Button(self.root, command=a.pre_music, text="前一首")
        self.next_music_button = tkinter.Button(self.root, command=a.next_music, text="后一首")
        self.volume_up_button = tkinter.Button(self.root, command=a.volume_up, text="音量+")
        self.volume_down_button = tkinter.Button(self.root, command=a.volume_down, text="音量-")
        self.music_duration_text = tkinter.IntVar()
        self.music_duration_label = tkinter.Label(self.root, textvariable=self.music_duration_text)
        # self.progress_bar = tkinter.Scale(self.root, command=test_progress_bar.show_values)
        self.frame = tkinter.Frame(self.root, width=50, height=50)

    def callback(self, event):
        new_duration = a.get_music_duration()
        self.music_duration_text.set(new_duration)

    def gui_bind(self):
        self.pre_music_button.bind("<Button-1>", self.callback)
        self.next_music_button.bind("<Button-1>", self.callback)

    def gui_music_duration_label_bind(self):
        pass

    def gui_arrange(self):
        self.play_button.pack()
        self.pause_button.pack()
        self.stop_button.pack()
        self.volume_up_button.pack()
        self.volume_down_button.pack()
        self.pre_music_button.pack()
        self.next_music_button.pack()
        self.music_duration_label.pack()
        self.frame.pack()


def main():
    m_p = MusicPlayer()
    m_p.gui_bind()
    m_p.gui_arrange()
    tkinter.mainloop()


if __name__ == "__main__":
    main()
