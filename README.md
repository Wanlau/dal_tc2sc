# dal_tc2sc
A tool to change the Traditional Chinese text to Simple Chinese in Date A Live Visual Novel 

# Date A Live 视觉小说简体中文补丁

此为Date A Live（通称『约会大作战』）的衍生视觉小说的简体中文补丁。

成品的补丁可在右侧[Releases](https://github.com/Wanlau/dal_tc2sc/releases)处下载，使用方法见[使用说明](docs/usage.md)。

本仓库还有一些奇怪的小工具和一些可能有用的说明文档。

## DAL脚本部分语句说明

[DAL脚本部分语句说明](docs/dalcodes.md)

凛绪轮回中Script.pck解包后反编译所得的文本文件中的部分语句的说明。

使用steam上的PC版凛绪轮回测试总结而得，不一定完全准确，还请以实际情况为准。

## DALRR剧本文本繁体转简体脚本

[DALRR_tc2sc.py](https://github.com/Wanlau/dal_tc2sc/blob/main/DALRR_tc2sc.py)

用于处理Script.pck。

需要把它和编译好的[DALTools](https://github.com/thesupersonic16/DALTools)一同放在游戏主程序（DATE A LIVE RIO-REINCARNATION.exe）所在的位置。

需要先装好python3以及所需的库（如OpenCC等）。

不会对错误进行处理，需要手动确保路径、权限等没问题。

对于某些字体无简繁之分，但简体区与繁体区习惯用字不同的，OpenCC不会对其进行转换。（比如“看着”“听着”在繁体版里会写成“看著”“听著”。）

对于某些字，因所用字体无法显示，故额外对其进行转换。（如“妳”转“你”等）（可能不全）

## DALRD剧本文本繁体转简体脚本

[DALRD_tc2sc](https://github.com/Wanlau/dal_tc2sc/blob/main/DALRD_tc2sc.py)

需要配合[DALTools](https://github.com/thesupersonic16/DALTools)中的ScriptDialogueEditor的批量导入、导出功能使用。

能够自动识别导出的.tsv文件并将其中『翻译文本』部分转换为简体后生成新的.tsv文件。

需要先装好python3以及所需的库（如OpenCC等）。

不会对错误进行处理，需要手动确保路径、权限等没问题。

对于某些字体无简繁之分，但简体区与繁体区习惯用字不同的，OpenCC不会对其进行转换。（比如“看着”“听着”在繁体版里会写成“看著”“听著”。）

## DALRR语音-文字提取脚本

[DALRR_findVT.py](https://github.com/Wanlau/dal_tc2sc/blob/main/DALRR_findVT.py)

从Script.pck中提取『语音标识-文本』信息，可用于训练TTS模型。

需要把它和编译好的[DALTools](https://github.com/thesupersonic16/DALTools)一同放在游戏主程序（DATE A LIVE RIO-REINCARNATION.exe）所在的位置。

将会在所在位置生成一个.tsv文件。