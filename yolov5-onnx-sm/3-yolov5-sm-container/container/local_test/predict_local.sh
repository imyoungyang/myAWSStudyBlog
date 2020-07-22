#!/bin/sh

image=$1
nvidia-docker run -v $(pwd)/test_dir:/opt/ml --rm ${image} serve
