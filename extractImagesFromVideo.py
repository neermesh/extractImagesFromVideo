import os
import cv2

def extractor(inpath,outpath,FPS=1):
	"""
	--------------------------------ARGS-----------------------------------------


	inpath  - Path of input video file
	outpath - Output folder where extracted images is going to save
	FPS     - Frame Rate  Per Second

	-----------------------------------------------------------------------------

	"""


	command = 'ffmpeg -i '+inpath+' -vf fps='+str(FPS)+' '+ outpath+'/ffmpeg_%0d.png'
	os.system(command)



def controller(inpath,outpath):


	'''


        inpath  - Path of input video file.
        outpath - Output folder where new folder for each video is going to created.

	'''





	lst = os.listdir(inpath)
	for  each_video in lst:
		if '.mp4' in each_video:
			folder_name = each_video.split('.')[0]
			complete_path = os.path.join(outpath,folder_name)
			if not os.path.exists(complete_path):
				os.makedirs(complete_path)
				extractor(os.path.join(inpath,each_video),complete_path)
				print(os.path.join(inpath,each_video),'            process completed...')






controller('untitled_folder/','data/')




