# Date A Live 视觉小说简体中文补丁使用说明

本补丁只对视觉小说中的文本部分进行简体化，视频及图片中的内容未进行改动。

视觉小说中的文本可分为两部分。

其中系统相关文本在database.bin中，可使用ScriptDatabaseEditor对其进行阅读和修改。

剧本相关文本在Script.pck中，可使用PCKTool将其解包得到一系列.bin文件，并使用STSCTool将其反编译为一系列便于阅读的文本文件。

这两个工具也可以将修改后的代码编译并打包回去。

也可以使用ScriptDialogueEditor对其进行有限的阅读及修改。

成品的补丁可在[Releases](https://github.com/Wanlau/dal_tc2sc/releases)处下载。

其中『DAL_RR_SC.zip』为凛绪轮回简体中文版的文件。

其中『DAL_RR_TC.zip』为凛绪轮回繁体中文版（即原版）的文件。

使用补丁时，用补丁里的文件替换视觉小说文件夹里的对应文件即可，反之亦然。

## 使用方法

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

## 备注

使用了由thesupersonic16制作的[DALTools](https://github.com/thesupersonic16/DALTools)。