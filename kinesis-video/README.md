# Installation Guide for Mac

### Build kinesis-video-producer-jni

1. Install [brew](https://brew.sh/)
1. Add the following line in the file `~/.bash_profile`

	`export PATH="/usr/local/bin:$PATH"`

1. download [kinesis cpp sdk](https://github.com/awslabs/amazon-kinesis-video-streams-producer-sdk-cpp)

	`git clone https://github.com/awslabs/amazon-kinesis-video-streams-producer-sdk-cpp`
	
1. Install [requirements](https://github.com/awslabs/amazon-kinesis-video-streams-producer-sdk-cpp#build-dependencies)

   * related packages
  
		`brew install cmake autoconf automake bison libtool`
		
	* **FIX the conflict of mac system `/usr/bin/bison`**
		* `brew link bison --force`
		* `source ~/.bash_profile`

	So the mac system will use `/usr/local/bin/bison` instead of `/usr/bin/bison`

1. Run `/kinesis-video-native-build/install-script script` and Good luck!!

### Run java sdk


### Face Dectection
* [OpenCV face detection](https://docs.opencv.org/3.3.0/d7/d8b/tutorial_py_face_detection.html)
* [OpenCV video display](http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html)
* [Install OpenCV3 on Mac](https://www.pyimagesearch.com/2016/12/19/install-opencv-3-on-macos-with-homebrew-the-easy-way/)
* [dectect number](https://www.pyimagesearch.com/2017/02/13/recognizing-digits-with-opencv-and-python/)