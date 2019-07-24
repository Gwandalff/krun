#!/usr/bin/env bash

#export NO_MSRS=1
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/
export BENCH_OPTS="" #--no-tickless-check 

git clean -fxd
sudo apt install -y virt-what python-cffi build-essential cpufrequtils cpuset linux-headers-4.9.0-9-all util-linux msr-tools policykit-1 openjdk-8-jdk pypy-dev luajit
make JAVA_CPPFLAGS='"-I${JAVA_HOME}/include -I${JAVA_HOME}/include/linux"' JAVA_LDFLAGS=-L${JAVA_HOME}/lib ENABLE_JAVA=1
python create_krunEntry.py
../krun.py benchmarks.krun $BENCH_OPTS

