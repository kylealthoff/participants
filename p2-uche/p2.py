import sys
sys.path.append('..')
import participant as p


participant = 'P02'
speed = sys.argv[1]
p.generate_files(participant, speed)
