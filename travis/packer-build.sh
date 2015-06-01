#!/usr/bin/env bash
set -eu

packer -machine-readable build packer/template.json
