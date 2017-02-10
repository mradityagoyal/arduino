'''
Created on Feb 10, 2017

@author: agoyal
'''

import falcon
import magicfly_resource

#start application 
api = application = falcon.API()

#add resource. 
magicfly = magicfly_resource.MagicflyResource("COM3")
#add route. 

api.add_route('/magicfly/transmit/{code}', magicfly)

