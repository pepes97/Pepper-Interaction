# First Test

After following the instructions in [setup_pepper.md](./setup_pepper.md) and in [setup_emulator.md](./setup_emulator.md) you should have launch the emulator and docker.

1. In the docker terminal go to `$HOME/src/pepper_tools/say` and run file

```
python say.py --sentence "Hello my friend"
```

you should see something like this

![image](https://drive.google.com/uc?export=view&id=1zOtaQcvf112yJ6EEE9LtbJPWFxKGdJ50)


2. Test page html (it should be the "tablet"): open another terminal with `tmux new-window` or split window with `tmux split-window` and go to `$HOME/src/modim/src/GUI` and start

```
python ws_server.py
```

after that open a new terminal (not with tmux, a simple normal termninal) and go to `$HOME/playground/html/sample/` and open the file html:

```
firefox index.html
```

you should have something like that:

![imagee](https://drive.google.com/uc?export=view&id=1gfw6Kq_TvrGdVFHaXgWcsgrP8C-VOux0)

3. To start interaction open new window with tmux and go in the folder `$HOME/playground/html/sample/scripts` and run

```
python demo1.py
```

Go to file the webpage that you open with firefox and you should see:

![images](https://drive.google.com/uc?export=view&id=1HSPYnrBSKrE3zofh7VseBnaSdFRpjCtA)

Press start and enjoy the interaction
