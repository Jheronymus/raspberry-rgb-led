import sys, os, logging
import threading

logging.basicConfig(filename='loader.log', format='%(asctime)s %(levelname)s : %(message)s', level=logging.DEBUG, datefmt='%d-%m-%Y %T')

def update_progress(progress):
    # print "\r%3d" % i, ('='*i)+('-'*(50-i))
    sys.stdout.write("\r[{0}] {1}%".format(('='*i)+(' '*(50-i)), i*2))
    sys.stdout.flush()

# main program
logging.info('Start of loader bar')
os.system('cls' if os.name=='nt' else 'clear')

for i in range(50+1):
    threading._sleep(0.1)
    update_progress(i)


sys.stdout.write("\r\n")
sys.stdout.flush()
logging.warning('The End is near!')

