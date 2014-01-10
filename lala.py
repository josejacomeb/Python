#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="josejacomeb1"
__date__ ="$28/10/2013 05:25:01 PM$"
str='Avounyy'
c = 'y'
otra = '' 
for i in range(len(str)) :
  if str[i] == c:
     continue
  else :
     otra += str[i]
print (otra)

 