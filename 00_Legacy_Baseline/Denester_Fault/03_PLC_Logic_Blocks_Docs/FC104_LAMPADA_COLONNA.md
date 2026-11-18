# `FC104` — `LAMPADA_COLONNA`

- **EN**: Beacon lamp control
- **DE**: Signalsaeulen-Steuerung

## OEM Revision Header (`CO.RI.M.A. SRL`)

```text
***************************************************************************************************
* PROPRIETA'..........: CO.RI.M.A. SRL                                                            *
*                       via delle Vigne, 8                                                        *
*                       53100 loc. Tognazza (SI) ITALY                                            *
* TIPO MACCHINA.......: MP1                                                                       *
* TIPO DI BLOCCO......: LAMPADA COLONNA                                                           *
* DESCRIZIONE.........: gestione personalizzazione lampada a colonna                              *
*                       STANDARD MG 3 COLORI:                                                     *
*                       - ROSSA   FISSA: sono presenti allarmi o warning, esclude VERDE e ARANCIO *
*                                 FLASH: non applicata                                            *
*                       - ARANCIO FISSA: in automatico o manuale in caso di carichi minimi con    *
*                                        ripartenza automatica                                    *
*                                 FLASH: non applicata                                            *
*                       - VERDE   FISSA: in automatico                                            *
*                                 FLASH: in manuale o stop in assenza di allarmi/warning e        *
*                                        pronta a partire con start o jog                         *
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
  RossaFix : BOOL ;	
  RossaFlash : BOOL ;	
END_VAR
```

## Sequence / Network Titles (Original Italian)

1. `test lampade`
2. `lampada colonna ROSSA`
3. `gestione della colona di seganlazione luminosa
- lampada verde lampeggiante indica che siamo pronti per partire
- lampada verde fissa indica che la macchina e' in lavorazione
- lampada rossa fissa indica che la macchina e' in allarme
- lampada blu lampeggiante indica condizioni di carichi min o scarichi max
- lampada arancione fissa indica che la macchina e' ferma e riparte in modo 
  automatico`
4. `lampada colonna ARANCIONE`
5. `lampada colonna VERDE`
6. `salto fittizio per label`
