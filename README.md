# DeepLearning jetson AI project
  <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"><img src="https://img.shields.io/badge/Google Mediapipe-4285F4?style=for-the-badge&logo=google&logoColor=white"><img src="https://img.shields.io/badge/tensorflow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white"><img src="https://img.shields.io/badge/Jetson Nano-76B900?style=for-the-badge&logo=nvidia&logoColor=white">
  
  ## Desktop controllers using gestures
  - Jetson Nano, Python, Mediapipe를 활용하여 카메라를 통해 유저의 손을 인식하고, 제스쳐를 통해 os를 조작합니다.
  - Using Jetson Nano, Python and Mediapipe, the camera recognizes the user's hand and manipulates the os through gestures.

# Outcomes
결과물 gif

# Youtube URL
[![Video Label]([http://img.youtube.com/vi/E2rpPNNWpo4/0.jpg](https://user-images.githubusercontent.com/65393001/206188445-a82cfd4a-43dc-41ae-a423-308d46b0df3a.PNG))](https://youtu.be/XbvgqPYqAnI)

## How to Install
0. Update and Upgrade the APT and PIP
  ```sh
  sudo apt-get update
  sudo apt-get upgrade
  pip3 install --upgrade pip
  ```
1. Download jetpack from Nvidia JetPack SDK
  * We used version 4.6 / https://developer.nvidia.com/embedded/jetpack-sdk-46
2. Create Boot image from Jetpack (We used Balena Etcher)
3. Install Pytorch and Torchvision(https://forums.developer.nvidia.com/t/pytorch-for-jetson/72048)
  **<h4>⚠️ DO NOT INSTALL PYTORCH AND TORCHVISON VIA ANY PACKAGE MANAGER ⚠️</h4>**
  * We used PyTorch v1.10.0 and torchvision v0.10.0
  * if error with PIL deprecated, install Pillow < v7
  * Pytorch Install
  ```sh
  sudo apt-get install python3-pip libopenblas-base libopenmpi-dev libomp-dev
  pip3 install Cython
  pip3 install numpy torch-1.11.0-cp36-cp36m-linux_aarch64.whl
  ```
  * Torchvision Install
  ```sh
  sudo apt-get install libjpeg-dev zlib1g-dev libpython3-dev libavcodec-dev libavformat-dev libswscale-dev
  git clone --branch v0.11.0 https://github.com/pytorch/vision torchvision
  cd torchvision
  export BUILD_VERSION=0.11.0 
  python3 setup.py install --user
  pip3 install 'pillow<7'
  ```
4. Install Mediapipe
  **<h4>⚠️ DO NOT INSTALL MEDIAPIPE VIA PIP ⚠️</h4>**
  * Reference : https://github.com/Melvinsajith/How-to-Install-Mediapipe-in-Jetson-Nano
  ```sh
  sudo apt-get install libhdf5-serial-dev hdf5-tools libhdf5-dev \
  zlib1g-dev zip libjpeg8-dev liblapack-dev libblas-dev gfortran
  ```
  ```sh
  sudo pip3 install -U pip testresources setuptools==49.6.0
  ```
  ```sh
  sudo pip3 install -U --no-deps numpy==1.19.4 future==0.18.2 mock==3.0.5 \
  keras_preprocessing==1.1.2 keras_applications==1.0.8 gast==0.4.0 \
  protobuf pybind11 cython pkgconfig
  ```
  ```sh
  sudo env H5PY_SETUP_REQUIRES=0 pip3 install -U h5py==3.1.0
  ```
5. Install OpenCV
  ```sh
  sudo apt-get install python3-opencv
  ```
6. (Optional) If you wanna input CSI Camera video source, install OpenCV using this method
  **<h4>⚠️ WARNING. This task lasts at least 4 hours ⚠️</h4>**
  * Reference : https://github.com/AastaNV/JEP/
  ```sh
  wget https://raw.githubusercontent.com/AastaNV/JEP/master/script/install_opencv4.5.0_Jetson.sh
  ./install_opencv4.5.0_Jetson.sh
  ```
  * Test the OpenCV
  ```python
  import cv2
  print(cv2.getBuildInformation())
  ```
  * Check for GSTREAMER support in VIDEO I/O section
  ```sh
  GStreamer:                   YES (1.14.5)tree/master/script
  ```

## Examples

스크린 샷과 코드 예제를 통해 사용 방법을 자세히 설명합니다.

## 코드블럭 설명

```c
//```뒤에 자신이 원하는 언어 (생략 가능)
#include <stdio.h>
int main(void) {
  printf("Hello World!");
}
```


## 업데이트 내역

* 0.2.1
    * 수정: 문서 업데이트 (모듈 코드 동일)
* 0.2.0
    * 수정: `setDefaultXYZ()` 메서드 제거
    * 추가: `init()` 메서드 추가
* 0.1.1
    * 버그 수정: `baz()` 메서드 호출 시 부팅되지 않는 현상 (@컨트리뷰터 감사합니다!)
* 0.1.0
    * 첫 출시
    * 수정: `foo()` 메서드 네이밍을 `bar()`로 수정
* 0.0.1
    * 작업 진행 중

## 정보

이름 – [@트위터 주소](https://twitter.com/dbader_org) – 이메일주소@example.com

XYZ 라이센스를 준수하며 ``LICENSE``에서 자세한 정보를 확인할 수 있습니다.

[https://github.com/yourname/github-link](https://github.com/dbader/)

## README 

1. https://github.com/kyechan99/capsule-render
2. https://yermi.tistory.com/entry/%EA%BF%80%ED%8C%81-Github-Readme-%EC%98%88%EC%81%98%EA%B2%8C-%EA%BE%B8%EB%AF%B8%EA%B8%B0-Readme-Header-Badge-Widget-%EB%93%B1


## 그외의 팁

취소선
~~취소선~~


인용글
> 인용글 1
> > 인용글 2
> > > 인용글 3

기울임
*기울임 꼴*

_기울임 꼴_


굵은글씨

**굵은 글씨**

__굵은 글씨__
