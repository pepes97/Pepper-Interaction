# Pepper-Interaction

## Requirements

### Install docker

```
curl -fsSL get.docker.com -o get-docker.sh
sudo sh get-docker.sh
rm get-docker.sh
sudo usermod -aG docker $USER
```

1. Clone

```
git clone https://bitbucket.org/iocchi/hri_software.git
```

2. Download files

[NaoQi](https://drive.google.com/file/d/11BKWwQe1uLxf3aVoEP1xJsgcUfIX-bYY), 
[Ctc](https://drive.google.com/file/d/1D9oXwiA1vYKGFO7qh81vVsRO189AGZvd),
[PyNaoQi](https://drive.google.com/file/d/18uqf8iAfqnzRZHS206oSAWFYhCgoZ11p)

place them in ```docker/downloads``` folder.

3. Download pepper tools

```
mkdir -p $HOME/src/Pepper
cd $HOME/src/Pepper
git clone https://bitbucket.org/mtlazaro/pepper_tools.git
```
4. Create a folder ```$HOME/playground``` that will be shared with the docker container.

```
mkdir -p $HOME/playground
```

5. Go to ```hri_software/docker``` and build image

```
./build.bash
```
6. Run image

```
./run.bash
```

7. Docker exec with ``tmux``

```
docker exec -it pepperhri tmux
```

8. Run NaoQi 

``` 
cd /opt/Aldebaran/naoqi-sdk-2.5.5.5-linux64
./naoqi
```

9. Install Android Studio and Pepper SDK

```
https://qisdk.softbankrobotics.com/sdk/doc/pepper-sdk/index.html 
```

10. If the emulator does not work

```
https://developer.softbankrobotics.com/blog/ubuntu-18-and-pepper-qisdk-emulator-troubleshooting
```

## Commands in tmux

*Tmux kill session*

```tmux kill-session ```

*Tmux new window*
``` tmux new-window ```

*Tmux split window*
```tmux split-window```


**After the first installation, just do ./run.bash to start the container with the image**

