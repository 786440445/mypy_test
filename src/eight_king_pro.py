#八皇后问题
import random
# 冲突处理,判断下一个位置nextX和之前的state是否存在冲突
def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i] - nextX) in (0, nextY - i):
            return True
    return False

def queens(num, state = ()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num - 1:
                yield (pos,)
            else:
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result

# 图形输出n皇后
def prettyprint(solution):
    def line(pos, length = len(solution)):
        return '.' * pos + '*' + '.' * (length-pos-1)
    for pos in solution:
        print(line(pos))

num = input("how would you want king number?:")
list1 = queens(int(num))
list2 = list(list1)
prettyprint(random.choice(list2))



