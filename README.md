# Santa Viewer

A window that allows you to view a 3D cubical model of Santa Claus by moving around the screen. This was written using the Pygame library in Python.

<p align="center">
  <img src="https://github.com/GrantPau/Santa-Viewer/blob/main/Clips/santa.gif" alt="animated" />
</p>
<p align="center">Figure 1: Movable Space to View Object

## How it Works
A cube is defined in a class (Cube) containing the position of its vertices, edges, and faces in a 3D graph. The distance between each point is 1 unit apart and each vertices has an assigned number from 0-7 keep track of the position. The parameters of this class takes in the coordinate of the 3D graph where the user can input the precise coordinates to place the block. By calling this class, one can virtually create anything in this graph just like Minecraft.

<p align="center">
  <img src="https://github.com/GrantPau/Santa-Viewer/blob/main/Clips/cube.PNG"/>
</p>
<p align="center">Figure 2: Assigned Numbers to Vertices for a Basic Cube
