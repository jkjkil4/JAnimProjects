from janim import *
from upload_videos._2023.GMS2BeginnerTutorial.header import *
from utils.codeview import *
from utils.shape import *

class Intro(IntroTemplate):
    str2 = '第5节 代码基本语法 前半'

class SubTitle1(SubTitleTemplate):
    text = '基本思维'

class SubTitle2(SubTitleTemplate):
    text = '注释'

class SubTitle3_1(SubTitleTemplate):
    text = '赋值语句'

class SubTitle3_2(SubTitleTemplate):
    text = '运算语句'

class SubTitle4(SubTitleTemplate):
    text = '基本数据类型'

class Indicator(IndicatorTemplate):
    verts = [
        [-3.42, 0.18, 0],
        [-0.96, -0.15, 0],
        [-1.67, 0.00, 0],
        [-0.55, -0.28, 0],
        [-3.47, 1.64, 0],
        [-2.55, 1.29, 0],
        [-3.51, 1.36, 0],
        [-2.53, 0.99, 0],
        [-3.44, 1.10, 0],
        [-1.39, 0.76, 0],
        # [-0.40, 2.00, 0],
        [-3.47, 1.45, 0],
        [-2.47, 1.13, 0],
        [-1.66, 1.27, 0],
        [-0.56, 0.90, 0],
    ]

class _1(Scene):
    def construct(self) -> None:
        apply_custom_colors()

        code = (
            '<c KEYWORD>var</c> <c TMPVAR>inst</c> = <c FUNC>instance_create_layer</c>(...);\n'
            '<c TMPVAR>inst</c>.<c BUILTIN_VAR>direction</c> = <c FUNC>point_direction</c>(...);\n'
            '<c TMPVAR>inst</c>.<c BUILTIN_VAR>speed</c> = <c DIGIT>5</c>;'
        )

        c = CodePlane(code)

        arrow = Arrow(ORIGIN, RIGHT * 0.5, buff=0).set_color(BLUE_D).next_to(c.txt[0], LEFT, SMALL_BUFF)
        self.wait()
        self.play(FadeIn(c, UP))
        self.wait(0.1)
        self.play(GrowArrow(arrow))
        self.wait(0.5)
        self.play(arrow.anim().next_to(c.txt[1], LEFT, SMALL_BUFF), run_time=0.5)
        self.wait(0.5)
        self.play(arrow.anim().next_to(c.txt[2], LEFT, SMALL_BUFF), run_time=0.5)
        self.wait()
        self.play(*map(FadeOut, (c, arrow)))
        self.wait()

class _2(Scene):
    def construct(self) -> None:
        apply_custom_colors()

        dl = DashedLine(ORIGIN, UP * FRAME_HEIGHT).set_color(GREY_D).move_to(ORIGIN)

        size = (5, 5)

        bgleft = VGroup(
            Text('需要的步骤', font_size=30),
            CodeBackground(*size)
        ).arrange(DOWN).next_to(dl, LEFT, LARGE_BUFF)

        left = Text(
            '用3块钱买苹果\n'
            '给苹果削皮\n'
            '给苹果切块\n'
            '吃下苹果',
            font='Noto Sans S Chinese Medium',
            font_size=18
        ).move_to(bgleft)

        bgright = VGroup(
            Text('代码逻辑', font_size=30),
            CodeBackground(*size)
        ).arrange(DOWN).next_to(dl, RIGHT, LARGE_BUFF)

        right = VCodeLines(
            '<c KEYWORD>var</c> <c TMPVAR>item</c> = <c FUNC>buy</c>(<c STR>"apple"</c>, <c DIGIT>3</c>);\n'
            '<c TMPVAR>item</c>.<c FUNC>peel</c>();\n'
            '<c TMPVAR>item</c>.<c FUNC>cut</c>();\n'
            '<c FUNC>eat</c>(<c TMPVAR>item</c>);'
        ).move_to(bgright)

        tip = Text('*瞎写的代码，实际没有内置这几个功能', font_size=14).to_border(UR)
        arrow = Arrow(bgleft.get_right() + LEFT * 0.5, bgright.get_left() + RIGHT * 0.5, buff=0).set_color(BLUE)

        self.add(dl, bgleft, bgright, left)
        self.wait()
        self.play(Write(right), FadeIn(tip))
        self.wait()
        self.play(GrowArrow(arrow))
        self.wait()
        self.play(*map(FadeOut, self.items), run_time=0.5)
        self.wait()

class _3(Scene):
    def construct(self) -> None:
        bg = surcamera().set_stroke(width=0).set_fill('#222222', 0.85)

        c = CodePlane(
            '/*\n'
            '    这是注释内容\n'
            '    可以写很多行\n'
            '*/',
            txt_kwargs={ 'color': custom_colors['COMMENT'] }
        )

        self.play(FadeIn(bg), FadeIn(c, UP))
        self.wait(2)

# class _4(Scene):
#     def construct(self) -> None:
#         c = CodePlane('<>变量名 = 表达式;')
#         c[0][:3].set_color(C_VAR)

#         anim1, old, new = c.lines.replace_animate(0, 'a = 1;')
#         new[0].set_color(C_VAR)
#         new[-2].set_color(C_DIGIT)
        
#         anim2, old, new = c.lines.replace_animate(0, 'a = (8 - 2) * 2;')
#         se = StrSearcher(new.text).s('a', C_VAR).s('8', C_DIGIT).s('2', C_DIGIT).s('2', C_DIGIT)
#         for rg, col in se.results:
#             rg = to_manimtext_idx(new.text, *rg)
#             new[rg[0]:rg[1]].set_color(col)
        
#         vg = Group(
#             Text('_', base_color=C_KEYWORD), *[Mobject() for _ in range(25)],
#             *[Text('|' + chr(l) + '|', base_color=C_KEYWORD, t2c={'|': '#222222'}) for l in range(ord('A'), ord('Z') + 1)],
#             *[Text('|' + chr(l) + '|', base_color=C_KEYWORD, t2c={'|': '#222222'}) for l in range(ord('a'), ord('z') + 1)],
#             *[Text(str(d), base_color=C_KEYWORD) for d in range(0, 10)], *[Mobject() for _ in range(16)]
#         ).arrange_in_grid(4, 26, h_buff=0, v_buff=0.2).to_edge(LEFT)
        
#         self.wait()
#         self.play(FadeIn(c, UP))
#         self.wait()
#         self.play(anim1)
#         self.wait()
#         self.play(anim2)
#         self.wait()
#         self.play(
#             FadeOut(c, run_time=0.6), 
#             FadeIn(vg, LEFT * 10, rate_func=rush_from, run_time=1.5)
#         )
#         self.wait()
        
#         c = CodePlane(
#             '''abcd1 = 1;
# 1abcd = 1;
# test_var = 1;
# test_@ = 1;
# '''
#         )
        
#         self.play(vg.animate.set_opacity(0.3), FadeIn(c, scale=1.2))
#         self.wait()
#         self.play(
#             ShowCreation(Cross(c.lines[1], stroke_width=6).set_opacity(0.6)), 
#             ShowCreation(Cross(c.lines[-1], stroke_width=6).set_opacity(0.6))
#         )
#         self.wait()
#         self.play(*map(FadeOut, self.mobjects))

# class _5(Scene):
#     def construct(self) -> None:
#         c = CodePlane(
#             '''val = 1;
# show_message(Val);'''
#         )
#         se = StrSearcher(c.lines.text).s('val', C_VAR).s('1', C_DIGIT)\
#             .s('show_message', C_FUNC).s('Val', C_VAR)
#         for rg, col in se.results:
#             c.lines.set_code_color(*rg, col)
        
#         self.add(c)
#         self.wait(2)

# class _6(Scene):
#     def construct(self) -> None:
#         vg = VGroup(
#             Text('基本运算', base_color=C_KEYWORD), Text('+   -   *   /   %', font='Source Code Pro'),
#             Text('逻辑运算', base_color=C_KEYWORD), Text('&&   ||   !', font='Source Code Pro'),
#             Text('位运算', base_color=C_KEYWORD), Text('&   |   ^   ~   <<   >>', font='Source Code Pro'),
#             Text('幂运算', base_color=C_KEYWORD), Text('power(3, 2)', font='Source Code Pro')
#         ).scale(0.7).arrange_in_grid(4, 2, h_buff=0, v_buff=0.4, aligned_edge=LEFT).shift(LEFT)
        
#         self.wait()
#         def anim(idx):
#             self.play(FadeIn(vg[2 * idx], scale=0.8, run_time=1), Write(vg[2 * idx + 1]))
#         for i in range(4):
#             anim(i)
#             self.wait()
#         self.wait(2)

# class _6_1(Scene):
#     def construct(self) -> None:
#         bg = surcamera().set_stroke(width=0).set_fill('#222222', 0.85)

#         t2c = { '÷': BLUE, '=': BLUE, '···': BLUE, '%': BLUE, '→': BLUE }

#         txt1 = Text('7 ÷ 3 = 2 ··· 1', t2c=t2c, font='Source Code Pro').scale(0.7)
#         txt2 = Text('7   % 3 → 1', t2c=t2c, font='Source Code Pro').scale(0.7)
#         txt3 = Text('5.2 % 2 → 1.20', t2c=t2c, font='Source Code Pro').scale(0.7)

#         vg1 = VGroup(txt2, txt3).arrange(DOWN, aligned_edge=LEFT)
#         vg2 = VGroup(txt1, vg1).arrange(DOWN, buff=LARGE_BUFF, aligned_edge=LEFT)
        
#         self.play(FadeIn(bg), Write(txt1))
#         self.wait()
#         self.play(Write(txt2))
#         self.wait()
#         self.play(Write(txt3))
#         self.wait(2)

# class _7(Scene):
#     def construct(self) -> None:
#         bg = surcamera().stretch(0.5, 1, about_edge=DOWN)
#         bg.set_stroke(width=0).set_fill('#222222', 0.85)

#         vg = VGroup(
#             Text('字符串').set_color(C_STR),
#             Text('数值').set_color(C_DIGIT),
#             Text('数值').set_color(C_DIGIT),
#             Text('字符串').set_color(C_STR),
#         ).scale(0.7).arrange_in_grid(2, 2, h_buff=2, v_buff=0.7).next_to(ORIGIN, DOWN, MED_LARGE_BUFF)

#         arrow1 = Arrow(LEFT, RIGHT, color=BLUE).move_to(vg[0], coor_mask=(0, 1, 0))
#         txt1 = Text('real()').scale(0.5).next_to(arrow1, UP, SMALL_BUFF)
#         txt1[:4].set_color(C_FUNC)

#         arrow2 = Arrow(LEFT, RIGHT, color=BLUE).move_to(vg[2], coor_mask=(0, 1, 0))
#         txt2 = Text('string()').scale(0.5).next_to(arrow2, UP, SMALL_BUFF)
#         txt2[:6].set_color(C_FUNC)

#         self.play(FadeIn(bg))
#         self.play(*[FadeIn(m, scale=1.2) for m in vg])
#         self.wait()
#         arrow1.generate_target()
#         arrow1.stretch(0, 0, about_edge=LEFT)
#         self.play(MoveToTarget(arrow1), Write(txt1))
#         self.wait()
#         arrow2.generate_target()
#         arrow2.stretch(0, 0, about_edge=LEFT)
#         self.play(MoveToTarget(arrow2), Write(txt2))
#         self.wait()

#         num46 = Text('46').scale(0.7).set_color(C_DIGIT).move_to(vg[2])
#         str46 = Text('"46"').scale(0.7).set_color(C_STR).move_to(vg[3])
#         txt46 = Text('string(46)').scale(0.5).move_to(txt2)
#         txt46[:6].set_color(C_FUNC)
#         txt46[7:9].set_color(C_DIGIT)

#         self.play(Transform(vg[2], num46))
#         self.play(Transform(txt2, txt46))
#         self.play(Transform(vg[3], str46))
#         self.wait(2)



