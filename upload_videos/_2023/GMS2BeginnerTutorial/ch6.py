from janim import *
from upload_videos._2023.GMS2BeginnerTutorial.header import *
from utils.svgicon import Gear
from utils.codeview import *

class Intro(IntroTemplate):
    str2 = '第6节 实例变量与临时变量'

class _1(Scene):
    def construct(self) -> None:
        obj_rect = RoundedRectangle(width=1, height=1, corner_radius=0.1)
        
        obj_gear = Gear().set_stroke(width=0.03).set_fill(GREY, 1)
        obj_gear.scale(0.5).rotate(12 * DEGREES)
        obj_gear.move_to(obj_rect.get_bbox_point(DR) + UL * 0.15)
        
        obj_text = Text('Obj', font_size=36, color=ht2c['Object'])
        obj_text.scale(0.5).next_to(obj_rect.get_bbox_point(UL), DR, SMALL_BUFF)

        obj = VGroup(obj_rect, obj_gear, obj_text)

        arrow = Arrow(LEFT, RIGHT)

        inst_img = ImgItem('assets/gm/sprite.png').set_height(1.5).next_to(arrow)
        inst_text = Text('Inst', font_size=36, color=ht2c['Instance'])
        inst_text.scale(0.5).next_to(inst_img.get_bbox_point(DL), UR, SMALL_BUFF)
        inst = Group(inst_img, inst_text)
        
        self.wait()
        self.play(ShowCreation(obj))
        self.wait()
        self.play(
            obj.anim(run_time=0.6).next_to(arrow, LEFT),
            GrowArrow(arrow, begin_time=0.4, run_time=0.6),
            FadeIn(inst, scale=1.2, run_time=0.6)
        )
        self.wait(2)

class _2(Scene):
    def construct(self) -> None:
        apply_custom_colors()

        c1 = CodePlane(
            '<c KEYWORD>var</c> <c VAR>a</c> = <c DIGIT>10</c>;',
            background_kwargs=dict(
                buff=(SMALL_BUFF, SMALL_BUFF, 0.5, SMALL_BUFF)
            )
        )
        c1.txt[0][:3].set_opacity(0)
        
        c2 = CodePlane(
            '<c COMMENT>// 在角色移动例子的 右方向键事件 中</c>\n'
            '<c KEYWORD>if</c> (<c BUILTIN_VAR>x</c> > <c DIGIT>500</c>) {\n'
            '    <c KEYWORD>var</c> <c TMPVAR>tmp</c> = <c FUNC>random_range</c>(<c DIGIT>100</c>, <c DIGIT>200</c>);\n'
            '    <c BUILTIN_VAR>x</c> = <c TMPVAR>tmp</c> * <c DIGIT>2</c>;\n'
            '    <c BUILTIN_VAR>y</c> = <c TMPVAR>tmp</c> * <c DIGIT>1.5</c>;\n'
            '}'
        )
        
        self.wait()
        self.play(FadeIn(c1, UP))
        self.wait()
        self.play(
            c1.txt[0][:3].anim().set_opacity(1), 
            c1.txt[0][4].anim().set_color(custom_colors['TMPVAR'])
        )
        self.wait(2)

        self.play(FadeOut(c1, run_time=0.6), FadeIn(c2))
        self.wait(2)

