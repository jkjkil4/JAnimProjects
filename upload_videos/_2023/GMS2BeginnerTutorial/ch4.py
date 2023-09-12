from janim import *
from upload_videos._2023.GMS2BeginnerTutorial.header import *
from utils.shape import *

class Intro(IntroTemplate_Light):
    str2 = '第4节 完善 Object 行为'

class Indicator(IndicatorTemplate):
    verts = [
        [-0.31, 0.36, 0],
        [2.13, 0.04, 0],
        [0.70, -1.26, 0],
        [1.87, -1.51, 0],
        [1.78, -0.61, 0],
        [2.74, -0.84, 0],
        [-0.36, -1.16, 0],
        [0.74, -1.39, 0],
        [0.68, -0.99, 0],
        [1.63, -1.24, 0],
        [-0.10, -0.46, 0],
        [0.80, -0.65, 0],
        [1.01, -0.81, 0],
        [1.96, -1.02, 0],
    ]

# class _1(Scene):
#     background_color = '#eeeeee'
#     def construct(self) -> None:
#         spr = ImgItem('assets/gm/sprite.png', height=1).shift(LEFT * 0.4)
        
#         self.wait()
#         self.play(FadeIn(spr, DOWN * 0.3))

#         gml_and_dnd = ImgItem('assets/gm/GML_and_DnD.png')

#         self.wait()
#         self.play(
#             FadeOut(spr, run_time=0.6), 
#             FadeIn(gml_and_dnd, scale=1.2)
#         )

#         txtGML = Text('GML').move_to([-1.28, 0.56, 0.0])
#         txtDnD = Text('DnD').move_to([1.28, 0.56, 0.0])

#         txtDescGML = Text('GameMaker Language', font_size=10).set_stroke(width=0).next_to(txtGML, DOWN, SMALL_BUFF)
#         txtDescDnD = Text('Drag and Drop', font_size=10).set_stroke(width=0).next_to(txtDnD, DOWN, SMALL_BUFF)

#         self.wait()
#         self.play(
#             AnimationGroup(*map(DrawBorderThenFill, (txtGML, txtDnD))),
#             AnimationGroup(*map(FadeIn, (txtDescGML, txtDescDnD)), begin_time=0.4),
#         )

#         self.wait()
#         self.play(NoRelVGroup(txtDnD, txtDescDnD).anim().set_color(GREY))

#         self.wait()
#         self.clear()
#         self.wait()

# class _2(Scene):
#     background_color = '#eeeeee'
#     def construct(self) -> None:
#         background = surcamera().set_stroke(width=0).set_fill('#eeeeee', 0.85)

#         txt_axe = Text(
#             "我们需要知道GM的<ds BLACK PURPLE>坐标系统</ds>", 
#             color = GREY_D,
#             font_size=28,
#             format=Text.Format.RichText
#         )
#         txt_axe.generate_target().to_border(UP, buff=DEFAULT_ITEM_TO_EDGE_BUFF + 0.1)

#         txt_axe_udl = Line(1.8 * LEFT, 1.8 * RIGHT, color = GREY_D)
#         txt_axe_udl.next_to(txt_axe.target(), DOWN, SMALL_BUFF)
#         self.play(FadeIn(background), DrawBorderThenFill(txt_axe))
#         self.wait(0.5)
#         self.play(MoveToTarget(txt_axe), ShowCreation(txt_axe_udl))

#         self.embed()

#         gmnp = GMRoomPlane(4.2, 4.2, GREY_D)
#         self.play(gmnp.animate1(), run_time = 1.5)
#         self.play(*gmnp.animate2Array())
#         self.wait(0.8)

#         gmdot = Dot(color = TEAL).set_stroke(BLACK, 3, 1, True)
#         gmpos = Text("(x, y)", color = GREY_D, t2c = ht2c)\
#             .scale(0.5).next_to(gmdot, UR, 0)
#         always(gmpos.next_to, gmdot, UR, 0)
#         self.play(Write(gmdot), Write(gmpos))
#         self.wait(0.5)

#         gmdot_center = gmdot.get_center()
#         path1 = bezier([gmdot_center, gmdot_center + (LEFT * 0.4 + UP * 0.9) * 1.5, gmdot_center + (LEFT + UP * 0.7) * 1.5])
#         path2 = bezier([gmdot_center + (LEFT + UP * 0.7) * 1.5, gmdot_center + (LEFT * 0.6 + DOWN * 0.2) * 1.5, gmdot_center])
#         pathAnimate1 = MoveAlongPath(gmdot, VMobject().add_subpath([path1(t / 50) for t in range(0, 51)]))
#         pathAnimate2 = MoveAlongPath(gmdot, VMobject().add_subpath([path2(t / 50) for t in range(0, 51)]))
#         self.play(pathAnimate1, run_time = 1.5)
#         self.wait(0.5)
#         self.play(pathAnimate2, run_time = 1.5)

#         gmspr = ImageMobject("assets/gm/sprite.png", height = 1)
#         f_always(gmspr.move_to, lambda: gmdot.get_center() + [gmspr.get_width() / 2, -gmspr.get_height() / 2, 0])
#         self.remove(gmdot)
#         self.add(gmspr, gmdot)
#         self.play(FadeIn(gmspr))
#         self.play(pathAnimate1, run_time = 1.5)
#         self.wait(0.5)
#         self.play(pathAnimate2, run_time = 1.5)
#         self.wait(0.5)

#         self.play(FadeOut(gmspr), run_time = 0.5)
#         self.play(FadeOut(Group(txtAxe, axeUnderline, gmnp, gmdot, gmpos)), FadeOut(background))

# class _3(Scene):
#     def construct(self) -> None:
#         class _Line(Line):
#             factor = 0
#             def fade(self):
#                 self.factor = max(0, self.factor - 0.05)
#                 self.set_color(interpolate_color(BLACK, ORANGE, self.factor))
        
#         class _Text(Text):
#             def __init__(self):
#                 super().__init__('x += 4')
#                 self.set_fill(RED_D, 1).set_stroke(width=0).scale(0.35)

#         class TimeLabel(Text):
#             def __init__(self, txt):
#                 super().__init__(txt)
#                 self.set_color(BLUE).set_stroke(BLACK, 4, 1, True).scale(0.4)

#         bg = surcamera().set_stroke(width=0).set_fill('#eeeeee', 0.85)

#         clock_lines = VGroup()
#         for i in range(60):
#             vet = RIGHT * np.sin(TAU * i / 60) + UP * np.cos(TAU * i / 60)
#             clock_lines.add(_Line(vet * 0.95, vet).set_color(BLACK))

#         clock = VGroup(
#             Circle().set_fill(WHITE, 1).set_stroke(BLACK, 4, 1, False),
#             clock_lines,
#             Arrow(ORIGIN, UP * 0.9, buff=0).set_color(BLACK),
#             VGroup(TimeLabel('0.0 s'), TimeLabel('0 次')).arrange(DOWN, buff=SMALL_BUFF)
#         ).scale(1.4)

#         self.play(FadeIn(bg), FadeIn(clock, DOWN * 0.5))

#         vgtxt = VGroup()
#         self.add(vgtxt)

#         t = 0
#         def loop():
#             nonlocal t
#             maxi = 60 * 1
#             for i in range(maxi + 1):
#                 if i / 60 > t:
#                     yield

#                 for j in range(60):
#                     clock_lines[j].fade()
#                 for txt in vgtxt:
#                     txt.set_opacity(txt.get_opacity() - 0.25)
#                 if len(vgtxt) and vgtxt[0].get_opacity() < 0:
#                     vgtxt.remove(vgtxt[0])
                
#                 vet = RIGHT * np.sin(TAU * i / 60) + UP * np.cos(TAU * i / 60)
#                 clock_lines[i % 60].factor = 1
#                 clock[3].become(VGroup(TimeLabel('%.2f s' % (i / 60)), TimeLabel(f'{i} 次')).arrange(DOWN, buff=SMALL_BUFF).scale(1.4))

#                 txt = _Text().move_to(vet * 1.8).rotate(PI / 2 - TAU * i / 60)
#                 vgtxt.add(txt)

#                 if i == maxi:
#                     # self.remove(vgtxt)
#                     break

#                 clock[2].rotate(-TAU / 60, about_point=ORIGIN)
#                 # self.wait(1 / 60)
        
#         iter = loop()
        
#         # for i in range(30):
#         #     for t in vgtxt:
#         #         t.set_opacity(t.get_opacity() - 0.5)
#         #     if len(vgtxt) != 0 and vgtxt[0].get_opacity() < 0:
#         #         vgtxt.remove(vgtxt[0])
#         #     self.wait(1 / 60)
        
#         flag = False
#         def clock_updater(m, dt):
#             nonlocal flag, t
#             t += dt
#             try:
#                 next(iter)
#             except StopIteration:
#                 flag = True
#         clock.add_updater(clock_updater)

#         while not flag:
#             self.play(Animation(clock), Animation(vgtxt), run_time=1)
        
#         self.play(FadeOut(vgtxt), run_time=0.3)
#         self.wait()

