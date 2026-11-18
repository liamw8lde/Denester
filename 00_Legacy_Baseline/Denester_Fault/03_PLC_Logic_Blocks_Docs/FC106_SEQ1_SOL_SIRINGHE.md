# `FC106` — `SEQ1_SOL_SIRINGHE`

- **EN**: Seq 1: Syringe lifter
- **DE**: Seq 1: Spritzenheber

## OEM Revision Header (`CO.RI.M.A. SRL`)

```text
***************************************************************************************************
* PROPRIETA'..........: CO.RI.M.A. SRL                                                            *
*                       via delle Vigne, 8                                                        *
*                       53100 loc. Tognazza (SI) ITALY                                            *
* TIPO MACCHINA.......: MP1                                                                       *
* TIPO DI BLOCCO......: SEQUENZA SOLLEVAMENTO SIRINGHE                                            *
* DESCRIZIONE.........: viene gestita la movimentazione per il sollevamento siringhe dal nest per *
*                       il prelievo della pinza sul pick&place di scarico                         *
*                                                                                                 *
* VERSIONE............: 0.0 del 3/10/2005                                                         *
* AUTORE..............: BOCCI                                                                     *
* DESCRIZIONE.........: EMISSIONE                                                                 *
*                                                                                                 *
*                                                                                                 *
* VERSIONE............: 0.1 del 15/06/2011                                                        *
* AUTORE..............: TRECCI                                                                    *
* DESCRIZIONE.........: REVISIONE:gestione nuovo formato nest 160                                 *
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
  SeqEnb : BOOL ;	//abilitazione seuqnza
  StopSeq : BOOL ;	
END_VAR
```

## Sequence / Network Titles (Original Italian)

1. `controllo fase stop`
2. `sequencer`
3. `attesa abilitazione nastro e presenza nest e fila siringhe`
4. `controlla se nest da 160 e fila dispari`
5. `attesa posizionatore esteso`
6. `attesa sollevatore alto`
7. `attesa trasferimento eseguito`
8. `attesa sollevatore basso e siringhe prelevate`
9. `controllo fila siringhe prelevate`
10. `attesa posizionatore retratto`
11. `salti fittizzi`
