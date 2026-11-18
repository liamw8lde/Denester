# `OB100` — `AVVIAMENTO`

- **EN**: Startup routine (Power on)
- **DE**: Anlaufprogramm / Neustart

## OEM Revision Header (`CO.RI.M.A. SRL`)

```text
***************************************************************************************************
* PROPRIETA'..........: CO.RI.M.A. SRL                                                            *
*                       via delle Vigne, 8                                                        *
*                       53100 loc. Tognazza (SI) ITALY                                            *
* TIPO MACCHINA.......: MP1                                                                       *
* TIPO DI BLOCCO......: AVVIAMENTO                                                                *
* DESCRIZIONE.........: vengono inizializzate le variabili macchina                               *
*                                                                                                 *
* VERSIONE............: 0.0 del 3/10/2005                                                         *
* AUTORE..............: BOCCI                                                                     *
* DESCRIZIONE.........: EMISSIONE                                                                 *
*                                                                                                 *
***************************************************************************************************
```

## Block Interface (`VAR_INPUT / VAR_OUTPUT / VAR_TEMP`)

```iecst
VAR_TEMP
  OB100_EV_CLASS : BYTE ;	//16#13, Event class 1, Entering event state, Event logged in diagnostic buffer
  OB100_STRTUP : BYTE ;	//16#81/82/83/84 Method of startup
  OB100_PRIORITY : BYTE ;	//27 (Priority of 1 is lowest)
  OB100_OB_NUMBR : BYTE ;	//100 (Organization block 100, OB100)
  OB100_RESERVED_1 : BYTE ;	//Reserved for system
  OB100_RESERVED_2 : BYTE ;	//Reserved for system
  OB100_STOP : WORD ;	//Event that caused CPU to stop (16#4xxx)
  OB100_STRT_INFO : DWORD ;	//Information on how system started
  OB100_DATE_TIME : DATE_AND_TIME ;	//Date and time OB100 started
END_VAR
```

## Sequence / Network Titles (Original Italian)

1. `prepara variabili`
