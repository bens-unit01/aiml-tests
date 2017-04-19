'''
Created on 2017-04-02

@author: admin
'''

import sys
import aiml 
import os 
import this

def test_tts(self):
    import pyttsx
    engine = pyttsx.init()
    engine.say('Good morning.')
    engine.runAndWait()


def test_aiml(self):
    """The main routine."""
    os.chdir("../aiml") 

    # Create the kernel and learn AIML files
    kernel = aiml.Kernel()
    kernel.learn("std-startup.xml")
    kernel.respond("load aiml b")
    # Press CTRL-C to break this loop
    while True:
        input = raw_input("Enter your message >> ")
        output = kernel.respond(input)

        print output
        
def main(args=None):
    if args is None:
        args = sys.argv[1:]
    print "App started ..."
    #test_aiml(this)
    test_tts(this)
 
if __name__ == "__main__":
    main()


