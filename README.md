# DeepLearning jetson AI project
  <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"><img src="https://img.shields.io/badge/Google Mediapipe-4285F4?style=for-the-badge&logo=google&logoColor=white"><img src="https://img.shields.io/badge/tensorflow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white"><img src="https://img.shields.io/badge/Jetson Nano-76B900?style=for-the-badge&logo=nvidia&logoColor=white">
  
  ## Desktop controllers using gestures
  - Jetson Nano, Python을 활용하여 카메라를 통해 유저의 손을 인식하고, 제스쳐를 통해 os를 조작합니다.
  - Using Jetson Nano and Python, the camera recognizes the user's hand and manipulates the os through gestures.

# Outcomes
결과물 gif

# Youtube URL
유튜브 링크

## How to Install
1. Download jetpack from Nvidia JetPack SDK
  * We used version 4.6 / https://developer.nvidia.com/embedded/jetpack-sdk-46
2. Create Boot image from Jetpack (We used Balena Etcher)
3. Install Pytorch and Torchvision(https://forums.developer.nvidia.com/t/pytorch-for-jetson/72048)
  * **<h4>DO NOT INSTALL PYTORCH AND TORCHVISON VIA ANY PACKAGE MANAGER</h4>**
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
https://github.com/Melvinsajith/How-to-Install-Mediapipe-in-Jetson-Nano
https://github.com/AastaNV/JEP/import cv2
print(cv2.getBuildInformation())
and check for GSTREAMER support in Video I/O section:

GStreamer:                   YES (1.14.5)tree/master/script


5. JetBot CSI camera setting:
CSI camera test
```sh
nvgstcapture-1.0 --automate --capture-auto
cd /dev/video0
```

```sh
npm install my-crazy-module --save
```

윈도우:

```sh
edit autoexec.bat
```

## Examples

스크린 샷과 코드 예제를 통해 사용 방법을 자세히 설명합니다.

## Devel

모든 개발 의존성 설치 방법과 자동 테스트 슈트 실행 방법을 운영체제 별로 작성합니다.

```sh
make install
npm test
```

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

<!-- Markdown link & img dfn's -->
[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
[wiki]: https://github.com/yourname/yourproject/wiki
