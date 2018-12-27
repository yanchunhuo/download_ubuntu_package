# -*-coding:utf-8
import argparse
import sys
import subprocess
import os

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--packagename', help='要下载的包名', type=str)
    args = parser.parse_args()
    packagename=args.packagename
    if not packagename:
        sys.exit('请指定--packagename参数,帮助python ubuntu_downlaod_package.py --help')
    if not os.path.exists('./download'):
        os.makedirs('./download')
    # 获得依赖包
    depend_packages_info=subprocess.check_output("apt-cache depends "+packagename+"|grep Depends|awk -F ':' '{print $2}'"
                                                 ,shell=True).strip()
    depend_packages=depend_packages_info.split('\n')
    # 下载包及依赖包到download目录
    download_packages=depend_packages
    download_packages.append(packagename)
    for package in download_packages:
        retuslt=subprocess.check_output('apt-get install '+package+' --reinstall -d -y -o Dir::Cache::Archives=./download',shell=True)
        print retuslt
