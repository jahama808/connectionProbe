#!/bin/bash

sudo dumpcap -w /test_59.pcapng.gz -i eth0  -a duration:120
