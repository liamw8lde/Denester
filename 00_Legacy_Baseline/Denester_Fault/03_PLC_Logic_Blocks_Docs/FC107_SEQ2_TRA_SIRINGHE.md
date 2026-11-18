# `FC107` — `SEQ2_TRA_SIRINGHE`

- **EN**: Seq 2: Syringe transfer head
- **DE**: Seq 2: Spritzenumsetzer

## OEM Revision Header (`CO.RI.M.A. SRL`)

```text
***************************************************************************************************
* PROPRIETA'..........: CO.RI.M.A. SRL                                                            *
*                       via delle Vigne, 8                                                        *
*                       53100 loc. Tognazza (SI) ITALY                                            *
* TIPO MACCHINA.......: MP1                                                                       *
* TIPO DI BLOCCO......: SEQUENZA TRASFERIMENTO                                                    *
* DESCRIZIONE.........: viene gestita la movimentazione per lo scarico siringhe nella guida       *
*                       d'uscita, vine controllato lo scarico massimo e l'interfaccia con la      *
*                       macchina a valle.                                                         *
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
  step0 : BOOL ;	
  step1 : BOOL ;	
  step2 : BOOL ;	
  step3 : BOOL ;	
  step4 : BOOL ;	
  step5 : BOOL ;	
  step6 : BOOL ;	
  step7 : BOOL ;	
  step8 : BOOL ;	
  step9 : BOOL ;	
  step10 : BOOL ;	
  step11 : BOOL ;	
  step12 : BOOL ;	
  step13 : BOOL ;	
  step14 : BOOL ;	
  step15 : BOOL ;	
  SeqEnb : BOOL ;	
END_VAR
```

## Sequence / Network Titles (Original Italian)

1. `abilitazione esecuzione passo`
2. `sequencer`
3. `apre pinza`
4. `attesa abilitazione da sollevatore`
5. `attesa asse Y basso`
6. `attesa pinza chiusa`
7. `attesa asse Y alto; abilitazione da valle`
8. `attesa asse X allo scarico`
9. `attesa pinza aperta`
10. `attesa asse X al carico`
