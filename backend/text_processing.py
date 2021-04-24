import re
import os

"""functions for cleaning up text"""

def apply_functions(functions, x):
  """apply a list of functions to some data x"""
  for f in functions: x = f(x)
  return x

#remove extra spaces and tabs placed in betwee text
remove_extra_spaces = lambda s: re.sub(' +', ' ', s)

#put spaces between these characters so model doesnt think they're part of word
def pad_chars(input,chars="-—{}[]():;,."):
  for c in chars: input = input.replace(c, " {} ".format(c))
  return input

def remove_chars(input,chars=['\n']):
  """remove these characters from the string input"""
  for c in chars: input = input.replace(c, '')
  return input

#get rid of newline
remove_newline = lambda s: s.replace('\n','')

#strip extra spaces in begining and end
strip = lambda s: s.strip()

#do all of these things
#clean_paragraph = lambda s: apply_functions([remove_extra_spaces, remove_newline, strip], s)
clean_paragraph = lambda s: apply_functions([remove_chars, pad_chars, remove_extra_spaces, strip], s)


#now we'd like to reverse this process 

#we paded these character with an extra space so we could tokenize it
#now we'd like to undo that
things_to_fix = [('( ','('), ('[ ','['), (' )',')'), (' ]',']'),
                 (' :','.'), (' ;',','),(' .','.'), (' ,',',')]
def remove_padding(input, pairs=things_to_fix):
  """remove extra padding we put in between things like parentheses and punct. marks"""
  for k,v in pairs: input = input.replace(k,v)
  return input