/******************************************************************************
* @F_NAME :          stima.h
* @F_PURPOSE :       Purpose
* @F_CREATED_BY :    Shengping Wang
* @F_CREATION_DATE : 2015-08-26
* @F_LANGUAGE :      C
* @F_MPROC_TYPE :   Both endian
*************************************** (C) Copyright 2015 Midea Group   *****/

#ifndef STIMA_H
#define STIMA_H

/*______ I N C L U D E - F I L E S ___________________________________________*/
#include "syst.h"

/*______ G L O B A L - D E F I N E S _________________________________________*/
#define STIMA_1ms (SYST_CLICK_1ms)
#define STIMA_Task_Cycle STIMA_1ms
#define STIMA_Task_Delay ((uint32_t)(0.5*STIMA_1ms))
/*______ G L O B A L - T Y P E S _____________________________________________*/
typedef enum{
	STIMA_DoDetect,
	STIMA_Max
}STIMA_TimeId_t;

typedef void(*pSTIMACallBack)(void);
typedef uint8_t(*pSTIMAResetCondition)(void);
/*______ G L O B A L - D A T A _______________________________________________*/

/*______ G L O B A L - M A C R O S ___________________________________________*/

/*______ G L O B A L - F U N C T I O N S - P R O T O T Y P E S _______________*/
extern uint8_t STIMA_StartTimer(STIMA_TimeId_t id, uint16_t ms, pSTIMACallBack callback, pSTIMAResetCondition resetCondition);
extern void STIMA_StopTimer(STIMA_TimeId_t id);
extern uint16_t STIMA_GetTimer(STIMA_TimeId_t id);

extern void STIMA_Init(void);
extern void STIMA_Main(void);
#endif /* STIMA_H */

/* _____ E N D _____ (stima.h) ____________________________________________*/
