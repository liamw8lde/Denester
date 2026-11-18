# `FC11` — `MOV_PISTONE`

- **EN**: Piston movement control
- **DE**: Zylinderbewegung Steuerung

## OEM Revision Header (`CO.RI.M.A. SRL`)

```text
***************************************************************************************************
* PROPRIETA'..........: CO.RI.M.A. SRL                                                            *
*                       via delle Vigne, 8                                                        *
*                       53100 loc. Tognazza (SI) ITALY                                            *
* TIPO MACCHINA.......: TUTTE                                                                     *
* TIPO DI BLOCCO......: CONTROLLO PISTONE DIGITALE                                                *
* DESCRIZIONE.........: viene comandato un pistone con valvola digitale. Si controllano i sensori *
*                       per la posizione di tutto esteso e tutto retratto con i prori allarmi.    *
*                                                                                                 *
* VERSIONE............: 0.0 del 3/01/2003                                                         *
* AUTORE..............: BOCCI                                                                     *
* DESCRIZIONE.........: EMISSIONE                                                                 *
*                                                                                                 *
***************************************************************************************************
```

## Block Interface (`VAR_INPUT / VAR_OUTPUT / VAR_TEMP`)

```iecst
VAR_INPUT
  SenExt : BOOL ;	
  SenRet : BOOL ;	
  Comando : BOOL ;	
  Reset : BOOL ;	
  TimeOut : TIMER ;	
  SecTime : S5TIME ;	
END_VAR
VAR_OUTPUT
  ValExt : BOOL ;	
  ValRet : BOOL ;	
  MesNoExt : BOOL ;	
  MesNoRet : BOOL ;	
END_VAR
```

## Sequence / Network Titles (Original Italian)

1. `comando pistone`
2. `Gestione Pinza 1`
3. `...controllo time-out`
4. `reset allarmi`
5. `...controllo messaggio pistone esteso`
6. `...controllo messaggio pistone retratto`
