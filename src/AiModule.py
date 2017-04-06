'''
Created on Apr 4, 2017

@author: raouf
'''
import sys
import aiml
import os 

class AiModule(object):
    '''
    classdocs
    '''
    kernel = None; 

    def respond(self, input):
        self.kernel.respond(input) 

       
        
    def __init__(self, path):
        os.chdir(path); 
        self.kernel = aiml.Kernel()
        if os.path.isfile("bot_brain.brn"):
            self.kernel.bootstrap(brainFile = "bot_brain.brn")
        else:
            self.kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
            self.kernel.saveBrain("bot_brain.brn")   

             
            
            


        
          
   
    