# Ubnutu下安裝arm-none-eabi-gcc
https://www.codenong.com/cs109738462/

1. 下載安裝gcc-arm-none-eabi
https://launchpad.net/gcc-arm-embedded/+下載

打開網址後找到如下圖所示最新版本gcc-arm-none-eabi-5_4-2016q3-20160926-linux.tar.bz2 (md5)，然後點擊就可下載


2. 解壓gcc-arm-none-eabi
    1. 在home下新建tools文件夾，並將下載好的壓縮包放入tools文件夾備用


    ```
    $:cd ~
    $:mkdir 工具
    $:mv ./Download/gcc-arm-none-eabi-5_4-2016q3-20160926-linux.tar.bz2 ./tools
    ```
    2. 在/usr/local/中新建文件夾arm，並將壓縮包拷貝過來


    ```
    $:cd /usr/local/
    $:sudo mkdir arm
    $:cd arm
    $:sudo cp ~/tools/gcc-arm-none-eabi-5_4-2016q3-20160926-linux.tar.bz2 ./
    ```
    3. 在/usr/local/arm中解壓壓縮包

    ```
    $:sudo tar -vxf gcc-arm-none-eabi-5_4-2016q3-20160926-linux.tar.bz2
    ```
3. 解壓後刪除壓縮包，留下文件夾

```
$:sudo rm gcc-arm-none-eabi-5_4-2016q3-20160926-linux.tar.bz2
```
3. 添加環境變量和按照依賴包
如果不安裝所有依賴包執行arm-none-eabi-gcc時會顯示找不到文件或文件夾

    1. 添加環境變量
    ```$ sudo vim /etc/配置文件```
    在profile中最下面加入下面一行語句，具體的位置亦可由你自定義，但必須與你解壓到的文件夾路徑相匹配
    導出 PATH=$PATH:/usr/local/arm/gcc-arm-none-eabi-5_4-2016q3/bin

    2. 安裝倆依賴包
    ```
    $ sudo apt-get 安裝 lsb-core
    $ sudo apt-get 安裝 lib32ncurses5 lib32tinfo5 libc6-i386
    ```

    3. 重啟驗證
    不想重啟亦可執行以下任意一個命令

    ```
    . /etc/profile //.與/間必須有個空格
    source /etc/profile
    ```

查詢gcc版本號驗證
```$ arm-none-eabi-gcc -v```
如果出現以下界面表示成功
