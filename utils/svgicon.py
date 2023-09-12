class Gear(Difference):
    def __init__(self, diam1=0.4, diam2=0.7, diam3=1, gear_width=0.2, **kwargs):
        line = Rectangle(diam3, gear_width)
        super().__init__(
            boolean_ops.Union(
                *[
                    line.copy().rotate(PI / 4 * i) 
                    for i in range(4)
                ],
                Circle(radius=diam2 / 2)
            ),
            Circle(radius=diam1 / 2),
            **kwargs
        )