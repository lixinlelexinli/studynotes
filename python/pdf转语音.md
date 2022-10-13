作者：朱卫军
链接：https://zhuanlan.zhihu.com/p/336643249
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



## **1. 转语音工具**

微信读书有一个功能，可以将书里的文字转换为音频，而且声音优化的不错，比传统的机械朗读听起来舒服很多。

记得之前看到过Python有一个工具包，可以将文字转换为语音，支持英文和中文，而且可以调节语速语调、导出mp3等。

去Github查了下，这个库叫：pyttsx3

![img](F:%5Cgithub%5Cgithubio%5Cstudynotes%5Cpython%5Cpdf%E8%BD%AC%E8%AF%AD%E9%9F%B3.assets%5Cv2-8aaedd842b291fe66f728e213b9f8fd1_b.jpg)

简单来说，pyttsx3可以文字转语音，而且是离线工作的，这一点就很实用。 

![img](F:%5Cgithub%5Cgithubio%5Cstudynotes%5Cpython%5Cpdf%E8%BD%AC%E8%AF%AD%E9%9F%B3.assets%5Cv2-7669efc6bf6ef7412bd26e51397381a1_b.jpg)



安装比较容易，直接在命令行用pip安装：

```python3
pip install pyttsx3
```

我准备动手试试，将PDF书籍转成音频。

用什么书呢？最近在群里看到有人发张磊的新作《价值》电子书，这本今年刚出的畅销书盗版猖獗，我之前在微信读书里看过，对作者长期主义的观点深信不疑。 

![img](F:%5Cgithub%5Cgithubio%5Cstudynotes%5Cpython%5Cpdf%E8%BD%AC%E8%AF%AD%E9%9F%B3.assets%5Cv2-83c75b991ec24c62a2461615b55505bc_b.jpg)



那就它了。

## **2. PDF转文本**

既然是把PDF转化成语音，肯定是需要先读取PDF中的文字，再利用pyttsx3转语音。

Python中操作PDF的工具库主要是PyPDF2，但发现编码实在有点繁琐，我就换了另一个库pdfplumber，与PyPDF2语法类似，用起来还算流畅。

pdfplumber可以处理PDF包括文本、表格、格式在内的各种信息，小而强大。

```python3
# 读取PDF文档
pdf = pdfplumber.open("价值.pdf")

# 获取页数
print("总页数：",len(pdf.pages))
print("-----------------------------------------")

# 读取第4页
first_page = pdf.pages[3]
print("本页：",first_page.page_number+1)
print("-----------------------------------------")

# 导出第4页文本
text = first_page.extract_text()
print(text)
```

输出： 

![img](F:%5Cgithub%5Cgithubio%5Cstudynotes%5Cpython%5Cpdf%E8%BD%AC%E8%AF%AD%E9%9F%B3.assets%5Cv2-e73000edcf6dda67382874fde2ad5c95_b.jpg)



上面的代码做了几件事情： **「读取PDF文档、读取页数、读取第4页、输出第4页文本」**

## **3. 文本转语音**

接下来开始将第4页的文本转化为音频。

```python3
import pyttsx3

# 初始化来获取语音引擎
engine = pyttsx3.init()

# 去掉文本中的换行符
text = text.replace('\n','')

# 朗读文本
engine.say(text)
engine.runAndWait()
```

上面代码使用pyttsx3将文本转化为音频，然后朗读出来。我是在jupyter notebook上做实验的，代码执行后，电脑会直接朗读。

也可以将生成的音频保存为mp3格式。

```python3
# 保存音频到本地，格式为mp3
engine.save_to_file(text, 'test.mp3')
engine.runAndWait()
```

当然你还可以调整声音的类型、速度、大小。

```python3
# 调整人声类型
voices = engine.getProperty('voices')  
engine.setProperty('voice', voices[0].id)

# 调整语速,范围一般在0~500之间
rate = engine.getProperty('rate')                         
engine.setProperty('rate', 200)     

# 调整声量，范围在0~1之间
volume = engine.getProperty('volume')                         
engine.setProperty('volume',0.8) 
```

最后听下生成的语音是什么样的？（已转成视频）