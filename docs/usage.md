# Date A Live 视觉小说简体中文补丁使用说明

本补丁只对视觉小说中的文本部分进行简体化，视频及图片中的内容未进行改动。

视觉小说中的文本可分为两部分。

其中系统相关文本在database.bin中，可使用ScriptDatabaseEditor对其进行阅读和修改。

剧情相关文本在Script.pck中，可使用PCKTool将其解包得到一系列.bin文件，并使用STSCTool将其反编译为一系列便于阅读的文本文件。

这两个工具也可以将修改后的代码编译并打包回去。

也可以使用ScriptDialogueEditor对其进行有限的阅读及修改。

成品的补丁可在[Releases](https://github.com/Wanlau/dal_tc2sc/releases)处下载。

其中『DAL_RR_SC.zip』为凛绪轮回简体中文版的文件。

其中『DAL_RR_TC.zip』为凛绪轮回繁体中文版（即原版）的文件。

其中『DAL_RD_SC.zip』为莲反理想乡简体中文版的文件，此补丁尚未完成。

其中『DAL_RD_SC_TMP.zip』为莲反理想乡临时简体中文补丁的文件，可暂且先使用这个。

其中『DAL_RD_TC.zip』为莲反理想乡繁体中文版（即原版）的文件。

使用补丁时，用补丁里的文件替换视觉小说文件夹里的对应文件即可，反之亦然。

## 凛绪轮回简体中文补丁使用方法

补丁中有database.bin和Script.pck以及数个字体文件。

名字带『Font』的是字体文件，此处的字体文件是从大凉山那里拿过来的。

使用时需要找到凛绪轮回的安装路径，并在游戏处于关闭状态时进行以下操作。

用补丁目录里的『FontC0.pck』替换『Data/CHN/』目录里的同名文件。

用补丁目录里的『FontC1.pck』替换『Data/CHN/』目录里的同名文件。

用补丁目录里的『FontMsgC0.pck』替换『Data/CHN/』目录里的同名文件。

用补丁目录里的『FontMsgC1.pck』替换『Data/CHN/』目录里的同名文件。

用补丁里的『Script/』目录里的『Script.pck』替换『Data/CHN/Script/』目录里的同名文件。

用补丁里的『Script/』目录里的『database.bin』替换『Data/CHN/Script/』目录里的同名文件。

完成后启动游戏即可。请将游戏语言设置为中文。

## 莲反理想乡临时简体中文补丁使用说明

补丁中有数个魔改字体文件。

使用方法和凛绪轮回的补丁一样，用补丁里的文件替换视觉小说文件夹里的对应文件即可。

莲反理想乡需要在STEAM页面中把语言设置为中文，不然游戏文件里可能会没有『CHN』这个目录。

只修改了字体中的图像，并没有对文本进行修改，文本还是繁体的。

大概不会在文字上出啥大问题，因为汉字简化大多是一对一和多对一的，很少有一对多的情况。

可能出问题的是『乾』和『徵』，不过游戏里似乎并没有用于可能出问题的含义。

这只是一个临时方案，等字体的问题解决后还是建议使用正常版的简体中文补丁。

## 莲反理想乡简体中文补丁相关说明

补丁中有存储系统相关文本的数个.bin文件和存储剧情相关文本的Script.pck以及数个字体文件。

使用方法和凛绪轮回的补丁一样，用补丁里的文件替换视觉小说文件夹里的对应文件即可。

莲反理想乡需要在STEAM页面中把语言设置为中文，不然游戏文件里可能会没有『CHN』这个目录。

目前系统相关文本的简体化已经完成，剧情相关文本的对话部分的简体化已经完成。

使用FontEditor制作了简体中文字体文件，但新增的字符似乎无法被游戏识别。

在字体问题解决之前，可以暂时先使用临时简体中文补丁。

## 备注

使用了由thesupersonic16制作的[DALTools](https://github.com/thesupersonic16/DALTools)。