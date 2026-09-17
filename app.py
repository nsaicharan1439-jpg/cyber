"""SentinelChain AI - GenAI Platform for Automated Content Transformation."""
import os
import streamlit as st
from ui.styles import inject_cyber_styles
from core.blockchain import Blockchain
from core.crypto_signer import CryptoSigner
from core.config import settings
from engines.ai_client import AIClient
from ui.views import (
    render_dashboard_view,
    render_transform_studio_view,
    render_smart_contract_view,
    render_ledger_explorer_view,
    render_tamper_verify_view,
)

# Page Configuration
st.set_page_config(
    page_title="SentinelChain AI // Cyber & Blockchain Transformation",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Inject Cyberpunk & Web3 CSS
st.markdown(inject_cyber_styles(), unsafe_allow_html=True)

# Session State Initialization
if "blockchain" not in st.session_state:
    st.session_state["blockchain"] = Blockchain()

if "crypto_signer" not in st.session_state:
    st.session_state["crypto_signer"] = CryptoSigner()

blockchain: Blockchain = st.session_state["blockchain"]
crypto_signer: CryptoSigner = st.session_state["crypto_signer"]

# Sidebar Configuration
with st.sidebar:
    st.markdown(
        """
        <div style="padding: 10px 0 20px 0; text-align: center;">
            <div style="font-size: 2.2rem; filter: drop-shadow(0 0 10px #00f5d4);">🛡️</div>
            <h2 style="margin: 6px 0 0 0; font-weight: 800; letter-spacing: -0.02em; color: #f8fafc;">
                SENTINEL<span style="color: #00f5d4;">CHAIN</span>
            </h2>
            <p style="font-size: 0.75rem; color: #94a3b8; font-family: var(--font-mono); margin-top: 4px;">
                GENAI CONTENT TRANSFORMATION
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### 🧭 Navigation")
    nav_selection = st.radio(
        "Platform Modules",
        [
            "⚡ Command Center",
            "🚀 Transformation Studio",
            "🛡️ Smart Contract Lab",
            "⛓️ Blockchain Explorer",
            "🔬 Forensic Tamper Lab",
        ],
        label_visibility="collapsed"
    )

    st.markdown("---")
    st.markdown("### ⚙️ Engine Settings")

    api_key_input = st.text_input(
        "Gemini API Key (Optional)",
        value=settings.GEMINI_API_KEY,
        type="password",
        help="Leave blank to run in Autonomous Local CyberAI Mode without network dependencies."
    )

    selected_model = st.selectbox(
        "AI Generation Model",
        ["gemini-2.5-flash", "gemini-2.5-pro", "gemini-2.0-flash"],
        index=0
    )

    # Initialize AI Client
    ai_client = AIClient(api_key=api_key_input, model=selected_model)

    # Status indicator
    if ai_client.is_online:
        st.markdown(
            """
            <div class="badge-online" style="margin: 8px 0; width: 100%; justify-content: center;">
                <span class="badge-pulse"></span>
                <span>ONLINE // GEMINI ACTIVE</span>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            """
            <div class="badge-online" style="margin: 8px 0; width: 100%; justify-content: center; border-color: rgba(0, 180, 216, 0.4); color: #00b4d8;">
                <span>⚡ LOCAL CYBER-AI ACTIVE</span>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")
    # Sovereign Node Identity Info
    pubkey = crypto_signer.get_public_key_hex()
    st.markdown(
        f"""
        <div style="font-family: var(--font-mono); font-size: 0.72rem; color: #64748b; background: rgba(0,0,0,0.3); padding: 10px; border-radius: 6px;">
            <span style="color: #94a3b8;">NODE AUTHORITY ID:</span><br/>
            <code style="color: #c084fc; word-break: break-all;">{pubkey[:18]}...{pubkey[-8:]}</code><br/><br/>
            <span style="color: #94a3b8;">CHAIN HEIGHT:</span> <span style="color: #00f5d4; font-weight: 700;">#{len(blockchain.chain)}</span><br/>
            <span style="color: #94a3b8;">POW DIFFICULTY:</span> <span style="color: #f59e0b;">{blockchain.difficulty}</span>
        </div>
        """,
        unsafe_allow_html=True
    )

# View Dispatcher
if nav_selection == "⚡ Command Center":
    render_dashboard_view(blockchain)
elif nav_selection == "🚀 Transformation Studio":
    render_transform_studio_view(blockchain, crypto_signer, ai_client)
elif nav_selection == "🛡️ Smart Contract Lab":
    render_smart_contract_view(blockchain, crypto_signer, ai_client)
elif nav_selection == "⛓️ Blockchain Explorer":
    render_ledger_explorer_view(blockchain)
elif nav_selection == "🔬 Forensic Tamper Lab":
    render_tamper_verify_view(blockchain, crypto_signer)
