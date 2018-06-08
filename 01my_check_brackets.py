# python3
# $actodo: stdin ; index1
import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":

    #initial cases
    #text= '{}([]' #'()[}' #'(foo[bar])' #']()' #'1[3]4(' #

    #sample cases
    #text = '1[3]4(' #'{}[]' #'[]' # 'foo(bar[i);' # 'foo(bar)';' #'{[}' # '[' #'{[]}()' #'(())' #'[()]' #
    text = sys.stdin.read() # input() #
    #print('you entered: ' + text)

    opening_brackets_stack = [] #type list

    def isBalanced(text):
        for i, next in enumerate(text):

            # Process opening bracket, write your code here
            if next == '(' or next == '[' or next == '{':
                myBracket1=Bracket(next,i)

                #add an opening bracket
                opening_brackets_stack.append(myBracket1)

                #if found an opening bracket, proceed to next character
                continue

            # Process closing bracket, write your code here
            if next == ')' or next == ']' or next == '}':

                myBracket2=Bracket(next, i)
                # find first unmatched closing bracket
                if not opening_brackets_stack:
                    return myBracket2.position + 1
                else:
                    top=opening_brackets_stack[len(opening_brackets_stack)-1]
                    # if found an opening bracket, proceed to look for a matching closing bracket

                    if top.Match(next):
                        opening_brackets_stack.pop()
                    else:
                        return (i + 1)

                        #continue


        # handled an unclosed bracket
        if opening_brackets_stack:
            opening_bracket = opening_brackets_stack[0]
            return opening_bracket.position + 1
        else:
            return 'Success'

print ( isBalanced(text))


'''
initial cases:
1  ]()   find first unmatched closing bracket, i.e. ']()'
2  ()[}  closes the wrong opening bracket, i.e. } in ()[}
3  {}([] find first unmatched opening bracket without the corresponding closing bracket, like ( in {}([]
4  {}([]) OK nested corresponding brackets

+9 Sample cases from the spec

'''
