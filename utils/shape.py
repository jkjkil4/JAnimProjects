from janim import *

def surcamera(buff=0, **kwargs) -> Rectangle:
    return Rectangle(FRAME_WIDTH + 2 * buff, FRAME_HEIGHT + 2 * buff, **kwargs)

def simple_sum(m1: VItem, m2: VItem, **kwargs) -> VItem:
    return VItem(**kwargs)\
        .append_points(m1.get_points())\
        .append_points(m2.get_points())

def simple_sub(m1: VItem, m2: VItem, **kwargs) -> VItem:
    return VItem(**kwargs)\
        .append_points(m1.get_points())\
        .append_points(m2.get_points()[::-1])
