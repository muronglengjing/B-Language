import re


def number(text):
    while re.search("[十百千万亿]", text):
        txt = text[re.search("[零一二三四五六七八九十百千万亿]+", text).start():re.search("[零一二三四五六七八九十百千万亿]+", text).end()]
        i = 0
        for num in txt:
            if num == "一":
                i += 1
            elif num == "二":
                i += 2
            elif num == "三":
                i += 3
            elif num == "四":
                i += 4
            elif num == "五":
                i += 5
            elif num == "六":
                i += 6
            elif num == "七":
                i += 7
            elif num == "八":
                i += 8
            elif num == "九":
                i += 9
            elif num == "十":
                i += 10
            elif num == "百":
                i *= 100
            elif num == "千":
                i *= 1000
            elif num == "万":
                i *= 10000
            elif num == "亿":
                i *= 100000000
        text = re.sub("[零一二三四五六七八九十百千万亿]+", str(i), text, 1)
    else:
        text = re.sub("零", "0", text)
        text = re.sub("一", "1", text)
        text = re.sub("二", "2", text)
        text = re.sub("三", "3", text)
        text = re.sub("四", "4", text)
        text = re.sub("五", "5", text)
        text = re.sub("六", "6", text)
        text = re.sub("七", "7", text)
        text = re.sub("八", "8", text)
        text = re.sub("九", "9", text)
    text = re.sub("点", ".", text)
    return text


class Analysis():
    def __init__(self):
        self.point = 0
        self.variable = {}
        self.function = {}
        self.to_class = {}
        self.name_variable = 0
        self.name_function = 0
        self.name_to_class = 0
        self.class_name = ""
        self.fun_name = ""
        self.pace = []

    def name(self, type, text):
        if type == 'v':
            txt = "_var{}".format(self.name_variable)
            self.variable[text] = txt
            self.name_variable += 1
        if type == 'f':
            txt = "_fun{}".format(self.name_function)
            self.function[text] = txt
            self.name_function += 1
        if type == 'c':
            txt = "_class{}".format(self.name_to_class)
            self.to_class[text] = txt
            self.name_to_class += 1
        return txt

    def output(self, text):
        if re.match("如果", text):
            text = "if"
            re.match("如果")
            self.point += 1
            self.name_function
            self.pace.append(self.name_function)

        if re.search("类", text):
            self.class_name = text[re.search(".+类：", text).start():re.search(".+类：", text).end()-2]
            self.pace.append(self.class_name)
            text = self.point*"\t" + "class {}:".format(self.name("c", self.class_name))
            self.point += 1
            return text

        if re.search("能", text):
            self.fun_name = text[re.search("能.+（", text).start()+1:re.search("能.+（", text).end() - 1]
            self.pace.append(self.fun_name)
            text = self.point*"\t" + "def {}:".format(self.name("f", self.fun_name))
            self.point += 1
            return text

        if re.search("[零一二三四五六七八九十百千万亿]+", text):
            text = number(text)

        if re.search("有", text):
            text = re.sub("有", ".", text)

        if self.class_name != "":
            if re.search(self.class_name, text):
                text = re.sub(self.class_name, "self", text)

        text = re.sub("的", ".", text)
        text = re.sub("加", "+", text)
        text = re.sub("减", "-", text)
        text = re.sub("乘", "*", text)
        text = re.sub("除", "/", text)
        text = re.sub("余", "%", text)

        text = re.sub("（", "(", text)
        text = re.sub("）", ")", text)

        text = re.sub("取", "=", text)
        text = re.sub("是", "=", text)

        text = re.sub("来", ".", text)

        text = self.point * "\t" + text

        if "。" in text:
            text = re.sub("。", "", text)
            self.point -= 1
            if self.pace:
                if self.pace[-1] == self.class_name:
                    self.pace.remove(self.class_name)
                    self.class_name = ""
                elif self.pace[-1] == self.fun_name:
                    self.pace.remove(self.fun_name)
                    self.fun_name = ""

        return text
