'''
Created on 2017-04-02

@author: admin
'''

import sys
import aiml 

def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]
    print "App started ..."
    
    # Create the kernel and learn AIML files
    kernel = aiml.Kernel()
    kernel.learn("std-startup.xml")
    kernel.respond("load aiml b")
    # Press CTRL-C to break this loop
    while True:
        print kernel.respond(raw_input("Enter your message >> "))

if __name__ == "__main__":
    main()

