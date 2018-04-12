# __author liuming
# 2018-04-12

eg = '''
int main(int argc,char **argv)
{
        printf("\033[44;37;5m hello world\033[0m\n");
        return 0;
}'''
print(eg)
eg2=r'''
代码分析
实例：printf(“\033[1;33m Hello World. \033[0m \n”);

\033      [1;        33m           xxxx

 |         |          |             |

开始    背景色       字体色        字符串

该段代码编译运行后显示的是蓝色背景，白色闪烁字的效果。
解释下特殊字符的使用及定义：
“\033”引导非常规字符序列。“m”意味着设置属性然后结束非常规字符序列
“44;37;5”为蓝色，前景白色，闪烁光标的特殊字符代码。
'''
print(eg2)
c = r'''
none         = "\033[0m"
black        = "\033[0;30m"
dark_gray    = "\033[1;30m"
blue         = "\033[0;34m"
light_blue   = "\033[1;34m"
green        = "\033[0;32m"
light_green -= "\033[1;32m"
cyan         = "\033[0;36m"
light_cyan   = "\033[1;36m"
red          = "\033[0;31m"
light_red    = "\033[1;31m"
purple       = "\033[0;35m"
light_purple = "\033[1;35m"
brown        = "\033[0;33m"
yellow       = "\033[1;33m"
light_gray   = "\033[0;37m"
white        = "\033[1;37m"
字背景颜色范围: 40--49                   字颜色: 30--39
        40: 黑                          30: 黑
        41:红                          31: 红
        42:绿                          32: 绿
        43:黄                          33: 黄
        44:蓝                          34: 蓝
        45:紫                          35: 紫
        46:深绿                        36: 深绿
        47:白色                        37: 白色
38
在缺省的前景颜色上设置下划线
39
在缺省的前景颜色上关闭下划线


输出特效格式控制：

\033[0m  关闭所有属性
\033[1m   设置高亮度
\033[2m   设置低亮度
\03[4m   下划线
\033[5m   闪烁
\033[7m   反显
\033[8m   消隐
\033[30m   --   \033[37m   设置前景色
\033[40m   --   \033[47m   设置背景色



光标位置等的格式控制：

\033[nA  光标上移n行
\03[nB   光标下移n行
\033[nC   光标右移n行
\033[nD   光标左移n行
\033[y;xH设置光标位置
\033[2J   清屏
\033[K   清除从光标到行尾的内容
\033[s   保存光标位置
\033[u   恢复光标位置
\033[?25l   隐藏光标
\33[?25h   显示光标
\033[0q
　关闭所有的键盘指示灯
\033[1q
　设置“滚动锁定”指示灯
(Scroll
Lock)
\033[2q
　设置“数值锁定”指示灯
(Num
Lock)
\007
　　发蜂鸣生beep

'''
# print(c)
colors = {
    'none': "\033[0m",
    'black': "\033[0;30m",
    'dark_gray': "\033[1;30m",
    'blue': "\033[0;34m",
    'dark_blue': "\033[1;34m",
    'green': "\033[0;32m",
    'dark_green': "\033[1;32m",
'light_green': "\033[2;32m",
    'cyan': "\033[0;36m",
    'dark_cyan': "\033[1;36m",
    'red': "\033[0;31m",
    'dark_red': "\033[1;31m",
    'purple': "\033[0;35m",
    'dark_purple': "\033[1;35m",
    'brown': "\033[0;33m",
    'yellow': "\033[1;33m",
    'dark_gray': "\033[0;37m",
    'white': "\033[1;37m",
}

sp = {
    'up': '\033[nA',  # 光标上移n行
    'down': '\033[nB',  # 光标下移n行
    'right': '\033[nC',  # 光标右移n行
    'left': '\033[nD',  # 光标左移n行
    'set': '\033[y;xH',  # 设置光标位置
    'clear': '\033[2J',  # 清屏
    'passwd': '\033[K',  # 清除从光标到行尾的内容
    'stay': '\033[s',  # 保存光标位置
    'resume': '\033[u',  # 恢复光标位置
    'hide': '\033[?25l',  # 隐藏光标
    'show': '\033[?25h',  # 显示光标

}
input('\033[46;35;22m hahaha\007')

print('%s hello %s world%s' % (colors['blue'], colors['red'], colors['none']))
# for key,value in colors.items():
#     print("%s%s-----%s"%(value,key,colors['none']))
for i, item in enumerate(colors):
    print(i, '%s%s- a quick brown fox jump over the lazy dog%s' % (item, colors[item], colors['none']))
