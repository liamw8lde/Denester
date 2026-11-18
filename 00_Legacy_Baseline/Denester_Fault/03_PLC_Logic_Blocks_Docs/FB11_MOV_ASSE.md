# `FB11` — `MOV_ASSE`

- **EN**: Pneumatic axis movement control
- **DE**: Pneumatikachse Bewegung

## OEM Revision Header (`CO.RI.M.A. SRL`)

```text
***************************************************************************************************
* PROPRIETA'..........: CO.RI.M.A. SRL                                                            *
*                       via delle Vigne, 8                                                        *
*                       53100 loc. Tognazza (SI) ITALY                                            *
* TIPO MACCHINA.......: TUTTE                                                                     *
* TIPO DI BLOCCO......: CONTROLLO PISTONE ANALOGICO                                               *
* DESCRIZIONE.........: viene comandato un pistone con valvola analogica tramite comando analogico*
*                       in tensione 0...10V. Il pistone e' a riposo quando la tensione è 5V, con  *
*                       tensione 0V il pistone viene comandato alla massima velocità in direzione *
*                       negativa, con tensione 10V il pistone viene comandato alla massima        *
*                       velocita in direzione positiva. la funzione esegue anche l'accelerazione e*
*                       la decelerazione sui sensori di pre-esteso e pre-retratto. Si controlla   *
*                       anche la posizione di tutto esteso e tutto retratto con i prori allarmi.  *
*                                                                                                 *
* VERSIONE............: 0.0 del 21/6/2003                                                         *
* AUTORE..............: BOCCI                                                                     *
* DESCRIZIONE.........: EMISSIONE                                                                 *
*                                                                                                 *
* VERSIONE............: 0.1 del 12/10/2005                                                        *
* AUTORE..............: BOCCI                                                                     *
* DESCRIZIONE.........: modificata struttura SP di ingresso da parametri INT a parametri BYTE per *
*                       quadagnare memoria nella struttura parametri del DB LAVORO, inserito      *
*                       azzeramento variabile temporanea Analog (INT) prche viene caricata con un *
*                       BYTE.                                                                     *
*                                                                                                 *
***************************************************************************************************
```

## Block Interface (`VAR_INPUT / VAR_OUTPUT / VAR_TEMP`)

```iecst
VAR_INPUT
  Ret : BOOL ;	//sensore retratto
  PreRet : BOOL ;	//sensore pre-retratto
  PreExt : BOOL ;	//sensore pre-esteso
  Ext : BOOL ;	//sensore esteso
  Comando : BOOL ;	//comando pistone
  Reset : BOOL ;	//comando reset allarmi
  TimeOut : TIMER ;	//temporizzatore time-out
  SecTime : S5TIME ;	//tempo time-out
  InsAria : BOOL ;	//aria non inserita
  SP : STRUCT 	//set-point ingresso
   ExtVel : BYTE ;	
   ExtAcc : BYTE ;	
   ExtDec : BYTE ;	
   RetVel : BYTE ;	
   RetAcc : BYTE ;	
   RetDec : BYTE ;	
  END_STRUCT ;	
END_VAR
VAR_OUTPUT
  AnaOut : WORD ;	//set-point canale analogico
  MesNoExt : BOOL ;	//messaggio allarme no esteso
  MesNoRet : BOOL ;	//messaggio allarme no retratto
END_VAR
VAR
  step0 : BOOL ;	
  ext1 : BOOL ;	
  ext2 : BOOL ;	
  ext3 : BOOL ;	
  ret1 : BOOL ;	
  ret2 : BOOL ;	
  ret3 : BOOL ;	
  step1 : BOOL ;	
  retratto : BOOL  := TRUE;	
  esteso : BOOL ;	
END_VAR
VAR_TEMP
  Analog : INT ;	
END_VAR
```

## Sequence / Network Titles (Original Italian)

1. `comando movimento in ESTESO`
2. `comando movimento in RETRATTO`
3. `azzeramento variabile temporanea`
4. `muove ESTESO - attesa sensore PRE_RETRATTO`
5. `muove ESTESO - attesa sensore PRE_ESTESO`
6. `muove ESTESO - attesa sensore ESTESO`
7. `muove ESTESO - comando stazionamento pistone ESTESO`
8. `muove RETRATTO - attesa sensore PRE_ESTESO`
9. `muove RETRATTO - attesa sensore PRE_RETRATTO`
10. `muove RETRATTO - attesa sensore RETRATTO`
11. `muove RETRATTO - comando stazionamento pistone RETRATTO`
12. `conversione da INT to BIN`
13. `...controllo time-out`
14. `reset allarmi`
15. `...controllo messaggio pistone esteso`
16. `...controllo messaggio pistone retratto`
17. `se seq ins aria non conclusa muove piano il pistone`
