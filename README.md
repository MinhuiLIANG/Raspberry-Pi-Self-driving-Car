# Raspberry Pi Self-driving Car
## Project Design Coursework of XJTU Auto
This is a project that can control a Raspberry Pi car to drive itself on a white track between two black borders.


We use `Open-CV` to capture video, `K-means` and `GMM` to detect the borders, the direction is controlled by comparing the trolley position with the offset from the track center.


Run `main.py` to start the Car. 


Run `PID_mian.py` to run the car with PID control.
