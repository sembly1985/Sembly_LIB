/******************************************************************************
* @F_NAME :         stima.c
* @F_PURPOSE :       Purpose
* @F_CREATED_BY :    Shengping Wang
* @F_CREATION_DATE : 2015-08-26
* @F_LANGUAGE :      C
* @F_MPROC_TYPE :   Both endian
*************************************** (C) Copyright 2015 Midea Group   *****/
/*______ I N C L U D E - F I L E S ___________________________________________*/
#include "syst.h"
#include "stima.h"
#include "stima_config.h"
/*______ L O C A L - D E F I N E S ___________________________________________*/

/*______ L O C A L - T Y P E S _______________________________________________*/ 
typedef struct{
	pSTIMACallBack callback;
	pSTIMAResetCondition resetCondition;
	uint16_t tick;
	uint16_t savedTick;
	uint8_t runStatus;
}STIMA_Time_t;
/*______ G L O B A L - D A T A _______________________________________________*/

/*______ P R I V A T E - D A T A _____________________________________________*/

/*______ L O C A L - D A T A _________________________________________________*/
volatile STIMA_Time_t Stima_Timer[STIMA_Max];
/*______ L O C A L - M A C R O S _____________________________________________*/

/*______ I M P O R T - F U N C T I O N S - P R O T O T Y P E S _______________*/

/*______ L O C A L - F U N C T I O N S - P R O T O T Y P E S _________________*/
void Stima_Task(void);
/*______ G L O B A L - F U N C T I O N S _____________________________________*/
uint8_t STIMA_StartTimer(STIMA_TimeId_t id, uint16_t ms, pSTIMACallBack callback, pSTIMAResetCondition resetCondition)
{
	uint8_t ret=0;
	if(Stima_Timer[id].runStatus==0)
	{
		Stima_Timer[id].tick=ms;
		Stima_Timer[id].savedTick=ms;
		Stima_Timer[id].callback=callback;
		Stima_Timer[id].resetCondition=resetCondition;
		Stima_Timer[id].runStatus=1;
		ret=1;
	}
	return ret;
}
void STIMA_StopTimer(STIMA_TimeId_t id)
{
	Stima_Timer[id].runStatus=0;
}
uint16_t STIMA_GetTimer(STIMA_TimeId_t id)
{
	return Stima_Timer[id].tick;
}

void STIMA_Init(void)
{
	uint8_t id;
	STIMA_Time_t* pTimer;
	for(id=0;id<STIMA_Max;id++)
	{
		pTimer=&Stima_Timer[id];
		pTimer->runStatus=0;
		pTimer->tick=0;
	}
}

void STIMA_Main(void)
{
	STIMA_Sensor();
	Stima_Task();
	STIMA_Actuator();
}
/*______ P R I V A T E - F U N C T I O N S ___________________________________*/

/*______ L O C A L - F U N C T I O N S _______________________________________*/
void Stima_Task(void)
{
	uint8_t id;
	STIMA_Time_t* pTimer;
	for(id=0;id<STIMA_Max;id++)
	{
		pTimer=&Stima_Timer[id];
		if(pTimer->runStatus)
		{
			(pTimer->tick)--;
			if(pTimer->resetCondition!=0)
			{
				if((*pTimer->resetCondition)())
					pTimer->tick=pTimer->savedTick;
			}
			if(pTimer->tick==0)
			{
				pTimer->runStatus=0;
				if(pTimer->callback!=0)
					(*pTimer->callback)();
			}
		}
	}
}
/*______ E N D _____ (stima.c) ____________________________________________*/
