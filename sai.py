import cv2
import argparse

def modify_template(cityname, color, fontsize=1.5, imgfile='school_of_ai_template.png'):
	image = cv2.imread(imgfile)

	# remove old city name
	image[172:208,336:540] = 0

	# font settings
	font = cv2.FONT_ITALIC
	fontthickness = 2
	textsize = cv2.getTextSize(cityname, font, fontsize, fontthickness)[0]
	textX = 440 - textsize[0] // 2
	textY = 184 + textsize[1] // 2

	# write new city name
	cv2.putText(image, cityname, (textX, textY), font, fontsize, color, fontthickness, cv2.LINE_AA)

	# recolor 'AI'
	mask = image[110:150, 510:555] > 10
	image[110:150, 510:555] = mask*color

	cv2.imwrite('school_of_ai_{}.png'.format(cityname), image)


if __name__ == '__main__':
	city_name = 'Ashdod'
	color = (250,100,100) # BGR not RGB
	modify_template(city_name, color)

