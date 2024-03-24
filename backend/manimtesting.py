from manim import *

class TextWrite(Scene):
    def construct(self):
        # Add text
        intro_text = Tex("Transforming a Square into a Circle")
        intro_text.scale(1.5)
        intro_text.to_edge(UP)
        self.play(Write(intro_text))


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)  

        square = Square()  
        square.rotate(PI / 4)
        
        self.wait(1)  
        self.play(Create(square))  
        self.play(Transform(square, circle))  
        self.play(FadeOut(square))  
        
class cheffin(Scene):
    def construct(self):
        TextWrite.construct(self)
        SquareToCircle.construct(self)