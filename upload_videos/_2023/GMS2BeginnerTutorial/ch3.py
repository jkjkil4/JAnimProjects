from janim import *
from upload_videos._2023.GMS2BeginnerTutorial.header import *
from utils.shape import *


class Intro(IntroTemplate_Light):
    str2 = '第3节 第一步尝试'

class Indicator1(IndicatorTemplate):
    verts = [
        [2.99, -0.77, 0],
        [5.21, -1.08, 0],
        [5.08, -2.84, 0],
        [6.43, -3.19, 0],
        [2.83, -0.74, 0],
        [5.02, -1.08, 0],
        [4.89, -1.24, 0],
        [6.24, -1.51, 0],

        [4.24, -2.10, 0],
        [6.98, -2.39, 0],
        [-4.24, 2.39, 0],
        [-1.88, 1.94, 0],
        [-2.98, 1.78, 0],
        [-1.96, 1.45, 0],
        [-2.96, 1.47, 0],
        [-1.94, 1.14, 0],
        [-4.18, 1.82, 0],
        [-3.08, 1.16, 0],

        [-4.18, 1.82, 0],
        [-3.08, 1.16, 0],
        [-6.87, 0.36, 0],
        [-5.96, 0.04, 0],

        [-2.98, 1.78, 0],
        [-1.96, 1.45, 0],

        [4.33, -1.90, 0],
        [6.95, -2.13, 0],
        [-3.38, 0.71, 0],
        [-1.99, 0.46, 0],
        [-0.24, 0.36, 0],
        [0.27, -0.18, 0],
        [4.44, -0.47, 0],
        [5.50, -0.73, 0],
    ]

class Indicator2(IndicatorTemplate):
    verts = [
        [6.68, 3.59, 0],
        [7.01, 3.32, 0],
        [-1.16, 2.86, 0],
        [0.74, 2.64, 0],
        [-4.89, 3.60, 0],
        [-4.61, 3.26, 0],
    ]

class _1(Scene):
    background_color = '#eeeeee'
    def construct(self) -> None:
        t1 = Text('Sprite', font_size=48, color=YELLOW_E)
        t2 = Text('Object', font_size=48, color=BLUE_D)
        vg_t1_t2 = VGroup(t1, t2).arrange(RIGHT, buff=LARGE_BUFF)
        vg_t1_t2.set_stroke(BLACK, 0.02, background=True)

        self.play(Write(t1))
        self.wait(0.5)
        self.play(Write(t2))
        self.wait()
        self.play(*map(FadeOut, (t1, t2)))

        vg1 = VGroup(
            Text(
                'Sprite（精灵）',
                font_size=48, 
                color=YELLOW_E
            ).set_stroke(BLACK, 0.02, 1, True),
            Text(
                'Sprite 是一个图像<c GREY_B>（序列）</c>，你可以对其进行编辑或者'
                '导入现有的图像文件', 
                font_size=32, 
                color=GREY_D,
                format=Text.Format.RichText
            ),
        ).arrange(DOWN, aligned_edge=LEFT)

        vg2 = VGroup(
            Text(
                'Object（物体）', 
                font_size=48,
                color=BLUE_D
            ).set_stroke(BLACK, 0.02, 1, True),
            Text(
                'Object 是游戏的“活动部件”，玩家、'
                '物品、敌人等都需要它来实现',
                font_size=32,
                color=GREY_D
            ),
        ).arrange(DOWN, aligned_edge=LEFT)
        
        vg = VGroup(vg1, vg2)
        vg.arrange(DOWN, aligned_edge=LEFT, buff=MED_LARGE_BUFF)
        vg.scale(0.7).to_border(UL)

        for g in vg:
            self.play(
                FadeIn(g[0], scale=0.9), 
                Write(g[1], begin_time=0.7)
            )
        self.wait()
        
        spr = ImgItem('assets/gm/sprite.png', height=1).shift(DR + UP * 0.5)
        rect = Rectangle(0.5, 1).set_stroke(BLUE_D, 0.06).shift(DOWN * 0.5)

        self.play(FadeIn(rect, scale=1.1))
        self.wait()
        self.play(
            Succession(
                rect.anim()                         .shift(UP * 0.5),
                rect.anim(path_arc=40 * DEGREES)    .shift(DR * 0.5),
                rect.anim(path_arc=230 * DEGREES)   .shift(LEFT * 0.5),
                run_time=1
            )
        )
        self.wait()
        self.play(FadeIn(spr, DOWN * 0.3, rate_func=rush_from))
        self.play(
            spr .anim()                 .shift(LEFT), 
            rect.anim(begin_time=0.4)   .shift(DL * 0.1), 
            rate_func=rush_into
        )
        self.wait()

class _4(Scene):
    background_color = '#eeeeee'
    def construct(self) -> None:
        bg = surcamera().set_stroke(width=0).set_fill('#eeeeee', 0.85)

        txt = Text(
            '       <ds BLACK YELLOW_E>Sprite</ds> 是游戏的贴图素材，可以设置到 '
            '<ds BLACK BLUE_D>Object</ds> 上使其展现出贴图的样子，构成游戏画面。\n\n'
            '       <ds BLACK BLUE_D>Object</ds> 处理了游戏的操作逻辑，作为“活动部件”，'
            '成为 <ds BLACK GREY_BROWN>Room</ds> 这一舞台上的角色。\n\n'
            '       暂未编写逻辑的 <ds BLACK BLUE_D>Object</ds> 无法进行操作。',
            color=GREY_D,
            format=Text.Format.RichText
        )
        txt_groups = [NoRelVGroup(*line) for line in (txt[0], txt[2], txt[4])]
        txt.word_wrap(FRAME_WIDTH * 0.63).shift(UL)

        self.play(FadeIn(bg))
        for group in txt_groups:
            self.play(Write(group))
            self.wait()
        self.play(*map(FadeOut, (bg, txt)))
