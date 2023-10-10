from upload_videos._2023.GMS2BeginnerTutorial.header import *
from utils.codeview import CodeView
from utils.shape import surcamera

import random

class Intro(IntroTemplate):
    str2 = '第7节 事件系统'

class _1(Scene):
    def construct(self) -> None:
        apply_custom_colors()

        self.wait()

        events = Group(*[
            CodeView(title, text, background_kwargs=dict(width=2.5), header_color=DARK_GREEN)
            for title, text in (
                ('Key Down - Left', '<c BUILTIN_VAR>x</c> -= <c DIGIT>4</c>;'),
                ('Key Down - Right', '<c BUILTIN_VAR>x</c> += <c DIGIT>4</c>;'),
                ('Key Down - Up', '<c BUILTIN_VAR>y</c> -= <c DIGIT>4</c>;'),
                ('Key Down - Down', '<c BUILTIN_VAR>y</c> += <c DIGIT>4</c>;'),
            )
        ])

        events[:2].arrange(RIGHT)
        NoRelGroup(
            events[2],
            events[:2],
            events[3]
        ).arrange(DOWN)

        self.play(
            Succession(*[
                FadeIn(event, shift)
                for event, shift in zip(
                    events,
                    (LEFT, RIGHT, UP, DOWN)
                )
            ], buff=-0.5),
        )
        self.wait()

        rect = SurroundingRectangle(events, buff=LARGE_BUFF)
        rect.set_stroke(DARK_GREEN).set_fill(BLACK, 0.75)
        
        txt = Text('事件系统', font_size=48, color=GREEN_E)
        
        self.play(
            DrawBorderThenFill(rect),
            Write(txt, begin_time=1.5)
        )
        self.wait()

        txt_frame = Text('帧', font_size=36, color=BLUE).next_to(txt, DOWN)
        
        self.play(
            FadeIn(txt_frame),
            self.camera.anim().move_to(txt_frame).scale(0.4)
        )
        self.wait()

        sur_rect = SurroundingRectangle(self.camera)
        sur_rect.set_fill(self.background_color, 1)

        self.play(FadeIn(sur_rect))
        self.wait(2)

class _2(Scene):
    def construct(self) -> None:
        self.wait()

        clock = VGroup(
            Circle(radius=2).set_fill(BLUE_E, 0.2).set_stroke(BLUE),
            VGroup(*[
                Line(
                    (RIGHT * np.sin(d) + UP * np.cos(d)) * 2,
                    (RIGHT * np.sin(d) + UP * np.cos(d)) * 1.9,
                    color=BLUE
                )
                for d in np.arange(0, TAU, TAU / 60)
            ])
        )

        arrow = Vector(UP * 2, color=BLUE_B)

        txt = Text('1s\n60帧')
        txt.arrange(DOWN, coor_mask=(1, 0, 0))

        self.add(clock, arrow, txt)
        arrow.set_visible(False)

        self.play(FadeIn(clock, scale=1.2), Write(txt))
        
        self.wait()

        self.play(FadeIn(arrow), run_time=0.3)
        self.play(Rotate(arrow, -TAU, about_point=ORIGIN, run_time=1.5))

        self.wait()

        self.play(self.camera.anim().move_to(clock[-1][1]).shift(UR * 0.2).scale(0.2))
        self.remove(txt)

        self.wait()

        def angle_txt(angle: float) -> VGroup:
            vg = VGroup(
                Text('帧', font_size=8, color=RED),
                Vector(DOWN * 0.08, stroke_width=0.01, color=RED)
            ).arrange(DOWN, buff=0.05)
            
            vg.next_to(UP * 2, UP, 0.05).rotate(-angle, about_point=ORIGIN)

            return vg
        
        arrow.save_state()

        txt_vg = VGroup()
        self.add(txt_vg)
        
        for i in range(1, 61):
            txt_vg.add(angle_txt(i * TAU / 60))
            arrow.rotate(-TAU / 60, about_point=ORIGIN)
            self.wait(0.02)

        self.wait()

        txt_frame = txt_vg[-1][0]

        self.play(
            *map(
                FadeOut,
                (clock, arrow, txt_vg[:-1], txt_vg[-1][-1])
            ),
            txt_frame.anim().set_color(BLUE),
            self.camera.anim().move_to(txt_frame).scale(0.8)
        )

        self.wait()

        ver_line = Line(ORIGIN, DOWN * (self.camera.get_height() * 0.8), stroke_width=0.01)
        ver_line.next_to(txt_frame, buff=0.05)
        events = Text(
            '创建事件（Create）\n'
            '销毁事件（Destroy）\n'
            '计时器事件（Alarm）\n'
            '碰撞事件（Collision）\n'
            '按键事件（Keyboard）\n'
            '鼠标事件（Mouse）\n'
            '步事件（Step）\n'
            '绘制事件（Draw）\n'
            '其它（Other）',
            font_size=4
        ).arrange_in_lines(buff=0.05).next_to(ver_line, buff=0.05)

        self.play(self.camera.anim().align_to(txt_frame, LEFT).shift(LEFT * 0.2))

        self.play(
            ShowCreation(ver_line),
            Succession(
                *map(lambda m: FadeIn(m, LEFT * 0.2, rate_func=rush_from), events), 
                buff=-0.7, 
                begin_time=0.5
            )
        )

        self.wait()

        self.play(self.camera.anim(rate_func=rush_into).next_to(events, buff=0.01))

class _3(Scene):
    def construct(self) -> None:
        apply_custom_colors()

        self.wait()

        events = Group(*[
            Group(
                PixelText(ch),
                PixelText(en, font_size=12, color=GREY)
            ).arrange(DOWN, buff=0.05, aligned_edge=LEFT)
            for ch, en in (
                ('创建事件', 'Create'),
                ('销毁事件', 'Destroy'),
                ('计时器事件', 'Alarm'),
                ('碰撞事件', 'Collision'),
                ('按键事件', 'Keyboard'),
                ('鼠标事件', 'Mouse'),
                ('步事件', 'Step'),
                ('绘制事件', 'Draw'),
                ('其它', 'Other')
            )
        ]).arrange(DOWN, buff=0.075, aligned_edge=LEFT)

        events.next_to(LEFT_SIDE, LEFT, SMALL_BUFF)
        events.set_opacity(0.3)

        self.add(events)

        events.generate_target().next_to(LEFT_SIDE)

        desc = PixelText(
            '    仅在实例被创建时才会执行一次，之后不会再执行。\n'
            '    仅在实例被销毁时才会执行一次。\n'
            '    你可以通过 “<c FUNC>alarm_set</c>(<c DIGIT>编号</c>, <c DIGIT>步数</c>);” '
            '\n或者 “<c BUILTIN_VAR>alarm</c>[<c DIGIT>编号</c>] = <c DIGIT>步数</c>;” 为指定'
            '编号（<c DIGIT>0~11</c>）的这个事件设定一个倒计时，例如 “<c FUNC>alarm_set</c>'
            '(<c DIGIT>0</c>, <c DIGIT>30</c>)” 将会让计时器事件 \n<c DIGIT>Alarm 0</c> 在'
            '半秒后执行（默认 <c DIGIT>1</c> 秒 <c DIGIT>60</c> 步的情况下）。\n'
            '    当实例与其它实例发生碰撞时会执行，当我们讲到碰撞时详细说明。\n'
            '    分为 <c BLUE>按下键（Key Press）</c>、<c BLUE>压住键（Key Down）</c>、<c BLUE>松开键（Key Release）</c>'
            '，我们前面已经用过 压住键事件 来在玩家按着方向键的时候控制角色移动。详细地说，当我们按下'
            '一个按键时，会先执行 按下键事件，接着在接下来的每一步都执行 压住键事件，直到你'
            '松开按键并执行 松开键事件。\n'
            '    与键盘事件同理。\n'
            '    每一帧都会执行一次，分为 <c BLUE>步开始（Begin Step）</c>、<c BLUE>普通步事件（Step）</c>、'
            '<c BLUE>步结束（End Step）</c>，这三者的执行有先后关系。\n'
            '    与步事件一样，是每帧都执行一次的事件，用于自定义绘制，绘制窗口图形的代码只有'
            '写在绘制事件里才有用。其中的各种事件，也都是在满足其条件下才会执行的事件，不再累赘讲述。\n'
            '    包含很多杂项事件。其中的 <c EVENT>用户事件（User Events）</c>由于 2.3 之后可以自由定义 <c KEYWORD>function</c>，'
            '因此已经意义不大。',
            font=['Consolas', 'LXGW WenKai Mono Lite'],
            format=Text.Format.RichText
        ).word_wrap(FRAME_WIDTH - 4 * DEFAULT_ITEM_TO_EDGE_BUFF - events.get_width())
        # print(len(desc[0]))
        desc.next_to(events.target()).next_to(TOP, DOWN, LARGE_BUFF, coor_mask=(0, 1, 0))
        # self.add(desc)

        self.play(MoveToTarget(events))
        self.wait()

        # global desc_part_prev
        desc_part_prev = None

        def idx_anim(item: Item, idx: int, desc_part, run_time=2) -> Item:
            nonlocal desc_part_prev
            # global desc_part_prev
            target = item.generate_target()
            target.set_opacity(0.3)
            target[idx].set_opacity(1)
            if desc_part_prev is None:
                anim = AnimationGroup(
                    MoveToTarget(item), 
                    FadeIn(desc_part, lag_ratio=0.1, rate_func=linear, run_time=run_time)
                )
            else:
                anim = AnimationGroup(
                    MoveToTarget(item),
                    desc_part_prev.anim().set_opacity(0.3),
                    FadeIn(desc_part, lag_ratio=0.1, rate_func=linear, run_time=run_time)
                )
            desc_part_prev = desc_part
            return anim
        
        self.play(idx_anim(events, 0, desc[0]))
        self.wait()
        self.play(idx_anim(events, 1, desc[1]))
        self.wait()
        self.play(idx_anim(events, 2, desc[2:6], 4))
        self.wait()
        self.play(idx_anim(events, 3, desc[6:8]))
        self.wait()
        self.play(desc[:8].anim().shift(UP * 3), run_time=0.5)
        desc[8:].shift(UP * 3)
        self.play(idx_anim(events, 4, desc[8:13], 4))
        self.wait()
        self.play(idx_anim(events, 5, desc[13]))
        self.wait()
        self.play(idx_anim(events, 6, desc[14:16]))
        self.wait()
        self.play(idx_anim(events, 7, desc[16:19], 4))
        self.wait()
        self.play(idx_anim(events, 8, desc[19:21]))
        self.wait(2)

class _3_1(Scene):
    def construct(self) -> None:
        self.wait(0)

        sur = surcamera().set_fill(BLACK, 0.3).set_stroke(width=0)

        finger = SVGItem('assets/finger.svg').stretch(0.002, 0).scale(0.5)
        anchor = Point(DOWN * 0.7 + RIGHT * 0.12)
        finger.add(anchor, is_helper=True)
        finger.rotate(-75 * DEGREES)

        btn = VGroup(
            Rectangle(0.6, 0.2).set_fill(RED, 1),
            Rectangle(1, 0.25).set_fill(GREY_B, 1),
        ).set_stroke(BLACK, 0.02).arrange(DOWN, buff=0)

        txt = Text(
            'Key Press\n'
            'Key Down\n'
            'Key Release',
            font_size=18
        )

        bar = (
            Rectangle(4, 0.35).set_stroke(YELLOW_D)
            * 3
        ).arrange(DOWN, buff=SMALL_BUFF)

        for t, b in zip(txt, bar):
            t.next_to(b, LEFT, SMALL_BUFF)

        finger.next_to(btn, LEFT).shift(UR * 0.4 + RIGHT * 0.15)

        gp = Group(
            Group(finger, btn),
            Group(txt, bar)
        ).arrange(DOWN)
        
        self.play(FadeIn(sur), FadeIn(gp, begin_time=0.5))

        def anim_finger_down(**kwargs) -> AnimationGroup:
            return AnimationGroup(
                finger.anim().rotate(-25 * DEGREES, about_point=anchor.get_pos()),
                btn[0].anim(begin_time=0.22, run_time=0.78).shift(DOWN * 0.15),
                rate_func=rush_into,
                **kwargs
            )
        def anim_finger_up(**kwargs) -> AnimationGroup:
            return AnimationGroup(
                finger.anim().rotate(25 * DEGREES, about_point=anchor.get_pos()),
                btn[0].anim(run_time=0.78).shift(UP * 0.15),
                rate_func=rush_from,
                **kwargs
            )

        plates = VGroup()
        global is_down
        is_down = False

        plate = lambda: Rectangle(0.1, bar[0].get_height())\
            .set_fill(YELLOW_D, [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1]).set_stroke(width=0)

        global plates_move_idx
        plates_move_idx = 0

        def set_is_down(flag: bool) -> None:
            # nonlocal is_down
            global is_down, plates_move_idx
            is_down = flag
            if flag:
                plates.add(plate().move_to(bar[0].get_left()))
                plates.add(plate().move_to(bar[1].get_left()))
                plates_move_idx = -1
            else:
                plates.add(plate().move_to(bar[2].get_left()))

        def plates_updater(_) -> None:
            global plates_move_idx
            if is_down:
                plates_move_idx += 1
                if plates_move_idx > 3:
                    plates_move_idx = 0
                    plates.add(plate().move_to(bar[1].get_left()))
            plates.shift(RIGHT * 0.04)
            
            items = plates.items.copy()
            for item in items:
                if item.get_x() < bar[0].get_x(RIGHT):
                    break
                plates.remove(item)
        plates.add_updater(plates_updater)

        self.add(plates)

        self.play(anim_finger_down(run_time=0.3))
        set_is_down(True)
        self.wait()
        set_is_down(False)
        self.play(anim_finger_up(run_time=0.3))

        self.wait(0.5)
        
        self.play(anim_finger_down(run_time=0.3))
        set_is_down(True)
        self.wait(0.5)
        set_is_down(False)
        self.play(anim_finger_up(run_time=0.3))

        self.wait(1.5)
        
        self.play(anim_finger_down(run_time=0.3))
        set_is_down(True)
        self.wait(1.5)
        set_is_down(False)
        self.play(anim_finger_up(run_time=0.3))

        self.wait(3)

class _4(Scene):
    def construct(self) -> None:
        self.wait()

        events = PixelText(
            '创建事件（Create）\n'
            '步开始事件（Begin Step）\n'
            '计时器事件（Alarm）\n'
            '键盘事件（Key）\n'
            '鼠标事件（Mouse）\n'
            '普通步事件（Step）\n'
            '<fs 0.7>实例进行移动（并非事件，只是注明 GM 在此时会依照实例的一些运动属性进行移动操作）</fs>\n'
            '碰撞事件（Collision）\n'
            '步结束事件（End Step）\n'
            '绘制事件（Draw）\n'
            '销毁事件（Destroy）',
            format=PixelText.Format.RichText
        )
        events[6].mark.scale(0.85, about_point=events[6].get_mark_orig())
        events.arrange_in_lines(buff=0.1).to_center()

        rect = SurroundingRectangle(events[1:-1], buff=0.05).set_stroke(WHITE, 0.01, 0.3).set_fill(WHITE, 0.05)

        single_char_list = list(it.chain(*[line.items for line in events]))
        random.shuffle(single_char_list)

        self.play(FadeIn(NoRelGroup(*single_char_list), lag_ratio=0.02))
        self.add_to_back(rect)
        self.play(ShowCreation(rect))
        self.wait()

        arrow = Arrow(ORIGIN, RIGHT).set_color(YELLOW)
        arrow.next_to(events[0], LEFT, SMALL_BUFF)

        self.play(GrowArrow(arrow))
        self.wait()

        def arrow_indicate_on(idx: int, run_time=0.1) -> None:
            arrow.next_to(events[idx], LEFT)
            self.play(
                arrow.anim().next_to(events[idx], LEFT, SMALL_BUFF),
                run_time=run_time,
                rate_func=rush_from
            )
        
        for _ in range(4):
            for i in range(1, 10):
                arrow_indicate_on(i)
        
        self.wait()

        arrow_indicate_on(10, 0.5)

        self.wait()

        self.play(FadeOut(arrow))
        self.wait()

        self.play(rect.anim().set_color(YELLOW))
        self.wait()

        self.play(events[2:10].anim().set_opacity(0.3))
        self.wait()

        curved_arrow = Arrow(
            events[1].get_left() + LEFT * 0.2, 
            events[2].get_left() + LEFT * 0.2, 
            path_arc=90 * DEGREES,
            buff=0
        ).set_color(YELLOW)

        self.play(GrowArrow(curved_arrow, rate_func=rush_from))
        self.play(
            events[1].anim().set_opacity(0.3), 
            events[2].anim().set_opacity(1), 
            run_time=0.5
        )
        self.wait()

        self.play(
            FadeOut(curved_arrow),
            rect.anim().set_color(WHITE),
            *map(
                lambda m: m.anim().set_opacity(0.3),
                (events[0], events[2], events[-1])
            ),
            *map(
                lambda m: m.anim().set_opacity(1),
                (events[1], events[5], events[8])
            )
        )
        self.wait()

        scr_rect = Rectangle(FRAME_WIDTH, FRAME_HEIGHT)
        scr_rect.set_fill(self.background_color, 1).set_stroke(width=0)

        scr_rect.generate_target()
        scr_rect.shift(LEFT * FRAME_WIDTH)

        self.play(MoveToTarget(scr_rect), run_time=0.6)
        self.wait(2)

class _5(Scene):
    def construct(self) -> None:
        apply_custom_colors()
        self.wait()

        events = Group(*[
            CodeView(title, text, background_kwargs=dict(width=2.5), header_color=DARK_GREEN)
            for title, text in (
                ('Key Down - Left', '<c BUILTIN_VAR>x</c> -= <c DIGIT>4</c>;'),
                ('Key Down - Right', '<c BUILTIN_VAR>x</c> += <c DIGIT>4</c>;'),
                ('Key Down - Up', '<c BUILTIN_VAR>y</c> -= <c DIGIT>4</c>;'),
                ('Key Down - Down', '<c BUILTIN_VAR>y</c> += <c DIGIT>4</c>;'),
            )
        ]).arrange(DOWN).to_border(LEFT, LARGE_BUFF)

        self.play(
            Succession(
                *[
                    FadeIn(event, RIGHT, rate_func=rush_from)
                    for event in events
                ],
                buff=-0.6
            )
        )
        self.wait()

        step = CodeView(
            'Step（普通步事件）',
            '<c KEYWORD>if</c> (<c FUNC>keyboard_check</c>(<c DIGIT>vk_left</c>)) {\n'
            '    <c BUILTIN_VAR>x</c> -= <c DIGIT>4</c>;\n'
            '}\n'
            '<c KEYWORD>if</c> (<c FUNC>keyboard_check</c>(<c DIGIT>vk_right</c>)) {\n'
            '    <c BUILTIN_VAR>x</c> += <c DIGIT>4</c>;\n'
            '}\n'
            '<c KEYWORD>if</c> (<c FUNC>keyboard_check</c>(<c DIGIT>vk_up</c>)) {\n'
            '    <c BUILTIN_VAR>y</c> -= <c DIGIT>4</c>;\n'
            '}\n'
            '<c KEYWORD>if</c> (<c FUNC>keyboard_check</c>(<c DIGIT>vk_down</c>)) {\n'
            '    <c BUILTIN_VAR>y</c> += <c DIGIT>4</c>;\n'
            '}',
            header_color=BLUE_E
        )

        arrow = Arrow(events.get_right(), step.get_left())

        self.play(
            FadeIn(step, begin_time=0.4),
            GrowArrow(arrow)
        )
        self.wait()

        vk_ch_vg = VGroup(*[
            Text(vk_ch).next_to(vk).next_to(step, coor_mask=(1, 0, 0))
            for vk, vk_ch in zip(
                step.plane.txt.select_parts('vk'), 
                ('左键', '右键', '上键', '下键')
            )
        ])

        self.play(
            Succession(
                *[
                    FadeIn(vk_ch)
                    for vk_ch in vk_ch_vg
                ],
                buff=-0.6
            )
        )
        self.wait(2)

class _6(Scene):
    def construct(self) -> None:
        self.wait()

        text = Text(
            '创建事件（Create）\n'
            '步事件（Step）\n'
            '绘制事件（Draw）'
        ).arrange_in_lines(0.1)

        self.play(Write(text))
        self.wait()
