/******************************************************************************
* @F_NAME :          stima_unittest.h
* @F_PURPOSE :       Purpose
* @F_CREATED_BY :    Shengping Wang
* @F_CREATION_DATE : 2015-08-26
* @F_LANGUAGE :      C
* @F_MPROC_TYPE :   Both endian
*************************************** (C) Copyright 2015 Midea Group   *****/

#ifndef STIMA_UNITTEST_H
#define STIMA_UNITTEST_H

/*______ I N C L U D E - F I L E S ___________________________________________*/
#include "syst.h"

/*______ G L O B A L - D E F I N E S _________________________________________*/

/*______ G L O B A L - T Y P E S _____________________________________________*/

/*______ G L O B A L - D A T A _______________________________________________*/

/*______ G L O B A L - M A C R O S ___________________________________________*/

/*______ G L O B A L - F U N C T I O N S - P R O T O T Y P E S _______________*/
extern void STIMA_UT_CallBack(void);
extern uint8_t STIMA_UT_Condition(void);
extern uint8_t STIMA_UT_GetState(void);
extern void STIMA_UT_ResetState(void);
extern void STIMA_UT_SetConditionValue(uint8_t value);
extern void STIMA_UnitTEST(void);
#endif /* STIMA_UNITTEST_H */

/* _____ E N D _____ (fanm.h) ____________________________________________*/
