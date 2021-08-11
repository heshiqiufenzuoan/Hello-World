# html-day01

## 第一章  开发前准备 

**1.www(world wide web)**
		万维网，是基于Internet的信息服务系统，官方定义为"WWW is a wide-area hypermedia information retrieval initiative aiming to give universal access to a large universe of documents",简而言之，WWW是一个以Internet为基础的计算机网络，它允许用户在一台计算机上通过Internet访问另一台计算机上的信息。从技术上讲，万维网是Internet上那些支持WWW协议和超文本传送协议的客户机与服务器的集合，通过它可以访问世界各地的超文本文件，包括文字，图形，声音，动画，资料库以及各种内容。

**2.Internet**

是由计算机连接起来的物理网络，它们依靠标准和固定的规则进行通信。

**3.W3C**

万维网联盟，创建于1994年，是Web技术领域最具权威和影响力的国际中立性技术标准机构。到目前为止，W3C已发布了200多项影响深远的Web技术标准及实施指南，如广为业界采用的超文本标记语言（标准通用标记语言下的一个应用）、可扩展标记语言（标准通用标记语言下的一个子集）

**4.IP**

IP地址是指互联网协议地址（英语：Internet Protocol Address，又译为网际协议地址），是IP Address的缩写。IP地址是IP协议提供的一种统一的地址格式，它为互联网上的每一个网络和每一台主机分配一个逻辑地址。例如：192.168.189.1

DHCP:自动分配IP地址

**5.域名**

IP地址是Internet主机的作为路由寻址用的数字型标识，人不容易记忆。因而产生了域名（domain name）这一种字符型标识。
		

> com:商业组织公司
> edu:教研机构
> gov:政府部门
> net:网络服务商
> org:非盈利组织
> cn:中国
> jp:日本
> uk:英国

​		



**6.网站(B/S架构项目)**
		是构成web的基础，指在万维网上根据一定的规则，使用html,css,java等语言制作的用于展示特定内容的相关网页的集合。

**7.网页**
	是网站中的一个页面，是构成网站的基础，网页是纯文本文件，但是具有一定的格式，也就是HTML语言定义的格式，由于HTML被翻译为超文本标记语言，因此网页也被称为超文本文件，用于展示文本，图片，影音等内容。

**8.互联网产业分类**
			行业服务类：

- 新闻资讯（网易）

- 信息搜索（百度，Google）

- 邮箱	（163）

- 购票类	（12306）

  

  商务应用类：

- 电子商务	（天猫，京东）

- 人才招聘	（赶集网，智联招聘）

- 网络教育	（极客学院）

- 第三方支付	（支付宝）

  

  其他类
  	由于"互联网+"概念的提出，互联网将渗入到医疗，教育，农业等传统行业



**网站制作流程**

前后端分离框架

目前，企业级web开发多采用前后台分离开发模式，这种模式要求前端开发者专注于前端开发，后端开发者专注于后端开发，各自完成自己擅长的任务模块。



需求分析->原型图（Axure）
			|
		前端设计->效果图（psd） 美工
			|
		前端开发->静态页面（html）
			|
		后台开发->接口服务（python）
			|
		部署运行（将网站部署到服务器上）



**网站的访问方式**

通过浏览器来读取网页的内容，浏览器可以将信息的格式进行处理，将内容以一定的方式呈现到屏幕上。我们可以通过URL地址进行网站的访问

每个网页在Internet中都有一个唯一的URL地址，URL是Internet上用来指定一个位置或一个网页的标准方式，URL的语法格式如下：

​		协议名称://主机名称[:端口号/存放目录/文件名称]

​		协议名称：浏览器默认协议为http协议

​				主机名称：网站所在的主机地址

​				端口号：  主机上存放该网站的服务器软件	

​				存放目录：要访问网页的存放目录

​				文件名称：要访问的网页的名称



## 第二章  基础知识

### html概念

超文本标记语言，是一种解释执行的文本类标记语言，是Internet上用于编写网页的主要语言。“超文本”就是指页面内可以包含图片、链接，甚至音乐、程序等非文字元素。

html也是一种规范，一种标准，它通过标记符号来标记要显示的网页中的各个部分。网页文件本身是一种文本文件，通过在文本文件中添加标记符，可以告诉浏览器如何显示其中的内容（如：文字如何处理，画面如何安排，图片如何显示等）。浏览器按顺序阅读网页文件，然后根据标记符解释和显示其标记的内容，对书写出错的标记将不指出其错误，且不停止其解释执行过程，编制者只能通过显示效果来分析出错原因和出错部位。

**简单的HTML结构**

```html
<!DOCTYPE html>
<!--规定了主要语言，这里的en为英语-->
<html lang="en">
<head>
    <!-- meta单标签 代表元信息 -->
  	<!-- 设置文档的文字编码格式 -->
    <meta charset="UTF-8">
    <!--指定网站的文件兼容性模式，判断一个网页该使用的文件模式，这里的内容是使用IE=edge来指示IE8使用它支持的最高模式-->
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <!-- 定宽同设备宽度，不可进行缩放-->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- 浏览器选项卡上的名字 -->
    <title>Document</title>
</head>
<body>
   
</body>
</html>

```



### html发展历程

| 版本        | 年份      |                                                              |
| ----------- | --------- | ------------------------------------------------------------ |
| HTML1.0~2.0 | 1989~1991 | 概念不明确                                                   |
| HTML3       | 1995      | 浏览器战争年代，Netscape和Microsoft都在试图争霸世界          |
| HTML4       | 1998      | 浏览器大战结束，万维网协会(W3C)解救我们，他们的计划是创建一个唯一的HTML标准。计划的关键是将HTML的结构和表现分解为两种语言，一种语言用于实现结构（HTML）一种语言用于表现（CSS）. |
| HTML4.01    | 1999      | 这段日子过得很惬意，HTML4.01在1999年闪亮登场，称为接下来十年中HTML"必备"版本 |
| XHTML1.0    | 2001      | 正当我们感觉安逸的时候一个新兴事物引起所有人注意，即XML。它让HTML开始心烦意乱，最终两者结合，XHTML1.0诞生。XHTML承诺，由于它的严格，再加上它提供的一些新方法，只要遵循这个标准，WEB的所有争端将就此平息。但是，大多数人都很讨厌XHTML，Web开发人员对HTML的灵活性更感兴趣，而不是XHTML的严格性。 |
| HTML5       | 2008      | 由于没有得到大家的祝福，这场婚姻的结局并不好，很快被HTML的新版本取代，即HTML5.它支持HTML4.01标准的大部分特性，还提供一些新特性。基于一些新特性，如支持类似博客的元素，新的视频和图形功能，以及一大堆用来构建web应用的功能，HTML5注定成为大家公认的标准。 |

​	

### 基本语法

**1）特性**

- 可以使用.html与.htm作为html文件的后缀名（扩展名）
- 可以使用任意文本编辑器创建HTML
  - 记事本：特点：无代码提示、无代码高亮显示、用户界面不友好；
  - sublime（推荐）：特点：运行速度快、代码提示、高亮显示、插件拓展、html 插件emmet
  - sublime text3 安装emmet插件；
  - vscode（推荐）：特点：开发方便，插件完善；
  - Idea：特点：集成开发工具、类似DW,node,npm...运行速度较慢；
- windows操作系统  
  - 文件名.扩展名
- linux操作系统
  - 文件名

**2）注释**
		<!-- 注释内容 -->

**3）基本概念**

标签：

​		标签用来标记内容，也是用标签表名文本的意义。标签使用"<",">"包围。标签分为成对标签和单标签

元素：
				一个元素通常是由一个开始标签，内容，其他元素以及一个结束标签组成的
		属性：
				与元素相关的特性称为属性，属性由键值对组成。
				<元素名 属性1=值1 属性2=值2></元素名>
				coreattrs属性		大多数元素都可以使用的属性。
				id     	唯一标识
				class	标识一类元素
				style	样式
				title	描述信息
		规范：
				元素名和属性都不区分大小写。

**4）文档结构**
		HTML文档（ HTML document）

DOCTYPE

在Html非常年轻的时候（1991、2年左右），doctype是用来作为一组规则的链接，HTML页面必须遵循这些规则才能被认为是好的HTML，这些规则会用来检测网页是不是存在问题。然而，这些年没有人真正的关心doctype，他们只是一个历史产物必须包含在页面中。

**HTML4**

```html
<!--严格的文档类型-->
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"  "http://www.w3.org/TR/html4/strict.dtd">
```

```html
<!--宽松的文档类型-->
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"  "http://www.w3.org/TR/html4/loose.dtd">
```

**HTML5**

```html
<!DOCTYPE html>
```

**html**:标识HTML文档

**head**:标识HTML文档的头部，可以包含该文档的标题，文档使用的脚本，样式定义，元数据等信息

**body**：标识HTML文档的体部，body中的内容可以显示到浏览器中。

**5）meta元素**

元数据不会显示在客户端，但是会被浏览器解析。通常用于指定网页的描述，关键词，文件的最后修改时间，作者及其他元数据。

元数据可以被使用浏览器（如何显示内容或重新加载页面），搜索引擎（关键词），或其他 Web 服务调用。

定义文档元数据

```html
<!--定义元数据关键字-->
<meta name="Author" content="haona">
<meta name="Copyright" content="版权信息">
<meta name="Description" content="描述信息">
<meta name="keywords" lang="zh-cn" content="精品图书">
<meta name="keywords" lang="en-us" content="good book">
```

**6） 颜色与大小**

1）颜色
			颜色由红(R)、绿(G)、蓝(B)组成，每个颜色的最低值为0(十六进制为00)，最高值为255(十六进制为FF)。十六进制值的写法为#号后跟三个或六个十六进制字符。

3位十六进制	6位16进制			rgb 							颜色

000					#000000			 rgb(0,0,0)					黑色	black

F00 					#FF0000 			rgb(255,0,0)				红色	red

FFF 					#FFFFFF 			 rgb(255,255,255)		白色	white

2）大小

​		px 像素	



### 标签介绍

#### 块级(block)标签

```html
<div><div>
```

特点：

- 独占一行

* 默认宽度为100%
* 高度由子元素或内容决定
* 可以通过css指定其宽度

```
h1~h6 标题
```

特点:
					1)有字体大小的设置
					2)文本有加粗强调设置
					3)上下文之间有较大间距

**p** :段落

特点：
					1)独占一行
					2)上下文之间具有距离

**ul li**: 列表
				特点：
					1) 配合使用
					2) ul li都独占一行空间
					3) ul 上下文之间有很大空间
					4) li与列表的样式显示(默认点状)，并且由文本缩进				

```html
<ul>
	<li>列表1</li>
	<li>列表2</li>
</ul>
```

**dl dt dd（definition list）**

特点：
					1)dl dt dd独占一行空间
					2)dl上下文之间有很大欧诺关键
					3)dd有文本缩进

```html
<dl>
	<dt>列表标题</dt>
	<dd>列表内容</dd>
	<dd>列表内容</dd>
	<dd>列表内容</dd>
</dl>
```

**ol li**：有序列表

```html
<ol>
	<li>列表1</li>
	<li>列表2</li>
	<li>列表3</li>
	<li>列表4</li>
</ol>
```



#### 行内（内联inline）标签

**span**
				特点：
					1)最干净的内联标签（没有任何修饰）
					2)不独占一行

**a**:超链接
				从一个web资源到另外一个web资源的连接
				特点:
					1)不独占一行
					2)点击可以发生跳转（或进行对应操作）
					3)文本具有颜色，具有下划线，指向后光标为手型，有状态的色彩提示

​		绝对路径：
​						每个网页都有一个唯一的地址，称为URI 统一资源定位符，也称为该网页的绝对路径。
​						http://ip:port/目录/文件名
​				相对路径：
​						相对于当前文档所在的路径
​						../imgs/a.jpg
​						./imgs/a.jpg
​						imgs/a.jpg
​				本地连接
​						file:///d:/html/index.html
​						超链接中不允许写本地连接
​				服务器路径
​						http://localhost:8888/test/index.html

> 连接状态：
> 			未被访问的链接带有下划线且颜色是蓝色
>
> ​	已被访问的链接带有下划线且颜色是紫色
>
> ​	活动链接带有下划线且颜色是红色

| 属性   | 意义                                                     | 选项                                                         |
| ------ | -------------------------------------------------------- | ------------------------------------------------------------ |
| href   | 定义连接的目标URL                                        | 绝对路径：http://www.baidu.com<br/>相对路径：b.html<br/>邮件地址：mailto:licy@briup.com<br/>锚点	：#mao<br/>空连接	：javascript:void(0); |
| target | 定义连接的目标窗口                                       | _blank：新窗口打开。<br/>_parent：在父窗口中打开链接。<br/>_selff：默认，当前页面跳转。<br/>_top：在当前窗体打开链接，并替换当前的整个窗体(框架页)。 |
| title  | 定义连接的提示信息                                       |                                                              |
| type   | 连接到任何类型的文件以供下载。仅在 href 属性存在时使用。 |                                                              |



**锚点**：
				锚点可以让用户在文档中设置标记，这些标记通常放在文档的特定主题处或顶部，然后创建到这些锚点的连接，指向网页中的特点位置。



**link	文档关系连接**
			只能出现在head标签中，定义了当前文档和另一个资源之间的联系。
			通常用于链接到外部样式表
			`<link rel="stylesheet" href="style.css" type="text/css">`
			属性：
				href：	定义关系链接地址
				rel:	定义当前文档与所连接文档之间的关系。
				type: 	文档类型



**base	基准链接地址**
			设置页面中所有文档相对路径相对的基准URI。如果设定了基准链接地址，当前页面中的所有相对路径都基于该路径

`<base href="http://localhost:8888/sg">`



**decoration**:文本修饰标签

```html
<u>下划线修饰</u>
<i>斜体修饰</i>
<b>加粗</b>
<em>强调</em>
<strong>加粗</strong>
<s>删除线</s>
<sup>上标</sup>
<sub>下标</sub>
```

**图片**

图片类型：适合在网站上进行快速查看的图片格式

GIF		（graphics interchange format,图形交换格式）

可以将背景设置为透明的，图片最多使用256中颜色，最适合显示色调不连续或具有大面积单一颜色的图片，如导航条，按钮，图标等。由于GIF图片中存储的颜色信息较少，因此占用空间极小，使用起来更方便。

JPEG（joint photographic experts group,联合图像专家组）

最适合摄影或连续色调图像的彩色照片，jpeg文件可以包含数百万中颜色，保证图片不失真。JPEG图片无法拥有透明的背景

PNG（portable network graphics,可移植网络图形）

PNG可以包含256种以上的颜色，并可以具有透明的背景。PNG文件可保留所有原始层，矢量，灰度，颜色和效果信息，并且在任何时候所有元素都是可以编辑的。



链入图片文字
				`<img src="" alt="">`

属性：

- src		: 图片的源地址

- title	: 对图片的文字说明，当用户把鼠标放在图片上稍作停留，alt属性的值就会以浮动的形式显示出来。

- width	: 图片的宽度

- height	: 图片的高度

- alt		: 当图片文件找不到的时候显示的文本信息	

- border	：图片的边框

- align	：图片和文字的对齐

- hspace	：图片的水平间距

  - 当align值为left时，图片靠在最左方，周围的文字显示在右侧上方
  - 当align值为right时，图片靠在最右方，周围的文字显示在左侧上方
  - 当align值为top时，图片靠在最上方，周围的文字显示在上方
  - 当align值为bottom时，图片靠在最上方，周围的文字显示在下方

- vspace	：图片的垂直间距

  

  为图片添加链接
  		<img src="" alt=""></a>

#### **表格**

1）table

| 标签       | 描述                 |
| :--------- | :------------------- |
| <table>    | 定义表格             |
| <th>       | 定义表格的表头       |
| <tr>       | 定义表格的行         |
| <td>       | 定义表格单元         |
| <caption>  | 定义表格标题         |
| <colgroup> | 定义表格列的组       |
| <col>      | 定义用于表格列的属性 |
| <thead>    | 定义表格的页眉       |
| <tbody>    | 定义表格的主体       |
| <tfoot>    | 定义表格的页脚       |

**属性**

| 属性        | 值                                                           | 描述                             |
| ----------- | ------------------------------------------------------------ | -------------------------------- |
| border      | 1                                                            | 规定表格单元是否拥有边框。       |
| width       |                                                              | 规定表格的宽度。                 |
| align       | left<br/>center<br/>right                                    | 规定表格相对周围元素的对齐方式。 |
| cellpadding |                                                              | 规定单元边沿与其内容之间的空白。 |
| cellspacing |                                                              | 规定单元格之间的空白。           |
| frame       | void：不显示边框<br/>above：上边框<br/>below：下边框<br/>hsides：上下边框<br/>lhs：左边框<br/>rhs：右边框<br/>vsides：左右边框<br/>box：四个边框<br/>border：四个边框 | 规定外侧边框的哪个部分是可见的。 |
| rules       | none：无分割线显示<br/> groups：仅在列分组间和行分组间显示分割线<br/> rows：仅在行间显示分割线<br/> cols：仅在列间显示分割线<br/> all：在所有行列间显示分割线 | 规定内侧边框的哪个部分是可见的。 |

[^1]: 注意：当学习完CSS就不要使用这些属性了

## 表单

主要用于收集来自用户的信息，并将收集的信息发送给服务器端处理程序处理。表单时客户端和服务器端传递数据的桥梁，是实现用于与服务器互动的最主要方式。

**form**

`<form></form>`

| 属性           | 值                                                           | 描述                                                         |
| -------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| action         |                                                              | 设定处理表单数据URI的地址                                    |
| method         | get<br/>post                                                 | 设定数据传送到服务器的方式<br/>get	将输入的数据追加到action地址后面<br/>post将输入的数据保存到HTTP协议的报文中 |
| name           |                                                              | 设定表单的名称，这个名称将与控件的当前值形参"名称/值"对 一同随表单提交 |
| enctype        | 1.application/x-www-form-urlencoded	在发送前编码所有字符（默认）<br/>2.multipart/form-data:不对字符编码。在使用包含文件上传控件的表单时，必须使用该值。<br />3.text/plain:空格转换为 "+" 加号，但不对特殊字符编码。 | 设定表单数据的内容类型                                       |
| accept-charset |                                                              | 设置服务器端可以处理的字符编码                               |

**enctype**

1.application/x-www-form-urlencoded	在发送前编码所有字符（默认）

编码方式：

​		1）控件的名称和值都被转义，空白字符使用【+】替换，保留的字符一般都是用来实现特定的目的，例如（: / ? ; @ = & 等）。非数字和字母的字符使用%HH（这里HH表示两个十六进制数字，代表该字符的ASCII码）进行转换

​		2）控件的"名称/值"对按照它们在文档数据流中出现的顺序列出来。"名称""值"使用"="分割，两个"名称/值"之间使用&隔开。

2.multipart/form-data		不对字符编码。在使用包含文件上传控件的表单时，必须使用该值。

​		1)数据分成多个部分，每个部分代表一个结构良好的控件，作为文档数据流的一部分，每一个部分都按照它们在文档数据流中出现的顺序依次发送到服务器端，并且，每一部分的边界不会出现在数据中。每一部分有一个content-desposition标题头，它的值的格式是：

Content-Disposition:form-data;name="myControl"

3.text/plain				空格转换为 "+" 加号，但不对特殊字符编码。



**input	基本表单控件**

<input type="text">

​		type				控件类型
​				text				单行文本框
​				textarea		多行文本框
​				password	  密码框
​				checkbox	   复选框
​				radio			  单选按钮
​				submit		   提交按钮
​				reset			  重置按钮
​				file				  文件
​				hidden		   隐藏域
​				image			图像按钮
​				button		   普通按钮



| 名称      | 描述                                                         |
| --------- | ------------------------------------------------------------ |
| name      | 控件名称，这个名称将与控件的当前值形参"名称/值"对 一同随表单提交 |
| value     | 用于设定初始化，可选。                                       |
| checked   | 单选框，复选框默认选中属性                                   |
| size      | 当前控件的初始宽度，这个宽度以像素为单位。除非控件类型是text,password，这时宽度是整数值，表示字符的数目 |
| maxlength | 指定可以输入的字符的最大值。适用于控件类型为text,password。  |



**button按钮控件**

<button></button>

| 名称  | 值                                                           | 描述       |
| ----- | ------------------------------------------------------------ | ---------- |
| name  |                                                              | 控件名称   |
| value |                                                              | 控件初始值 |
| type  | button	普通按钮<br/>submit	提交按钮<br/>reset	重置按钮 | 控件类型   |

图片按钮
					`<button><img src="" alt=""></button>	`	



**select：下拉列表或列表**			

```html
<select name="" id="">
	<option value=""></option>
	<option value=""></option>
</select>
```

​	

| 名称     | 描述                                                         |
| -------- | ------------------------------------------------------------ |
| name     | 控件名称                                                     |
| size     | 列表框中行的显示数量                                         |
| multiple | 是否允许多选<br>如果select元素不包含属性size和属性multiple时，表单类型显示为菜单（组合框）<br/>如果使用了属性size和属性multiple中的任意一个，则表单类型显示为列表框 |
| selected | 默认选中                                                     |
| option   | 下拉列表选项                                                 |
| value    | 定义控件的初始值。提交表单时，初始值会被提交给服务器。       |

**optgroup：分组选项**

```html
<select name="" id="">
    <optgroup label="大洋">
        <option value="">太平洋</option>
		<option value="">大西洋</option>
		<option value="">印度洋</option>
	</optgroup>
	<optgroup label="大海">
		 <option value="">东海</option>
		 <option value="">南海</option>
		 <option value="">渤海</option>
	</optgroup>
</select>
```

**textarea：多行文本框**  

| 名称 | 值                                                           | 描述           |
| ---- | ------------------------------------------------------------ | -------------- |
| name |                                                              | 控件名称       |
| rows |                                                              | 定义文本框行数 |
| cols |                                                              | 定义文本框列数 |
| warp | off	不自动换行<br/>hard自动硬回车换行，换行元素一同被传送到服务器中<br/>soft自动软回车换行，换行元素不会传到服务器中 | 是否自动换行   |



**label：为表单控件定义标签**		

一些表单控件内建有标签，当内建有标签时，一般使用value属性的值作为标签，而另外一些表单控件没有标签，则直接使用文本作为标签来说明控件的意义。每个label元素都要和表单控件关联到一起

```html
<table>
    <tr>
        <td><label for="username">用户名：</label></td>
        <td><input type="text" id="username" name="username"></td>
	</tr>
	<tr>
		<td><label for="passwold">密码：</label></td>
		<td><input type="password" id="password" name="password"></td>
	</tr>
</table>
```



**fieldset：为表单添加结构**

一般与legend元素配合使用，fieldset元素可以包含其他的表单控件，在这些表单控件周围画一个方框，而legend元素可以显示一个标签说明被包含的这些表单控件。



**其他控件特性**

disabled	禁用

支持该属性的控件：button,input,optgroup,option,select,textarea

​		1）禁止的元素不接受焦点

​		2）禁止的控件的值不与表单一起被提交

readonly	只读

支持该属性的控件：input,textarea

​		1）可以接受焦点，但是不能被用户修改

​		2）只读元素的值可以与表单一起被提交。			



## CSS简介

CSS(cascading style sheet，层叠样式表)是描述文档怎么样被呈现的语言，使用CSS可以对HTML文档进行描述。

**语法：**

1)CSS属性和值之间用冒号分隔

2)CSS属性之间用分号分隔（建议每个属性后都书写分号）

3)CSS的值有多个的时候使用空格分隔	

### CSS在网页中的使用

1）内嵌式 style="css" 

每个HTML元素都包含有一个style属性，使用该属性可以直接指定样式

存在问题：

- 1.不方便修改
- 2.结构与显示不能很好的分离
- 3.建议在测试或个别情况下使用

2）嵌入式

CSS样式定义内容位于style元素之间，其type属性必须被定义为text/css

```html
<head>
    <style type="text/css"></style>
</head>
```



3）外部引用式

可以在多个文档间共享样式表，提高效率；可以改变样式表而无须改变HTML文档。

```html
<head>
    <link rel="stylesheet" href="">
    <style type="text/css">
        @import "style.css";
        @import url("style.css");
	</style>
</head>
```

​		

## 表单

主要用于收集来自用户的信息，并将收集的信息发送给服务器端处理程序处理。表单时客户端和服务器端传递数据的桥梁，是实现用于与服务器互动的最主要方式。

**form**

`<form></form>`

| 属性           | 值                                                           | 描述                                                         |
| -------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| action         |                                                              | 设定处理表单数据URI的地址                                    |
| method         | get<br/>post                                                 | 设定数据传送到服务器的方式<br/>get	将输入的数据追加到action地址后面<br/>post将输入的数据保存到HTTP协议的报文中 |
| name           |                                                              | 设定表单的名称，这个名称将与控件的当前值形参"名称/值"对 一同随表单提交 |
| enctype        | 1.application/x-www-form-urlencoded	在发送前编码所有字符（默认）<br/>2.multipart/form-data:不对字符编码。在使用包含文件上传控件的表单时，必须使用该值。<br />3.text/plain:空格转换为 "+" 加号，但不对特殊字符编码。 | 设定表单数据的内容类型                                       |
| accept-charset |                                                              | 设置服务器端可以处理的字符编码                               |

**enctype**

1.application/x-www-form-urlencoded	在发送前编码所有字符（默认）

编码方式：

​		1）控件的名称和值都被转义，空白字符使用【+】替换，保留的字符一般都是用来实现特定的目的，例如（: / ? ; @ = & 等）。非数字和字母的字符使用%HH（这里HH表示两个十六进制数字，代表该字符的ASCII码）进行转换

​		2）控件的"名称/值"对按照它们在文档数据流中出现的顺序列出来。"名称""值"使用"="分割，两个"名称/值"之间使用&隔开。

2.multipart/form-data		不对字符编码。在使用包含文件上传控件的表单时，必须使用该值。

​		1)数据分成多个部分，每个部分代表一个结构良好的控件，作为文档数据流的一部分，每一个部分都按照它们在文档数据流中出现的顺序依次发送到服务器端，并且，每一部分的边界不会出现在数据中。每一部分有一个content-desposition标题头，它的值的格式是：

Content-Disposition:form-data;name="myControl"

3.text/plain				空格转换为 "+" 加号，但不对特殊字符编码。



**input	基本表单控件**

<input type="text">

​		type				控件类型
​				text				单行文本框
​				textarea		多行文本框
​				password	  密码框
​				checkbox	   复选框
​				radio			  单选按钮
​				submit		   提交按钮
​				reset			  重置按钮
​				file				  文件
​				hidden		   隐藏域
​				image			图像按钮
​				button		   普通按钮



| 名称      | 描述                                                         |
| --------- | ------------------------------------------------------------ |
| name      | 控件名称，这个名称将与控件的当前值形参"名称/值"对 一同随表单提交 |
| value     | 用于设定初始化，可选。                                       |
| checked   | 单选框，复选框默认选中属性                                   |
| size      | 当前控件的初始宽度，这个宽度以像素为单位。除非控件类型是text,password，这时宽度是整数值，表示字符的数目 |
| maxlength | 指定可以输入的字符的最大值。适用于控件类型为text,password。  |



**button按钮控件**

<button></button>

| 名称  | 值                                                           | 描述       |
| ----- | ------------------------------------------------------------ | ---------- |
| name  |                                                              | 控件名称   |
| value |                                                              | 控件初始值 |
| type  | button	普通按钮<br/>submit	提交按钮<br/>reset	重置按钮 | 控件类型   |

图片按钮
					`<button><img src="" alt=""></button>	`	



**select：下拉列表或列表**			

```html
<select name="" id="">
	<option value=""></option>
	<option value=""></option>
</select>
```

​	

| 名称     | 描述                                                         |
| -------- | ------------------------------------------------------------ |
| name     | 控件名称                                                     |
| size     | 列表框中行的显示数量                                         |
| multiple | 是否允许多选<br>如果select元素不包含属性size和属性multiple时，表单类型显示为菜单（组合框）<br/>如果使用了属性size和属性multiple中的任意一个，则表单类型显示为列表框 |
| selected | 默认选中                                                     |
| option   | 下拉列表选项                                                 |
| value    | 定义控件的初始值。提交表单时，初始值会被提交给服务器。       |

**optgroup：分组选项**

```html
<select name="" id="">
    <optgroup label="大洋">
        <option value="">太平洋</option>
		<option value="">大西洋</option>
		<option value="">印度洋</option>
	</optgroup>
	<optgroup label="大海">
		 <option value="">东海</option>
		 <option value="">南海</option>
		 <option value="">渤海</option>
	</optgroup>
</select>
```

**textarea：多行文本框**  

| 名称 | 值                                                           | 描述           |
| ---- | ------------------------------------------------------------ | -------------- |
| name |                                                              | 控件名称       |
| rows |                                                              | 定义文本框行数 |
| cols |                                                              | 定义文本框列数 |
| warp | off	不自动换行<br/>hard自动硬回车换行，换行元素一同被传送到服务器中<br/>soft自动软回车换行，换行元素不会传到服务器中 | 是否自动换行   |



**label：为表单控件定义标签**		

一些表单控件内建有标签，当内建有标签时，一般使用value属性的值作为标签，而另外一些表单控件没有标签，则直接使用文本作为标签来说明控件的意义。每个label元素都要和表单控件关联到一起

```html
<table>
    <tr>
        <td><label for="username">用户名：</label></td>
        <td><input type="text" id="username" name="username"></td>
	</tr>
	<tr>
		<td><label for="passwold">密码：</label></td>
		<td><input type="password" id="password" name="password"></td>
	</tr>
</table>
```



**fieldset：为表单添加结构**

一般与legend元素配合使用，fieldset元素可以包含其他的表单控件，在这些表单控件周围画一个方框，而legend元素可以显示一个标签说明被包含的这些表单控件。



**其他控件特性**

disabled	禁用

支持该属性的控件：button,input,optgroup,option,select,textarea

​		1）禁止的元素不接受焦点

​		2）禁止的控件的值不与表单一起被提交

readonly	只读

支持该属性的控件：input,textarea

​		1）可以接受焦点，但是不能被用户修改

​		2）只读元素的值可以与表单一起被提交。			



## CSS简介

CSS(cascading style sheet，层叠样式表)是描述文档怎么样被呈现的语言，使用CSS可以对HTML文档进行描述。

**语法：**

1)CSS属性和值之间用冒号分隔

2)CSS属性之间用分号分隔（建议每个属性后都书写分号）

3)CSS的值有多个的时候使用空格分隔	

### CSS在网页中的使用

1）内嵌式 style="css" 

每个HTML元素都包含有一个style属性，使用该属性可以直接指定样式

存在问题：

- 1.不方便修改
- 2.结构与显示不能很好的分离
- 3.建议在测试或个别情况下使用

2）嵌入式

CSS样式定义内容位于style元素之间，其type属性必须被定义为text/css

```html
<head>
    <style type="text/css"></style>
</head>
```



3）外部引用式

可以在多个文档间共享样式表，提高效率；可以改变样式表而无须改变HTML文档。

```html
<head>
    <link rel="stylesheet" href="">
    <style type="text/css">
        @import "style.css";
        @import url("style.css");
	</style>
</head>
```













《