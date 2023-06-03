import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',datefmt='%Y.%m.%d %H:%M:%S')
logger = logging.getLogger()
"""

Santa was hoping for a white Christmas, but his weather machine's "snow" function is powered by stars, and he's fresh out! 
To save Christmas, he needs you to collect fifty stars by December 25th.
Collect stars by helping Santa solve puzzles. 
Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. 
Each puzzle grants one star. Good luck!
Here's an easy puzzle to warm you up.
Santa is trying to deliver presents in a large apartment building, but he can't find the right floor - the directions he got are a little confusing. 
He starts on the ground floor (floor 0) and then follows the instructions one character at a time.
An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor.
The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors.
For example:
(()) and ()() both result in floor 0.
((( and (()(()( both result in floor 3.
))((((( also results in floor 3.
()) and ))( both result in floor -1 (the first basement level).
))) and )())()) both result in floor -3.
To what floor do the instructions take Santa?

"""
def solve_part1():
    open_counter=0
    close_counter=0
    with open("input.txt",'r') as file:
        for line in file:
            for char in line:
                if char=="(":
                    open_counter=open_counter+1
                elif char==")":
                    close_counter=close_counter+1
    return open_counter-close_counter
"""
That's the right answer! You are one gold star closer to powering the weather machine. [Continue to Part Two]

--- Part Two ---
Now, given the same instructions, find the position of the first character that causes him to enter the basement (floor -1). 

The first character in the instructions has position 1, the second character has position 2, and so on.

For example:

) causes him to enter the basement at character position 1.
()()) causes him to enter the basement at character position 5.
What is the position of the character that causes Santa to first enter the basement?    
"""
def solve_part2():
    open_counter=0
    close_counter=0
    answer=0
    counter=1
    with open("input.txt",'r') as file:
        for line in file:
            for char in line:
                if char=="(":
                    open_counter=open_counter+1
                elif char==")":
                    close_counter=close_counter+1
                if open_counter-close_counter==-1:
                    print(open_counter-close_counter)
                    answer=counter
                    break
                counter=counter+1            
    return answer
"""
That's the right answer! You are one gold star closer to powering the weather machine.

You have completed Day 1! You can [Share] this victory or [Return to Your Advent Calendar].

Both parts of this puzzle are complete! They provide two gold stars: **
"""
def main():
    logger.info('The program is starting...')
    logger.info('The result for part1 is %s.', solve_part1())
    logger.info('The result for part2 is %s.', solve_part2())
    logger.info('The program will shutdown....')
if __name__ == "__main__":
    main()

