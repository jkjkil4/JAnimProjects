from upload_videos._2023.GMS2BeginnerTutorial.header import *

class Intro(IntroTemplate_Light):
    str2 = '第1节 概况介绍'

class _1(Scene):
    background_color = '#eeeeee'
    def construct(self) -> None:
        txt1 = Text("GameMaker", font_size=32)
        txt2 = Text("游戏引擎", font_size=32)
        vg = NoRelVGroup(txt1, txt2).set_color(GREY_D).arrange(DOWN)

        self.play(Succession(*map(Write, vg), buff=-0.3))
        self.wait()
        self.play(NoRelVGroup(txt1[0][1:4], txt1[0][5:]).anim().set_color(GREY_B))
        self.wait()
        self.play(*map(Uncreate, vg))

class _2(Scene):
    background_color = '#eeeeee'
    def construct(self) -> None:
        ico = [
            ImgItem(f'assets/gm/{name}.png', height=1)
            for name in ['GM8', 'GMS1', 'GMS2']
        ]
        title = [
            'GameMaker 8',
            'GameMaker Studio',
            'GameMaker Studio 2'
        ]
        desc = [
            '上一代 GM，由于 GM8 的破解版盛行，因此也是有一定用户群体的版本',
            'GMS，新代 GM 的旧版',
            'GMS2，目前持续维护的 GM 版本，和 GM8 一样有很多人用'
        ]

        ver = Group(*[
            Group(
                Group(
                    a, 
                    Text(b, font_size=32, color=GREY_D)
                ).arrange(RIGHT),
                Text(c, color='#666666')
            ).arrange(DOWN, aligned_edge=LEFT)
            for a, b, c in zip(ico, title, desc)
        ]).arrange(DOWN, aligned_edge=LEFT, buff=MED_LARGE_BUFF).to_border(UL)

        for one in ver:
            self.wait()
            self.play(
                Succession(
                    FadeIn(one[0], scale=0.8),
                    Write(one[1], run_time=1),
                    buff=-0.8
                )
            )

        self.wait()
        self.play(
            FadeOut(ver[1], run_time=0.5),
            NoRelGroup(ver[0], ver[2]).anim().arrange(DOWN, aligned_edge=LEFT, buff=MED_LARGE_BUFF)
        )
        self.wait()

        gms2 = ver[2][0]
        self.play(
            FadeOut(NoRelGroup(ver[0], ver[2][1]), run_time=0.5),
            gms2.anim().scale(0.9).move_to(ORIGIN)
        )
        self.wait(2)

        txtMDZ = Text('买断制', color=GREY)
        txtDYZ = Text('订阅制', color=GREY)
        txt_MDZ_DYZ = VGroup(txtMDZ, txtDYZ).arrange(buff=LARGE_BUFF).next_to(gms2, DOWN)
        arrow = Arrow(txtMDZ.get_right(), txtDYZ.get_left(), color=GREY)

        self.play(Write(txtMDZ))
        self.wait()
        self.play(Write(txtDYZ), FadeIn(arrow))
        self.wait()

        txtMFB = Text('免费版', font_size=16, color='#999999')
        txtMFB.next_to(txtDYZ, DOWN, SMALL_BUFF, RIGHT)

        self.play(FadeIn(txtMFB, scale=1.2))
        self.wait(2)

class _3(Scene):
    background_color = '#eeeeee'
    def construct(self) -> None:
        txt23 = Text('2.3+', font_size=48).set_color(GREY_D)

        txt1 = Text('程序', font_size=36)
        txt2 = Text('美术', font_size=36)
        txt3 = Text('音乐', font_size=36)
        vg = VGroup(txt1, txt2, txt3)
        vg.set_color(GREY_D).arrange(buff=MED_LARGE_BUFF)
        
        self.add(txt23)
        self.wait()
        self.play(FadeOut(txt23), FadeIn(vg), run_time=0.7)

        line1 = Line(txt2.get_left(), txt2.get_right(), buff=0)
        line2 = Line(txt3.get_left(), txt3.get_right(), buff=0)
        vg2 = VGroup(line1, line2)
        vg2.set_height(0.05, True).set_stroke(RED, 0.03)
        for line in vg2:
            line.generate_target()
            line.scale(0, about_edge=LEFT)

        self.wait()
        self.play(
            Succession(
                AnimationGroup(txt2.anim().set_color(GREY_B), MoveToTarget(line1)),
                AnimationGroup(txt3.anim().set_color(GREY_B), MoveToTarget(line2)),
                buff=-0.25
            )
        )
        self.wait()
