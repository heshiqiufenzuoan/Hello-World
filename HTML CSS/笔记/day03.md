# day03

## css基本语法

选择器{属性1: 值1;属性2: 值2;......}

### 选择器

选择器：用于选择html中的元素

1，html选择器（标签选择器）

即html标签，任何一个HTML元素的标签名都可以是css的选择器

```css
p{	
	text-indent:10px
}  /段落第一行缩进10像素/
h1{ 
	color:red
}
```

优先级：

​		默认情况下，子级通常先继承父级标签属性

​		如果子级和父级拥有相同的属性，子级优先，就近原则

​		类选择器的优先级高于标签选择器
​		2,类选择器

​		class属性

​		.类名(类名不能使用数字开头，不能使用关键字来命名) 

​		`.rr{ color :red}`

​		使用class属性来调用类名称

```css
<p class="rr">one</p>
<p class="rr">two</p>
<p class="rr">three</p>
```

3，ID选择器：id属性、id名

````css
two{background-color:green}

<p class="rr">one</p>
<p id="two" class="rr">two</p>
<p class="rr">three</p>
````

4，关联选择器
			     用一个空格隔开的两个或者多个单一选择器组成的字符串
			     它们的优先级比单一的选择器大。
			    ` table a{color:red}`
			       定义了table中的a样式，而多table外的a样式不做改变
		5，组合选择器
			     使用逗号,隔开选择器，可以减少样式表的重复声明
			    ` h1,h2,h3,h4{color:red}`
		6，伪元素选择器
			     是指对同一个HTML元素的不同状态的一种定义方式
			     HTML标签:伪元素{}
			   ` a:link{}	超链接没有任何动作前的状态`
			    `a:hover{}	光标移动到超链接上的状态`
			    `a:active{}	选中超链接时的状态`
			    `a:visited{}访问过超链接的状态`
				`text-decoration:none  去掉下划线`



**选择器优先级**

多个CSS选择器同时作用于同一个html时，声明不同的属性具有继承的关系，如果声明的是相同的属性，则以优先级高的为主。

​	内嵌式
​			> 关联选择器(后代，子代，组合(且)) 
​			> ID选择器 
​			> 类选择器
​			> HTML选择器

​	同级别的后者覆盖前者--------->就近原则	



**样式**

样式是零个或多个以分号分割的【属性名：属性值】列表

**规则集**

选择器 样式

选择器{属性名:属性值;属性名:属性值}

**注释**

/*
				注释内容
		*/

### 基本布局

**布局顺序**

​		由上至下，由左至右，由内至外

块居中

​		要居中的块必须小于父级元素

​		利用margin-left margin-right的自动值来居中

布局级别：

​		1）行布局级（横排）

​		2）列布局级（浮动布局）

​		1.设置浮动 float

​		任何元素都可以浮动，可以改变普通文档流的排列方式，可以使得块元素在同一行中排列，使我们的布局更加方便，浮动是脱离文档流的，也就是其他元素视而不见。

浮动何时停止？
   1. 当遇到一个浮动元素后
         当遇到父级元素后
         			多个盒子都浮动后，就产生了块级元素水平排列的效果
         			多个浮动元素不会相互覆盖
         			若包含的容器太窄，无法容纳水平排列的多个浮动元素，那么最后的浮动盒子会向下移动，但如果浮动元素的高度不同，那么它们向下移动时可能会被卡住。
         			float:
         			left 	元素浮动到容器的左侧。
         			right 	元素浮动到容器的右侧。
         			none 	默认值。元素不浮动，并会显示在其在文本中出现的位置。

         ​			inherit    元素继承其父级的float值

         ​	

         2. 清理浮动
           clear

           ​	left 	在左侧不允许浮动元素
           ​	right 	在右侧不允许浮动元素
           ​	both 	在左右两侧均不允许浮动元素
           ​	margin上下值在行布局时共用，浮动后不再共用
           ​	clear 清除浮动对象对当前对象的影响

           3.
           	1)假如某个div元素A是浮动的,如果A元素上一个元素也是浮动的,那么A元素会跟随在上一个元素的后边(如果一行放不下这两个元素,那么A元素会被挤到下一行);如果A元素上一个元素是标准流中的元素,那么A的相对位置不会改变,也就是说A的顶部总是和上一个元素的底部对齐.div的顺序是HTML中div的顺序决定的.
           		2)高度尽量给予子级,父级高度自动
           		3)子级浮动,父级未浮动,父级高度无法依赖子级,这时父级需要自己添加高度.(overflow:hidden)
           		4)margin上下值在行布局时共用，浮动后不再共用.



**CSS常见的样式属性和值 **

1）CSS 尺寸属性
 		height	设置元素高度。	
 		width	设置元素的宽度。
 		max-height	设置元素的最大高度。	
 		max-width	设置元素的最大宽度。	
 		min-height	设置元素的最小高度。	
 		min-width	设置元素的最小宽度。

2） 字体属性
	    	font-family字体族科
			宋体 SimSun	黑体 SimHei
			微软雅黑 Microsoft YaHei
			微软正黑体 Microsoft JhengHei
			新宋体 NSimSun
			新细明体 PMingLiU
			细明体 MingLiU
			标楷体 DFKai-SB
			仿宋 FangSong
			仿宋_GB2312 FangSong_GB2312
			楷体_GB2312 KaiTi_GB2312
 	   	font-size	字体大小
			font-style	字体风格
			normal	正常;italic  斜体;oblique  倾斜
			font-weight字体加粗
			normal  正常;bold  粗体;bolder 更粗;lighter  更细
			text-decoration 规定添加到文本的修饰 ：
			none 		默认。定义标准的文本。
			underline 	定义文本下的一条线。
			overline 	定义文本上的一条线。
			line-through定义穿过文本下的一条线。
			blink 		定义闪烁的文本。



3） 颜色
		color	设定文本的颜色
		opcity	设置透明度
		所有浏览器都支持 opacity 属性。
		注释：IE8 以及更早的版本支持替代的 filter 属性。
		例如：filter:Alpha(opacity=50)。
		一般两个属性一起写，保证兼容性
		opacity：0.5;
		filter:Alpha(opacity=50)





		4） 背景
		    设置元素的背景颜色。background-color:#CCC;
		    background-image	
		    	设置元素的背景图像。
				url(bgimage.gif);
		    background-repeat	
		    	设置是否及如何重复背景图像。
				repeat 	默认。背景图像将在垂直方向和水平方向重复。
				repeat-x 	背景图像将在水平方向重复。
				repeat-y 	背景图像将在垂直方向重复。
				no-repeat 	背景图像将仅显示一次。
				inherit 	规定应该从父元素继承 background-repeat 属性的设置。	
		    background-attachment
		    	设置背景图像是否固定或者随着页面的其余部分滚动。
				fixed	固定	
				scroll	滚动
		    background-position	
		    	设置背景图像的开始位置。这个属性设置背景原图像（由 background-image 定义）的位置，	背景图像如果要重复，将从这一点开始。您需要把 background-attachment属性设置为 "fixed"，才能保证该属性在 Firefox 和 Opera 中正常工作。
				  横向关键字： left center right
				  纵向关键字： top center bottom
				百分比：
				  左上角是 0% 0%。右下角是 100% 100%。
		    background 
		    	简写属性在一个声明中设置所有的背景属性。如果不设置其中的某个值，也不会出问题，比如 background:#ff0000 url('smiley.gif'); 也是允许的。
	
			图片精灵技术：
				也叫CSS背景图片精灵技术，是将多张背景图片放到一个图片中，通过定位的方式来获取响应位置的图片，使得一个图片一次载入，多次使用，使得页面下载速度加快
	
		5） 边框属性
		    border-style  设置4个边框的样式
				dotted 	定义点状边框。在大多数浏览器中呈现为实线。
				solid 	定义实线。
				double 	定义双线。
				none 	定义无边框
				...
				如果4个值都给定了，分别应用于上，右，下;
				左如果给定1个值，应用于各边;
				如果给定2个值，第一个值应用于上下边，第二个值应用于左右边
			border-width  设置4个边框的宽度
				值为关键字或者长度  medium,thin,thick
		    border-color  设置边框颜色
		    border  在一个声明设置所有的边框属性。
			border:1px solid #ff0000
		6） 鼠标光标属性
			cursor	属性规定要显示的光标的类型（形状）。
				none	无
				auto 	默认。浏览器设置的光标。
				pointer 光标呈现为指示链接的指针（一只手）
				wait 	此光标指示程序正忙（通常是一只表或沙漏）。
				help 	此光标指示可用的帮助（通常是一个问号或一个气球）。
		7） 列表属性
		    list-style 		在一个声明中设置所有的列表属性。 
			list-style: square inside url('/i/eg_arrow.gif')
		    list-style-image 	将图象设置为列表项标记。 
			list-style-image:url("/i/arrow.gif");
		    list-style-position 设置列表项标记的放置位置。
			inside 	列表项目标记放置在文本以内，且环绕文本根据标记对齐。
			outside 默认值。保持标记位于文本的左侧。列表项目标
				记放置在文本以外，且环绕文本不根据标记对齐。
		    list-style-type 	设置列表项标记的类型。
				none 	无标记。
				disc 	默认。标记是实心圆。
				circle 	标记是空心圆。
				square 	标记是实心方块。
				decimal 标记是数字。
				ower-roman	小写罗马数字(i, ii, iii, iv, v, 等。)
				upper-roman	大写罗马数字(I, II, III, IV, V, 等。)
				lower-alpha	小写英文字母The marker is lower-alpha (a, b, c, d, e, 等。)
				upper-alpha	大写英文字母The marker is upper-alpha (A, B, C, D, E, 等。)
				lower-latin	小写拉丁字母(a, b, c, d, e, 等。)
				upper-latin	大写拉丁字母(A, B, C, D, E, 等。)
		8）表格
			优先级：
				td,th-->tr-->tbody,thead,tfoot-->table
			color,font-size
			text-align	文字对齐
			background
			border 		边框，只能用于table,th,td
			margin 		间距，只能用于table,caption
			padding 	内间距，只能用于th,td
			width 		宽，只能用于table,td,th
			height 		高，只能用于table,td,th、可以用于tr并且优先级高于td
			border-collapse:
				separate 	默认值，分开
				collapse 	边框合并
				inherit		从父元素中继承该属性
			table-layout 宽度类型：
				fixed	固定宽度
				auto	自动宽度
			caption-side 标题位置：
				top/left/right/botton
	3. div+css
		div+css是一种网页的布局方法。
		标签div span无特殊含义，配合css才具有特殊的样式
		网页就是由许多个盒子通过不同的排列方式堆积而成，网页上每个元素都被浏览器看成是一个矩形的盒子，这个盒子由元素的内容，填充，边框，边界组成。默认盒子边框无，背景色透明，默认看不到盒子
		1） 盒子模型
		    margin  外边距，定义区块外边界与上级元素距离的属性，值为长度
		    padding 内边距（填充），是设置区块的内边距的属性，是边框和元素内容之间的间隔距离
		    border  边框，在一个声明设置所有的边框属性。
		    width   盒子的宽度
		    height  盒子的高度
		    内容	盒子里面所包含的元素和内容
	
		    属性值：
		    	1个：上下左右都是该值
		    	2个：前者表示上下的值，后者表示左右的值
		    	3个：前者表示上边的值，中间表示左右的值，后者表示下边的值
		    	4个：上右下左，顺时针排序
		2） 不同浏览器解析盒子模型的差异：
		    IE5盒子  width = 内容 + border + padding
		        盒子占据的宽度 = margin*2+width
				盒子占据的高度 = margin*2+height
		        盒子实际的宽度 = width
				盒子实际的高度 = height
	
		    W3C盒子 width = 内容
		        盒子占据的宽度 = margin*2+border*2+padding*2+width
				盒子占据的高度 = margin*2+border*2+padding*2+height
		        盒子实际的宽度 = border*2+padding*2+width
				盒子实际的高度 = border*2+padding*2+height
		3） 设置浏览器去遵循w3c标准
			只需要在网页的顶部加上DOCTYPE声明即可
		    !important的使用
		    p{
				color:red !important;
				color:blue;
		    }
		    当不加!important;的时候，后者覆盖前者，当加上之后说明第一个,样式优先级更高，采用前者，但是Ie6不支持!important;
		4）其他属性
			border-width	边框高度
			border-color	边框颜色
			border-style	边框样式
				none	无样式
				dotted	点线
				dashed	虚线
				solid	实线
				double	双线
				groove	槽线
				ridge	脊线
				inset	内凹
				outset	外凸
		5）关于填充和边框的常见问题
			1. 大部分的html元素的盒子属性（margin,padding）默认值为0，有少数html元素的（marigin，padding不为0）例如：body,p,ul,li,form等标签，有时需要将其先设置为0
			2. 相邻两个兄弟元素的外边框会发生合并，一般布局会设定他们的外边距
			3. 如果没有设置父级元素的内边距或边框，那么它的子元素的边界会和其合并。
			4. 设置一个块元素居中： marigin:0 auto;
			5. margin可以设置负值，padding不可以设置
			6. 行内元素的margin值，只有左右值，没有上下值
		6）行内元素与块级元素
			行内元素
				行内元素不可以设置宽（width）和高（height【但是可以通过line-height设置】），但可以与其他行内元素位于同一行，行内元素内一般不可以包含块级元素。行内元素的高度一般由元素内部的字体大小决定，宽度由内容的长度控制。常见的行内元素有:em,font,b,span,a,strong
			块级元素
				块状元素排斥其他元素与其位于同一行，可以设定元素的宽（width）和高（height），块级元素一般是其他元素的容器，可容纳块级元素和行内元素。常见的块级元素有div, p ,h1~h6等
	
				IE6/7及IE8混杂模式中，text- align:center可以使块级元素也居中对齐。其他浏览器中，text-align:center仅作用于行内内容上。
			改变元素类型：
				display
					可以将一个行级元素转换为块级元素，但是这种转换并不能改变元素本质，转换的只是CSS的盒子的外观
					需要转换盒子类型的情况：
					水平的列表菜单，不断行的标题，隐藏元素
					none 	隐藏元素。不会被显示，不占空间
					block	块级元素。独占一行空间
					inline  默认。此元素会被显示为内联元素，元素前后没有换行符。
					inline-block	兼有块级和行级元素特性，在行内显示但是可以设定宽高
	
					list-item 		此元素会作为列表显示。
	
					table 	此元素会作为块级表格来显示（类似 <table>），表格前后带有换行符。
					inline-table 	此元素会作为内联表格来显示（类似 <table>），表格前后没有换行符。
					table-row-group 	此元素会作为一个或多个行的分组来显示（类似 <tbody>）。
					table-header-group 	此元素会作为一个或多个行的分组来显示（类似 <thead>）。
					table-footer-group 	此元素会作为一个或多个行的分组来显示（类似 <tfoot>）。
					table-row 		此元素会作为一个表格行显示（类似 <tr>）。
					table-column 	此元素会作为一个单元格列显示（类似 <col>）
					table-cell 		此元素会作为一个表格单元格显示（类似 <td> 和 <th>）
					table-caption 	此元素会作为一个表格标题显示（类似 <caption>）
					inherit 		规定应该从父元素继承 display 属性的值。
				float,position
					应用了浮动和绝对定位的元素，变成了块级元素，因此display属性一般被忽略
				如果元素应用了display:none，该元素（以及子元素）被隐藏起来，对其再使用float,position将不再有意义		