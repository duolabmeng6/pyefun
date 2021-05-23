from pyefun.javscript import *


js = javscript("JScript")
data = js.运行("1 + 2")
print(data, js.取运行环境())

js = javscript("Node")
data = js.运行("1 + 2")
print(data, js.取运行环境())

js = javscript("Node")
data = js.加载代码(""" 
function add(x, y) { 
  return x + y; 
} 
""")
data = js.执行("add", 1, 2)
print(data)
data = js.运行("add(1,2)")
print(data)

data = 运行js(""" 
function add(x, y) { 
  return x + y; 
} 
""", "add(1,2)")
print(data)

