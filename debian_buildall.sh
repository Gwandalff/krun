#!/usr/bin/env bash

export NO_MSRS=1
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/
export BENCH_OPTS=--no-tickless-check

git clean -fxd
sudo apt install -y virt-what python-cffi build-essential cpufrequtils cpuset linux-headers-$(uname -r) util-linux msr-tools policykit-1
#make
#make clean
ENABLE_JAVA=1 make 
cd examples/benchmarks
make
make java-bench
cd ..
../krun.py java.krun $BENCH_OPTS