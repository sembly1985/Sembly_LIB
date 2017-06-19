# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 13:47:40 2015

@author: WANGSP1
"""
import numpy
import math
class freqResp:
    freq=numpy.zeros([1,1],'float')
    resp=numpy.zeros([1,1],'complex')
    def __init__(self,t_freq,t_resp):
        self.freq=abs(t_freq);
        self.resp=t_resp;
    def __add__(self,data):
        if(isinstance(data,freqResp)):
            temp=self.resp+data.resp;
        else:
            temp=self.resp+data;
        return freqResp(self.freq,temp)
    def __sub__(self,data):
        if(isinstance(data,freqResp)):
            temp=self.resp-data.resp;
        else:
            temp=self.resp-data;
        return freqResp(self.freq,temp)
    def __mul__(self,data):
        if(isinstance(data,freqResp)):
            temp=self.resp*data.resp;
        else:
            temp=self.resp*data;
        return freqResp(self.freq,temp)
    def __div__(self,data):
        if(isinstance(data,freqResp)):
            temp=self.resp/data.resp;
        else:
            temp=self.resp/data;
        return freqResp(self.freq,temp)
    def __neg__(self):
        return freqResp(self.freq,-self.resp);
    def inv(self):
        temp=numpy.zeros(self.resp.shape,'complex');
        for i in range(0,self.resp.size):
            temp[i]=complex(1,0)/self.resp[i];
        return freqResp(self.freq,temp);
    def mag(self):
        temp=numpy.zeros(self.resp.shape);
        for i in range(0,self.resp.size):
            temp[i]=abs(self.resp[i]);
        return temp;
    def angle(self):
        temp=numpy.zeros(self.resp.shape);
        for i in range(0,self.resp.size):
            c_data=self.resp[i];
            r_data=c_data.real;
            i_data=c_data.imag;
            radius=math.acos(r_data/math.sqrt(r_data*r_data+i_data*i_data));
            if(i_data<0):
                radius=-radius;
            temp[i]=radius;
        return temp;