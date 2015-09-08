import sys
sys.path.append('..')
import peaks as peaks

participant = 'P22'
speed = sys.argv[1]
peaks.getAverages(participant, speed)