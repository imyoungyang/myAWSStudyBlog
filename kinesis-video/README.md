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