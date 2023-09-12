from typing import Optional, Tuple

from janim import *
from janim.utils.dict_ops import local_kwargs, merge_dicts_recursively

class VCodeLines(Text):
    def __init__(
        self,
        *args,
        color: JAnimColor = GREY_B,
        font: str | Iterable[str] = ['Consolas', 'Noto Sans S Chinese Medium'],
        font_size: float = 16,
        format: Text.Format = Text.Format.RichText,
        **kwargs
    ) -> None:
        super().__init__(*args, **local_kwargs(), **kwargs)

class CodeLines(VCodeLines, PixelText):
    pass

class CodeBackground(Rectangle):
    def __init__(
        self,
        *args,
        fill_color: JAnimColor = BLACK,
        fill_opacity: float = 1.0,
        stroke_width: float = 0.01,
        color: JAnimColor = GREY_A,
        **kwargs
    ) -> None:
        super().__init__(*args, **local_kwargs(), **kwargs)

class CodeSurroundingBackground(CodeBackground, SurroundingRectangle):
    def __init__(self, *args, buff: float = 0.2, **kwargs) -> None:
        super().__init__(*args, buff=buff, **kwargs)

class CodeHeader(Rectangle):
    def __init__(
        self,
        fill_opacity: float = 1.0,
        stroke_width: float = 0.01,
        color: JAnimColor = GREY_A,
        **kwargs
    ) -> None:
        super().__init__(**local_kwargs(), **kwargs)

class CodePlane(Group):
    def __init__(self, text: str, txt_kwargs = {}, background_kwargs = {}) -> None:
        self.txt = CodeLines(text, **txt_kwargs)
        self.background = CodeSurroundingBackground(self.txt, **background_kwargs)
        super().__init__(self.background, self.txt)

# class CodeView(VGroup):
#     def __init__(self, title, texts, base_color=GREY_B, lines_kwargs={}, title_color=WHITE, header_color=GREY_D) -> None:
#         self.lines = CodeLines(texts, base_color, lines_kwargs={})
#         self.background = CodeBackground(self.lines)
#         txt_title = Text(title, color = title_color).scale(0.35)
#         self.header = CodeHeader(self.background.get_width(), txt_title.get_height() + 0.2, fill_color=header_color)
#         self.header.move_to(self.background.get_top() + [0, self.header.get_height() / 2, 0])
#         txt_title.move_to(self.header)
#         self.others = VGroup(self.header, self.background, txt_title)
#         super().__init__(self.others, self.lines)