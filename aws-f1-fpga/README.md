# AWS F1 setup

## installation

```
$ git clone https://github.com/aws/aws-fpga.git $AWS_FPGA_REPO_DIR  
$ cd $AWS_FPGA_REPO_DIR                                         
$ source vitis_setup.sh
```

## Start the driver

```
systemctl is-active --quiet mpd || sudo systemctl start mpd
systemctl status mpd
```

## Reference

* [aws-fpga](https://github.com/aws/aws-fpga/blob/master/Vitis/README.md#github-and-environment-setup)