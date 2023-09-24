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
        *args,
        fill_opacity: float = 1.0,
        stroke_width: float = 0.01,
        color: JAnimColor = GREY_A,
        **kwargs
    ) -> None:
        super().__init__(*args, **local_kwargs(), **kwargs)

class CodePlane(Group):
    def __init__(self, text: str, txt_kwargs = {}, background_kwargs = {}) -> None:
        self.txt = VCodeLines(text, **txt_kwargs)
        self.background = CodeSurroundingBackground(self.txt, **background_kwargs)
        super().__init__(self.background, self.txt)

class CodeView(Group):
    def __init__(
        self,
        title: str,
        text: str,
        *,
        header_color: JAnimColor = GREY_D,
        title_color: JAnimColor = WHITE,
        txt_color: JAnimColor = GREY_B,
        title_kwargs: dict = {},
        txt_kwargs: dict = {},
        background_kwargs: dict = {},
    ) -> None:
        title_kwargs['color'] = title_color
        txt_kwargs['color'] = txt_color
        self.plane = CodePlane(text, txt_kwargs, background_kwargs)

        txt_title = Text(title, font_size=17, **title_kwargs)
        header_bg = CodeHeader(
            self.plane.background.get_width(), 
            txt_title.get_height() + 0.2,
            fill_color=header_color
        )
        self.header = VGroup(
            header_bg,
            txt_title
        )
        super().__init__(self.plane, self.header)
        self.arrange(UP, buff=0)

