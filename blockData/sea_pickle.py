import sys
sys.path.append(".")
import share
# 载入依赖项



def main():
    cluster_count = share.ans["cluster_count:3"]
    dead_bit = share.ans["dead_bit:1"]
    #
    if dead_bit == 1:
        return cluster_count + 4
    else:
        return cluster_count
    #