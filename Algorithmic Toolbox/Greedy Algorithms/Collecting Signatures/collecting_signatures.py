# python3

from collections import namedtuple
from sys import stdin

Segment = namedtuple('Segment', 'start end')


def compute_optimal_points(segments):

    def choose_min_right(s):
        rights = [i.end for i in s]
        return min(rights)

    def include_tenant(s, r):
        return (s.start <= r and s.end >= r)

    points = []
    while len(segments) > 0:
        min_right = choose_min_right(segments)
        points.append(min_right)
        segments = list(filter(lambda x: not include_tenant(x, min_right), segments))
    return points


if __name__ == '__main__':
    n, *data = map(int, stdin.read().split())
    input_segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    assert n == len(input_segments)
    output_points = compute_optimal_points(input_segments)
    print(len(output_points))
    print(" ".join(map(str, output_points)))
