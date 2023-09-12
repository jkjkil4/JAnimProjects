from janim import *
# import janim.item.boolean_ops as boolean_ops
from upload_videos._2023.GMS2BeginnerTutorial.header import *
from utils.codeview import *
# from utils.svgicon import *

class Intro(IntroTemplate):
    str2 = '第5节 代码基本语法 后半'

class SubTitle1(SubTitleTemplate):
    text = '函数调用'

class SubTitle2(SubTitleTemplate):
    text = '条件语句'

class SubTitle3(SubTitleTemplate):
    text = '实例变量与临时变量'

class SubTitle4(SubTitleTemplate):
    text = '报错信息'

class Indicator(IndicatorTemplate):
    verts = [
        [-2.56, 1.20, 0],
        [-0.07, 0.99, 0],
        [-0.73, 1.33, 0],
        [0.43, 1.13, 0]
    ]

class _1(Scene):
    def construct(self) -> None:
        apply_custom_colors()

        c = CodePlane(
            '<c FUNC>show_message</c>(<c VAR>a</c>)\n'
            '<c FUNC>string</c>(<c VAR>res</c>)\n'
            '<c FUNC>real</c>(<c VAR>str</c>)\n'
            '<c FUNC>get_string</c>(<c STR>"Input:"</c>, <c STR>""</c>)'
        )
        
        txtL, txtR = Group(), Group()
        for line in c.txt:
            idx = line.text.index('(')
            txtL.add(line[:idx])
            txtR.add(line[idx:])
        
        self.wait()
        self.play(FadeIn(c, UP))
        self.wait()

        self.play(txtR.anim().set_opacity(0.3))
        self.wait()
        self.play(txtL.anim().set_opacity(0.3), txtR.anim().set_opacity(1))
        self.wait()

        self.play(txtL[0].anim().set_opacity(1))
        self.play(ShowCreationThenFadeAround(txtL[0]))
        self.wait()
        self.play(ShowCreationThenFadeAround(txtR[0]))
        self.wait()

        txtRet = Text(
            '没有返回值\n'
            '返回字符串\n'
            '返回数值\n'
            '返回字符串',
            font_size=16
        ).set_opacity(0.5)

        self.play(txtL.anim().set_opacity(1))

        NoRelGroup(c.background.generate_target(), txtRet).arrange().to_center()
        c.txt.generate_target().arrange(DOWN, aligned_edge=RIGHT, coor_mask=(1, 0, 0)).move_to(c.background.target())

        self.play(
            *map(MoveToTarget, (c.background, c.txt)),
            FadeIn(txtRet, LEFT)
        )
        self.wait()

        self.play(txtRet[0].anim().set_opacity(1))
        self.wait()
        self.play(txtRet[2].anim().set_opacity(1))
        self.wait()

        indication1 = ShowCreationThenDestruction(Underline(txtR[-1][1:9], color=YELLOW), run_time=1.5, begin_time=0.6)
        indication2 = ShowCreationThenDestruction(Underline(txtR[-1][11:13], color=YELLOW).set_y(indication1.item_for_anim.get_y()), run_time=1.2)
        self.play(
            c.txt[-1].anim().set_opacity(1),
            indication1
        )
        self.wait()
        self.play(indication2)
        self.wait(2)        

# class _2(Scene):
#     def construct(self) -> None:
#         apply_custom_colors()

#         txtRd = Text(
#             '<c VAR>a</c> = <c FUNC>random_range</c>(<c DIGIT>400</c>, <c DIGIT>800</c>);'
#             font_size=32,
#             format=Text.Format.RichText
#         )
        
#         nline = NumberLine((400, 800, 100), unit_size=0.006, include_numbers=True)
#         nline.rotate(PI / 2, about_point=nline.get_left())
#         for number in nline.numbers:
#             number.scale(0.6).next_to(nline[0], LEFT, buff=SMALL_BUFF, coor_mask=(1, 0, 0))

#         Group(txtRd, nline).arrange(DOWN, MED_LARGE_BUFF, aligned_edge=LEFT)

#         arrow = Arrow(ORIGIN, RIGHT * 0.5, buff=0).next_to(txtRd, LEFT)

#         self.add(txtRd)
#         self.wait(2)
#         self.play(Write(nline), FadeIn(arrow))
#         self.wait()
        
#         num = None
#         txtRd.save_state()
#         random.seed(5)
#         for _ in range(8):
#             val = random.randint(40000, 80000) / 100
#             new = Text(f'a = {val}', t2c={ 'a': C_VAR, f'{val}': C_DIGIT })
#             new.scale(0.6).next_to(nline.n2p(val), RIGHT, MED_SMALL_BUFF)

#             self.play(
#                 arrow.animate.shift(LEFT * 0.3),
#                 rate_func=there_and_back,
#                 run_time=0.2
#             )

#             txtRd.set_color(YELLOW)
#             if num:
#                 num.become(new)
#             else:
#                 num = new
#                 self.add(num)
            
#             self.play(txtRd.animate.restore(), run_time=0.15)
#         self.wait()

# class _3(Scene):
#     def construct(self) -> None:
#         c = CodePlane(
#             '''if (条件) {
# ····代码块···
# }''')
#         se = StrSearcher(c.lines.text).s('if', C_KEYWORD).s('条件', C_VAR).s('代码块', C_VAR)
#         for rg, col in se.results:
#             c.lines.set_code_color(*rg, col)
        
        
#         self.wait()
#         self.play(FadeIn(c, UP))
#         self.wait()
#         self.play(Indicate(c.lines[0][3:5], scale_factor=1.05))
#         self.wait()
#         self.play(Indicate(c.lines[1][4:7], scale_factor=1.05))
#         self.wait(2)

# class _4(Scene):
#     def construct(self) -> None:
#         c1 = CodePlane(
#             '''a > b
# a < b
# a == b
# a != b''')
        
#         c2 = CodePlane(
#             '''a >= b
# a <= b''')
        
#         se = StrSearcher(c1.lines.text).all('a', C_VAR).all('b', C_VAR)
#         for rg, col in se.results:
#             c1.lines.set_code_color(*rg, col)
#         se = StrSearcher(c2.lines.text).all('a', C_VAR).all('b', C_VAR)
#         for rg, col in se.results:
#             c2.lines.set_code_color(*rg, col)
        
#         planes = Group(c1, c2).arrange(DOWN, buff=SMALL_BUFF)

#         txt1 = VGroup(
#             Text('a 和 b 是否相同'), 
#             Text('(虽然GM允许你省略成单个等号，但是仍然建议你写全)').scale(0.6).set_color(GREY).set_stroke(width=0)
#         ).scale(0.35).arrange(RIGHT, buff=SMALL_BUFF, aligned_edge=DOWN).next_to(c1.lines[2])

#         txt2 = Text('a 和 b 是否不同').scale(0.35).next_to(c1.lines[3])
#         txt3 = Text('a 大于或等于 b').scale(0.35).next_to(c2.lines[0])
#         txt4 = Text('a 小于或等于 b').scale(0.35).next_to(c2.lines[1])

#         txts = Group(txt1, txt2, txt3, txt4)
        
#         g = Group(planes, txts).arrange(RIGHT, coor_mask=(1, 0, 0), buff=SMALL_BUFF).shift(RIGHT)

#         self.wait()
#         self.play(FadeIn(c1, scale=1.2))
#         self.wait()
#         self.play(Write(txt1))
#         self.wait()
#         self.play(Write(txt2))
#         self.wait()
#         self.play(FadeIn(c2, scale=1.2))
#         self.wait()
#         self.play(Write(txt3))
#         self.wait()
#         self.play(Write(txt4))
#         self.wait(2)

# class _5(Scene):
#     def construct(self) -> None:
#         table = ImageMobject('assets/gm/Cond.png').set_height(2.5).shift(UP * 0.6)

#         self.add(table)
#         self.wait(2)
            
#         plane = Rectangle(7, 4.5, **CodeBackground.CONFIG)

#         txt1 = Text('x > 500', font='Source Code Pro').scale(0.4).next_to(plane, UP, SMALL_BUFF)
#         txt2 = Text('y > 400', font='Source Code Pro').scale(0.4).next_to(plane, UP, SMALL_BUFF)
#         txt3 = Text('x > 500 && y > 400', font='Source Code Pro').scale(0.4).next_to(plane, UP, SMALL_BUFF)
#         txt4 = Text('x > 500 || y > 400', font='Source Code Pro').scale(0.4).next_to(plane, UP, SMALL_BUFF)
#         for txt in (txt1, txt2, txt3, txt4):
#             se = StrSearcher(txt.text).s('x', C_BUILTIN_VAR).s('500', C_DIGIT).s('y', C_BUILTIN_VAR).s('400', C_DIGIT)
#             for rg, col in se.results:
#                 rg = to_manimtext_idx(txt.text, *rg)
#                 txt[rg[0]:rg[1]].set_color(col)

#         rect_config = {
#             'fill_color': BLUE,
#             'fill_opacity': 0.5,
#             'stroke_width': 0
#         }

#         rect1 = Rectangle(7, 4.5, **rect_config).stretch(0.6, 0, about_edge=RIGHT)
#         rect2 = Rectangle(7, 4.5, **rect_config).stretch(0.5, 1, about_edge=DOWN)
#         rect3 = boolean_ops.Intersection(rect1, rect2, **rect_config)
#         rect4 = boolean_ops.Union(rect1, rect2, **rect_config)

#         self.play(FadeOut(table), FadeIn(plane, scale=1.2))
#         self.wait()
#         self.play(Write(txt1), FadeIn(rect1))
#         self.wait()
#         self.play(*[FadeOut(m, run_time=0.2) for m in (txt1, rect1)], Write(txt2), FadeIn(rect2))
#         self.wait()
#         self.play(*[FadeOut(m, run_time=0.2) for m in (txt2, rect2)], Write(txt3), FadeIn(rect3))
#         self.wait()
#         self.play(*[FadeOut(m, run_time=0.2) for m in (txt3, rect3)], Write(txt4), FadeIn(rect4))
#         self.wait(2)

# class _6(Scene):
#     def construct(self) -> None:
#         txt1 = Text('40 < a < 50', font='Source Code Pro').scale(0.5)
#         txt2 = Text('40 < a && a < 50', font='Source Code Pro').scale(0.5)
#         arrow = Arrow(ORIGIN, DOWN, color=GREY)

#         for txt in (txt1, txt2):
#             se = StrSearcher(txt.text).s('40', C_DIGIT).all('a', C_VAR).s('50', C_DIGIT)
#             for rg, col in se.results:
#                 rg = to_manimtext_idx(txt.text, *rg)
#                 txt[rg[0]:rg[1]].set_color(col)

#         g = Group(txt1, arrow, txt2).arrange(DOWN)

#         cross = VCross().scale(0.6).next_to(txt1)
#         tick = Tick().scale(0.6).next_to(txt2)

#         self.wait()
#         self.play(Write(txt1))
#         self.wait()
#         self.play(FadeIn(cross, scale=1.2))
#         self.wait()
#         self.play(Write(txt2), FadeIn(arrow))
#         self.wait()
#         self.play(FadeIn(tick, scale=1.2))
#         self.wait(2)

# class _7(Scene):
#     def construct(self) -> None:
#         c = CodePlane(
#             '''if ((条件1 && 条件2) || (条件3 && 条件4)) {
# ····// 在 条件1和条件2同时成立 或者 条件3和条件4同时成立时
# ····// 执行大括号内的语句
# }
# ·
# if (条件6 && 条件7 || 条件8) {
# ····// 不建议在 && 和 || 混用的情况下抛弃括号，不然难以弄清运算顺序
# }''', 
#             lines_kwargs={ 't2f': { '条件': 'Noto Sans S Chinese Medium' } }
#         )
#         se = StrSearcher(c.lines.text).all('if', C_KEYWORD)
#         for i in range(1, 9):
#             se.s(f'条件{i}', C_VAR)
#         for rg, col in se.results:
#             c.lines.set_code_color(*rg, col)
#         for line in c.lines[1:3]:
#             line[4:].set_color(C_COMMENT)
#         c.lines[6][4:].set_color(C_COMMENT)

#         self.add(c)
#         self.wait(2)

# class _8(Scene):
#     def construct(self) -> None:
#         c = CodePlane(
#             '''flag1 = x > 500 && y > 500;
# flag2 = x < 200 && y < 200;
# if (flag1 || flag2) {
# ····x = 350;
# ····y = 350;
# }
# ''')
#         se = StrSearcher(c.lines.text).all('flag1', C_VAR).all('flag2', C_VAR)\
#             .all('500', C_DIGIT).all('200', C_DIGIT).all('350', C_DIGIT)\
#             .all('x', C_BUILTIN_VAR).all('y', C_BUILTIN_VAR).s('if', C_KEYWORD)
#         for rg, col in se.results:
#             c.lines.set_code_color(*rg, col)

#         self.add(c)
#         self.wait(2)

# class _9(Scene):
#     def construct(self) -> None:
#         c1 = CodePlane(
#             '''if (条件1) {
# ····代码块A;    // 成立的时候执行
# } else {
# ····代码块B;    // 否则执行
# }''', 
#             lines_kwargs={ 't2f': { '条件': 'Noto Sans S Chinese Medium' } }
#         )
#         c2 = CodePlane(
#             '''if (条件1) {
# ····A;    // 如果 条件1 成立，那么执行 A
# } else if (条件2) {
# ····B;    // 否则如果 条件2 成立，那么执行 B
# } else if (条件3) {
# ····C;    // 否则如果 条件3 成立，那么执行 C
# } else {
# ····D;    // 否则执行 D
# }''',
#             lines_kwargs={ 't2f': { '条件': 'Noto Sans S Chinese Medium' } }
#         )
#         for c in (c1, c2):
#             se = StrSearcher(c.lines.text).all('if', C_KEYWORD).all('else', C_KEYWORD)
#             for i in range(1, 4):
#                 se.s(f'条件{i}', C_VAR)
#             for rg, col in se.results:
#                 c.lines.set_code_color(*rg, col)
#         for i in (1, 3):
#             c1.lines[i][9:].set_color(C_COMMENT)
#         for i in (1, 3, 5, 7):
#             c2.lines[i][6:].set_color(C_COMMENT)

#         g = Group(c1, c2).arrange()
#         self.wait()
#         self.play(FadeIn(c1, UP))
#         self.wait()
#         self.play(FadeIn(c2, UP))
#         self.wait(2)


