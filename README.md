---
title: 分布式子域名扫描轮子（demo）
date:  2020-5-6
tags: [Python]
grammar_cjkRuby: true
status: public
author: Guoker
---


Github：[domain_scan_demo](https://github.com/GuoKerS/domain_scan_demo)
# 前言
这是之前的一个很简陋的分布式子域名扫描的轮子，为了尝试分布式以及docker的使用（后来再了解到了celery这样的任务调度神器，也用celery写了一个），这里程序是以mysql作为broker和backend，然后调用 [oneforall](https://github.com/shmilylty/OneForAll)进行子域名扫描，并且做成了docker方便自己在其他vps上开箱即用。

# 说明

```shell
docker-compose up -d . # 启动镜像（不含mysql）


- mysql起一个就够了，可以自行用docker起（SRC_Scan.sql为数据库结构）
- 记得修改Mysql数据库配置信息 __config__.py
- 记得修改oneforall用到的api信息 lib\oneforall\api.py

```
domains表中的domain为待进行扫描的域名（其他字段可以留空）

subdomains表为子域名结果
```sql
SELECT * FROM subdomains WHERE `status` IS NOT NULL AND title IS NOT NULL LIMIT 500

过滤掉了状态码和title为空的结果
```

![结果](https://photo.o0o0.club/_分布式子域名扫描轮子（demo）/1588756110496.png)

![数量](https://photo.o0o0.club/_分布式子域名扫描轮子（demo）/1588756452969.png)

# 运行的流程图

![](https://photo.o0o0.club/_分布式子域名扫描轮子（demo）/1588753552438.png)