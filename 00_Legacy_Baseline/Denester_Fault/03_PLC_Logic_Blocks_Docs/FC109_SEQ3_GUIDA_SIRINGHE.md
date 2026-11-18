# `FC109` — `SEQ3_GUIDA_SIRINGHE`

- **EN**: Seq 3: Extraction guide
- **DE**: Seq 3: Entnahmefuehrung

## OEM Revision Header (`CO.RI.M.A. SRL`)

```text
***************************************************************************************************
* PROPRIETA'..........: CO.RI.M.A. SRL                                                            *
*                       via delle Vigne, 8                                                        *
*                       53100 loc. Tognazza (SI) ITALY                                            *
* TIPO MACCHINA.......: MP1                                                                       *
* TIPO DI BLOCCO......: SEQUENZA SCARICAMENTO GUIDA SIRINGHE                                      *
* DESCRIZIONE.........: viene gestita la movimentazione per lo scarico siringhe nella guida       *
*                       d'uscita, vine controllato lo scarico massimo e l'interfaccia con la      *
*                       macchina a valle.                                                         *
*                                                                                                 *
* VERSIONE............: 0.0 del 18/01/2007                                                        *
* AUTORE..............: TRECCI                                                                    *
* DESCRIZIONE.........: EMISSIONE                                                                 *
*                                                                                                 *
***************************************************************************************************
```

## Block Interface (`VAR_INPUT / VAR_OUTPUT / VAR_TEMP`)

```iecst
VAR_TEMP
  Step0 : BOOL ;	
  Step1 : BOOL ;	
  Step2 : BOOL ;	
  Step3 : BOOL ;	
  Step4 : BOOL ;	
  Step5 : BOOL ;	
  Step6 : BOOL ;	
  Step7 : BOOL ;	
  Step8 : BOOL ;	
  Step9 : BOOL ;	
  Step10 : BOOL ;	
  Step11 : BOOL ;	
  Step12 : BOOL ;	
  Step13 : BOOL ;	
  Step14 : BOOL ;	
  Step15 : BOOL ;	
  SeqEnb : BOOL ;	
END_VAR
```

## Sequence / Network Titles (Original Italian)

1. `abilitazione esecuzione passo`
2. `sequencer`
3. `attesa abilitazione da trasferitore siringhe`
4. `comando estrattore siringhe alto`
5. `attesa estrattore siringhe alto e chk scarico max e valle`
6. `comando estrattore siringhe avanti`
7. `attesa estrattore siringhe avanti`
8. `comando estrattore siringhe indietro`
9. `attesa estrattore siringhe indietro`
10. `comando estrattore siringhe basso e enb a seq trasferisci sir`
