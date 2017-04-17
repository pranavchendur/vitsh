import webbrowser
import sys
from vitsh.constants import *


def ffcs(args):
    
	sys.stdout.write('Opening VIT Academics ... \n')
	url = "https://academicscc.vit.ac.in/student/"
	webbrowser.open(url,new=2)
	sys.stdout.flush()

	return SHELL_STATUS_RUN