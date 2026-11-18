# Unpacked & Reorganized `Denester_Fault` Project (`C6060007S_12`)

The legacy `C6060007S_12.zip` (`MP1P-Ferring` Denester Fault archive) has been completely unpacked, decoded, and reorganized into clean, browsable folders below (while keeping the byte-identical master archive in [`../PLC_HMI_Archive/C6060007S_12.zip`](../PLC_HMI_Archive/C6060007S_12.zip) for GAMP 5 audit traceability):

| Folder | Contents |
| :--- | :--- |
| [`01_VAT1_Fault_Diagnostic_Table/`](./01_VAT1_Fault_Diagnostic_Table/) | All **`88` diagnostic variables** from the Sept 2026 `VAT_1` fault-finding watch table (`VAT1_Denester_Fault_WatchTable.csv` + ready-to-import `VAT1_TIA_Portal_WatchTable.tsv` for `S7-1500`). |
| [`02_PLC_DataBlocks_Source/`](./02_PLC_DataBlocks_Source/) | Human-readable `.db` STEP 7 `STRUCT` source files for all **`9` Data Blocks** (`DB10`–`DB12`, `DB20`–`DB21`, `DB90`, `DB100`, `DB105`, `DB106`). |
| [`03_PLC_Logic_Blocks_Docs/`](./03_PLC_Logic_Blocks_Docs/) | Human-readable `.md` documentation for all **`22` logic & system blocks** (`OB1`, `OB100`, `FB11`, `FB50`, `FC10`–`FC109`, `SFB47`, `SFC0`, `SFC1`) including `CO.RI.M.A. SRL` revision headers, `VAR_INPUT/OUTPUT` interfaces, and network step titles. |
| [`04_ProTool_HMI_TP170B/`](./04_ProTool_HMI_TP170B/) | Separated `TDOP_Project/` (`PRO.PDB`, `S7TDOP.DBF`) + [`protool_screens.csv`](./04_ProTool_HMI_TP170B/protool_screens.csv) (`37` screens) + [`protool_hmi_tags.csv`](./04_ProTool_HMI_TP170B/protool_hmi_tags.csv). |
| [`05_STEP7_Clean_Project/`](./05_STEP7_Clean_Project/C6060007S_12/) | Clean unpacked active STEP 7 v5.7 project (`C6060007.s7p`) with duplicate backup folders removed for clean SIMATIC Manager opening. |
| [`06_Original_2016_Backup/`](./06_Original_2016_Backup/) | Isolated `2016-03-17` `offline_ORIGINAL_BACKUP/` & `YDBs_ORIGINAL_BACKUP/` + [`sept2026_denester_fault_diff.csv`](./06_Original_2016_Backup/sept2026_denester_fault_diff.csv) proving `0` MC7 logic bytes changed. |

---

## Optional: Adding Extra Local Files from `E:\Denester_Fault` (If Any Exist Outside `C6060007S_12.zip`)

Why couldn't the cloud chat read `E:\Denester_Fault` directly? Because this web/cloud chat runs on a remote Google server on the internet (not installed on your Windows PC), so it has no physical connection to your PC's `E:\` drive.
- If `C6060007S_12.zip` was the whole project: **everything is already unpacked and pushed to GitHub above!**
- If you also have extra PDFs, photos, or notes sitting only on your local `E:\` drive, either drag-and-drop them into this chat window OR open the repository in the **Antigravity Desktop** app on your Windows PC.
