"""修复py文件以num.xxx.py命名的bug
	将第一个.改为_
"""

import os
# 修改当前目录下的py文件
path = './'

# 获取该目录下所有文件，存入列表中
f = os.listdir(path)

for i in f:
	if i.startswith('0') or i.startswith('1') or i.startswith('2'):
		if i.endswith('.py'):
			index, name = i.split('.', maxsplit=1)
			# 设置旧文件名（就是路径+文件名）
			old_name = i

			# 设置新文件名
			new_name = index + '_' + name

			# 用os模块中的rename方法对文件改名
			os.rename(old_name, new_name)
			print(old_name, '======>', new_name)
