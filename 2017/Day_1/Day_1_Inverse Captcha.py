import logging

"""
The night before Christmas, one of Santa's Elves calls you in a panic. 
"The printer's broken! 
We can't print the Naughty or Nice List!" By the time you make it to sub-basement 17, there are only a few minutes until midnight. 
"We have a big problem," she says; "there must be almost fifty bugs in this system, but nothing else can print The List. 
Stand in this square, quick! 
There's no time to explain; if you can convince them to pay you in stars, you'll be able to--" She pulls a lever and the world goes blurry.
When your eyes can focus again, everything seems a lot more pixelated than before. 
She must have sent you inside the computer! You check the system clock: 25 milliseconds until midnight. 
With that much time, you should be able to collect all fifty stars by December 25th.
Collect stars by solving puzzles. 
Two puzzles will be made available on each day millisecond in the Advent calendar; the second puzzle is unlocked when you complete the first. 
Each puzzle grants one star. Good luck!
You're standing in a room with "digitization quarantine" written in LEDs along one wall. The only door is locked, but it includes a small interface. "Restricted Area - Strictly No Digitized Users Allowed."
It goes on to explain that you may only leave by solving a captcha to prove you're not a human. 
Apparently, you only get one millisecond to solve the captcha: too fast for a normal human, but it feels like hours to you.
The captcha requires you to review a sequence of digits (your puzzle input) and find the sum of all digits that match the next digit in the list. 
The list is circular, so the digit after the last digit is the first digit in the list.

For example:

1122 produces a sum of 3 (1 + 2) because the first digit (1) matches the second digit and the third digit (2) matches the fourth digit.
1111 produces 4 because each digit (all 1) matches the next.
1234 produces 0 because no digit matches the next.
91212129 produces 9 because the only digit that matches the next one is the last digit, 9.

What is the solution to your captcha?
"""
def solve(num_STR):
    answer=0
    for i in range(0,len(num_STR)):
        if i!=len(num_STR)-1 and num_STR[i]==num_STR[i+1]:
            answer=answer+int(num_STR[i])
        elif i==len(num_STR)-1 and num_STR[i]==num_STR[0]:
            answer=answer+int(num_STR[i])
    return answer

def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',datefmt='%Y.%m.%d %H:%M:%S')
    logger = logging.getLogger()
    logger.info('Reading the input.txt')
    num_str=""
    with open("input.txt",'r') as file:
        for i in file:
            num_str=num_str+i
    logger.info('Finished reading the input.txt')
    logger.info('The result is %s.', solve(num_str))
    logger.info('The program closing...')
    """
        That's the right answer! You are one gold star closer to debugging the printer. [Continue to Part Two]
    """
if __name__ == "__main__":
    main()