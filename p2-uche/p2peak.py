import sys
sys.path.append('..')
import peaks as peaks

participant = 'P02'
speed = sys.argv[1]
peaks.getAverages(participant, speed)