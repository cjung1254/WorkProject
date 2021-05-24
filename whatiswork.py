from manimlib.imports import *


class WhatisWork(Scene):
#Adding text on the screen
	def construct(self):
		my_first_text=TextMobject("What is work?")
		second_line=TextMobject("Work is what happens when a ", "force", " is applied over distance.")
		third_line=TextMobject("Work is the transfer of ", "energy", " from one object to another.")
		third_line.next_to(my_first_text,DOWN)
		circle = Circle(color = WHITE, opacity = .2, fill_opacity = 0).scale(.3)
		tipesOfText = TexMobject("F = ma", " =  m",r"\frac{dv}{dt}")
		#third_line.set_color_by_tex("energy", YELLOW)
		square1 = Square().scale(.5)
		gravity = Vector([0,-1,0])
		gravity.set_color(BLUE_B)
		normal = Vector([0,1,0])
		gravity.move_to([0, -1,0])
		normal.set_color(BLUE_C)
		normal.move_to([0, -.1,0])
		START = [0,-.5,0]
		END = [2,-.5,0]
		line = Line(START,END)
		line.set_color(GREY)
		line.move_to([0, -.5,0])
		Newtext = TexMobject(r"F_{12}", " =  ",r"F_{21}")
		Newtext[0].set_color(BLUE_B)
		Newtext[2].set_color(BLUE_C)
		Newtext.move_to([0, -2,0])

		self.play(Write(my_first_text))
		self.wait(3)
		self.play(ReplacementTransform(my_first_text,second_line))
		self.wait(3)
		self.play(ApplyMethod(second_line.shift, 0.5*UP))
		self.play(Write(third_line))

		self.wait(4)

		self.play(Write(second_line[1].set_color(BLUE)))
		self.play(Write(third_line[1].set_color(YELLOW)))
		#self.play(Transform(second_line,third_line))
		#insert potential circle transition
		self.wait(3)
		group = VGroup(second_line, third_line).arrange(DOWN)
		self.play(ReplacementTransform(group, circle))
		#elf.play(ShowCreation(circle))
		self.play(Uncreate(circle))
		self.wait(3)
		self.play(Write(tipesOfText))
		self.wait(3)
		self.play(ApplyMethod(tipesOfText.shift, 2*UP))

		self.play(ShowCreation(line))
		self.play(FadeIn(square1))
		self.play(ShowCreation(gravity))
		self.play(ShowCreation(normal))
		self.wait(2)
		self.play(Write(Newtext))
		self.wait(2)

class Units(Scene):
	def construct(self):
		defn = TexMobject("F", " = ", "m", "a")
		defn[0].set_color(BLUE_B)
		defn[2].set_color(GREEN_D)
		defn[3].set_color(YELLOW_E)
		units = TextMobject("F", " = ", "kg", r"*", "$\\frac{m}{s^2}$", "= Newtons (N)")
		units[0].set_color(BLUE_B)
		units[2].set_color(GREEN_D)
		units[4].set_color(YELLOW_E)
		self.play(Write(defn))
		self.wait(3)
		self.play(Transform(defn, units))
		self.wait(3)


class ForceEx(Scene):
	def construct(self):
		particle1 = Circle().scale(.5)
		particle2 = Circle().scale(.5)
		particle1.set_color(WHITE)
		particle2.set_color(WHITE)
		particle1.move_to([-3,0,0])
		particle2.move_to([3,0,0])
		text1 = TexMobject(r"m_1")
		text2 = TexMobject(r"m_2")
		text1.move_to([-3,0,0])
		text2.move_to([3,0,0])
		text3 =TexMobject(r"q_1")
		text4 = TexMobject(r"q_2")
		text3.move_to([-3,0,0])
		text4.move_to([3,0,0])
		F1 = Vector([-1,0,0])
		F1.set_color(BLUE_B)
		F2 = Vector([1,0,0])
		F1.move_to([2,0,0])
		F2.move_to([-2,0,0])
		F2.set_color(BLUE_B)
		label1 = TexMobject(r"F_{12}")
		label1.next_to(F1, .6*UP)
		label1.scale(.7)
		label1.set_color(BLUE_B)
		label2 = TexMobject(r"F_{21}")
		label2.next_to(F2, .6*UP)
		label2.scale(.7)
		label2.set_color(BLUE_B)

		self.play(ShowCreation(particle1), ShowCreation(particle2), Write(text1), Write(text2))
		self.wait(2)
		self.play(ShowCreation(F1), ShowCreation(F2), Write(label1), Write(label2))
		self.wait(2)

		self.play(ReplacementTransform(text1, text3), ReplacementTransform(text2, text4))
		self.wait(2)
		block = Square().scale(.5)

		Force = Vector([2,0,0])
		Force.set_color(BLUE_B)
		label3 = TextMobject("F")
		label3.set_color(BLUE_B)
		label3.next_to(Force, UP)

		Group1 = VGroup(particle1, particle2, text3, text4, F1, F2, label1, label2)
		self.play(FadeOut(Group1))
		self.play(ShowCreation(block))
		self.play(ShowCreation(Force))
		self.play(Write(label3))
		self.wait(2)

		Force2 = VGroup(Force, label3)

		self.play(ApplyMethod(block.shift, 2*RIGHT), ApplyMethod(Force2.shift, 2*RIGHT), run_time=2)
       
class energy(Scene):
	def construct(self):
		energy=TextMobject("energy")
		energy.set_color(GREEN_E)
		energydefn = TextMobject("the ability to do work")
		energy2 = TextMobject("property of matter")
		circle = Circle().scale(.5).set_color(WHITE)
		circle.to_edge(LEFT)

		energy.move_to([0,1,0])

		self.play(Write(energy))
		self.play(Write(energydefn))
		self.wait(6)
		self.play(Transform(energydefn, energy2))
		self.wait(3)

		self.play(FadeOut(energy), FadeOut(energydefn))

		self.play(ApplyMethod(circle.move_to, [8,0,0]))
		self.wait()

		circle2 = Circle().scale(.5).set_color(WHITE)
		self.play(ShowCreation(circle2))
		self.play(ApplyMethod(circle2.move_to, [0,3.5,0]))


		

class Formulas(Scene):
	def construct(self):
		tipesOfText = TextMobject("\\text{Work}", "$ = $", "$F$", "$\\cdot$",  "$d$",  "$=$", "$F$", "$d$",  "$\\cos(\\theta)$")
		tipesOfText[0].set_color(GREEN_B)
		tipesOfText[2].set_color(BLUE_B)
		tipesOfText[4].set_color(YELLOW_E)
		tipesOfText[6].set_color(BLUE_B)
		tipesOfText[7].set_color(YELLOW_E)
		self.play(Write(tipesOfText))
		self.wait(2)
		self.play(ApplyMethod(tipesOfText.shift, 2*UP))
		self.wait()

		tex = TextMobject("Work = ", "$\\displaystyle\\int $", "$F(x)$", "$dx$").set_color(WHITE)
		tex[0].set_color(GREEN_B)
		tex[2].set_color(BLUE_B)
		tex[3].set_color(YELLOW_E)
		self.play(Write(tex))
		self.wait(2)
		self.play(ApplyMethod(tex.shift, 1*UP))
		self.wait()

		work = TexMobject("\\text{Work}",  "= \\int ", "\\tau ", "d\\theta").scale(.8)
		work[0].set_color(GREEN_B)
		work[2].set_color(BLUE_B)
		work[3].set_color(YELLOW_E)

		self.play(Write(work), run_time = 1)
		self.wait(2)


		Power = TexMobject("\\text{Power} = \\frac{\\text{Work}}{\\text{time}}").scale(.8)
		Power[0].set_color(PURPLE_B)
		#work[2].set_color(BLUE_B)
		#work[4].set_color(YELLOW_E)
		Power.move_to([0,-1,0])

		self.play(Write(Power), run_time = 1)
		self.wait(2)


		psi = TextMobject("Work = ", "$\\displaystyle\\int$", "$P $", "$dV$").set_color(WHITE).scale(.8)
		psi[0].set_color(GREEN_B)
		psi[2].set_color(BLUE_B)
		psi[3].set_color(YELLOW_E)
		psi.move_to([0,-2,0])
		self.play(Write(psi), run_time = 1)
		self.wait(2)
	