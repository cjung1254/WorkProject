#important necessary libs
from manimlib.imports import *
import scipy


FORCE_COLOR = BLUE_B
WORK_COLOR = GREEN_B
DISTANCE_COLOR = YELLOW_E
#Work is described as the dot product of force and distance traveled, or FDcostheta.
class DisplayFormula(Scene): 
    def construct(self): 
        tipesOfText = TextMobject("\\text{Work}", "$ = $", "$F$", "$\\cdot$",  "$d$",  "$=$", "$F$", "$d$",  "$\\cos(\\theta)$")
        tipesOfText[0].set_color(GREEN_B)
        tipesOfText[2].set_color(BLUE_B)
        tipesOfText[4].set_color(YELLOW_E)
        tipesOfText[6].set_color(BLUE_B)
        tipesOfText[7].set_color(YELLOW_E)
        self.play(Write(tipesOfText))
        self.wait(3)
        self.play(ApplyMethod(tipesOfText.shift, 2.5*UP))
        self.wait()

        myVec = Vector([3,1])
        myVec2 = Vector([2,3])
        myVec.move_to([0,-1.5,0])
        myVec2.move_to([-.5,-.5,0])
        myVec.set_color(BLUE)
        labelVector = Matrix(["A_x", "A_y"]).scale(.7)
        labelVector.set_color(BLUE)
        labelVector2 = Matrix(["B_x", "B_y"]).scale(.7)
        labelVector.next_to(myVec, RIGHT)
        labelVector2.next_to(myVec2, RIGHT+.1*UP)
        self.play(ShowCreation(myVec), ShowCreation(labelVector))
        self.play(ShowCreation(myVec2), ShowCreation(labelVector2))
        self.wait()


        eq = TexMobject(r"A_x", r"*", r"B_x", r"+", r"A_y", r"*", r"B_y")
        eq[0].set_color(BLUE)
        eq[4].set_color(BLUE)
        eq.move_to([0,-3,0])
        group = VGroup(labelVector, labelVector2)
        self.play(Transform(group, eq))
        self.wait(6)
        self.play(FadeOut(group), FadeOut(eq), FadeOut(myVec), FadeOut(myVec2))
        self.wait(2)

        START = (-4,-.5,0)
        END = (4,-.5,0)
        line=Line(START, END)
        line.set_color(GREY)
        line.set_opacity(.5)
        self.play(ShowCreation(line))
        self.wait(3)
        #horizontal line
        #block
        block = Square().scale(.5)
        self.play(ShowCreation(block))

        Force = Vector([4,0,0])
        Force.set_color(FORCE_COLOR)
        Distance = Vector([2,0,0])
        Distance.set_color(DISTANCE_COLOR)
        label3 = TextMobject("F")
        label3.set_color(FORCE_COLOR)
        label3.next_to(Force, UP)
        label4 = TextMobject("d")
        label4.set_color(DISTANCE_COLOR)
        label4.next_to(Distance, UP)

        self.play(ShowCreation(Force))
        self.play(Write(label3))
        self.wait(2)

        Force2 = VGroup(Force, label3)

        self.play(ApplyMethod(block.shift, 2*RIGHT), ApplyMethod(Force2.shift, 2*RIGHT), ShowCreation(Distance), run_time=2)
       # self.play(ApplyMethod(Force2.shift, 2*RIGHT), run_time=3)
        #self.play(ShowCreation(Distance), run_time=3)
        self.play(Write(label4))
        self.wait(2)

        self.play(FadeOut(block), FadeOut(line), ApplyMethod(Force2.shift, 2*LEFT))

        theta = TexMobject(r"\theta = 0")
        theta.move_to([0,-1,0])
        theta.scale(.6)
        self.play(Write(theta))
        self.wait(2)

        ans = TextMobject("\\text{Work}", "$ = $", "$F$", "$d$",  "$\\cos(0)$","$ = $", "$F$", "$d$")
        ans[0].set_color(GREEN_B)
        ans[2].set_color(BLUE_B)
        ans[3].set_color(YELLOW_E)
        ans[6].set_color(BLUE_B)
        ans[7].set_color(YELLOW_E)
        ans.move_to([0,-2,0])
        self.play(Write(ans))
        self.wait(2)
        self.play(FadeOut(ans), FadeOut(theta), FadeOut(Force2), FadeOut(Distance), FadeOut(label4))
        self.wait()

        START = (-4,-.5,0)
        END = (4,-.5,0)
        line=Line(START, END)
        line.set_color(GREY)
        line.set_opacity(.5)
        block = Square().scale(.5)
        Force = Vector([4,0,0])
        Forcecos = Vector([3.5778, 0, 0])
        Forcecos.set_color(BLUE_A)
        Forcesin = Vector([0, 1.7887, 0])
        Forcesin.set_color(BLUE_A)
        Force.set_color(FORCE_COLOR)
        Distance = Vector([2.4,0,0])
        Distance.set_color(DISTANCE_COLOR)
        label3 = TextMobject("F")
        label3.set_color(FORCE_COLOR)
        label3.next_to(Force, UP)
        #label4 = TextMobject("d")
        #label4.set_color(DISTANCE_COLOR)
        #label4.next_to(Distance, 1.5*DOWN+.5*LEFT)

        line_block = VGroup(line, block, Distance, Forcecos, Forcesin)
        line_block.rotate(-.463647609, about_point=(0,0,0))

        self.play(ShowCreation(line))
        self.wait(1)
        self.play(ShowCreation(block))
        self.play(ShowCreation(Force), ShowCreation(label3))
        self.wait(2)
        #

        Force2 = VGroup(Force, label3)
        arc = Arc(radius = .5, angle = -.463647609)

        self.play(ApplyMethod(block.shift, 2*RIGHT+1*DOWN), ApplyMethod(Force2.shift, 2*RIGHT+1*DOWN), ShowCreation(Distance), run_time=2)
       # self.play(ApplyMethod(Force2.shift, 2*RIGHT), run_time=3)
        #self.play(ShowCreation(Distance), run_time=3)
        #self.play(Write(label4))
        self.wait(2)

        self.play(FadeOut(block), FadeOut(line), ApplyMethod(Force2.shift, UP+2*LEFT))
        self.play(ShowCreation(arc))
        theta = TexMobject(r"\theta")
        theta.next_to(arc, RIGHT)
        theta.scale(.6)
        self.add(theta)
        self.wait()
        self.play(ShowCreation(Forcecos), ShowCreation(Forcesin))
        self.wait(2)
        self.play(FadeOut(Forcesin))
        self.wait()

        bew = TextMobject("\\text{Work}",  "$ =$", "$F\\cos(\\theta)$", "d")
        bew[0].set_color(GREEN_B)
        bew[2].set_color(BLUE_A)
        bew[3].set_color(YELLOW_E)
        bew.next_to(line, 1*DOWN)
        self.play(Write(bew))
        self.wait(2)
        self.play(FadeOut(bew), FadeOut(Forcecos), FadeOut(Force2), FadeOut(Distance), FadeOut(arc), FadeOut(theta))
        self.wait(2)

        self.play(ApplyMethod(tipesOfText.move_to, [0,0,0]))
        #units = TextMobject("""
         #   \\text{Units}
          #  $ = N * m$
       #     """)
        replace1 = TextMobject("\\text{Work}", "$ = $", "$F$", "$\\cdot$",  "$d$")
        replace1[0].set_color(GREEN_B)
        replace1[2].set_color(BLUE_B)
        replace1[4].set_color(YELLOW_E)
        replace = TextMobject("\\text{Units}", " ", "$ = $", " ", "$N$", "$m$")
        replace[0].set_color(GREEN_B)
        replace[4].set_color(BLUE_B)
        replace[5].set_color(YELLOW_E)
        Joules = TextMobject("\\text{Units}", " ", "$ = $", " ", "Joules")
        Joules[0].set_color(GREEN_B)
        Joules[4].set_color(GREEN_B)
        self.play(Transform(tipesOfText, replace1))
        self.wait()
        self.play(Transform(tipesOfText, replace))
        self.wait()
        self.play(Transform(tipesOfText, Joules))
        self.wait(3)

class Example(Scene):
    def construct(self):
        START = (-4,-.5,0)
        END = (4,-.5,0)
        line=Line(START, END)
        line.set_color(GREY)
        line.set_opacity(.5)
        self.play(ShowCreation(line))
        self.wait(3)
        #horizontal line
        #block
        block = Square().scale(.5)
        block.move_to([-2, 0, 0])
        self.play(ShowCreation(block))

        Force = Vector([2,0,0])
        Force.set_color(FORCE_COLOR)
        Force.move_to([-1,0,0])
        Distance = Vector([6,0,0])
        Distance.set_color(DISTANCE_COLOR)
        Distance.move_to([-.05,0,0])
        label3 = TextMobject("F = 30 N")
        label3.set_color(FORCE_COLOR)
        label3.next_to(Force, 4*UP)
        label4 = TextMobject("x = 50 m")
        label4.set_color(DISTANCE_COLOR)
        label4.next_to(Distance, DOWN)

        self.play(ShowCreation(Force))
        Force3=Force.rotate(np.pi/6, about_edge=[-2,0,0])
        self.play(Transform(Force, Force3), run_time=3)
        self.play(Write(label3))
        self.wait(2)

        Force2 = VGroup(Force, label3)

        self.play(ApplyMethod(block.shift, 5*RIGHT), ApplyMethod(Force2.shift, 5*RIGHT), ShowCreation(Distance), run_time=2)
       # self.play(ApplyMethod(Force2.shift, 2*RIGHT), run_time=3)
        #self.play(ShowCreation(Distance), run_time=3)
        self.play(Write(label4))
        self.wait(2)

        self.play(FadeOut(block), FadeOut(line), ApplyMethod(Force2.move_to, [-2,.75,0]))

        arc = Arc(radius = .2, angle = np.pi/3)
        arc.move_to([-2.5,.13,0])
        theta = TexMobject(r"30 ^o").scale(.5)
        theta.next_to(arc, .05*UP+RIGHT)
        self.play(ShowCreation(arc))
        self.play(Write(theta))
        self.wait(2)

        tipesOfText = TexMobject("\\text{Work}", r" = Fd \cos(\theta) = ", r"30 N", r"*", r"50 m", r"*", r"\cos(30^o)")
        tipesOfText[2].set_color(BLUE_B)
        tipesOfText[4].set_color(YELLOW_E)
        tipesOfText.next_to(line, 3*DOWN)
        self.play(Write(tipesOfText))
        self.wait(5)
        Text=TexMobject("\\text{Work = }", r"750 \frac{\sqrt{3}}{2} J")
        Text.next_to(line, 3*DOWN)
        self.play(Transform(tipesOfText, Text))

class Spring(Scene):
    def construct(self):
        Hooke = TextMobject("Hooke's Law")
        Hooke.to_edge(UP)
        text = TexMobject("F", " = ", "-k", "x")
        text[0].set_color(BLUE_B)
        text[3].set_color(YELLOW_E)
        text.next_to(Hooke, DOWN)

        self.play(Write(Hooke))
        self.play(Write(text))
        self.wait(3)

        new = TexMobject("5 N", " = ", "k", "3 m")
        new[0].set_color(BLUE_B)
        new[3].set_color(YELLOW_E)
        new.move_to([0,-1, 0])
        self.play(Write(new))
        self.wait(2)
        k = TexMobject("k = \\frac{5}{3} \\frac{N}{m}")
        work = TexMobject("\\text{Work} ", "=", "\\int_{0}^{10} \\frac{5}{3}x \\: dx")
        ans = TextMobject("83.3 J").set_color(GREEN_B)
        k.move_to([0,-1,0])
        work.next_to(k, DOWN)
        ans.next_to(k, DOWN)
        self.play(Transform(new, k))
        self.play(Write(work))
        self.wait(2)
        self.play(Transform(work, ans))
        self.wait(2)


class Torque(Scene):
    def construct(self):
        START = (0,0,0)
        END = (3,0,0)
        line=Line(START, END)
        label4 = TextMobject("r")
        label4.next_to(line, UP)
        label4.set_color(YELLOW_E)
        line.set_color(GREY)
        Force = Vector([0,1,0])
        Force.set_color(BLUE_B)
        Force.move_to([3,-.5,0])
        theta = Arc(radius = .7, angle = np.pi/6)
        arclength = Arc(radius = 3, angle = np.pi/6)
        label = TexMobject(r"\theta")
        label.next_to(theta)
        torque = TexMobject("\\text{Torque} = \\tau = f \\times r")
        work = TexMobject("\\text{Work}",  "= \\int ", "\\tau ", "d\\theta").scale(.8)
        work[0].set_color(GREEN_B)
        work[2].set_color(BLUE_B)
        work[3].set_color(YELLOW_E)
        dx = TexMobject("dx = r*d\\theta").set_color(YELLOW_E).scale(.8)
        dx.move_to([0,-1,0])
        dforce = TexMobject("\\text{dW}", "=", " F", "*", "dx").scale(.8)
        dforce[0].set_color(GREEN_B)
        dforce[2].set_color(BLUE_B)
        dforce[4].set_color(YELLOW_E)
        dforce.move_to([0,-2,0])
        dwork = TexMobject("\\text{dW}", "= ", "F", "*", "r * d\\theta").scale(.8)
        dwork[0].set_color(GREEN_B)
        dwork[2].set_color(BLUE_B)
        dwork[4].set_color(YELLOW_E)
        dwork.move_to([0,-2,0])
        torque.move_to([0,3.5,0])
        work.move_to([0,2.5,0])
        label2 = TexMobject("d = r\\theta")
        label2.next_to(arclength, RIGHT)
        arclength.set_color(YELLOW_E)
        label2.set_color(YELLOW_E)


        line2 = VGroup(line, label4, Force)
        self.play(ShowCreation(line2))
        self.wait(2)
        self.play(Rotate(line2, np.pi/6, about_point = [0,0,0]), ShowCreation(theta), ShowCreation(label))
        self.wait(3)
        self.play(Write(torque))
        self.wait(2)
        self.play(Write(work))
        self.wait(2)
        self.play(FadeOut(Force))
        line3=Line(START,END)
        line3.set_color(GREY)
        label5 = TextMobject("r")
        label5.set_color(YELLOW_E)
        label5.next_to(line3, DOWN)
        self.play(ShowCreation(line3), ShowCreation(label5))
        self.wait(2)
        self.play(ShowCreation(arclength), ShowCreation(label2))
        self.wait(3)

        self.play(Write(dx))
        self.wait(2)
        self.play(Write(dforce))
        self.wait(2)
        self.play(Transform(dforce, dwork))
        self.wait(2)
        self.play(ApplyMethod(work.move_to, [0,-3,0]))
        self.wait(3)


class Power(Scene):
    def construct(self):
        Power = TexMobject("\\text{Power} = \\frac{\\text{Work}}{\\text{time}}")
        Power.move_to([0, 3, 0])
        Power.set_color(PURPLE_B)
        Units = TexMobject("\\text{Units} = ", "\\frac{\\text{Joules}}{\\text{seconds}}")
        Units.next_to(Power, DOWN)
        Units.scale(.6)
        Watts = TextMobject("Units = Watts")
        Watts.scale(.6)
        Watts.next_to(Power, 1.8*DOWN)
        START = (-4,-.4,0)
        END = (4,-.4,0)
        line=Line(START, END)
        line.set_color(GREY)
        line.set_opacity(.5)

        self.play(Write(Power))
        self.wait()
        self.play(Write(Units))
        self.wait()
        self.play(Transform(Units, Watts))
        self.play(ShowCreation(line))
        self.wait(3)
        #horizontal line
        #block
        block = Square().scale(.4)
        self.play(ShowCreation(block))

        Force = Vector([2,0,0])
        Force.set_color(FORCE_COLOR)
        Distance = Vector([2,0,0])
        Distance.set_color(DISTANCE_COLOR)
        label3 = TextMobject("5x")
        label3.set_color(FORCE_COLOR)
        label3.next_to(Force, UP)
        label4 = TextMobject("10 m")
        label4.set_color(DISTANCE_COLOR)
        label4.next_to(Distance, UP)

        self.play(ShowCreation(Force))
        self.play(Write(label3))
        self.wait(2)

        Force2 = VGroup(Force, label3)

        self.play(ApplyMethod(block.shift, 2*RIGHT), ApplyMethod(Force2.shift, 2*RIGHT), ShowCreation(Distance), run_time=2)
       # self.play(ApplyMethod(Force2.shift, 2*RIGHT), run_time=3)
        #self.play(ShowCreation(Distance), run_time=3)
        self.play(Write(label4))
        self.wait(2)

        self.play(FadeOut(block), FadeOut(line))
        self.wait(2)

        tipesOfText = TextMobject("Work = ", "$\\displaystyle\\int_0^{10}$", "$5x $", " ", "$dx$").set_color(WHITE).scale(1.1)
        tipesOfText[0].set_color(GREEN_B)
        tipesOfText[2].set_color(BLUE_B)
        tipesOfText[4].set_color(YELLOW_E)
        Answer = TextMobject("Work = 250 J").set_color(GREEN_B).scale(1.1)
        tipesOfText.next_to(line, 3*DOWN)
        Answer.next_to(line, 3*DOWN)
        self.add(tipesOfText)
        self.wait(2)
        self.play(Transform(tipesOfText,Answer))
        self.wait(3)
        powerex = TexMobject("\\text{Power} = \\frac{250 J}{30 s}} = 8.3 ", "\\text{ }", "\\text{Watts}")
        powerex.set_color(PURPLE_B)

        self.play(FadeOut(Force2), FadeOut(Distance), FadeOut(label4), FadeOut(Units), FadeOut(tipesOfText), ApplyMethod(Power.move_to, [0,0,0]), Transform(Power, powerex))
        self.wait(2)

class Pressure(Scene):
    def construct(self):
        psi = TextMobject("Work = ", "$\\displaystyle\\int$", "$P $", "$dV$").set_color(WHITE).scale(.8)
        psi[0].set_color(GREEN_B)
        psi[2].set_color(BLUE_B)
        psi[3].set_color(YELLOW_E)
        psi.to_edge(DOWN)
        self.play(Write(psi), run_time = 1)

class AddingMoreText(Scene):
    def construct(self):
        quote2 = TextMobject("Remember: The first principle is that you must not fool yourself")
        quote2.scale(.5)
        quote3 = TextMobject("- and you are the easiest person to fool.")
        quote3.scale(.5)
        quote3.next_to(quote2, DOWN)
        quote2.set_color(WHITE)
        author2=TextMobject("-Richard Feynman")
        author2.set_color(BLUE_B)
        author2.scale(0.5)
        author2.next_to(quote2.get_corner(DOWN+RIGHT),3*DOWN)
 
        self.play(Write(quote2))
        self.play(Write(quote3))
        self.wait(2)
        self.play(Write(author2))

class Title(Scene):
    def construct(self): 
        tipesOfText = TextMobject("Applications/Extensions").scale(1.1)
        self.play(Write(tipesOfText))

class Basketball(Scene):
    def construct(self):
        sball = Circle().scale(.6).set_color(WHITE)
        bball = Circle().scale(.6).set_color(RED_A)

        blabel = TextMobject("0.6 kg").scale(.6)
        slabel = TextMobject("0.4 kg").scale(.6)
        slabel.move_to([-2,2,0])
        blabel.move_to([2,1.5,0])

        G1 = Vector([0, -1, 0]).set_color(BLUE_B)
        G2 = Vector([0,-1,0]).set_color(BLUE_B)
        G2.move_to([2,.8,0])
        G1.move_to([-2,1.2,0])
        text = TextMobject("F = ma = .6 kg * 10 ", "$\\frac{m}{s^2}$")
        text2 = TextMobject("F = ma = .4 kg * 10 ", "$\\frac{m}{s^2}$")
        tipesOfText = TextMobject("Work", "$ = $", "6 N", "*", "1.5 m", "*", "$\\cos(0)$")
        ex1 = TextMobject("Work", "$ = $", "4 N", "*", "2 m", "*", "$\\cos(0)$")

        tipesOfText[0].set_color(GREEN_B)
        tipesOfText[2].set_color(BLUE_B)
        tipesOfText[4].set_color(YELLOW_E)


        ex1[0].set_color(GREEN_B)
        ex1[2].set_color(BLUE_B)
        ex1[4].set_color(YELLOW_E)

        ans = TextMobject("Work", "$ = $", "9 J").set_color(GREEN_B)
        ans2 = TextMobject("Work", "$ = $", "8 J").set_color(GREEN_B)

        text.move_to([0, 0,0])
        text2.move_to([0, 0,0])
        tipesOfText.next_to(text, DOWN)
        ex1.next_to(text2, DOWN)
        ans2.next_to(ex1, DOWN)
        ans.next_to(tipesOfText,DOWN)


        sball.move_to([-2,2,0])
        bball.move_to([2,0,0])

        self.play(ShowCreation(bball))
        self.play(ApplyMethod(bball.move_to, [2,1.5,0]), Write(blabel))
        self.play(ShowCreation(G2))
        self.wait(3)

        self.play(Write(text))
        self.play(Write(tipesOfText))
        self.play(Write(ans))
        self.wait(3)

        self.play(ShowCreation(sball), Write(slabel))
        self.play(ShowCreation(G1))
        self.wait(3)

        self.play(Transform(text, text2))
        self.play(Transform(tipesOfText, ex1))
        self.play(Transform(ans, ans2))
        self.wait(3)

        self.play(FadeOut(bball), FadeOut(G2), FadeOut(blabel))
        self.wait(3)


class Rotation(Scene):
    def construct(self):
        torque = TexMobject("\\text{Torque} = \\tau = f \\times r")
        torque2 = TexMobject("\\tau = (3\\theta^3 + 2)\\times 1").set_color(RED_A)
        torque2.to_edge(LEFT)
        torque3 = TexMobject("\\tau = (3\\theta^3 + 2)\\times 1.5").set_color(PURPLE_A)
        torque3.to_edge(RIGHT)
        torque.to_edge(UP)
        torque2.next_to(torque, DOWN)
        torque3.next_to(torque2, DOWN)

        integral = TexMobject("\\text{Work} = \\int_{0}^{\\frac{\\pi}{6}} (3\\theta^3 + 2)\\times 1.5").set_color(PURPLE_A).scale(.8)
        integral.next_to(torque3, 5*DOWN)
        integral2 = TexMobject("\\text{Work} = \\int_{0}^{\\frac{\\pi}{3}} (3\\theta^3 + 2)\\times 1").set_color(RED_A).scale(.8)
        integral2.next_to(torque2, 4*DOWN)

        ans1 = TexMobject("\\text{Work} = 3 J").set_color(RED_A).scale(.8)
        ans1.next_to(integral2, 5.5*DOWN)
        ans2 = TexMobject("\\text{Work} = 1.66 J").set_color(PURPLE_A).scale(.8)
        ans2.next_to(integral, 5*DOWN)

        small = TextMobject("Small Door").set_color(PURPLE_A)

        self.play(Write(torque))
        self.play(Write(torque2), Write(torque3))
        self.wait(3)

        self.play(Write(integral), Write(integral2))

        self.play(Write(ans1), Write(ans2))
        self.wait(3)

        GRoup = VGroup(torque, torque2, torque3, integral, integral2, ans1, ans2)

        self.play(Transform(GRoup, small))
        self.wait(3)