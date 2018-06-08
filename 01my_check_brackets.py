# python3

# Description: edX UCSanDiegoX: ALGS201x PA#1
# Problem 1: Check brackets in the code

'''
all possible cases:
Success:
    abc     no brackets
    [](){}  consecutive matching brackets
    [({})]  nested matching brackets
    [()]{}  combo of previous two

Error:
1  ]()   first (obviously) unmatched closing bracket
2  ()[}  closes the wrong opening bracket
3  {}([] first unmatched opening bracket without the corresponding closing bracket

+9 Sample cases from the spec
'''

import sys

#define class Bracket
class Bracket:
    #to track its type, position
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    #to check if corresponding brackets match
    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

#define function to check errors in usage of brackets
def isBalanced(text_in):
    for i, next in enumerate(text_in):

        # Process opening bracket, write your code here
        if next == '(' or next == '[' or next == '{':
            openBracket=Bracket(next, i)

            #add an opening bracket to stack
            opening_brackets_stack.append(openBracket)

            #if found an opening bracket, proceed to next character
            continue

        # Process closing bracket, write your code here
        if next == ')' or next == ']' or next == '}':

            closeBracket=Bracket(next, i)
            # find first unmatched closing bracket
            if not opening_brackets_stack:
                return closeBracket.position + 1
            else:
                # if found an opening bracket, proceed to look for a matching closing bracket
                topOpenBracket = opening_brackets_stack[len(opening_brackets_stack) - 1]

                #if 2 consecutive brackets match, remove top opening bracket from stack; else error
                if topOpenBracket.Match(next):
                    opening_brackets_stack.pop()
                else:
                    return (i + 1)

    # handle an unclosed opening bracket
    if opening_brackets_stack:
        opening_bracket = opening_brackets_stack[0]
        return opening_bracket.position + 1
    # all brackets matched
    else:
        return 'Success'

if __name__ == "__main__":

    #initial cases
    #text= '{}([]' #'()[}' #'(foo[bar])' #']()' #'1[3]4(' #

    #sample cases
    #text = '1[3]4(' #'{}[]' #'[]' # 'foo(bar[i);' # 'foo(bar)';' #'{[}' # '[' #'{[]}()' #'(())' #'[()]' #
    text = sys.stdin.read() #input() #

    opening_brackets_stack = [] #type list

    print ( isBalanced(text))



