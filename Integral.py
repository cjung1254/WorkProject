#important necessary libs
from manimlib.imports import *
import numpy as np



#develop the graph and integration area under the curve
class Work(GraphScene):
	CONFIG = {
		"x_max" : 5,
	    "y_max" : 7,
        "y_axis_label" : "F(x)",
    }
	#Define Construction
	def construct(self):
		self.show_function_graph()

	#Define functions
	def show_function_graph(self):
		self.setup_axes(animate=True)
		#Math function

		def func(x):
			return x*(5-x)

		#graph
		graph=self.get_graph(func, x_min=0, x_max = 5)
		graph.set_color(WHITE)


		#Play graphs
		self.play(ShowCreation(graph), run_time=3)
		self.wait(1)

		def rect(x):
			return x
		recta=self.get_graph(rect,x_min=-1, x_max=5)
		# Adding Riemann Rectangle
		kwargs = {
			"x_min" : 0,
			"x_max" : 5,
			"fill_opacity": 0.75,
			"stroke_width" : 0.25,
		}

		self.graph=graph
		iteraciones=10

		self.rect_list = self.get_riemann_rectangles_list(
			graph, iteraciones, start_color=BLUE_B, end_color=YELLOW_E, **kwargs
		)
		flat_rects = self.get_riemann_rectangles(
			self.get_graph(lambda x : 0), dx = 0.5, start_color = invert_color(BLUE), end_color=invert_color(ORANGE), **kwargs
		)
		rects = self.rect_list[0]
		self.transform_between_riemann_rects(
			flat_rects, rects,
			replace_mobject_with_target_in_scene = True,
			run_time = 1.1
		)



		#Make a loop
		for j in range(1,10):
			self.transform_between_riemann_rects(
			self.rect_list[j-1], self.rect_list[j], dx =1,
			replace_mobject_with_target_in_scene = True,
			run_time=.5
			)
		vector=np.array([3,3,0])
		tex = TextMobject("Work = ", "$\\displaystyle\\int F(x) dx$").set_color(WHITE).scale(1.1)
		tex.move_to(vector)
		self.play(Write(tex), run_time = 1)
		self.wait(3)
		self.play(FadeOut(graph))