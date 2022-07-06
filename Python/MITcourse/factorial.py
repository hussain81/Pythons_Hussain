#!/usr/bin/python


def fact(n):
  "function is for factorial"
  if (n==0): 
     facts=1;	
  else: 
     facts=n*fact(n-1);
  return facts;

print fact(6)
