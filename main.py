import pyttsx3
import pyscreenshot
import turtle
import pyautogui
import cv2
import numpy as np
import time
from moviepy.editor import *


def turtle_fun(x=0, y=0, width=400, height=400):
    sc = turtle.Screen()
    sc.setup(width, height, startx=x, starty=y)
    # sc.bgcolor("blue")

    t = turtle.Turtle()
    t.forward(200)
    # turtle.done()


def text_to_voice(text: str, file_name='temp.mp3') -> None:
    engine = pyttsx3.init()
    engine.say(text)
    engine.save_to_file(text, file_name)
    engine.runAndWait()


def screenshot(x=0, y=0, w=550, h=550):
    w += 110
    h += 140
    # To capture the screen
    image = pyscreenshot.grab(bbox=(x, y, w, h))
    # To display the captured screenshot
    image.show()
    # To save the screenshot
    image.save("GeeksforGeeks.png")


def video_screen_capture(width=1920,
                         height=1080,
                         codec='XVID',
                         output_video_file='output.avi',
                         fps=120.0,
                         video_clip_duration=10
                         ):
    SCREEN_SIZE = (width, height)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video_file, fourcc, fps / 3, SCREEN_SIZE)
    prev = 0
    start = time.time()
    while True:
        cur_time = time.time()
        time_elapsed = cur_time - prev
        img = pyautogui.screenshot()
        if time_elapsed > 1.0 / fps:
            prev = cur_time
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            out.write(frame)
        if cur_time > start + video_clip_duration:
            break
    cv2.destroyAllWindows()


def combine_audio(video_file='temp.avi',
                  audio_file='temp.mp3',
                  output_video_file='va_output.avi'
                  ) -> None:
    video_clip = VideoFileClip(output_video_file)
    video_clip.write_videofile(video_file, audio=audio_file, threads=1, codec="libx264")


if __name__ == "__main__":
    # text_to_voice('Курс для 9 класса по ФГОС. 2 часа в неделю • Массивы. Создание, ввод/вывод Продолжить Урок 2. Добавление элементов в массивДомашняя работа «Добавление элементов в массив»')
    # text_to_voice
    # combine_audio()
    video_screen_capture(output_video_file='123.avi')
