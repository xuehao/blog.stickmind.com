Title: macOS 制作 Linux 系统启动盘
Slug: create-a-bootable-linux-usb-in-macos
Authors: xuehao
Date: 2019-12-29 20:24
Modified: 2019-12-29 20:24
Summary: 记录 macOS 命令行工具制作 Linux USB 启动盘的步骤
Description: 在 macOS 下制作 Linux 系统启动盘。记录了 macOS 命令行工具制作 Linux USB 启动盘的步骤。
Category: 备忘
Tags: Tools
Status: published

有一个老的笔记本，运行 Windows 比较吃力，所以测试一些 Linux 发行版，目的是找一个驱动管理好，运行流畅的系统。

以下记录 macOS 命令行工具制作 USB 启动盘的步骤：

## 1. 转换系统镜像格式

```bash
$ hdiutil convert -format UDRW -o linuxmint-19.1-cinnamon-64bit.dmg linuxmint-19.1-cinnamon-64bit.iso
created: /Users/xuehao/Downloads/linuxmint-19.1-cinnamon-64bit.dmg
```

## 2. 查看 U 盘编号

```bash
$ diskutil list
......
/dev/disk3 (external, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:     FDisk_partition_scheme                        *15.6 GB    disk3
   1:                       0xCD                         2.0 GB     disk3s1
   2:                       0xEF                         4.2 MB     disk3s2
```

## 3. 写入前先卸载 U 盘

```bash
$ diskutil umountDisk /dev/disk3
Unmount of all volumes on disk3 was successful
```

## 4. 将系统写入 U 盘

```bash
$ sudo dd bs=1m if=linuxmint-19.1-cinnamon-64bit.dmg of=/dev/rdisk3
Password:
```

此过程会持续数分钟，请耐心等待。
