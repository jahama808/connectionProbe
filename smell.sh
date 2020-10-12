#!/bin/bash

sudo dumpcap -w /test.pcapng.gz -i eth0  -a duration:120
