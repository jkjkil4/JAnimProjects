from utils.shape import *
from upload_videos._2023.GMS2BeginnerTutorial.header import *

class Intro(IntroTemplate_Light):
    str2 = '第2节 下载安装'

class Indicator(IndicatorTemplate):
    verts = [
        [4.27, 2.86, 0],
        [5.67, 2.37, 0],
        [-1.81, 0.18, 0],
        [-0.90, -0.39, 0],
        [-6.31, 2.61, 0],
        [1.72, 2.09, 0],
        [-6.41, 3.85, 0],
        [-5.91, 3.54, 0],
        [-6.40, 2.07, 0],
        [-5.01, 1.76, 0],
        [-3.64, 2.53, 0],
        [-2.41, 2.27, 0],
        [-2.24, 2.09, 0],
        [1.35, 1.70, 0],
    ]

class _1(Scene):
    background_color = '#eeeeee'
    def construct(self) -> None:
        ico8 = ImgItem('assets/gm/GM8.png', height=1)
        ico2 = ImgItem('assets/gm/GMS2.png', height=1)

        txt8 = Text('Windows XP +', font_size=36, color=GREY_D)
        txt2 = Text('x64 Windows 7 +', font_size=36, color=GREY_D)

        vg = Group(
            Group(ico8, txt8).arrange(),
            Group(ico2, txt2).arrange()
        ).arrange(DOWN, buff=MED_LARGE_BUFF, aligned_edge=LEFT)

        self.wait()
        self.play(FadeIn(ico8, scale=0.9), Write(txt8))
        self.wait()
        self.play(FadeIn(ico2, scale=0.9), Write(txt2))
        self.wait()

class _2(Scene):
    def construct(self) -> None:
        txt = Text('进行了剪辑，实际情况用时会长一些', font_size=20)
        txt.set_stroke(BLACK, 0.04, background=True).to_border(UL)
        self.add(txt)
        self.wait(0.1)
