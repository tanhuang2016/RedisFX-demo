@echo off
setlocal enabledelayedexpansion

:: 从标准输入读取数据
set /p inputData=

:: 将数据转换为字符串（实际上在批处理中默认就是字符串）
set resultString=%inputData%

:: 拼接上 "word"
set finalResult=%resultString%word

:: 通过标准输出返回结果
echo %finalResult%
