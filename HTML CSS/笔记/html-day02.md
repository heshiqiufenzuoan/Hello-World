# html-day02

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

其他样式的导入
			@import url(common.css);











