def changetext(text):
    # 'первый','второй','третий','четвертый','пятый','шестой','седьмой','восьмой',
    # 'девятый','первая','вторая','третяя','четвертая','пятая','шестая','седьмая',
    # 'восьмая','девятая',
    # text=text.replace('две тысячи','2000')
    # text=text.replace('двух тысячный','2000')
    text = text.replace('двухтысячный', '2000')
    text = text.replace('тысяча', '1000')
    text = text.replace('тысячный', '1000')
    text = text.replace('восемьсотый', '800')
    text = text.replace('восемьсот', '800')
    text = text.replace('девятьсотый', '900')
    text = text.replace('девятьсот', '900')
    text = text.replace('первый', '1')
    text = text.replace('второй', '2')
    text = text.replace('третий', '3')
    text = text.replace('четвертый', '4')
    text = text.replace('пятый', '5')
    text = text.replace('шестой', '6')
    text = text.replace('седьмой', '7')
    text = text.replace('восьмой', '8')
    text = text.replace('девятый', '9')
    text = text.replace('нулевой', '0')
    text = text.replace('первая', '1')
    text = text.replace('вторая', '2')
    text = text.replace('третяя', '3')
    text = text.replace('четвертая', '4')
    text = text.replace('пятая', '5')
    text = text.replace('шестая', '6')
    text = text.replace('седьмая', '7')
    text = text.replace('восьмая', '8')
    text = text.replace('девятая', '9')
    text = text.replace('нулевая', '0')
    text = text.replace('одиннадцатый', '11')
    text = text.replace('двенадцатый', '12')
    text = text.replace('тринадцатый', '13')
    text = text.replace('четырнадцатый', '14')
    text = text.replace('пятнадцатый', '15')
    text = text.replace('шестнадцатый', '16')
    text = text.replace('семнадцатый', '17')
    text = text.replace('восемнадцатый', '18')
    text = text.replace('девятнадцатый', '19')
    text = text.replace('двадцатый', '20')
    text = text.replace('тридцатый', '30')
    text = text.replace('сороковой', '40')
    text = text.replace('пятидесятый', '50')
    text = text.replace('шестидесятый', '60')
    text = text.replace('семидесятый', '70')
    text = text.replace('восьмедесятый', '80')
    text = text.replace('девяностый', '90')
    text = text.replace('одиннадцатая', '11')
    text = text.replace('двенадцатая', '12')
    text = text.replace('тринадцатая', '13')
    text = text.replace('четырнадцатая', '14')
    text = text.replace('пятнадцатая', '15')
    text = text.replace('шестнадцатая', '16')
    text = text.replace('семнадцатая', '17')
    text = text.replace('восемнадцатая', '18')
    text = text.replace('девятнадцатая', '19')
    text = text.replace('одиннадцать', '11')
    text = text.replace('деванадцать', '12')
    text = text.replace('тринадцать', '13')
    text = text.replace('четырнадцать', '14')
    text = text.replace('пятнадцать', '15')
    text = text.replace('шестнадцать', '16')
    text = text.replace('семнадцать', '17')
    text = text.replace('восемнадцатыь', '18')
    text = text.replace('девятнадцать', '19')
    text = text.replace('двадцатая', '20')
    text = text.replace('тридцатая', '30')
    text = text.replace('сороковая', '40')
    text = text.replace('пятидесятая', '50')
    text = text.replace('шестидесятая', '60')
    text = text.replace('семидесятая', '70')
    text = text.replace('восьмедесятая', '80')
    text = text.replace('девяностая', '90')
    text = text.replace('двадцать', '20')
    text = text.replace('тридцать', '30')
    text = text.replace('сорок', '40')
    text = text.replace('пятьдесят', '50')
    text = text.replace('шестьдесят', '60')
    text = text.replace('семьдесят', '70')
    text = text.replace('восемьдесят', '80')
    text = text.replace('девяносто', '90')
    text = text.replace('двести', '200')
    text = text.replace('триста', '300')
    text = text.replace('четыресто', '400')
    text = text.replace('двесте', '200')
    text = text.replace('тристо', '300')
    text = text.replace('четыреста', '400')
    text = text.replace('пятьсот', '500')
    text = text.replace('шестьсот', '600')
    text = text.replace('семьсот', '700')
    text = text.replace('восемьсот', '800')
    text = text.replace('девятьсот', '900')
    text = text.replace('сто', '100')
    text = text.replace('сотый', '100')
    text = text.replace('тысяча', '1000')
    text = text.replace('один', '1')
    text = text.replace('два', '2')
    text = text.replace('три', '3')
    text = text.replace('четыре', '4')
    text = text.replace('пять', '5')
    text = text.replace('шесть', '6')
    text = text.replace('восемь', '8')
    text = text.replace('семь', '7')
    text = text.replace('девять', '9')
    text = text.replace('ноль', '0')
    text = text.replace('нуль', '0')
    return text


def change(test):
    test = test.split()
    result = ''
    temp = 0
    length = 0
    try:
        for i in test:
            try:
                b = changetext(i)
                a = int(b)
            except ValueError:
                result += b + ' '
                continue
            a = str(a)
            if length == 0:
                length = len(a)
                temp = int(a)
                continue
            if len(a) < length:
                temp += int(a)
            else:
                result += str(temp)
                length = len(a)
                temp = int(a)
        if temp == 0:
            temp = ''
        result += str(temp)
        return result
    except:
        return 'NOTdetected'
