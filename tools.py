# 给文件最后添加一个换行符，返回一个列表
def lines(file):
    for line in file:
        yield line
    yield '\n'

def blocks(file):
    block = []
    text = lines(file)
    # print(type(text)) # 一个生成器
    for line in text:
        print(file)
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []
