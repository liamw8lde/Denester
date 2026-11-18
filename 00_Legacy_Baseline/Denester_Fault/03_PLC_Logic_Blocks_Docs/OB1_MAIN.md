# `OB1` — `MAIN`

- **EN**: General routine / Main loop
- **DE**: Hauptprogramm Allgemein

## OEM Revision Header (`CO.RI.M.A. SRL`)

```text
***************************************************************************************************
* PROPRIETA'..........: CO.RI.M.A. SRL                                                            *
*                       via delle Vigne, 8                                                        *
*                       53100 loc. Tognazza (SI) ITALY                                            *
* TIPO MACCHINA.......: MP1                                                                       *
* TIPO DI BLOCCO......: PRINCIPALE MACCHINA                                                       *
* DESCRIZIONE.........: vengono richiamate tutte le funzioni macchina                             *
*                                                                                                 *
* VERSIONE............: 0.0 del 3/10/2005                                                         *
* AUTORE..............: BOCCI                                                                     *
* DESCRIZIONE.........: EMISSIONE                                                                 *
*                                                                                                 *
* VERSIONE............: 0.1 del 15/06/2011                                                        *
* AUTORE..............: TRECCI                                                                    *
* DESCRIZIONE.........: REVISIONE: modificate per cambio formato nest                             *
*                                                                                                 *
* VERSIONE............: 0.2 del 14/03/2016                                                        *
* AUTORE..............: TRECCI                                                                    *
* DESCRIZIONE.........: REVISIONE: modificate per cambio formato nest 64                          *
*                                                                                                 *
***************************************************************************************************
```

## Block Interface (`VAR_INPUT / VAR_OUTPUT / VAR_TEMP`)

```iecst
VAR_TEMP
  OB1_EV_CLASS : BYTE ;	//Bits 0-3 = 1 (Coming event), Bits 4-7 = 1 (Event class 1)
  OB1_SCAN_1 : BYTE ;	//1 (Cold restart scan 1 of OB 1), 3 (Scan 2-n of OB 1)
  OB1_PRIORITY : BYTE ;	//1 (Priority of 1 is lowest)
  OB1_OB_NUMBR : BYTE ;	//1 (Organization block 1, OB1)
  OB1_RESERVED_1 : BYTE ;	//Reserved for system
  OB1_RESERVED_2 : BYTE ;	//Reserved for system
  OB1_PREV_CYCLE : INT ;	//Cycle time of previous OB1 scan (milliseconds)
  OB1_MIN_CYCLE : INT ;	//Minimum cycle time of OB1 (milliseconds)
  OB1_MAX_CYCLE : INT ;	//Maximum cycle time of OB1 (milliseconds)
  OB1_DATE_TIME : DATE_AND_TIME ;	//Date and time OB1 started
END_VAR
```

## Sequence / Network Titles (Original Italian)

1. `gestione stati macchina`
2. `Flag nest in lavorazione`
3. `master reset`
4. `master reset`
5. `gestione stati macchina`
6. `lampada colonna`
7. `gestione interfaccia terminale`
8. `gestione scarico siringhe`
9. `gestione sequenza sollevamento`
10. `gestione sequenza trasferimento`
11. `gestione sequenza guida scarico siringhe`
12. `gestione uscite fisiche`
13. `gestione allarmi`
14. `gestione natro nest`
15. `reset bit prima scansione`
16. `uscita`
