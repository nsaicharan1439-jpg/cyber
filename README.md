# 🛡️ SentinelChain AI

> **GenAI Platform for Automated Content Transformation**  
> *Specialized for Cybersecurity Operations & Blockchain Integrity*  
> **100% Python Modules Architecture**

---

## 🌟 Executive Overview

**SentinelChain AI** is an autonomous GenAI platform specifically engineered to solve the acute challenge of unstructured technical content in **Cybersecurity** and **Blockchain** environments. 

Raw threat intelligence, firewall/syslog dumps, vulnerability disclosures (CVEs), and smart contract code are continuously ingested and automatically transformed into:
1. **MITRE ATT&CK Mapped SOC Incident Runbooks & Containment Scripts**
2. **Audited & Hardened Smart Contracts (SWC Vulnerability Mapping & OpenZeppelin Patches)**
3. **Dual-Audience C-Suite Risk Briefings & DevSecOps Engineering Patch Plans**
4. **Custom STIX 2.1 Bundles, YARA Detection Rules & Cryptographic Explanations**

Every transformed output is automatically stamped with an **Ed25519 digital signature**, cryptographically fingerprinted via **SHA-256**, and anchored onto a **Local Hash-Chained Blockchain Ledger with Merkle Tree Roots** for zero-tamper authenticity.

---

## 🚀 Key Features

### 1. Multi-Pipeline Automated Content Transformation
- **Incident & Threat Intelligence Transformer**: Ingests raw auth logs, syslog, or firewall alerts, extracts IoCs (IPs, domains, hashes), deduces MITRE ATT&CK techniques (T1110, T1190, T1078), and generates automated Linux `iptables` and Sigma rules.
- **Smart Contract Security Auditor & Hardener**: Performs static analysis on Solidity contracts, flags critical SWC vulnerabilities (SWC-107 Reentrancy, SWC-115 `tx.origin` authentication bypass, SWC-104 unchecked calls), and outputs hardened OpenZeppelin v5.0 code alongside Foundry exploit test suites.
- **Vulnerability Advisory Transformer**: Transforms complex CVE disclosures (e.g. CVE-2024-3094) into executive business risk memos (financial liability under GDPR, SEC, and DORA) and technical DevSecOps command-line patch procedures.
- **Custom Transformation Studio**: Prompt-driven restructuring for STIX/TAXII, YARA rules, and Zero-Knowledge cryptographic explainers.

### 2. Built-in Cryptographic Blockchain Ledger (100% Python)
- **Hash-Chained Blocks**: Every block links to the previous block via SHA-256 with proof-of-work/stamping difficulty.
- **Merkle Tree Root Generation**: Calculates deterministic Merkle roots over all transformation transactions.
- **Proof-of-Authority Node Signing**: Uses Ed25519 elliptic curve keypairs to sign every transformation report.
- **Cryptographic Certificate**: Produces downloadable proof-of-transformation certificates with block index, SHA-256 digests, and signatures.

### 3. Autonomous Zero-Leak Secret Redactor
- Pre-processing security layer that strips Ethereum private keys, BIP-39 mnemonic seed phrases (12/24 words), AWS access keys, database passwords, and API tokens before content is processed by the AI or saved to disk.

### 4. Forensic Tamper Verification Lab
- One-click cryptographic lookup: Paste any report or code snippet to verify if its SHA-256 hash exists in the blockchain.
- **Interactive Tamper Simulator**: Modifying even 1 single character breaks the hash and triggers an immediate cryptographic tamper alert (demonstrating the SHA-256 Avalanche Effect).

### 5. Dual Engine: Online GenAI + Autonomous Offline CyberAI
- Seamlessly integrates with **Google Gemini** (`gemini-2.5-flash`, `gemini-2.5-pro`) via the official `google-genai` SDK.
- Automatically falls back to a built-in **Deterministic Heuristic Cyber Engine** when offline or without an API key, allowing the platform to run 100% locally out-of-the-box!

---

## 📂 Project Architecture

```
Cyber security/
├── app.py                             # Main Streamlit Application Entrypoint
├── core/                              # Cryptographic & Blockchain Foundation
│   ├── blockchain.py                  # Hash-Chained Merkle Block Ledger
│   ├── crypto_signer.py               # Ed25519 Signer & Digital Certificate Generator
│   ├── sanitizer.py                   # Zero-Leak Secret & PII Redactor
│   └── config.py                      # System Configuration & Path Manager
├── engines/                           # Transformation Pipelines
│   ├── ai_client.py                   # Unified GenAI Client (Gemini + Local CyberAI)
│   ├── threat_intel_transformer.py    # Logs -> MITRE ATT&CK & SOC Runbooks
│   ├── smart_contract_auditor.py      # Solidity -> Audited & Hardened Code
│   ├── advisory_transformer.py        # CVEs -> Executive Briefs & Patch Guides
│   └── custom_studio.py               # Custom Cyber/Crypto Transformation Studio
├── ui/                                # Cyberpunk Web3 Design System
│   ├── styles.py                      # Glassmorphism & Neon CSS Tokens
│   ├── components.py                  # Metric Cards, Certificates, Tamper Badges
│   └── views/                         # Modular Dashboard & Lab Views
├── samples/                           # Ready-to-Test Datasets
│   ├── sample_smart_contract.sol      # Vulnerable Solidity Contract (Reentrancy)
│   ├── sample_incident_log.log        # Raw Auth Log with Embedded Secrets
│   ├── sample_cve_report.json         # Real-world CVE-2024-3094 Vulnerability Data
│   └── sample_threat_feed.txt         # Threat Campaign Intelligence
├── tests/                             # Automated Unit Test Suite
│   ├── test_blockchain.py             # Blockchain & Tamper Detection Tests
│   ├── test_sanitizer.py              # Secret Redaction Tests
│   └── test_transformers.py           # Transformation Engine Tests
├── requirements.txt                   # Pinned Dependencies (100% Python)
├── pyproject.toml                     # Python Project Metadata
├── setup_env.bat / setup_env.ps1      # 1-Click Environment Setup Scripts
└── run.bat / run.ps1                  # 1-Click Platform Launchers
```

---

## ⚡ Quick Start Guide

### Option 1: 1-Click Setup (Windows)
Double-click `setup_env.bat` (or run `.\setup_env.ps1` in PowerShell).  
This automatically detects `uv` or Python, creates a `.venv` in Python 3.12, installs all packages, and creates `.env`.

Then launch the platform:
```cmd
run.bat
```
or in PowerShell:
```powershell
.\run.ps1
```

### Option 2: Manual Terminal Commands
```powershell
# 1. Create Virtual Environment
uv venv .venv --python 3.12
# Or: python -m venv .venv

# 2. Install Dependencies
uv pip install -r requirements.txt --python .\.venv\Scripts\python.exe
# Or: .\.venv\Scripts\pip install -r requirements.txt

# 3. Launch SentinelChain Platform
.\.venv\Scripts\streamlit.exe run app.py
```

Open your browser to: **`http://localhost:8501`**

---

## 🧪 Running Automated Tests

Verify blockchain integrity, tamper detection, and transformation pipelines:
```powershell
.\.venv\Scripts\python.exe -m unittest discover tests
```

---

## 🔒 Security & Privacy Notice
All transformations run with **Zero-Leak Redaction** enabled by default. Cryptographic private keys and seed phrases are masked in memory prior to transformation. Ledger blocks and keys are stored locally in the `data/` directory.
