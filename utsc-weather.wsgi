activate_this = '/home/rein/utsc-weather/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
import sys
sys.path.insert(0, '/home/rein/utsc-weather/')
from utsc-weather import app as application
