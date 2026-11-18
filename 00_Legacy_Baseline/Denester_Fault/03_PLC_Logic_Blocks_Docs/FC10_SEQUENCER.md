# `FC10` — `SEQUENCER`

- **EN**: Sequence step manager
- **DE**: Schrittketten-Verwaltung

## OEM Revision Header (`CO.RI.M.A. SRL`)

```text
***************************************************************************************************
* PROPRIETA'..........: CO.RI.M.A. SRL                                                            *
*                       via delle Vigne, 8                                                        *
*                       53100 loc. Tognazza (SI) ITALY                                            *
* TIPO MACCHINA.......: TUTTE                                                                     *
* TIPO DI BLOCCO......: SEQUENCER                                                                 *
* DESCRIZIONE.........: viene convertito numero in ingresso (BYTE) in passo (BIT) (MAX OUT 16BIT) *
*                                                                                                 *
* VERSIONE............: 0.0 del 3/10/2005                                                         *
* AUTORE..............: BOCCI                                                                     *
* DESCRIZIONE.........: EMISSIONE                                                                 *
*                                                                                                 *
***************************************************************************************************
```

## Block Interface (`VAR_INPUT / VAR_OUTPUT / VAR_TEMP`)

```iecst
VAR_INPUT
  NrPasso : BYTE ;	
END_VAR
VAR_OUTPUT
  BitPasso : WORD ;	
END_VAR
VAR_TEMP
  Passo : WORD ;	
END_VAR
```

## Sequence / Network Titles (Original Italian)

1. `converte il NR di passo nel BIT di passo`
