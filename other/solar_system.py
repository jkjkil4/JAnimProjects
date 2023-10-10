from manimlib import *

planet_datas = [
    ('太阳', YELLOW, 1391900 * 1e-1, 0),
    ('水星', BLUE, 4866, 57950000),
    ('金星', GOLD, 12106, 108110000),
    ('地球', GREEN, 12742, 149570000),
    ('火星', RED, 6760, 227840000),
    ('木星', LIGHT_BROWN, 142984 * 0.5, 778140000),
]

theta_list = [5.628762853112583, 4.206280138025183, 4.9442585084286685, 0.3100574945692615, 1.2451245475500123, 2.2196206936259775]

SIZE_SCALE_FACTOR = 1e-4 * 0.3
RADIUS_SCALE_FACTOR = 1e-7
FONT_SIZE = 60

class SolarSystem(Scene):
    def construct(self) -> None:
        frame = self.camera.frame

        tracks = VGroup(*[
            Circle(radius=radius * RADIUS_SCALE_FACTOR, color=WHITE, stroke_width=2)
            for name, color, size, radius in planet_datas
        ])

        planets = DotCloud(
            [
                radius * RADIUS_SCALE_FACTOR * (RIGHT * np.cos(theta) + UP * np.sin(theta))
                for (name, color, size, radius), theta in zip(planet_datas, theta_list)
            ]
        )
        planets.set_color([
            color
            for name, color, size, radius in planet_datas
        ])
        planets.set_radii([
            size * SIZE_SCALE_FACTOR
            for name, color, size, radius in planet_datas
        ])

        txts = VGroup(*[
            Text(name, font_size=FONT_SIZE)\
                .set_color(color).set_stroke(BLACK, 4, background=True)\
                .next_to(RIGHT * (radius * RADIUS_SCALE_FACTOR + size * SIZE_SCALE_FACTOR))\
                .rotate_about_origin(theta)
            for (name, color, size, radius), theta in zip(planet_datas, theta_list)
        ])

        frame.save_state()

        self.wait(0.5)
        self.play(
            *map(lambda m: FadeIn(m, run_time=1), (tracks, planets, txts)),
            frame.animate.scale(4).increment_phi(60 * DEGREES).increment_theta(30 * DEGREES),
            run_time=2
        )

        c_radius = 4.8 * 1e8 * RADIUS_SCALE_FACTOR

        circle = Circle(radius=c_radius, opacity=0.3)

        circles = VGroup(*[
            Circle().rotate(PI / 2, RIGHT).shift(RIGHT * c_radius).rotate_about_origin(degree)
            for degree in np.arange(0, TAU, TAU / 320)
        ])

        self.play(
            AnimationGroup(
                FadeOut(txts),
                frame.animate.scale(1.5).increment_phi(23 * DEGREES).increment_theta(20 * DEGREES),
                ShowCreation(circle),
                ShowCreation(circles, lag_ratio=0.05),
                lag_ratio=0.5
            )
        )

        self.wait()

        self.play(frame.animate.scale(1.4).increment_phi(-20 * DEGREES))
        self.wait(1.5)
        
            

