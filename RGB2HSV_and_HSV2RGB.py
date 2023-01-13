def RGB2HSV(r,g,b):
    r, g, b = r / 255, g / 255, b / 255
    ma = max(r, g, b)
    mi = min(r, g, b)
    diff = ma - mi
    if ma == mi:
        h = 0
    elif ma == r and g >= b:
        h = 60 * ((g - b)/diff) + 0
    elif ma == r and g < b:
        h = 60 * ((g - b)/diff) + 360
    elif ma == g:
        h = 60 * ((b - r)/diff) + 120
    elif ma == b:
        h = 60 * ((r - g)/diff) + 240

    if ma == 0:
        s = 0
    else:
        s = diff / ma

    v = ma
    return h, s, v


# 参数输入范围 h(0~360), s(0% ~ 100%), v(0% ~ 100%)
# 转换结果R(0~255),G(0~255),B(0~255)，如需转换到0~100，只需把后面的乘255改成乘100
def HSV2RGB(h, s, v):
    # s, v = s / 100, v /100

    i = round(h / 60) % 6
    f = (h / 60) - i
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)

    R, G, B = 0, 0, 0
    if i == 0:
        R, G, B = v, t, p
    elif i == 1:
        R, G, B = q, v, p
    elif i == 2:
        R, G, B = p, v, t
    elif i == 3:
        R, G, B = p, q, v
    elif i == 4:
        R, G, B = t, p, v
    elif i == 5:
        R, G, B = v, p, q

    r, g, b = round(R * 255), round(G * 255), round(B * 255)
    return r, g, b


if __name__ == '__main__':
    # a = RGB2HSV(100,100,100)
    # print(a)
    b = HSV2RGB(0,0,120)
    print(b)
