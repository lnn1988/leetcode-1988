# 判断点分十进制格式的IPv4地址是否符合协议要求。
# 函数的输入限制为一个字符串。

def check(s):
    s_list = s.strip().split('.')
    if len(s_list) != 4:
        return False
    for i in s_list:
        if not i.isdigit():
            return False
        x = int(i)
        if str(x) != i:
            return False
        if x < 0 or x > 255:
            return False
    return True

a = "127.0.0.1"
b = "127.0.0.01"
c = "127.0..1"
print(check(a))
print(check(b))
print(check(c))