from Tool.analysis import Analysis

a = Analysis()

with open("example/面向对象.b", "r", encoding='utf-8') as f:
    for line in f:
        print(a.output(line))
