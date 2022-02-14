# Animation Basics
* Animation is not real movement, it's a trick of the eye
* A series of still images going by very fast appears as motion
* Like a flip-book
* Game animation usually 60 or 120 images/second
# Terminology
* Single image from this series is called a frame
* Like a single page in a flipbook
* In code, a frame is usually one iteration of a loop
* Calculating the offset shows where objects should be placed
# Offset
* Offset is increased each frame
* This shows how far objects have moved since the start
* The same offset can be applied to multiple points or objects to make them move together
* Normally we apply an offset by drawing the shape with variables as its coordinates
* This way the variables can change every frame
* Adding to x will make the shape move right; subtracting will make it move left
* Adding to y will make the shape move down; subtracting will make it move up
* This works for lines, circles, and polygons
# Rectangle Offset
* Rectangles are a special case
* We can get the x or y position of a Rect object using the . operator
* We can also assign new values to these variables to move the Rect
* Once we create a Rect, we can move it by its x and y
* This works for rectangles and ellipses
# Slow Animation
* We can use this to slow down an animation
* Wait lets us pause a tiny, tiny amount - measured in milliseconds
# Animations Steps
* To animate, follow these steps in each frame
* Update position: Change where the object will draw
* Draw background: Draws over the previous frame
* Draw object: Draw the object in its new position
* Flip: Reveal the animation
* Wait: Pause so the animation doesn't go too fast
