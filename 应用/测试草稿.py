from 文件.文件读写 import 保存蓝图, 工程目录, 读取泛蓝图文件, 保存所有建筑

# python -m 应用.测试草稿

本蓝图 = 读取泛蓝图文件(Rf"{工程目录()}\蓝图库\临时\输入蓝图.txt")
保存蓝图(本蓝图).为json文件(Rf"{工程目录()}\蓝图库\临时\输出蓝图1.json")
保存蓝图(本蓝图).为蓝图txt文件(Rf"{工程目录()}\蓝图库\临时\输出蓝图1.txt")
保存所有建筑(本蓝图).为json文件(Rf"{工程目录()}\蓝图库\临时\输出所有建筑1.json")

本蓝图 = 读取泛蓝图文件(Rf"{工程目录()}\蓝图库\临时\输入蓝图.json")
保存蓝图(本蓝图).为json文件(Rf"{工程目录()}\蓝图库\临时\输出蓝图2.json")
保存蓝图(本蓝图).为蓝图txt文件(Rf"{工程目录()}\蓝图库\临时\输出蓝图2.txt")
保存所有建筑(本蓝图).为json文件(Rf"{工程目录()}\蓝图库\临时\输出所有建筑2.json")
