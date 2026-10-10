#!/bin/bash

echo "Loading Tau and GProfNg"
export PATH=/home/lochannk/software_build/tau-2.33.1/x86_64/bin:$PATH
export LD_LIBRARY_PATH=/home/lochannk/software_build/tau-2.33.1/x86_64/lib:$LD_LIBRARY_PATH
export PATH=/home/lochannk/software_build/binutils-2.41.90/ins_dir/bin:$PATH
export LD_LIBRARY_PATH=/home/lochannk/software_build/binutils-2.41.90/ins_dir/lib:$LD_LIBRARY_PATH
gprofng
tau_exec

