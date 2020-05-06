#!/bin/bash

ROOT_BASE=/opt/domain_src
cd $ROOT_BASE
nohup python3 ${ROOT_BASE}/run_subdomain.py &
/usr/bin/tail -f nohup.out