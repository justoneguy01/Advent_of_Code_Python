import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',datefmt='%Y.%m.%d %H:%M:%S')
logger = logging.getLogger()
"""
--- Day 2: I Was Told There Would Be No Math ---

The elves are running low on wrapping paper, and so they need to submit an order for more. 
They have a list of the dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as they need.

Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping paper for each gift a little easier: 
find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also need a little extra paper for each present: the area of the smallest side.

For example:

A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet.
A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.
All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?

To begin, get your puzzle input.
"""
def solve_part1():
    answer=0
    with open("input.txt",'r') as file:
        for line in file:
            properties_str=line.split('x')
            properties=list()
            properties.append(int(properties_str[0]))
            properties.append(int(properties_str[1]))
            if '\n' in properties_str[2]:
                properties.append(int((properties_str[2])[:-1]))
            else:
                properties.append(int(properties_str[2]))
            smallest_side=min(+(properties[0]*properties[1]),(properties[1]*properties[2]),(properties[0]*properties[2]))
            answer = answer + ((2*properties[0]*properties[1])+(2*properties[1]*properties[2])+(2*properties[2]*properties[0]))+smallest_side
    return answer
"""
That's the right answer! You are one gold star closer to powering the weather machine. [Continue to Part Two]

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
The elves are also running low on ribbon. 
Ribbon is all the same width, so they only have to worry about the length they need to order, which they would again like to be exact.
The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any one face. 
Each present also requires a bow made out of ribbon as well; the feet of ribbon required for the perfect bow is equal to the cubic feet of volume of the present. 
Don't ask how they tie the bow, though; they'll never tell.
For example:

A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to wrap the present plus 2*3*4 = 24 feet of ribbon for the bow, for a total of 34 feet.
A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon to wrap the present plus 1*1*10 = 10 feet of ribbon for the bow, for a total of 14 feet.
How many total feet of ribbon should they order?

"""

def solve_part2():
    answer=0
    with open("input.txt",'r') as file:
        for line in file:
            properties_str=line.split('x')
            properties=list()
            properties.append(int(properties_str[0]))
            properties.append(int(properties_str[1]))
            if '\n' in properties_str[2]:
                properties.append(int((properties_str[2])[:-1]))
            else:
                properties.append(int(properties_str[2]))
            smallest_width=2*min((properties[0]+properties[1]),(properties[1]+properties[2]),(properties[0]+properties[2]))
            answer=answer+smallest_width+properties[0]*properties[1]*properties[2]
    return answer

"""
That's the right answer! You are one gold star closer to powering the weather machine.

You have completed Day 2! You can [Share] this victory or [Return to Your Advent Calendar].

Both parts of this puzzle are complete! They provide two gold stars: **
"""
def main():
    logger.info('The program is starting...')
    logger.info('The result for part1 is %s.', solve_part1())
    logger.info('The result for part2 is %s.', solve_part2())
    logger.info('The program will shutdown....')
if __name__ == "__main__":
    main()

