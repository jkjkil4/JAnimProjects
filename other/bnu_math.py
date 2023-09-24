from janim import *

doc = r'''
\documentclass[preview]{standalone}
\usepackage[UTF8]{ctex}

\usepackage[english]{babel}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{dsfont}
\usepackage{setspace}
\usepackage{tipa}
\usepackage{relsize}
\usepackage{textcomp}
\usepackage{mathrsfs}
\usepackage{calligra}
\usepackage{wasysym}
\usepackage{ragged2e}
\usepackage{physics}
\usepackage{xcolor}
\usepackage{microtype}
\usepackage{xeCJK}
\setCJKmainfont{NotoSansSChineseMedium-7.ttf}
\linespread{1}

\begin{document}

$$
\centering
\text{数科} := \{x \ | \ (x\in\text{数科老生}) \lor(x\in\text{数科新生})\}
$$

\end{document}
'''

class _1(Scene):
    def construct(self) -> None:
        tex = TexDoc(doc)

        self.add(tex)

class _2(Scene):
    def construct(self) -> None:
        l = (
            r'\sum_{i=1}^n x_i',
            r'''\begin{bmatrix}
                a_{11} & a_{12} & a_{13} \\
                a_{21} & a_{22} & a_{23} \\
                a_{31} & a_{32} & a_{33}
            \end{bmatrix}''',
            r'''\begin{bmatrix}
                a_{11} & a_{12} & \cdots & a_{1n} \\
                a_{21} & a_{22} & \cdots & a_{2n} \\
                \vdots & \vdots & \ddots & \vdots \\
                a_{m1} & a_{m2} & \cdots & a_{mn} \\
            \end{bmatrix}''',
            r'(\lim_{x\rightarrow a} f(x) = A) := \forall\varepsilon > 0 \ \ \exists\delta > 0 \ \ \forall x \in \mathbb R \ (0 < |x-a| < \delta \Rightarrow |f(x) - A| < \varepsilon) '
        )
        vg = VGroup(*[Tex(v) for v in l]).arrange(DOWN)
        self.add(vg)
