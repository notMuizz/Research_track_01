## RT1_Assingment_01

In the Assingment 1 we have to built a program in which **Robot** grabs the silver(token) Boxes and place them near to golden(token) boxes

### The Grabber

The **Robot** is equipped with an arm called **Grabber**, which can pick up the the token  with the help of program function called `R.grab`. The function returns `True` if a token was successfully picked up, or `False` otherwise. And after successful pickup it can relase the token infront of other token with a function called 'R.release'.

```python
 R.grab()
```
```python
 R.release()
```
### Defined variables:

<br>a_th : The threshold for controlling the linear distance. </br>
d_th : The threshold for controlling the orientation.

<br> silver_toke_List = [] : List contains the codes of silver boxes.</br>
golden_token_List = [] : List contains the codes of golden boxes.	

### Find_silver_token & find_golden_token:
This function tries to find the **silver box**, by updating the distance of nearest token non paired (not in List).
<pre>
dist=100
    for token in R.see():
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_SILVER and token.info.code not in silver_token_list:
            dist=token.dist
	    rot_y=token.rot_y
	    box_id = token.info.code
    if dist==100:
	return -1, -1, -1
    else:
   	return dist, rot_y, box_id
</pre>
Same principle for the function find_golden_token

### Grabb Silver and Relase at Golden Token:
The main task is to first find the Silver Token by constantly updating the distance & orientation. And when the **Robot** is near to Silver token Grabb the token by calling the function. After Grabbing the Silver token the next task is to place(release) it near the closest Golden Token. All these tasks are performed by functions which were created in the **assignment.py file**.

### Run The Program	
	When done, copy this python file in folder of simulator and run with:
	$ python run.py assignment.py
	
	
![flow](https://user-images.githubusercontent.com/48551115/201193198-5d2d1acd-9900-4c3e-904a-6c1867b53741.svg)



### Input: 

![input](https://user-images.githubusercontent.com/48551115/201195037-45b27c93-6eb0-4d0e-90e4-b6a7dd29a022.png)


### Ouput: 

![output](https://user-images.githubusercontent.com/48551115/201195045-f4791d94-c300-47ef-a18e-e0dc839c9ec5.png)


