# -*- coding: utf-8 -*-
''' trace module: software monitor '''
import numpy
import numConvert as numC
from trace_interface import *
class trace:
    def __init__(self):
        ''' initial '''
        channels=[];
        traceData=[];
        dataLen=0;
        channelBuffIndex=[]
        traceLength=0;
        pass;
    
    def Clr(self):
        self.channels=[];
        self.traceData=[];
        self.dataLen=0;
        trace_clr();
        self.channelBuffIndex=[]
        self.traceLength=0;
        pass;
    
    def SetChannel(self,channelAddr,channelLength,ifSign,ifFloat=0):
        tmp=[channelAddr,channelLength,ifSign,ifFloat];
        self.channels.append(tmp);
        self.dataLen = self.dataLen+channelLength;
        if(len(self.channelBuffIndex)==0):
            self.channelBuffIndex.append([0,channelLength-1]);
        else:
            tmp=[self.channelBuffIndex[len(self.channelBuffIndex)-1][1]+1,self.channelBuffIndex[len(self.channelBuffIndex)-1][1]+channelLength]
            self.channelBuffIndex.append(tmp)
        return trace_SetChannel(channelAddr,channelLength);
        pass;
    
    def SetTrigger(self,triggerAddr,triggerMask,triggerLevel,triggerTerm):
        return trace_SetTrigger(triggerAddr,triggerMask,triggerLevel,triggerTerm)
        pass;
        
    def SetConfig(self,preCount,postCount,timeout,sampleRate,traceClock):
        return trace_SetConfig(preCount,postCount,timeout,sampleRate,traceClock)
        pass;
        
    def GetStatus(self):
        u=[0,0]
        trace_GetStatus(u);
        return u
    
    def GetTracedLength(self):
        return len(self.traceData);
        pass;
        
    def GetTracedData(self,trace_len):
        tmp=trace_GetTraceData(trace_len);
        tmp=map(ord,tmp);
        traceLen=len(tmp)/self.dataLen;
        tmp=tmp[(len(tmp)-traceLen*self.dataLen):];
        for i in range(0,traceLen):
            self.traceData.append(tmp[i*self.dataLen:(i*self.dataLen+self.dataLen)])
        self.traceLength=len(self.traceData)
        pass;
        
    def GetChannel(self,channel):
        ret=[]
        if(channel<len(self.channels)):
            buffIndex=self.channelBuffIndex[channel];
            rawData=[];
            for i in range(0,self.traceLength):
                rawData.append(self.traceData[i][buffIndex[0]:buffIndex[1]+1])
            if(self.channels[channel][3]):
                ''' float data '''
                ret=map(numC.byteArray2Float,rawData);
            else:
                ifSign=self.channels[channel][2]
                ret=[0]*len(rawData)
                for i in range(0,len(ret)):
                    ret[i]=numC.byteArray2Int(rawData[i],ifSign);
        return ret;
    
    def GetPollingData(self):
        tmp=trace_GetPollingData(self.dataLen);
        if(len(tmp)==self.dataLen):
            self.traceData.append(tmp);
            self.traceLength = self.traceLength+1;
        pass;
    
    def Start(self):
        return trace_start();
        pass;
        
    def StartPolling(self):
        return trace_StartPolling()
        pass;