@echo off
rem create project name
mkdir %1
rem enter project fold
cd %1

mkdir 1.采购申请及样机分析
mkdir 2.产品企划
mkdir 3.方案设计

rem enter 方案设计
cd 3.方案设计
mkdir 3.1.硬件设计
mkdir 3.2.软件设计
mkdir 3.3.电器设计
mkdir 3.4.结构设计
rem exit 方案设计 
cd ..

mkdir 4.样机文件
mkdir 5.试制
mkdir 6.试产
mkdir 7.工作计划
mkdir 8.参考文献
mkdir 9.报告汇总

rem exit %1
cd ..