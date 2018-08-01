import tkinter
import app

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

    def gui_arrange(self):
        self.play_button.pack()
        self.pause_button.pack()
        self.stop_button.pack()
        self.volume_up_button.pack()
        self.volume_down_button.pack()
        self.pre_music_button.pack()
        self.next_music_button.pack()


def main():
    MP = MusicPlayer()
    MP.gui_arrange()
    tkinter.mainloop()


if __name__ == "__main__":
    main()
