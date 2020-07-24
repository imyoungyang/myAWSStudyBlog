#!/bin/sh

image=$1

mkdir -p test_dir/model
mkdir -p test_dir/output

rm test_dir/model/*
rm test_dir/output/*

nvidia-docker run -v $(pwd)/test_dir:/opt/ml --shm-size=8g --rm ${image} train
# docker run -v $(pwd)/test_dir:/opt/ml --shm-size=8g --rm ${image} train
