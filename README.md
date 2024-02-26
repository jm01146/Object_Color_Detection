Test color detection for future projects.

So I figured out how make it look for 'general' colors rather and a specific range of color.

Heres what I mean, originally I wanted to find like shades of green, such as faded mossy green, VIBRANT neo looking greens, you name it.
To even light soft green mixed with turquoise, the list goes on. But it wasn't working and I didn't know how. I finally understood the documentation but holy hell it was complicated.

To find general/like colors you need to mess with S and V values of the HSV range. the three values you give during the numpy array is H,S,V respecfully. THere is also some things they don't tell you.

H goes from 0-180 and this sets the color you want. There's like what 6 colors in the visable spectrum??? Red, Orange, Yellow, Green, Blue, and Purple. so each color is within a 30 range.
Red being 0-30, orange: 30-60, yellow:60-90 you get it. EXCEPT FUCKING RED. HERE IS WHERE WE GET TO THE PART THEY CASUALLY FORGET AND MY GOD ITS ANNOYING. Red goes from both 0-10 and 170-180.
(Remember that 30 range isn't the actual range its and estimate range for easier understanding and less specifc project please look this up via doucmentation for specfic ranges.) 
THIS WAS SO ANNOYING TO FIND OUT. 0-10 is for brighter red, the type of red like seen in the Iron Man suits. 170-180 is the darker type of reds such as maroon. If you want to find both types, you have to make you mask a Bitwise_and function. (Or works as well but "and" merges and I think that is better try both and/or to find out which is better.)

S is how white the color is. If you have 0 saturation it would be pure white the color is GONE. but the closer you get to full saturation the more color there is. This is where it gets slightly complicated.
V is how light the color is 0 means its pure black and as close as it gets to max the lighter the tone the color will be. 
These two things sound like the same thing right? WELP EVERY CHART THAT EXPLAINS THIS CONCEPT SUCKS AND YEAH IT KIND OF LOOKS THE SAME.

So here is how I defined it and it does somewhat help. V is how Vibrant the color is. Pure color will SHINE it will catch your eye but then it color fades. It not getting darker the color is running out, it fading. It solely focuses on that color and if that color is leaving it becomes more white. On the oppisite end is V (value I forgot to mention thats what V stands for). V goes for how dirty the color is. You don't wash you white car you will see the dirt. You mix a bunch of paints together you get black. This works for darker colors that transisiton to other darker colors.

Yeah this is the best I got to explain it I know it is some what confusing (if not completely) but to simplify. S for light tones, V for dark tones. (Also the range for both S and V is 0-255).
