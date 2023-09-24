from janim import *

ht2c = {
    'GML': GREEN, 'Rooms': GREY_BROWN,
    'Sprite': YELLOW_E, 'Object': BLUE_D, 'Instance': GREEN_D, 'Room': GREY_BROWN, 'Script': GREEN_D, 'Event': GREEN_D,
}

custom_colors = {
    'KEYWORD': '#ffb871',
    'FUNC': '#ffb871',
    'BUILTIN_VAR': '#58e35a',
    'VAR': '#b2b1ff',
    'TMPVAR': '#fff899',
    'DIGIT': '#ff8080',
    'STR': '#fcfc00',
    'COMMENT': '#5a985a',
    'EVENT': ht2c['Event']
}

DARK_GREEN = '#3f6e2b'

def apply_custom_colors() -> None:
    import janim.constants.colors as colors
    colors.__dict__.update(custom_colors)

class IntroTemplate(Scene):
    str1 = '<c BLUE>【GMS2】</c>GameMaker Studio 2 零基础入门教程'
    str2 = 'TEST'
    str1_color = GREY_A
    str2_color = GREY_B
    background_color = '#222222'

    def construct(self) -> None:
        txt1 = Text(self.str1, color=self.str1_color, font_size=28, format=Text.Format.RichText)
        txt2 = Text(self.str2, color=self.str2_color, font_size=32, format=Text.Format.RichText)
        txt = VGroup(txt1, txt2).arrange(DOWN)

        self.wait(0.1)
        self.play(DrawBorderThenFill(txt))
        self.wait()
        self.play(FadeOut(txt))

class IntroTemplate_Light(IntroTemplate):
    str1_color = GREY_D
    str2_color = GREY
    background_color = '#eeeeee'

class SubTitleTemplate(Scene):
    text = 'TEST'
    buff = MED_SMALL_BUFF

    def construct(self) -> None:
        txt = Text(self.text, font_size=36).set_color(BLUE_D).set_stroke(BLACK, 0.02, background=True)
        rect = Rectangle(FRAME_WIDTH, txt.get_height() + 2 * self.buff)
        rect.set_fill(WHITE, 0.85).set_stroke(width=0).shift(LEFT * FRAME_WIDTH)

        self.play(rect.anim().shift(RIGHT * FRAME_WIDTH), Write(txt), rate_func=rush_from, run_time=0.5)
        self.wait(2)
        self.play(rect.anim().shift(RIGHT * FRAME_WIDTH), FadeOut(txt), rate_func=rush_into, run_time=0.5)

class IndicatorTemplate(Scene):
    verts = []

    def construct(self) -> None:
        for i in range(0, len(self.verts) // 2):
            r = Rectangle(self.verts[i * 2], self.verts[i * 2 + 1])
            r.set_stroke(YELLOW, 0.02, 1, False)
            self.play(FadeIn(r, scale=0.65, rate_func=rush_from, run_time=0.5))
            self.wait()
            self.play(FadeOut(r, run_time=0.5))
            self.wait()

# class GMRoomPlane(VGroup):
#     def __init__(self, xlen, ylen, color, **kwargs):
#         self.np = NumberPlane((0, xlen), (0, ylen)).stretch(-1, 1).set_color(color)
#         self.npOrig = Dot(self.np.c2p(), color = BLACK)
#         self.npXArrow = Arrow(self.np.x_axis.get_start(), self.np.x_axis.get_end() + RIGHT * 0.3, buff = 0).set_color(BLACK)
#         self.npYArrow = Arrow(self.np.y_axis.get_start(), self.np.y_axis.get_end() + DOWN * 0.3, buff = 0).set_color(BLACK)
#         self.npXLabel = Tex('x', color = BLACK).next_to(self.npXArrow)
#         self.npYLabel = Tex('y', color = BLACK).next_to(self.npYArrow, DOWN)
#         super().__init__(*[self.np, self.npOrig, self.npXArrow, self.npYArrow, self.npXLabel, self.npYLabel], **kwargs)

#     def animate1(self):
#         return ShowCreation(self.np, lag_ratio = 0.01)
#     def animate2Array(self):
#         return [FadeIn(self.npOrig, scale_factor = 1.3), 
#             GrowArrow(self.npXArrow), GrowArrow(self.npYArrow),
#             DrawBorderThenFill(self.npXLabel), DrawBorderThenFill(self.npYLabel)]