# -*- coding: utf-8 -*-
"""
Created on Sat May 16 01:26:57 2015

@author: MarcosScholl
"""
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from aware import *
from data import *
from hmi import *

import xml.etree.ElementTree as ET

from PyQt4 import Qt,QtGui, QtCore


class XMLFactor:
    def __init__(self,arquive):
        self._arquive = arquive
        self._componentes = []
        
    
    #def parseXML(self, arquive):
        
        tree = ET.parse(self._arquive)
        root = tree.getroot()
        
        for widgets in root.iter('widget'):
        #print widget.attrib
            if (widgets.attrib["class"] == "Dial" or widgets.attrib["class"] == "Dial_1" or widgets.attrib["class"] == "Dial_2" or widgets.attrib["class"] == "Dial_3"):
                #print "Classe:", widgets.attrib["class"] ,"  Componente:", widgets.attrib["name"]
                widget = eval(widgets.attrib["class"])()
                widget.setName(widgets.attrib["name"])
                for propert in  widgets.findall('property'):   
                    if propert.find('number') is not None:
                        atributoNumber =  propert.find('number')                        
                        if propert.attrib["name"] == "Value":
                            #print propert.attrib["name"], ":", atributoNumber.text
                            widget.value = int(atributoNumber.text)
                        elif propert.attrib["name"] == "MinimumRange":
                            #print propert.attrib["name"], ":", atributoNumber.text
                            widget.setMinValue(int(atributoNumber.text))
                        elif propert.attrib["name"] == "MaximumRange":
                            #print propert.attrib["name"], ":", atributoNumber.text
                            widget.setMaxValue(int(atributoNumber.text))
                        elif propert.attrib["name"] == "MinimumScale":
                            #print propert.attrib["name"], ":", atributoNumber.text
                            widget.setLowerLimit(int(atributoNumber.text))
                        elif propert.attrib["name"] == "MaximumScale":
                            #print propert.attrib["name"], ":", atributoNumber.text
                            widget.setUpperLimit(int(atributoNumber.text))
                        elif propert.attrib["name"] == "StepScale":
                            #print propert.attrib["name"], ":", atributoNumber.text
                            widget.setStep(int(atributoNumber.text))
                            
                    """
                    elif propert.find('rect') is not None:    
                        print "x:", propert.find('rect').find('x').text
                        print "y:", propert.find('rect').find('y').text
                        print "width:", propert.find('rect').find('width').text
                        print "height:", propert.find('rect').find('height').text
                    """
                self._componentes.append(widget)
             
            elif (widgets.attrib["class"] == "Display"):
                #print "Classe:", widgets.attrib["class"] ,"  Componente:", widgets.attrib["name"]
                widget = eval(widgets.attrib["class"])()
                widget.setName(widgets.attrib["name"])
                for propert in  widgets.findall('property'):
                    if propert.find('string') is not None:
                        atributoString =  propert.find('string')
                        if propert.attrib["name"] == "StartText":
                            #print propert.attrib["name"], "  " ,atributoString.text
                            widget.value = (atributoString.text)
                        elif propert.attrib["name"] == "StaticText":
                            #print propert.attrib["name"], "  " ,atributoString.text
                            widget.staticText = (atributoString.text)
                           
                    elif propert.find('bool') is not None:
                        atributoBoolean =  propert.find('bool')                        
                        if propert.attrib["name"] == "DisplayVisible":
                            widget.setEnable(atributoBoolean.text)
                    """
                    elif propert.find('rect') is not None:    
                        print "x:", propert.find('rect').find('x').text
                        print "y:", propert.find('rect').find('y').text
                        print "width:", propert.find('rect').find('width').text
                        print "height:", propert.find('rect').find('height').text
                    """
                      
                self._componentes.append(widget)        
            elif (widgets.attrib["class"] == "DisplayLCD"):
                #print "Classe:", widgets.attrib["class"] ,"  Componente:", widgets.attrib["name"]
                widget = eval(widgets.attrib["class"])()
                widget.setName(widgets.attrib["name"])
                for propert in  widgets.findall('property'):
                    if propert.find('number') is not None:                       
                        if propert.attrib["name"] == "Value":
                            #print propert.attrib["name"], ":", propert.find('number').text
                            widget.value = float(propert.find('number').text)                    
                    
                    """
                    elif propert.find('rect') is not None:    
                        print "x:", propert.find('rect').find('x').text
                        print "y:", propert.find('rect').find('y').text
                        print "width:", propert.find('rect').find('width').text
                        print "height:", propert.find('rect').find('height').text
                    """
                self._componentes.append(widget)        
            elif (widgets.attrib["class"] == "Led"):
                #print "Classe:", widgets.attrib["class"] ,"  Componente:", widgets.attrib["name"]
                widget = eval(widgets.attrib["class"])()
                widget.setName(widgets.attrib["name"])
                for propert in  widgets.findall('property'):
                    if propert.find('number') is not None:
                        atributoNumber =  propert.find('number')                        
                        if propert.attrib["name"] == "MinimumSizeX":
                            #print propert.attrib["name"], ":", atributoNumber.text
                            minX = atributoNumber.text
                        elif propert.attrib["name"] == "MinimumSizeY":
                            #print propert.attrib["name"], ":", atributoNumber.text
                            minY = atributoNumber.text
                        elif propert.attrib["name"] == "MaximumSizeX":
                            #print propert.attrib["name"], ":", atributoNumber.text
                            maxX = atributoNumber.text
                        elif propert.attrib["name"] == "MaximumSizey":
                            #print propert.attrib["name"], ":", atributoNumber.text
                            maxY = atributoNumber.text
                        
                    elif propert.find('string') is not None:                       
                        if propert.attrib["name"] == "Value":
                            #print propert.attrib["name"], ":", propert.find('string').text
                            widget.value = propert.find('string').text
                    
                    """
                    elif propert.find('rect') is not None:    
                        print "x:", propert.find('rect').find('x').text
                        print "y:", propert.find('rect').find('y').text
                        print "width:", propert.find('rect').find('width').text
                        print "height:", propert.find('rect').find('height').text
                    """
                widget.minimunSize(int(minX),int(minY))
                widget.maximumSize(int(maxX),int(maxY))
                    
                self._componentes.append(widget)        
            elif (widgets.attrib["class"] == "OnOffButton"):
                #print "Classe:", widgets.attrib["class"] ,"  Componente:", widgets.attrib["name"]
                widget = eval(widgets.attrib["class"])()
                widget.setName(widgets.attrib["name"])
                for propert in  widgets.findall('property'):
                    #print propert.attrib
                    if propert.find('string') is not None:
                        atributoString =  propert.find('string')
                        if propert.attrib["name"] == "Value":
                            #print propert.attrib["name"], "  " ,atributoString.text
                            widget.value = bool(atributoString.text)
                        elif propert.attrib["name"] == "TextTrue":
                            #print propert.attrib["name"], "  " ,atributoString.text
                            widget.textTrue = atributoString.text
                        elif propert.attrib["name"] == "TextFalse":
                            #print propert.attrib["name"], "  " ,atributoString.text
                            widget.textFalse = atributoString.text
                    """
                    elif propert.find('rect') is not None:    
                        print "x:", propert.find('rect').find('x').text
                        print "y:", propert.find('rect').find('y').text
                        print "width:", propert.find('rect').find('width').text
                        print "height:", propert.find('rect').find('height').text
                    """
                    
                self._componentes.append(widget)         
            elif (widgets.attrib["class"] == "Slider"):
                #print "Classe:", widgets.attrib["class"] ,"  Componente:", widgets.attrib["name"]
                widget = eval(widgets.attrib["class"])()
                widget.setName(widgets.attrib["name"])
                for propert in  widgets.findall('property'):
                    if propert.find('string') is not None:                       
                        if propert.attrib["name"] == "Name":
                            #print propert.attrib["name"], ":", propert.find('string').text
                            pass
                    
                    elif propert.find('number') is not None:
                        atributoNumber =  propert.find('number')                        
                        if propert.attrib["name"] == "Value":
                            #print propert.attrib["name"], ":", atributoNumber.text
                            widget.value = int(atributoNumber.text)
                        elif propert.attrib["name"] == "MinimumValue":
                            #print propert.attrib["name"], ":", atributoNumber.text
                            widget.setMinimum(int(atributoNumber.text))
                        elif propert.attrib["name"] == "MaximumValue":
                            #print propert.attrib["name"], ":", atributoNumber.text
                            widget.setMaximum(int(atributoNumber.text))
                        
                    """
                    elif propert.find('rect') is not None:    
                        print "x:", propert.find('rect').find('x').text
                        print "y:", propert.find('rect').find('y').text
                        print "width:", propert.find('rect').find('width').text
                        print "height:", propert.find('rect').find('height').text
                    """
                self._componentes.append(widget)         
            elif (widgets.attrib["class"] == "Thermo"):
                #print "Classe:", widgets.attrib["class"] ,"  Componente:", widgets.attrib["name"]
                widget = eval(widgets.attrib["class"])()
                widget.setName(widgets.attrib["name"])
                for propert in  widgets.findall('property'):
                    if propert.find('number') is not None:
                        atributoNumber =  propert.find('number')                        
                        if propert.attrib["name"] == "Value":
                            #print propert.attrib["name"], ":", atributoNumber.text
                            widget.value = float(atributoNumber.text)
                        if propert.attrib["name"] == "MinimumValue":
                            #print propert.attrib["name"], ":", atributoNumber.text
                            widget.setMinValue(float(atributoNumber.text))
                        elif propert.attrib["name"] == "MaximumValue":
                            #print propert.attrib["name"], ":", atributoNumber.text
                            widget.setMaxValue(float(atributoNumber.text))
                        elif propert.attrib["name"] == "AlarmLevel":
                            #print propert.attrib["name"], ":", atributoNumber.text
                            widget.setAlarmLevel(float(atributoNumber.text))
                    
                    elif propert.find('bool') is not None:
                        atributoBoolean =  propert.find('bool')                        
                        if propert.attrib["name"] == "DisplayVisible":
                            #print propert.attrib["name"], "  " ,atributoBoolean.text
                            widget.setEnable(bool(atributoBoolean.text))
                    """
                    elif propert.find('rect') is not None:    
                        print "x:", propert.find('rect').find('x').text
                        print "y:", propert.find('rect').find('y').text
                        print "width:", propert.find('rect').find('width').text
                        print "height:", propert.find('rect').find('height').text
                    """
                self._componentes.append(widget)        
            elif (widgets.attrib["class"] == "Thermometer"):
                #print "Classe:", widgets.attrib["class"] ,"  Componente:", widgets.attrib["name"]
                widget = eval(widgets.attrib["class"])()
                widget.setName(widgets.attrib["name"])
                for propert in  widgets.findall('property'):
                    if propert.find('number') is not None:
                        atributoNumber =  propert.find('number')                        
                        if propert.attrib["name"] == "Value":
                            #print propert.attrib["name"], ":", atributoNumber.text
                            widget.value = float(atributoNumber.text)
                        elif propert.attrib["name"] == "MinimumValue":
                            #print propert.attrib["name"], ":", atributoNumber.text
                            widget.setValueMin(float(atributoNumber.text))
                        elif propert.attrib["name"] == "MaximumValue":
                            #print propert.attrib["name"], ":", atributoNumber.text
                            widget.setValueMax(float(atributoNumber.text))
                        elif propert.attrib["name"] == "AlarmLevelNormal":
                            #print propert.attrib["name"], ":", atributoNumber.text
                            widget.setMinLimit(float(atributoNumber.text))
                        elif propert.attrib["name"] == "AlarmLevelCritical":
                            #print propert.attrib["name"], ":", atributoNumber.text
                            widget.setMaxLimit(float(atributoNumber.text))
                            
                    elif propert.find('bool') is not None:                       
                        if propert.attrib["name"] == "Enable":
                            #print propert.attrib["name"], "  " ,propert.find('bool').text
                            widget.setEnable(bool(propert.find('bool').text))
                    """
                    elif propert.find('rect') is not None:    
                        print "x:", propert.find('rect').find('x').text
                        print "y:", propert.find('rect').find('y').text
                        print "width:", propert.find('rect').find('width').text
                        print "height:", propert.find('rect').find('height').text
                    """ 
                self._componentes.append(widget)     
            """            
            if (widgets.attrib["class"] == "Plot"):
                for propert in  widgets.findall('property'):
                    print propert.attrib
                    for atributo in  propert.findall('string'):
                        print atributo.text 
            """
        print "Componentes:", self._componentes

        
    @property
    def create(self):
        return self._componentes