from upload_videos._2023.GMS2BeginnerTutorial.header import *

class Intro(IntroTemplate):
    str2 = '内置变量（初步了解）'

class _1(Scene):
    def construct(self) -> None:
        self.wait()

        vars = Text('id、x、y、speed、direction、···', color=custom_colors['BUILTIN_VAR'])
        rect = SurroundingRectangle(vars, buff=MED_SMALL_BUFF).set_color(DARK_GREEN)
        txt_vars = Text('内置变量', color=GREEN).next_to(rect, UP, SMALL_BUFF, LEFT)

        self.play(Write(vars), ShowCreation(rect, begin_time=0.5))
        self.wait()
        self.play(FadeIn(txt_vars))

        self.wait(2)

class _2(Scene):
    def construct(self) -> None:
        spr = ImgItem('assets/gm/sprite.png')
        
        self.wait(0)

        dl = DashedLine(TOP, BOTTOM).set_color(GREY)
        
        txt1 = Text('Sprite 编辑器').shift(LEFT_SIDE * 0.5)
        txt2 = Text('运行界面').shift(RIGHT_SIDE * 0.5)
        txts = VGroup(txt1, txt2).align_to(TOP, UP).shift(DOWN * DEFAULT_ITEM_TO_EDGE_BUFF)
        self.add(dl, txts)



