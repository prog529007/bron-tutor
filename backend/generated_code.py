from manim import *

class Solution(Scene):
    def construct(self):
        # Create title
        title = Tex("Fundamental Linear Algebra").scale(1.5)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Create introduction
        intro = Tex("Linear algebra is a branch of mathematics that deals with vector spaces and linear transformations.").scale(0.8)
        self.play(Write(intro))
        self.wait(1)
        
        self.play(FadeOut(title), FadeOut(intro))
        
        # Create definition
        definition = Tex("A vector space is a collection of objects called vectors, which can be added together and multiplied by scalars (numbers).").scale(0.8)
        self.play(Write(definition))
        self.wait(1)

        # Fade out title, intro, and definition
        self.play(FadeOut(definition))

        # Create addition example
        example1 = Tex("Addition: $\\begin{bmatrix}1 \\\\ 2 \\\\ 3 \\\\ 4 \\end{bmatrix} + \\begin{bmatrix}5 \\\\ 6 \\\\ 7 \\\\ 8 \\end{bmatrix} = \\begin{bmatrix}6 \\\\ 8 \\\\ 10 \\\\ 12 \\end{bmatrix}$").shift(UP)
        self.play(Write(example1))
        self.wait(1)

        # Create scalar multiplication example
        example2 = Tex("Scalar Multiplication: $2\\begin{bmatrix}1 \\\\ 2 \\\\ 3 \\\\ 4 \\end{bmatrix} = \\begin{bmatrix}2 \\\\ 4 \\\\ 6 \\\\ 8 \\end{bmatrix}$").shift(DOWN)
        self.play(Write(example2))
        self.wait(1)

        # Fade out addition and scalar multiplication examples
        self.play(FadeOut(example1), FadeOut(example2))

        # Create linear transformation example
        example3 = Tex("Linear Transformation: $T(\\begin{bmatrix}1 \\\\ 2 \\\\ 3 \\\\ 4 \\end{bmatrix}) = \\begin{bmatrix}2 \\\\ 3 \\\\ 4 \\\\ 5 \\end{bmatrix}$").shift(UP)
        self.play(Write(example3))
        self.wait(1)

        # Fade out linear transformation example
        self.play(FadeOut(example3))

        # Create matrix multiplication example
        example4 = Tex("Matrix Multiplication: $\\begin{bmatrix}1 & 2 & 3 \\\\ 4 & 5 & 6 \\end{bmatrix} \\begin{bmatrix}7 \\\\ 8 \\\\ 9 \\end{bmatrix} = \\begin{bmatrix}50 \\\\ 122 \\end{bmatrix}$").shift(DOWN)
        self.play(Write(example4))
        self.wait(1)

        # Fade out matrix multiplication example
        self.play(FadeOut(example4))

        # Create identity and inverse matrices
        identity = Tex("Identity Matrix: $I = \\begin{bmatrix}1 & 0 \\\\ 0 & 1 \\end{bmatrix}$").shift(UP)
        inverse = Tex("Inverse Matrix: $\\begin{bmatrix}a & b \\\\ c & d \\end{bmatrix}^{-1} = \\frac{1}{ad-bc}\\begin{bmatrix}d & -b \\\\ -c & a \\end{bmatrix}$").shift(DOWN)
        self.play(Write(identity), Write(inverse))
        self.wait(1)

        # Fade out identity and inverse matrices
        self.play(FadeOut(identity), FadeOut(inverse))

        # Create determinant and eigenvalues
        determinant = Tex("Determinant: $\\det(A) = ad-bc$").shift(UP)
        eigenvalues = Tex("Eigenvalues: $Av = \\lambda v$").shift(DOWN)
        self.play(Write(determinant), Write(eigenvalues))
        self.wait(1)

        # Fade out determinant and eigenvalues
        self.play(FadeOut(determinant), FadeOut(eigenvalues))

        # Create conclusion
        conclusion = Tex("Linear algebra is a fundamental tool in many areas of mathematics and has numerous applications in physics, engineering, and computer science.").scale(0.8)
        self.play(Write(conclusion))
        self.wait(1)

        # Fade out conclusion
        self.play(FadeOut(conclusion))
        self.wait(1)
