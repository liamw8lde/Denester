# Legacy Fault Investigation Archive (`E:\Denester_Fault`)

## 1. Already Extracted from `C6060007S_12.zip` (`2026-09` Fault Audit)

Byte-level inspection of [`C6060007S_12.zip`](../PLC_HMI_Archive/C6060007S_12.zip) confirmed that the September 2026 `Denester_Fault` work preserved the original `2016-03-17` validated OEM backup inside `ombstx/offline_ORIGINAL_BACKUP/` and `YDBs_ORIGINAL_BACKUP/` while updating `ombstx/offline/` and `YDBs/25319/SYMLIST.DBF`:

| Verification Check | Result | GAMP 5 Validation Impact |
| :--- | :--- | :--- |
| **Executable MC7 Block Checksums (`OB`, `FB`, `FC`, `DB`)** | **`0` bytes modified** across all `31` blocks (`2016-03-17` vs. `2026-09-16`) | Confirms [`C6060007S_12.zip`](../PLC_HMI_Archive/C6060007S_12.zip) holds the exact validated `MP1P-Ferring` machine logic. |
| **Symbol Table Audit (`SYMLIST.DBF`)** | **`362` symbols** translated from Italian (`IT`) into bilingual **`EN / DE`** | Saved in [`sept2026_denester_fault_diff.csv`](./sept2026_denester_fault_diff.csv) and ready for direct TIA Portal tag import in Phase 2. |
| **Know-How Protection (`PASSWORD`)** | **`0` protected blocks** | Full source transparency for Phase 2 `S7-1500` migration without OEM black-box lock-in. |

---

## 2. Importing Remaining Local Files from `E:\Denester_Fault`

Because the cloud agent runs on an isolated Linux VM and cannot directly mount your local Windows `E:\` drive, choose **either Option A or Option B** on your Windows PC to bring any remaining files from `E:\Denester_Fault` (electrical schematics PDFs, fault logs, photos, `ProSave` backups, or notes) into this folder:

### Option A — Drag & Drop into Antigravity Chat (Fastest)
1. Right-click `E:\Denester_Fault` in Windows Explorer → **Compress to ZIP file** (or run `.\tools\upload_denester_fault.ps1 -Mode Zip` in PowerShell).
2. Drag and drop `Denester_Fault_Upload.zip` into the chat message box and send `"Organize uploaded Denester_Fault zip"`.
3. The agent will unpack, classify, commit, and cross-reference every file into the Phase 1/2 engineering deliverables automatically.

### Option B — Direct 1-Click GitHub Push from PowerShell
Run [`tools/upload_denester_fault.ps1`](../../tools/upload_denester_fault.ps1) on your Windows PC:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\upload_denester_fault.ps1 -SourcePath "E:\Denester_Fault" -Mode GitPush
```

This automatically sorts every file from `E:\Denester_Fault` into clean GAMP 5 baseline subfolders:
- `Schematics_and_Manuals/` (`.pdf`, `.dwg`, `.dxf`, `.eplan`)
- `PLC_and_HMI_Exports/` (`.s7p`, `.awl`, `.scl`, `.pdb`, `.psb`, `.zip`)
- `Fault_Logs_and_Notes/` (`.txt`, `.md`, `.docx`, `.xlsx`, `.csv`, `.log`)
- `Photos_and_Videos/` (`.jpg`, `.png`, `.mp4`)
