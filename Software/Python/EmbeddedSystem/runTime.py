# -*- coding: utf-8 -*-
"""
Created on Tue Dec 06 14:54:14 2016

@author: WANGSP1
"""

from datetime import datetime
class runTime:
    startTime=datetime.now();
    def __init__(self):
        self.startTime=datetime.now();
    def DeltaMiniTime(self):
        curTime=datetime.now();
        delta=curTime-self.startTime;
        return (delta.seconds*1000000+delta.microseconds)*1.0/1000;