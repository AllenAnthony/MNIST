# import tensorflow as tf
# hello = tf.constant('Hello, TensorFlow!')
# sess = tf.Session()
# print(sess.run(hello))
#
# a = tf.constant(10)
# b = tf.constant(32)
# print(sess.run(a+b))

# !/usr/bin/python
# -*- coding: UTF-8 -*-

# 打开一个文件
filename = __file__
filename=filename[0:-3]
filename+=".txt"

re = open(filename, "a+")
re.write("www.runoob.com!\nVery good site!\n%d\n"%(123))
re.close()

# 关闭打开的文件
