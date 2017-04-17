import webbrowser
import sys
from vitsh.constants import *


def moodle(args):
    
	sys.stdout.write('Opening VITCC Moodle ... \n')
	url = "http://moodlecc.vit.ac.in/"
	webbrowser.open(url,new=2)
	sys.stdout.flush()

	return SHELL_STATUS_RUN