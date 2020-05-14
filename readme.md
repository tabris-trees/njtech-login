# 简介
这个是我无聊时候自己做的南京工业大学自动登录脚本，自己用的时候可以打包成exe文件

因为登陆时需要自己选择一个下拉菜单，所以使用request方法在我这种菜鸡看来实在是太难了，所以采用了简单的selenium无头浏览器进行自动化模拟登录。

# 依赖包
需要安装的python库：
- pywifi
- selenium 

其中selenium需要安装浏览器的driver，具体的教程可以[看这里](https://www.cnblogs.com/chenxiaohan/p/7654667.html#four)

你使用什么浏览器就用什么浏览器的driver，原文件中使用的是chrome浏览器，如果你换成其他浏览器需要在 xxx.py 文件中修改

```
browser = webdriver.Chrome() # 修改这里的Chrome，具体参见教程
```
# 使用
直接运行

简单实现了一下内容（自己写着玩的，所以很垃圾）：

- [x] 自动连接WiFi（可以在代码里面直接将相应的改为自己的内容，就不用每次输入）
- [x] 连接后自动登录校园网
- [ ] 更加轻便的cookie方法