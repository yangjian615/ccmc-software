/*******************************************************************************
 *                                                                             *
 *       NAME:          var_exists.c                                           *
 *                                                                             *
 *       VERSION:       1.0                                                    *
 *                                                                             *
 *       AUTHOR:        Marlo M. H. Maddox                                     *
 *                      NASA-GSFC-AETD-ISD-ADMA(587)-CCMC                      *
 *                      Marlo.Maddox@nasa.gov                                  *
 *                      (301) 286 - 5202                                       *
 *                                                                             *
 *       PURPOSE:       Checks for the existence of a specified variable in    *
 *                      currently open cdf file                                *
 *                                                                             *
 *       INPUTS:        int var_exists( char *variable_name )                  *
 *                                                                             *
 *       OUTPUTS:                                                              *
 *                                                                             *
 *       FUNCTIONS:                                                            *
 *                                                                             *
 *       VARIABLES:                                                            *
 *                                                                             *
 *       MODIFICATION                                                          *
 *       HISTORY:                                                              *
 *                                                                             *
 *       10.30.2006     Maddox, Marlo                                          *
 *                      Initial Development Started                            *
 ******************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "cdf.h"

#define DEBUG_FLAG 0

int var_exists(
      char *variable_name)
{

   if (CDFlib( CONFIRM_, zVAR_EXISTENCE_, variable_name, NULL_) == CDF_OK)
   {
      /** specified variable exists in currently open CDF file **/
      return 1;
   }
   else
   {
      return 0;
   }

}

