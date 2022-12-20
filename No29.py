# manim No29.py No29_1 -pql
# manim No29.py No29_1 -qk -> 4k
# manim No29.py No29_1 -s -> pic
# https://infograph.tistory.com/122
from cmath import pi
from manim import *
import numpy as np
import math

class No29_1(MovingCameraScene):
    def construct(self):
        theta = 1/9*np.pi
        theta_vt = ValueTracker(theta)
        semicircle = Arc(angle=PI, radius=4, stroke_color = GREY, arc_center=np.array([0, -1.5, 0]))
        bottom_line = Line(start=np.array([-4.0,-1.5,0]), end=np.array([4.0,-1.5,0]), stroke_color = GREY)
        tri_lenth = (8/(1+(math.sqrt(3)/2*(np.tan(1/2*np.pi - theta)+np.tan(1/2*np.pi - theta*2)))))

        dot_A = np.array([-4.0,-1.5,0])
        dot_A_text = Text('A', font_size=35).next_to(dot_A, LEFT+DOWN, buff=0.05)
        dot_B = np.array([4.0,-1.5,0])
        dot_B_text = Text('B', font_size=35).next_to(dot_B, RIGHT+DOWN, buff=0.1)
        dot_U = np.array([-4.0+math.sqrt(3)/2*tri_lenth/np.tan(theta), -1.5+math.sqrt(3)/2*tri_lenth, 0])
        dot_U_text = Text('U', font_size=35).next_to(dot_U, LEFT+UP, buff=0.05)
        dot_T = np.array([-4.0+math.sqrt(3)/2*tri_lenth/np.tan(theta) + tri_lenth, -1.5+math.sqrt(3)/2*tri_lenth, 0])
        dot_T_text = Text('T', font_size=35).next_to(dot_T, RIGHT+UP, buff=0.05)
        dot_S = np.array([(-4.0+math.sqrt(3)/2*tri_lenth/np.tan(theta))/2.0 + (-4.0+math.sqrt(3)/2*tri_lenth/np.tan(theta) + tri_lenth)/2.0, -1.5, 0])
        dot_S_text = Text('S', font_size=35).next_to(dot_S, DOWN, buff=0.15)
        dot_P = np.array([4*np.cos(theta*2),4*np.sin(theta*2)-1.5,0])
        dot_P_text = Text('P', font_size=35).next_to(dot_P, RIGHT+UP, buff=0.1)
        dot_Q = np.array([4*np.cos(np.pi-4*theta),4*np.sin(np.pi-4*theta)-1.5,0])
        dot_Q_text = Text('Q', font_size=35).next_to(dot_Q, LEFT+UP, buff=0.1)
        dot_R = np.array([8/(np.tan(1/2*np.pi-theta)+np.tan(1/2*np.pi-2*theta))*np.tan(1/2*np.pi-theta)-4,8/(np.tan(1/2*np.pi-theta)+np.tan(1/2*np.pi-2*theta))-1.5, 0])
        dot_R_text = Text('R', font_size=35).next_to(dot_R, UP, buff=0.2)

        line_SU = Line(start=dot_S, end=dot_U, stroke_color = GREY)
        line_TU = Line(start=dot_T, end=dot_U, stroke_color = GREY)
        line_TS = Line(start=dot_S, end=dot_T, stroke_color = GREY)
        line_AP = Line(start=np.array([-4.0,-1.5,0]), end=np.array([4*np.cos(2*theta),4*np.sin(2*theta)-1.5,0]), stroke_color = GREY)
        line_BQ = Line(start=np.array([4.0,-1.5,0]), end=np.array([4*np.cos(np.pi-4*theta),4*np.sin(np.pi-4*theta)-1.5,0]), stroke_color = GREY)

        theta1 = Angle(bottom_line, line_AP, radius=0.8, other_angle=False)
        ang_tex1 = MathTex(r"\theta").move_to(
            Angle(
                bottom_line, line_AP, radius=0.5 + 3 * MED_SMALL_BUFF, other_angle=False
            ).point_from_proportion(0.5)
        )
        theta2 = Angle(line_BQ, bottom_line, radius=0.7, quadrant=(1,-1))
        ang_tex2 = MathTex(r"2\theta").move_to(
            Angle(
                line_BQ, bottom_line, quadrant=(1,-1), radius=0.5 + 3 * MED_SMALL_BUFF, other_angle=False
            ).point_from_proportion(0.5)
        )
        
        f_theta = MathTex(
            r"f( \theta )" ,font_size=43
        ).move_to(np.array([-0.9, 0.7, 0]))
        g_theta = MathTex(
            r"g( \theta )" ,font_size=43
        ).move_to(np.array([1.22, -0.5, 0]))
        problem = VGroup(semicircle, bottom_line, Dot(dot_A, radius=0), dot_A_text, Dot(dot_B, radius=0), dot_B_text, Dot(dot_P, radius=0), dot_P_text, Dot(dot_Q, radius=0), dot_Q_text, Dot(dot_S, radius=0), dot_S_text, Dot(dot_U, radius=0), dot_U_text, Dot(dot_T, radius=0), dot_T_text, line_AP, line_BQ, line_SU, line_TS, line_TU, theta1, theta2, ang_tex1, ang_tex2, Dot(dot_R, radius=0), dot_R_text, f_theta, g_theta)
        problem.save_state()
        problem_equ = MathTex(
            r"\angle PAB=\theta,\ \angle QBA=2\theta \\ \overline{AB} \parallel \overline{UT} \\ \triangle STU = equilateral\ triangle " ,font_size=35
        ).move_to(np.array([3.5, 1, 0]))

        problem_equ2 = MathTex(
            r"\lim_{\theta \to 0 +}", r"{g( \theta )", r"\over", r"\theta \times", r"f( \theta )}", r"= {p \over q} \sqrt{3}" ,font_size=60,
        ).move_to(np.array([0, -2, 0]))
        problem_equ2[1].set_color(GOLD_D)
        problem_equ2[4].set_color(BLUE_C)
        problem_equ3 = MathTex(
            r"p + q =\ ?" ,font_size=60,
        ).move_to(np.array([3.5, -2, 0]))  

        self.play(Create(semicircle), Create(dot_A_text), Create(dot_B_text))
        self.play(Create(line_BQ),Create(dot_Q_text), Create(theta2), Create(ang_tex2))
        self.play(Create(bottom_line), Create(dot_R_text),Create(dot_P_text), Create(theta1), Create(ang_tex1), Create(line_AP))
        self.play(Create(line_SU), Create(line_TU), Create(line_TS), Create(dot_S_text), Create(dot_U_text), Create(dot_T_text), Create(f_theta), Create(g_theta))
        self.play(problem.animate(run_time=1, lag_ratio=0).scale(0.85).shift(UP+3*LEFT))
        self.play(Create(problem_equ))
        problem += f_theta; problem
        problem += g_theta; problem
        self.wait(1)
        self.play(Create(problem_equ2), f_theta.animate.set_color(BLUE_C), g_theta.animate.set_color(GOLD_D))
        self.play(problem_equ2.animate(run_time=0.7).shift(2*LEFT))
        self.play(Create(problem_equ3))
        self.wait(2)
        self.play(Uncreate(problem_equ), Uncreate(problem_equ2), Uncreate(problem_equ3), Uncreate(f_theta), Uncreate(g_theta))
        self.play(problem.animate(run_time=1, lag_ratio=0).scale(1/0.85).shift(3*RIGHT, DOWN*0.3))

        #설명 시작
        fst_sol = MathTex(
            r"\overline{AR} : \overline{RB} ", r"\simeq", r"2 : 1", r"\Rightarrow \overline{AR} \simeq \overline{QR} \simeq {4 \over 3}" ,font_size=45
        ).move_to(np.array([0, -2, 0]))
        surround_rect_1 = SurroundingRectangle(mobject=fst_sol[:1], color=YELLOW)
        surround_rect_2 = SurroundingRectangle(mobject=fst_sol[2], color=YELLOW)
        line_AR = Line(start=dot_A, end=dot_R, stroke_color=MAROON_C)
        line_AR.save_state()
        line_BR = Line(start=dot_B, end=dot_R, stroke_color=MAROON_C)
        ratio_1 = Text('2', font_size=35, color=MAROON_D).next_to(dot_A).shift(RIGHT*2.2+UP*1.3)
        ratio_2 = Text('1', font_size=35, color=MAROON_D).next_to(dot_B).shift(LEFT*1.3+UP*1.2)
        self.play(Create(fst_sol))
        self.wait()
        self.play(Create(surround_rect_1))
        self.wait()
        self.play(surround_rect_1.animate.become(surround_rect_2))
        self.wait(2)
        move_dot_R = Dot(dot_R, radius=0.05, color=GOLD)
        self.play(problem.animate.shift(DOWN*0.7), Uncreate(fst_sol), Uncreate(dot_R_text), Uncreate(dot_U_text), Uncreate(dot_T_text), Uncreate(dot_S_text), Create(ratio_1), Create(ratio_2), Uncreate(theta1), Uncreate(theta2), Create(line_AR), Create(line_BR), Create(move_dot_R), Uncreate(surround_rect_1))
        ratio_1.save_state()
        ratio_2.save_state()
        self.play(Uncreate(ratio_1), Uncreate(ratio_2), Uncreate(ang_tex1), Uncreate(ang_tex2))
        ratio_1.restore()
        ratio_2.restore()
        self.wait(2)

        dot_P_text.add_updater(
            lambda mobj: mobj.next_to([4*np.cos(theta_vt.get_value()*2),4*np.sin(theta_vt.get_value()*2)-1.5,0], RIGHT+UP, buff=0.1)
            )
        line_AP.add_updater(
            lambda mobj: mobj.put_start_and_end_on(dot_A, [4*np.cos(theta_vt.get_value()*2),4*np.sin(theta_vt.get_value()*2)-1.5,0])
            )
        line_BQ.add_updater(
            lambda mobj: mobj.put_start_and_end_on(dot_B, [4*np.cos(np.pi-4*theta_vt.get_value()),4*np.sin(np.pi-4*theta_vt.get_value())-1.5,0])
            )
        dot_Q_text.add_updater(
            lambda mobj: mobj.next_to([4*np.cos(np.pi-4*theta_vt.get_value()),4*np.sin(np.pi-4*theta_vt.get_value())-1.5,0], LEFT+UP, buff=0.1)
            )
        line_AR.add_updater(
            lambda mobj: mobj.put_start_and_end_on(dot_A, [8/(np.tan(1/2*np.pi-theta_vt.get_value())+np.tan(1/2*np.pi-2*theta_vt.get_value()))*np.tan(1/2*np.pi-theta_vt.get_value())-4,8/(np.tan(1/2*np.pi-theta_vt.get_value())+np.tan(1/2*np.pi-2*theta_vt.get_value()))-1.5, 0])
        )
        line_SU.add_updater(
            lambda mobj: mobj.put_start_and_end_on([(-4.0+math.sqrt(3)/2*(8/(1+(math.sqrt(3)/2*(np.tan(1/2*np.pi - theta_vt.get_value())+np.tan(1/2*np.pi - theta_vt.get_value()*2)))))/np.tan(theta_vt.get_value()))/2.0 + (-4.0+math.sqrt(3)/2*(8/(1+(math.sqrt(3)/2*(np.tan(1/2*np.pi - theta_vt.get_value())+np.tan(1/2*np.pi - theta_vt.get_value()*2)))))/np.tan(theta_vt.get_value()) + (8/(1+(math.sqrt(3)/2*(np.tan(1/2*np.pi - theta_vt.get_value())+np.tan(1/2*np.pi - theta_vt.get_value()*2))))))/2.0, -1.5, 0], [-4.0+math.sqrt(3)/2*(8/(1+(math.sqrt(3)/2*(np.tan(1/2*np.pi - theta_vt.get_value())+np.tan(1/2*np.pi - theta_vt.get_value()*2)))))/np.tan(theta_vt.get_value()), -1.5+math.sqrt(3)/2*(8/(1+(math.sqrt(3)/2*(np.tan(1/2*np.pi - theta_vt.get_value())+np.tan(1/2*np.pi - theta_vt.get_value()*2))))), 0])
        )
        line_TS.add_updater(
            lambda mobj: mobj.put_start_and_end_on([(-4.0+math.sqrt(3)/2*(8/(1+(math.sqrt(3)/2*(np.tan(1/2*np.pi - theta_vt.get_value())+np.tan(1/2*np.pi - theta_vt.get_value()*2)))))/np.tan(theta_vt.get_value()))/2.0 + (-4.0+math.sqrt(3)/2*(8/(1+(math.sqrt(3)/2*(np.tan(1/2*np.pi - theta_vt.get_value())+np.tan(1/2*np.pi - theta_vt.get_value()*2)))))/np.tan(theta_vt.get_value()) + (8/(1+(math.sqrt(3)/2*(np.tan(1/2*np.pi - theta_vt.get_value())+np.tan(1/2*np.pi - theta_vt.get_value()*2))))))/2.0, -1.5, 0], [-4.0+math.sqrt(3)/2*(8/(1+(math.sqrt(3)/2*(np.tan(1/2*np.pi - theta_vt.get_value())+np.tan(1/2*np.pi - theta_vt.get_value()*2)))))/np.tan(theta_vt.get_value()) + (8/(1+(math.sqrt(3)/2*(np.tan(1/2*np.pi - theta_vt.get_value())+np.tan(1/2*np.pi - theta_vt.get_value()*2))))), -1.5+math.sqrt(3)/2*(8/(1+(math.sqrt(3)/2*(np.tan(1/2*np.pi - theta_vt.get_value())+np.tan(1/2*np.pi - theta_vt.get_value()*2))))), 0])
        )
        line_TU.add_updater(
            lambda mobj: mobj.put_start_and_end_on([-4.0+math.sqrt(3)/2*(8/(1+(math.sqrt(3)/2*(np.tan(1/2*np.pi - theta_vt.get_value())+np.tan(1/2*np.pi - theta_vt.get_value()*2)))))/np.tan(theta_vt.get_value()), -1.5+math.sqrt(3)/2*(8/(1+(math.sqrt(3)/2*(np.tan(1/2*np.pi - theta_vt.get_value())+np.tan(1/2*np.pi - theta_vt.get_value()*2))))), 0], [-4.0+math.sqrt(3)/2*(8/(1+(math.sqrt(3)/2*(np.tan(1/2*np.pi - theta_vt.get_value())+np.tan(1/2*np.pi - theta_vt.get_value()*2)))))/np.tan(theta_vt.get_value()) + (8/(1+(math.sqrt(3)/2*(np.tan(1/2*np.pi - theta_vt.get_value())+np.tan(1/2*np.pi - theta_vt.get_value()*2))))), -1.5+math.sqrt(3)/2*(8/(1+(math.sqrt(3)/2*(np.tan(1/2*np.pi - theta_vt.get_value())+np.tan(1/2*np.pi - theta_vt.get_value()*2))))), 0])
        )
        line_AR.add_updater(
            lambda mobj: mobj.put_start_and_end_on(dot_A, [8/(np.tan(1/2*np.pi-theta_vt.get_value())+np.tan(1/2*np.pi-2*theta_vt.get_value()))*np.tan(1/2*np.pi-theta_vt.get_value())-4,8/(np.tan(1/2*np.pi-theta_vt.get_value())+np.tan(1/2*np.pi-2*theta_vt.get_value()))-1.5, 0])
        )
        line_BR.add_updater(
            lambda mobj: mobj.put_start_and_end_on(dot_B, [8/(np.tan(1/2*np.pi-theta_vt.get_value())+np.tan(1/2*np.pi-2*theta_vt.get_value()))*np.tan(1/2*np.pi-theta_vt.get_value())-4,8/(np.tan(1/2*np.pi-theta_vt.get_value())+np.tan(1/2*np.pi-2*theta_vt.get_value()))-1.5, 0])
        )
        move_dot_R.add_updater(
            lambda mobj: mobj.move_to([8/(np.tan(1/2*np.pi-theta_vt.get_value())+np.tan(1/2*np.pi-2*theta_vt.get_value()))*np.tan(1/2*np.pi-theta_vt.get_value())-4,8/(np.tan(1/2*np.pi-theta_vt.get_value())+np.tan(1/2*np.pi-2*theta_vt.get_value()))-1.5, 0])
            )

        self.play(theta_vt.animate.set_value(1/100*np.pi))
        self.wait(2)
        self.play(theta_vt.animate.set_value(1/1000*np.pi))
        dot_A_text_trans = Text('A', font_size=35).next_to([4*np.cos(np.pi-4*theta_vt.get_value()),4*np.sin(np.pi-4*theta_vt.get_value())-1.5,0], LEFT+UP, buff=0.1)
        self.wait()
        dot_Q_text.save_state()
        self.play(Transform(dot_Q_text, dot_A_text_trans))

        b1 = BraceBetweenPoints(dot_A, [8/(np.tan(1/2*np.pi-theta_vt.get_value())+np.tan(1/2*np.pi-2*theta_vt.get_value()))*np.tan(1/2*np.pi-theta_vt.get_value())-4,8/(np.tan(1/2*np.pi-theta_vt.get_value())+np.tan(1/2*np.pi-2*theta_vt.get_value()))-1.5, 0], color = GOLD)
        b2 = BraceBetweenPoints([8/(np.tan(1/2*np.pi-theta_vt.get_value())+np.tan(1/2*np.pi-2*theta_vt.get_value()))*np.tan(1/2*np.pi-theta_vt.get_value())-4,8/(np.tan(1/2*np.pi-theta_vt.get_value())+np.tan(1/2*np.pi-2*theta_vt.get_value()))-1.5, 0], dot_B, color = GOLD)
        self.play(Create(b1), Create(b2), Create(ratio_1.next_to(b1, DOWN)), Create(ratio_2.next_to(b2, DOWN)))
        self.wait()
        b1_tans = BraceBetweenPoints(dot_R, dot_A, color = GOLD)
        b1_tras_text = MathTex(
            r"{4 \over 3}",font_size=35, color=YELLOW
        ).move_to([-1.5, 0.5, 0])
        self.play(theta_vt.animate.set_value(1/9*np.pi), Transform(b1, b1_tans), Uncreate(b2), Uncreate(ratio_1), Uncreate(ratio_2))
        dot_Q_text.restore()
        line_AR.restore()
        b1_tans_2 = BraceBetweenPoints(dot_R, dot_Q, color = GOLD)
        b1_tans_2_text = MathTex(
            r"{4 \over 3}",font_size=35, color=YELLOW
        ).move_to([1, 2, 0])
        line_AR_2 = Line(start=dot_A, end=dot_R, stroke_color=TEAL_C)
        line_QR = Line(start=dot_Q, end=dot_R, stroke_color=TEAL_C)
        self.play(Create(b1_tras_text), Create(dot_Q_text), Transform(b1_tans, b1_tans_2), Create(b1_tans_2_text), Create(line_AR_2), Create(line_QR))
        self.wait()
        
        self.play(
            self.camera.frame.animate.move_to([0,-2,0]).scale(1.3)
            )
        
        # lim x->0 f(x)=0
        lim_x_0_fx = MathTex(
            r"\lim_{ x \to 0}\frac{ln(1+x)}{x}=\lim_{ x \to 0}\frac{e^x-1}{x}=\lim_{ x \to 0}\frac{\sin{x}}{x}=\lim_{ x \to 0}\frac{\tan{x}}{x}=1" ,font_size=60,
        ).move_to(np.array([0, -4, 0]))
        
        if_lim_x_0 = MathTex(
            r"if \quad \lim_{ x \to 0}" ,font_size=60,
        ).move_to(np.array([-4, -4.5, 0]))
        
        lim_x_0 = MathTex(
            r"\ln(1+ax)\approx e^{ax}-1 \approx \sin{ax} \approx \tan{ax} \approx ax" ,font_size=60,
        ).move_to(np.array([0, -5.7, 0]))
        
        self.play(Create(lim_x_0_fx))
        self.play(lim_x_0_fx.animate.move_to([0,-2.8,0]).scale(0.7))
        self.play(Create(if_lim_x_0),Create(lim_x_0))
        self.wait()
        
        self.play(Restore(problem), Uncreate(if_lim_x_0), Uncreate(lim_x_0), Uncreate(lim_x_0_fx), Uncreate(b1), Uncreate(b1_tans), Uncreate(b1_tras_text), Uncreate(b1_tans_2), Uncreate(b1_tans_2_text), Uncreate(move_dot_R))
        self.play(
            self.camera.frame.animate.move_to([0,0,0]).scale(0.7)
            )
        self.wait(2)
        
        line_AQ = Line(start=dot_Q, end=dot_A, stroke_color = RED)
        line_AR = Line(start=dot_A, end=dot_R, stroke_color = RED)
        line_RQ = Line(start=dot_R, end=dot_Q, stroke_color = RED)
        ARQ = VGroup(line_RQ, line_AR, line_AQ)
        self.play(Create(ARQ), f_theta.animate.set_color(RED))
        self.wait()
        self.play(line_RQ.animate.set_color(TEAL_C), line_AR.animate.set_color(TEAL_C))
        
        self.play(
            self.camera.frame.animate.move_to([0,-1,0]).scale(1.3)
            )
        S_AQR = MathTex(
            r"S \triangle AQR = {1 \over 2} \cdot \overline{AR} \cdot \overline{RQ} \cdot \sin{\angle ARQ}" ,font_size=60,
        ).move_to(np.array([0, -3.5, 0]))
        self.play(Create(S_AQR))
        S_AQR_2 = MathTex(
            r"f( \theta ) \approx S \triangle AQR = {1 \over 2} \cdot \overline{AR} \cdot \overline{RQ} \cdot \sin{\angle ARQ}" ,font_size=60,
        ).move_to(np.array([0, -3.5, 0]))
        self.play(ReplacementTransform(S_AQR, S_AQR_2))
        
        A_ARQ = MathTex(
            r"\angle ARQ = \angle RAB + \angle RBA" ,font_size=60,
        ).move_to(np.array([0, -4.7, 0]))
        self.play(S_AQR_2.animate.move_to(np.array([0,-3,0])))
        self.play(Create(A_ARQ))
        a_ARQ = Angle( line_RQ, line_AR, radius=0.8, color=MAROON_B, quadrant=(1,-1))
        a_ARQ_tex = MathTex(
            r"3 \theta" ,font_size=50, color=MAROON_B
        ).move_to(np.array([0.3,0.8,0]))
        self.play(theta1.animate.set_color(MAROON_B), theta2.animate.set_color(MAROON_B), ang_tex1.animate.set_color(MAROON_B), ang_tex2.animate.set_color(MAROON_B))
        self.play(Create(a_ARQ), Create(a_ARQ_tex))
        self.wait()
        A_ARQ_2 = MathTex(
            r"\angle ARQ = \angle RAB + \angle RBA = 3 \theta" ,font_size=60,
        ).move_to(np.array([0, -4.7, 0]))
        self.play(ReplacementTransform(A_ARQ, A_ARQ_2))
        mt = VGroup(A_ARQ_2, S_AQR_2)
        self.wait()
        S_ARQ_3 = MathTex(
            r"f( \theta ) = S \triangle AQR \approx {1 \over 2} \cdot \left( {4 \over 3} \right) ^2 \cdot 3 \theta = " ,font_size=60,
        ).move_to(np.array([-0.4, -3.5, 0]))
        S_ARQ_4 = MathTex(
            r"{8 \over 3} \theta" ,font_size=60,
        ).move_to(np.array([5, -3.5, 0]))
        
        self.play(Uncreate(mt))
        self.play(Create(S_ARQ_3), Create(S_ARQ_4))
        self.wait()
        
        
        self.play(Uncreate(S_ARQ_3), Uncreate(a_ARQ), Uncreate(a_ARQ_tex), theta1.animate.set_color(WHITE), theta2.animate.set_color(WHITE), ang_tex1.animate.set_color(WHITE), ang_tex2.animate.set_color(WHITE))
        bow_AQ = Arc(angle=4*theta, radius=4, stroke_color=BLUE_C, arc_center=np.array([0, -1.5, 0])).rotate(pi-4*theta, about_point=np.array([0,-1.5,0]))
        self.play(
            self.camera.frame.animate(run_time=1).move_to([0,0.6,0]).scale(0.7),
            S_ARQ_4.animate(run_time=2).move_to(np.array([-0.9,0.7,0])).scale(0.7).set_color(BLUE_C), Uncreate(f_theta), Create(bow_AQ), line_AQ.animate(run_time=1.5).set_color(GREY), line_RQ.animate(run_time=1.5).set_color(BLUE_C), line_AR.animate(run_time=1.5).set_color(BLUE_C), Uncreate(theta1), Uncreate(theta2), Uncreate(ang_tex1), Uncreate(ang_tex2)
            )
        self.wait()
        self.play(g_theta.animate.set_color(GOLD_D), line_SU.animate.set_color(GOLD_D), line_TU.animate.set_color(GOLD_D), line_TS.animate.set_color(GOLD_D))
        self.wait()
        
        ROP_R = np.array([8/(np.tan(1/2*np.pi-theta)+np.tan(1/2*np.pi-2*theta))*np.tan(1/2*np.pi-theta)-4, -1.5, 0])
        H_R = Line(start=dot_R, end=ROP_R, stroke_color = RED)
        dot_H_text = Text('H', font_size=35).next_to(ROP_R, DOWN, buff=0.15)
        ROP_S = np.array([(-4.0+math.sqrt(3)/2*tri_lenth/np.tan(theta))/2.0 + (-4.0+math.sqrt(3)/2*tri_lenth/np.tan(theta) + tri_lenth)/2.0, -1.5+math.sqrt(3)/2*tri_lenth, 0])
        Hh_R = Line(start=dot_S, end=ROP_S, stroke_color = RED)
        dot_Hh_text = Text('H\'', font_size=35).next_to(ROP_S, UP, buff=0.1)
        
        self.play(line_RQ.animate.set_color(GREY), line_AR.animate.set_color(GREY), Uncreate(bow_AQ), Uncreate(S_ARQ_4), Uncreate(g_theta))
        self.wait()
        self.play(Create(H_R), Create(dot_H_text), Create(Hh_R), Create(dot_Hh_text))
        
        dot_Hhh = np.array([8/(np.tan(1/2*np.pi-theta)+np.tan(1/2*np.pi-2*theta))*np.tan(1/2*np.pi-theta)-4, -1.5+math.sqrt(3)/2*tri_lenth, 0])
        
        R_to_zero = Line(start=dot_R, 
        end=dot_Hhh, 
        color=BLUE_C
        )
        self.play(Create(R_to_zero), Uncreate(H_R), Uncreate(dot_H_text), Uncreate(Hh_R), Uncreate(dot_Hh_text))
        self.wait(0.5)
        self.play(
            self.camera.frame.animate.move_to([0,-1,0]).scale(1.3)
            )
        
        S_TUS_1 = MathTex(
            r"g( \theta ) = {4 \over 3} \theta \cdot {2 \over \sqrt{3}} \cdot {4 \over 3} \theta \cdot {1 \over 2} =", font_size=60,
        ).move_to(np.array([-1, -3.5, 0]))
        S_TUS_2 = MathTex(
            r"{16 \over 9\sqrt{3}} \theta ^2", font_size=60
        ).move_to(np.array([3.6, -3.5, 0]))
        self.wait(0.5)
        self.play(Create(S_TUS_1), Create(S_TUS_2), Uncreate(R_to_zero))

        self.play(Uncreate(S_TUS_1))
        self.play(self.camera.frame.animate.move_to([0,0.3,0]).scale(0.7),
        S_TUS_2.animate.move_to([1.33, -0.5, 0]).scale(0.5).set_color(GOLD_D),
        )
        bow_AQ = Arc(angle=4*theta, radius=4, stroke_color=BLUE_C, arc_center=np.array([0, -1.5, 0])).rotate(pi-4*theta, about_point=np.array([0,-1.5,0]))
        S_ARQ_4 = MathTex(
            r"{8 \over 3} \theta" ,font_size=60, color=BLUE_C
        ).move_to(np.array([-0.9,0.7,0])).scale(0.7)
        self.play(line_AR.animate.set_color(BLUE_C),
        line_RQ.animate.set_color(BLUE_C),
        Create(bow_AQ),
        Create(S_ARQ_4)
        )
        self.wait()
        self.play(self.camera.frame.animate.move_to([0,-0.7,0]).scale(1.3))
        final_ans = MathTex(
            r"\lim_{\theta \to 0 +} {g( \theta ) \over {\theta \times f( \theta )}} = \cfrac{\frac{16}{9\sqrt{3}}}{\frac{8}{3}} = \frac{2}{9}\sqrt{3}" ,font_size=60,
        ).move_to(np.array([0, -3.5, 0]))
        self.play(Create(final_ans))
        final_final_ans = MathTex(
            r"\therefore p+q = 11", color=RED
        ).move_to(np.array([4.5, -3.5, 0]))
        self.play(final_ans.animate.move_to([-1.5, -3.5, 0]))
        self.play(Create(final_final_ans))

        self.wait(3)