'''
Created on 2017-04-02

@author: Raouf
'''

import sys
import aiml 
import os 
import this
import aiml
import os 

def test_tts(self):
    import pyttsx
    engine = pyttsx.init()
    engine.say('Good morning.')
    engine.runAndWait()


def test_aiml(self):
    """The main routine."""
    os.chdir("../aiml") 

    # Create the kernel and learn AIML files
    os.chdir("../aiml"); 
    kernel = aiml.Kernel()
    kernel.learn("std-startup.xml")
    kernel.respond("load aiml b")
    kernel.setBotPredicate("name", "RSAI")
    kernel.setBotPredicate("favoritecolor", "blue")
    kernel.setBotPredicate("city", "Montreal")
    kernel.setBotPredicate("country", "Canada")
    kernel.setBotPredicate("nationality", "Canadian")
    kernel.setBotPredicate("birthplace", "Montreal")
    kernel.setBotPredicate("location", "Montreal")

    '''
    if os.path.isfile("bot_brain.brn"):
        kernel.bootstrap(brainFile = "bot_brain.brn")
    else:
        kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
        kernel.saveBrain("bot_brain.brn")
     '''
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


