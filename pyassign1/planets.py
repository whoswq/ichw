'''
planet.py 
__name__: wangchongbin
__pkuid__: 1800011716
__email__: 1800011716@pku.edu.cn

'''
import turtle 
#引入turtle模块

s = turtle.Screen()

list_turtle = ['mercury','venus','earth','mars','jupiter','saturn']
#不同行星的名称
list_color = ['red','blue','orange','black','grey','green']
#不同行星的颜色


# 相关的物理参量 量纲均为国际单位制
# 引力相关参量
G = 6.67259e-11 * 8e5    #修改过的万有引力常数，为了保证周期与真实一致
M = 1.989e30 / 1e35      #修改过的太阳质量，

# 位置参量
list_x = [57900000000,108200000000,149600000000,227940000000,778330000000,1429400000000]    # 数据为真实的距离（米）
list_y = [0,0,0,0,0,0]
for i in range (6):
	list_x[i] = list_x[i] / 5e9
# x为椭圆轨道的通径，坐标列表,经过处理后为在像素点数目

# 速度列表
list_vx = [0,0,0,0,0,0]
list_vy = [0,0,0,0,0,0]
for i in range (6):
	list_vy[i] = (G * M / list_x[i])**0.5  
	#运动起初时垂直与行星与太阳连线，由万有引力计算而来
	
list_ax = [0,0,0,0,0,0]
list_ay = [0,0,0,0,0,0]
# 加速度列表


dt = 3600 * 12
# 每一次计算的时间间隔，单位为秒


# 引入太阳
sun = turtle.Turtle ()
sun.shape ('circle')
sun.pencolor('yellow')
sun.shapesize (0.7,0.7,1.0)

s.delay(0)
# 让它们跑的快一点


# 确定每个行星的颜色、位置
for i in range (6): 
	list_turtle[i] = turtle.Turtle()
	list_turtle[i].pencolor(list_color[i])
	list_turtle[i].shape ('circle')
	list_turtle[i].shapesize (0.2,0.2,0)
	list_turtle[i].penup()
	list_turtle[i].goto (list_x[i] ,0)
	list_turtle[i].speed(0)
	# 出发点的位置，假设是同时从x轴出发
	list_turtle[i].pendown()

def draw (i,dt):
	# 在dt时间内每个行星的运动
	for i in range (6):
		list_ax[i] = -G*M / ( list_x[i] ** 2 + list_y[i] ** 2 ) * (list_x[i] / (list_x[i] ** 2 + list_y[i] ** 2) ** 0.5)
		list_ay[i] = -G*M / ( list_x[i] ** 2 + list_y[i] ** 2 ) * (list_y[i] / (list_x[i] ** 2 + list_y[i] ** 2) ** 0.5)
		list_vx[i] = list_vx[i] + list_ax[i] * dt
		list_vy[i] = list_vy[i] + list_ay[i] * dt
		list_x[i] = list_x[i] + list_vx[i] * dt
		list_y[i] = list_y[i] + list_vy[i] * dt
		if list_x[i] ** 2 + list_y[i] ** 2 <= 100:
			break
		list_turtle[i].goto(list_x[i] , list_y[i] )



def draw_solar_system ():
	t = 0
	while True:
		draw (i,dt)
		t += dt
		day = int(t / (3600*24))
		days = int (day % 365.24)
		year = int(day / 365.24)
		time = 'year =' + str(year) + ' day =' + str(days)
		print (time)
	else:
		return
		

if __name__ == '__main__':
	draw_solar_system ()

s.exitonclick()