/******************************************************************************
* @F_NAME :          stima_unittest.c
* @F_PURPOSE :       Purpose
* @F_CREATED_BY :    Shengping Wang
* @F_CREATION_DATE : 2015-08-26
* @F_LANGUAGE :      C
* @F_MPROC_TYPE :   Both endian
*************************************** (C) Copyright 2015 Midea Group   *****/
/*______ I N C L U D E - F I L E S ___________________________________________*/
#include "syst.h"
#include "stima.h"
/*______ L O C A L - D E F I N E S ___________________________________________*/

/*______ L O C A L - T Y P E S _______________________________________________*/ 

/*______ G L O B A L - D A T A _______________________________________________*/

/*______ P R I V A T E - D A T A _____________________________________________*/
static uint8_t Stima_UT_state;
static uint8_t Stima_UT_condition;
/*______ L O C A L - D A T A _________________________________________________*/

/*______ L O C A L - M A C R O S _____________________________________________*/

/*______ I M P O R T - F U N C T I O N S - P R O T O T Y P E S _______________*/

/*______ L O C A L - F U N C T I O N S - P R O T O T Y P E S _________________*/

/*______ G L O B A L - F U N C T I O N S _____________________________________*/
int STIMA_initDefaultSuite(void)
{
	return 0;
}

int STIMA_cleanDefaultSuite(void)
{
	return 0;
}

void STIMA_UT_CallBack(void)
{
	Stima_UT_state=1;
}
uint8_t STIMA_UT_Condition(void)
{
	return Stima_UT_condition;
}
uint8_t STIMA_UT_GetState(void)
{
	return Stima_UT_state;
}
void STIMA_UT_ResetState(void)
{
	Stima_UT_state=0;
}
void STIMA_UT_SetConditionValue(uint8_t value)
{
	Stima_UT_condition=value;
}

void STIMA_UT_TimeoutTest(void)
{
	uint8_t i;
	STIMA_UT_ResetState();
	STIMA_UT_SetConditionValue(0);
	STIMA_StartTimer(STIMA_DoDetect,5,STIMA_UT_CallBack,STIMA_UT_Condition);
	for(i=0;i<5;i++)
	{
		CU_ASSERT_EQUAL(5-i,STIMA_GetTimer(STIMA_DoDetect));
		CU_ASSERT_EQUAL(0,STIMA_UT_GetState());
		STIMA_Main();
	}
	CU_ASSERT_EQUAL(0,STIMA_GetTimer(STIMA_DoDetect));
	CU_ASSERT_EQUAL(1,STIMA_UT_GetState());
	STIMA_Main();
	CU_ASSERT_EQUAL(0,STIMA_GetTimer(STIMA_DoDetect));
	CU_ASSERT_EQUAL(1,STIMA_UT_GetState());
}

void STIMA_UT_ResetTest(void)
{
	uint8_t i;
	STIMA_StopTimer(STIMA_DoDetect);
	STIMA_UT_ResetState();
	STIMA_UT_SetConditionValue(0);
	STIMA_StartTimer(STIMA_DoDetect,5,STIMA_UT_CallBack,STIMA_UT_Condition);
	STIMA_Main();
	STIMA_Main();
	STIMA_StartTimer(STIMA_DoDetect,5,STIMA_UT_CallBack,STIMA_UT_Condition);
	CU_ASSERT_NOT_EQUAL(5,STIMA_GetTimer(STIMA_DoDetect));
	STIMA_Main();
	CU_ASSERT_NOT_EQUAL(5,STIMA_GetTimer(STIMA_DoDetect));
	STIMA_UT_SetConditionValue(1);
	STIMA_Main();
	CU_ASSERT_EQUAL(5,STIMA_GetTimer(STIMA_DoDetect));
	STIMA_UT_SetConditionValue(0);
	for(i=0;i<5;i++)
	{
		CU_ASSERT_EQUAL(5-i,STIMA_GetTimer(STIMA_DoDetect));
		CU_ASSERT_EQUAL(0,STIMA_UT_GetState());
		STIMA_Main();
	}
	CU_ASSERT_EQUAL(0,STIMA_GetTimer(STIMA_DoDetect));
	CU_ASSERT_EQUAL(1,STIMA_UT_GetState());
}

void STIMA_UnitTEST(void)
{
	CU_pSuite pSuite=NULL;
	CU_initialize_registry();
	printf("STIMA Starting...\n");
	STIMA_Init();

	pSuite = CU_add_suite("STIMA TIMEOUT", STIMA_initDefaultSuite, STIMA_cleanDefaultSuite);
	printf("STIMA Timeout Test...\n");
	CU_add_test(pSuite,"STIMA_UT_TIMEOUTTEST",STIMA_UT_TimeoutTest);

	pSuite = CU_add_suite("STIMA Reset", STIMA_initDefaultSuite, STIMA_cleanDefaultSuite);
	printf("STIMA Reset Condition Test...\n");
	CU_add_test(pSuite,"STIMA_UT_RESETEST",STIMA_UT_ResetTest);

	/*Run all tests using the CUnit Automatic interface*/
	CU_set_output_filename("STIMA");
	CU_list_tests_to_file();
	CU_automated_run_tests();
	CU_cleanup_registry();
	CU_get_error();

}
/*______ P R I V A T E - F U N C T I O N S ___________________________________*/

/*______ L O C A L - F U N C T I O N S _______________________________________*/

/*______ E N D _____ (fanmp.c) ____________________________________________*/
