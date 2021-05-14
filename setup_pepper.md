# Setup Pepper Environment

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
4. Create a folder `$HOME/playground` that will be shared with the docker container.

```
mkdir -p $HOME/playground
```

4. Download modim folder and put it in `$HOME/src`

``` 
git clone https://bitbucket.org/mtlazaro/modim.git 
```
5. Create a playground folder for new demo files (default `$HOME/playground`) and `playground/html` for HTML files

```
mkdir -p $HOME/playground/html
cd $HOME/playground/html
cp -a $HOME/src/modim/demo/sample .
```

6. Go to Dockerfile in `hri_software/docker` and add environment `MODIM_HOME`, in row 96, after ` ENV PEPPER_TOOLS_HOME`

```
ENV MODIM_HOME /home/robot/src/modim
```

7. Do build, go to `hri_software/docker` and build image

```
./build.bash
```

8. Modify file `run.bash` in `hri_software/docker`, add in row 16

```
 MODIM_HOME=$HOME/src/modim
 
```

and in row 47 of the same file add

```
-v $MODIM_HOME:/home/robot/src/modim
```

9. Run image

```
./run.bash
```

10. Launch Docker 

```
docker exec -it pepperhri tmux
```


