#!/usr/bin/env bash

export NO_MSRS=1
export ENABLE_JAVA=1
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/
export BENCH_OPTS=--no-tickless-check

sudo apt install -y virt-what python-cffi build-essential cpufrequtils cpuset linux-headers-$(uname -r) util-linux mst-tools policykit-1
make clean
make JAVA_CPPFLAGS='"-I${JAVA_HOME}/include -I${JAVA_HOME}/include/linux"' JAVA_LDFLAGS=-L${JAVA_HOME}/lib ENABLE_JAVA=1
cd examples/benchmarks
make clean
make
make java-bench
cd ..
../krun.py example.krun $BENCH_OPTS

