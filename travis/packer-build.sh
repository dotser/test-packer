#!/usr/bin/env bash
set -eu

export AWS_SOURCE_AMI='ami-a10897d6'

packer -machine-readable build packer/template.json
