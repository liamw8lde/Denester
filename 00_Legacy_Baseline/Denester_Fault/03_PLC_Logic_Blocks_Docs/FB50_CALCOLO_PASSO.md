# `FB50` — `CALCOLO_PASSO`

- **EN**: Format pitch calculation
- **DE**: Schritt-Berechnung Format

## OEM Revision Header (`CO.RI.M.A. SRL`)

```text
***************************************************************************************************
* PROPRIETA'..........: CO.RI.M.A. SRL                                                            *
*                       via delle Vigne, 8                                                        *
*                       53100 loc. Tognazza (SI) ITALY                                            *
* TIPO MACCHINA.......: MP1                                                                       *
* TIPO DI BLOCCO......: CALCOLO PASSO NASTRO NEST                                                 *
* DESCRIZIONE.........: in base al formato nest si calcola il passo nest, I DB di istanza         *
*                       contengono i passi relativi al formato in uso, i dati sono inseriti       *
*                       manualmente nel DB di formato.                                            *
*                       Ogni volta che l'encoder supera la quota puntata dalla posizione,         *
*                       viene settata l'uscita raggiunta della funzione.                          *
*                       L'uscita raggiuta della funzione deve essere elaborata dal programma di   *
*                       richiamo ed azzerata secondo proprie necessità.                           *
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
  ActualPos : DINT ;	//posizione encoder
END_VAR
VAR_OUTPUT
  NextPos : INT ;	//posizione successiva
END_VAR
VAR_IN_OUT
  NrPos : INT  := 1;	//numero posizione
  CmdMove : BOOL ;	//comando movimento
  PosReserced : BOOL ;	//posizione puntata raggiunta
END_VAR
VAR
  FineTabella : INT ;	//indice di fine tabella 
  P1 : INT ;	//passo nest
  P2 : INT ;	
  P3 : INT ;	
  P4 : INT ;	
  P5 : INT ;	
  P6 : INT ;	
  P7 : INT ;	
  P8 : INT ;	
  P9 : INT ;	
  P10 : INT ;	
  P11 : INT ;	
  P12 : INT ;	
  P13 : INT ;	
  P14 : INT ;	
  P15 : INT ;	
  P16 : INT ;	
  P17 : INT ;	
  P18 : INT ;	
  P19 : INT ;	
  P20 : INT ;	
  AppRead : BOOL ;	
  Read : BOOL ;	
  AppMove : BOOL ;	
END_VAR
VAR_TEMP
  AdrPunta : DWORD ;	
END_VAR
```

## Sequence / Network Titles (Original Italian)

1. `gestione indice tabella e quota`
