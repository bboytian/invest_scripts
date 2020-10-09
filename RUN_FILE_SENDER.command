#!/bin/bash

realpath=/usr/local/bin/realpath
wd=$(dirname $($realpath ${BASH_SOURCE[0]}))

$wd/file_manager/file_sender.sh
