import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    attachment = share.ans["attachment:8"]
    #
    direction = share.ans["direction:3"]
    #
    if attachment == 'standing':
        return direction
    if attachment == 'hanging':
        return direction + 4
    if attachment == 'side':
        return direction + 8
    if attachment == 'multiple':
        return direction + 12
    #