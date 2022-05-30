# Robomaster standard program
This is a standard algorithm to gain control under the Robomaster S1 EP. 
* *Still in work...*
* Will be happy to see your commitment in the development
  
To find out more information about how all of this work see the [protocol api](<https://robomaster-dev.readthedocs.io/zh_CN/release_en/text_sdk/protocol_api.html>) for Robomaster

So, to begin the work, firs of all:
1. clone the repo to the desired directory.
2. Use conda `pip3 install conda` to create the virtual environment
3. Create the virtual ennviroment called dji to use python 3.7 `conda create -n dji python=3.7`
4. Then write `conda activate dji` in terminal to enter the virtual environment

Now open the python file in desired editor and find the block 
```
def program(): 
    pass
```
In this block you can write the algorithm using functions like `directional_movement(x-axis, y-axis, socket)` and `rotation(degree, socket)`
