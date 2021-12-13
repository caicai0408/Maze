# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys  # 导入sys模块
sys.setrecursionlimit(1000000)  # 将默认的递归深度修改为3000


class Block(object):
    def __init__(self, mmap, x, y, direction=None):
        super(Block, self).__init__()
        self.walls = [True, True, True, True]  # top,right,bottom,left
        self.mmap = mmap
        if mmap:
            mmap.mmap[x][y] = self
        self.x, self.y = x, y
        if direction is not None:
            direction = (direction + 2) % 4
            self.walls[direction] = False

    def __unicode__(self):
        return "%s" % [1 if e else 0 for e in self.walls]

    def __str__(self):
        return str(self).encode('utf-8')

    def get_next_block_pos(self, direction, mmap_h = [], mmap_z = []):
        self.mmap_h, self.mmap_z = mmap_h, mmap_z
        x = self.x
        y = self.y
        if direction == 0 and self.mmap_h[y][x] == 1:  # Top
            y -= 1
        elif direction == 1 and self.mmap_z[y][x+1] == 1:  # Right
            x += 1
        if direction == 2 and self.mmap_h[y+1][x] == 1:  # Bottom
            y += 1
        if direction == 3 and self.mmap_z[y][x] == 1:  # Left
            x -= 1
        return x, y

    def get_next_block(self, mmap_h= [], mmap_z = []):
        self.mmap_h, self.mmap_z = mmap_h, mmap_z
        directions = list(range(4))
        # random.shuffle(directions)
        for direction in directions:
            x, y = self.get_next_block_pos(direction, self.mmap_h, self.mmap_z)

            if x >= self.mmap.max_x or x < 0 or y >= self.mmap.max_y or y < 0:
                continue
            if self.mmap.mmap[x][y]:  # if walked
                continue
            self.walls[direction] = False
            return Block(self.mmap, x, y, direction)
        return None


class Map(object):
    def __init__(self):
        super(Map, self).__init__()

    def reset_map(self):
        self.gen_map(self.max_x, self.max_y)

    def gen_map(self, max_x=10, max_y=10, mmap_z=[], mmap_h=[]):
        self.max_x, self.max_y, self.mmap_z, self.mmap_h= max_x, max_y, mmap_z, mmap_h
        self.mmap = [[None for j in range(self.max_y)] for i in range(self.max_x)]
        self.solution = []
        self.solution_1 = []
        self.solution_2 = []
        for each_x in range(self.max_x):
            for each_y in range(self.max_y):
                block_stack = [Block(self, each_x, each_y)]  # a unused block
                while block_stack:
                    block = block_stack.pop()
                    next_block = block.get_next_block(self.mmap_h, self.mmap_z)
                    if next_block:
                        block_stack.append(block)
                        block_stack.append(next_block)
                        for o in block_stack:
                            self.solution.append((o.y+1, o.x+1))
                        self.solution_1.append(self.solution)
                        self.solution = []
            self.max_path = self.solution_1[0]
            for each in self.solution_1:
                if len(each) > len(self.max_path):
                    self.max_path = each
            self.solution_2.append(self.max_path)
        self.max_path_1 = self.solution_2[0]
        # print(self.solution_2)
        for each in self.solution_2:
            if len(each) > len(self.max_path_1):
                self.max_path_1 = each

    def __str__(self):
        return str(self.max_path_1)

def main():
    m = Map()
    size = input('')
    size = int(size)
    mmap = []
    mmap_z = []
    mmap_h = []
    for each in range(2 * size - 1):
        map_in_1 = input('').split()
        map_in_2 = list(map(int, map_in_1))
        mmap.append(map_in_2)
    # print(mmap)
    for each in mmap:
        if len(each) == size-1:
            each.insert(0, 0)
            each.append(0)
            mmap_z.append(each)
        else:
            mmap_h.append(each)
    mmap_h.insert(0, [0 for i in range(size)])
    mmap_h.append([0 for i in range(size)])
    # print(mmap_h, mmap_z)
    m.gen_map(size, size, mmap_z, mmap_h)
    out = m.__str__()
    out = out.replace('[', '')
    out = out.replace(']', '')
    out = out.replace(' ', '')
    out = out.replace('),(', ')(')
    print(out)
    sys.stdout.flush()
    sys.exit()




if __name__ == '__main__':
    main()
