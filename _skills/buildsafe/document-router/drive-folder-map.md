---
name: drive-folder-map
description: Maps local vault paths to Google Drive folder IDs for use by the document-router skill's Drive push step.
type: reference
---

# Google Drive Folder ID Map
_Used by `/route-inbox` Step 7 to push routed files to the correct Drive folder._
_Last audited: 2026-04-29_

## How to use
When pushing a file to Drive, look up its local destination path in the left column and use the folder ID in the right column as the `parentId` for `mcp__claude_ai_Google_Drive__create_file`.

---

## BuildSafe IQ

| Local Vault Path | Drive Folder ID |
|---|---|
| `BuildSafe IQ/` | `1L_4CO3ipqPC20fiFVahvAOfRBttc_Dhf` |
| `BuildSafe IQ/Finance/` | `10EQNZa7d9OhZsOheZHhz3w7m5LquAm0e` |
| `BuildSafe IQ/Operations/` | `1YsxLJU1znHZx1sBRXnNZJKGZbrf5EJB5` |
| `BuildSafe IQ/Operations/Daily Notes/` | `1U7kbHMFoZ9I3iCmyg-4EFcztWRkNqj07` |
| `BuildSafe IQ/Operations/Meeting Notes/` | `1P0RRpLFpt41cu-ATQ3uFz-lkbPQSpl7w` |
| `BuildSafe IQ/Marketing & Content/` | `1CMI30fYJ5g-fKyCziOMoNznDG7yLf_cW` |
| `BuildSafe IQ/Marketing & Content/Brand/` | `1RbWdr3CJwQLA6Rre-jXL9snGWmHsfJsR` |
| `BuildSafe IQ/Marketing & Content/GTM/` | `1yakE2rBdcAgiKQqvr2ipAEDiMNO0_pOf` |
| `BuildSafe IQ/Marketing & Content/Messaging/` | `1CMI30fYJ5g-fKyCziOMoNznDG7yLf_cW` _(use parent — folder not yet confirmed in Drive)_ |
| `BuildSafe IQ/Marketing & Content/Content/` | `1deqFWPHcCM6A-HD0TzuLtvxDqQ346cVe` |
| `BuildSafe IQ/Marketing & Content/Content/Pipeline/` | `1O9izqiTq24l-09P00IKI0yQe7u58YtV-` |
| `BuildSafe IQ/Marketing & Content/Research_Base/` | `1yUcvN0iFSCj_zQ8y2cT7MMEUsk3Bk1fn` |
| `BuildSafe IQ/Marketing & Content/Research_Base/Project_Oracle_Feeds/` | `1rWie_caCQET80favVX3hmvFv3FiwcRnx` |
| `BuildSafe IQ/Product/` | `1JnopatZnHClA474aGas3fqrxqwcsmbkl` |
| `BuildSafe IQ/Legal/` | `1G-XOzdrn1_SAo8OxIBxe5XXpBz14dLLD` |
| `BuildSafe IQ/Sales & CRM/` | `1JOPYxRiz09Ws0FDaTUkh5jVSwNWz9hRN` |
| `BuildSafe IQ/HR & Team/` | `1moTS8ZldyEzcwoO70hpwKGuIWqyScme8` |
| `BuildSafe IQ/Brokerage/` | `1qSypHOa_ZGr1s_Sto7kpisZFt81k1c8-` |

---

## Brokerage

| Local Vault Path | Drive Folder ID |
|---|---|
| `Brokerage/` | `1plhE_gfHcG2V_93eFXFDv8Y5clYySWcR` |
| `Brokerage/Finance/` | `1SmMCo07dOGzspCk_pXiHg-RknT5h9l1F` |
| `Brokerage/Operations/` | `1YSOzq-OlKrVccjC7t5Yq2ziwiyNu43-d` |
| `Brokerage/Marketing & Content/` | `1iA4oNrJeTNYr8rY0R12zA-JYtVni7H4J` |
| `Brokerage/Sales & CRM/` | `1iWe7CJoCEYnjx9ioxDAZ6UzFkWWFMZmc` |
| `Brokerage/HR & Team/` | `1E_EoMdDN-Ik1MAugjaOWj5CrHqHN5ruU` |
| `Brokerage/Legal/` | `1-dWF49rg5CMbjGym2geU4FE4RED_NZD5` |
| `Brokerage/Active_Submissions/` | `13L4PqEugqVuRPR8vIV93GpJlccCPNfBg` |

---

## _Personal

| Local Vault Path | Drive Folder ID |
|---|---|
| `_Personal/` | `1CmOwn23Pzy4WPp7kw-TTZ8HloCpnfGqx` |
| `_Personal/Finance/` | `1bPbH6qvgzPI4Dxim8PcEfpLKbOBeBQrK` |
| `_Personal/Health & Fitness/` | `1LaIBu61UYZsvPgcmKwtgI2ThUZYEazb1` |
| `_Personal/Goals/` | `1lG6rsee75R6zREQCXfbgkzsJA4VG8WEF` |

---

## _OS

| Local Vault Path | Drive Folder ID |
|---|---|
| `_OS/` | `1Um6pC47fz0W7nE_8ILy2hXMqmj6jmj8Y` |
| `_OS/Knowledge Base/` | `1FxUcWueCFQvtpb_8s2D5AkpuPJiPL4C9` |
| `_OS/Governance/` | `1JOHxAKLOhYndHRdFpmCsJxkr4hxTBABA` |
| `_OS/_brain/` | `1NK6sBLpRR7KscOKhQr6vpzvhEk1NL1x8` |
| `_OS/AI Skills/` | `1APuy_veFf37zne73MaG1nxp1tZXDMm00` |
| `_inbox/` | `13nFwabXbTAj_GOn4vCypnH_k8Y5AXir9` |

---

## Notes
- All IDs verified against live Drive as of 2026-04-29.
- If a subfolder doesn't exist in Drive yet, use the nearest parent ID and create the subfolder first using `mcp__claude_ai_Google_Drive__create_file` with `mimeType: application/vnd.google-apps.folder`.
- For `Brokerage/Active_Submissions/[client-name]/`, create the client subfolder under `13L4PqEugqVuRPR8vIV93GpJlccCPNfBg` if it doesn't exist.
