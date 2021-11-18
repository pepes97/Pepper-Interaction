# Pepper Interaction

# Requirements

1. Follow the instructions of [pepper instructions](./setup_pepper.md)
2. Follow the instructions of [emulator instructions](./setup_emulator.md)
3. Follow the instructions for the [first test](./fist_test.md)

# Launch the project after the requirements (requirements only need to be done once)

1. Start Android Studio, run the studio file in the `android-studio-ide/bin/` folder:

```
./studio.sh 
```

and then the emulator (`Tools-> Pepper SDK-> Emulator`)

2. Go to 

`path_to/hri_software/docker` and execute:
```
./run.bash
```

to start the docker image

3. Open terminal and run:

```
docker exec -it pepperhri tmux
```

4. Split windows using command `tmux split-window` and:
  + 4.1 In one terminale go to `$HOME/src/modim/src/GUI` and run 
    ```
    python ws_server.py
    ```
   
   + 4.2 Open the `$HOME/playground/Pepper-Interaction/project-pepper/tablet/index.html` file on the browser and keep the Robot, Dialog View and terminal windows open
   
   + 4.3 In the open terminal go to `/playground/Pepper-Interaction/project-pepper` and
     ```
     python main.py --project-path PROJECT_PATH 
     ```
      with python (not python3)
      
      WHERE `PROJECT_PATH` is a string that identifies the absolute path, for instance we it should be something like `/home/user/playground/Pepper-Interaction/project-pepper`. user is obviously different for everyone.

# Commands in tmux

*Tmux kill session*

```tmux kill-session ```

*Tmux new window*
``` tmux new-window ```

*Tmux split window*
```tmux split-window```

# Video

https://user-images.githubusercontent.com/56698309/127374195-143e59be-0189-4b59-afb3-cfac4ccdde6b.mp4



