import threading
import tkinter
import utils
from app.app import App
from app.lyric import Lyric

a = App()
l = Lyric(a)


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

        self.playback_mode_text = tkinter.StringVar(value="顺序播放")
        self.switch_playback_mode_button = tkinter.Button(self.root, textvariable=self.playback_mode_text, )

        self.test_end_event_button = tkinter.Button(self.root, command=utils.test_end_event, text="快进250s(for test)")

        self.test_get_pos_button = tkinter.Button(self.root, command=utils.test_get_pos, text="获取当前播放时间(for test)")

        self.lyric_text = tkinter.StringVar()
        self.lyric_label = tkinter.Label(self.root, textvariable=self.lyric_text)

    def gui_bind(self):
        self.pre_music_button.bind("<Button-1>", self.music_duration_callback)
        self.next_music_button.bind("<Button-1>", self.music_duration_callback)
        self.switch_playback_mode_button.bind("<Button-1>", self.playback_mode_callback)

    def music_duration_callback(self, event):
        new_duration = a.get_music_duration()
        self.music_duration_text.set(new_duration)

    def playback_mode_callback(self, event):
        a.switch_playback_mode()
        mode = ["顺序播放", "单曲循环", "随机播放"]
        self.playback_mode_text.set(mode[a.playback_mode])

    def gui_update_lyric(self):
        l.start_update_lyric_thread()
        while True:
            self.lyric_text.set(l.sentence)

    def gui_update(self):
        update_lyric_thread = threading.Thread(target=self.gui_update_lyric)
        update_lyric_thread.daemon = True
        update_lyric_thread.start()

    def gui_arrange(self):
        self.play_button.pack()
        self.pause_button.pack()
        self.stop_button.pack()
        self.volume_up_button.pack()
        self.volume_down_button.pack()
        self.pre_music_button.pack()
        self.next_music_button.pack()
        self.music_duration_label.pack()
        self.switch_playback_mode_button.pack()

        self.test_end_event_button.pack()

        self.test_get_pos_button.pack()

        self.lyric_label.pack()


def main():
    m_p = MusicPlayer()
    m_p.gui_bind()
    m_p.gui_arrange()
    m_p.gui_update()
    tkinter.mainloop()


if __name__ == "__main__":
    main()
