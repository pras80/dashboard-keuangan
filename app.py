import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import io

# ==========================================
# 1. PAGE CONFIG & POWER BI / TABLEAU ENTERPRISE STYLING
# ==========================================
st.set_page_config(
    page_title="Executive Financial Decision Support Platform",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling (Power BI Clean White Executive Theme)
st.markdown("""
<style>
    /* Global Canvas */
    .stApp {
        background-color: #f1f5f9;
        color: #0f172a;
        font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
    }
    
    /* Clean Sidebar */
    [data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #cbd5e1;
    }

    /* Executive Hero Header */
    .hero-banner {
        background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%);
        color: #ffffff;
        border-radius: 14px;
        padding: 24px 28px;
        box-shadow: 0 10px 25px rgba(15, 23, 42, 0.15);
        margin-bottom: 24px;
        border-left: 6px solid #38bdf8;
    }
    .hero-title {
        font-size: 1.6rem;
        font-weight: 800;
        letter-spacing: -0.02em;
        margin-bottom: 4px;
        color: #ffffff;
    }
    .hero-sub {
        font-size: 0.95rem;
        color: #93c5fd;
        font-weight: 500;
    }

    /* Premium Power BI Container Cards */
    .pbi-card {
        background: #ffffff;
        border-radius: 12px;
        padding: 20px;
        border: 1px solid #cbd5e1;
        box-shadow: 0 4px 12px rgba(15, 23, 42, 0.03);
        margin-bottom: 20px;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .pbi-card:hover {
        box-shadow: 0 8px 20px rgba(15, 23, 42, 0.08);
    }

    /* Hero Primary Metric Cards (Revenue, Profit, Cash) */
    .hero-kpi-card {
        background: #ffffff;
        border-radius: 12px;
        padding: 18px 22px;
        border: 1px solid #cbd5e1;
        box-shadow: 0 4px 14px rgba(0,0,0,0.04);
        margin-bottom: 16px;
        position: relative;
        overflow: hidden;
    }
    .hero-kpi-emerald { border-top: 6px solid #10b981; }
    .hero-kpi-indigo { border-top: 6px solid #6366f1; }
    .hero-kpi-purple { border-top: 6px solid #a855f7; }

    .kpi-title {
        font-size: 0.8rem;
        font-weight: 700;
        color: #64748b;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    .kpi-big-val {
        font-size: 2.1rem;
        font-weight: 800;
        color: #0f172a;
        margin: 4px 0;
        letter-spacing: -0.02em;
    }

    /* Custom Modern Rounded Pill Cards */
    .metric-card-box {
        background-color: #ffffff;
        border-radius: 18px;
        padding: 16px 20px;
        margin-bottom: 12px;
        box-shadow: 0 4px 12px rgba(15, 23, 42, 0.05);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        min-height: 125px;
    }
    
    .card-border-blue { border: 4px solid #93c5fd; }
    .card-border-green { border: 4px solid #a7f3d0; }
    .card-border-amber { border: 4px solid #fde68a; }
    .card-border-purple { border: 4px solid #ddd6fe; }

    .card-metric-title {
        font-size: 0.82rem;
        font-weight: 800;
        color: #475569;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 6px;
    }
    .card-metric-val {
        font-size: 1.85rem;
        font-weight: 800;
        color: #0f172a;
        margin: 2px 0;
        letter-spacing: -0.02em;
    }

    /* Storytelling & AR AP Modern Banner Cards */
    .story-box-blue { background-color: #f0f9ff; border-left: 5px solid #0284c7; color: #0369a1; padding: 12px 16px; border-radius: 8px; margin-bottom: 10px; font-size: 0.93rem; line-height: 1.5; }
    .story-box-indigo { background-color: #f5f3ff; border-left: 5px solid #7c3aed; color: #5b21b6; padding: 12px 16px; border-radius: 8px; margin-bottom: 10px; font-size: 0.93rem; line-height: 1.5; }
    .story-box-green { background-color: #f0fdf4; border-left: 5px solid #16a34a; color: #166534; padding: 12px 16px; border-radius: 8px; margin-bottom: 10px; font-size: 0.93rem; line-height: 1.5; }
    .story-box-amber { background-color: #fffbeb; border-left: 5px solid #f59e0b; color: #92400e; padding: 12px 16px; border-radius: 8px; margin-bottom: 10px; font-size: 0.93rem; line-height: 1.5; }

    /* Status Pills */
    .pill-green { background-color: #dcfce7; color: #15803d; padding: 4px 12px; border-radius: 20px; font-size: 0.8rem; font-weight: 700; display: inline-block; }
    .pill-red { background-color: #fee2e2; color: #b91c1c; padding: 4px 12px; border-radius: 20px; font-size: 0.8rem; font-weight: 700; display: inline-block; }
    .pill-amber { background-color: #fef3c7; color: #b45309; padding: 4px 12px; border-radius: 20px; font-size: 0.8rem; font-weight: 700; display: inline-block; }

    /* Custom Executive Table */
    .custom-table {
        width: 100%;
        border-collapse: collapse;
        font-size: 0.88rem;
        text-align: center;
    }
    .custom-table th {
        background-color: #0f172a;
        color: #ffffff;
        padding: 12px 10px;
        border: 1px solid #1e293b;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.03em;
    }
    .custom-table td {
        padding: 10px;
        border-bottom: 1px solid #e2e8f0;
        color: #334155;
    }
    .custom-table tr:hover td {
        background-color: #f8fafc;
    }

    /* Early Warning Alert Boxes */
    .ews-card-red { background-color: #fef2f2; border-left: 5px solid #ef4444; color: #991b1b; padding: 14px 18px; border-radius: 8px; margin-bottom: 10px; font-size: 0.92rem; font-weight: 500; }
    .ews-card-amber { background-color: #fffbeb; border-left: 5px solid #f59e0b; color: #92400e; padding: 14px 18px; border-radius: 8px; margin-bottom: 10px; font-size: 0.92rem; font-weight: 500; }
    .ews-card-green { background-color: #f0fdf4; border-left: 5px solid #22c55e; color: #166534; padding: 14px 18px; border-radius: 8px; margin-bottom: 10px; font-size: 0.92rem; font-weight: 500; }

    /* Action Buttons */
    div.stButton > button:first-child {
        background-color: #0f172a !important;
        color: white !important;
        border: none !important;
        font-weight: bold !important;
        font-size: 15px !important;
        padding: 10px 20px !important;
        border-radius: 8px !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }

    @media print {
        [data-testid="stSidebar"], .no-print, header, footer { display: none !important; }
        .stApp { background-color: #ffffff !important; }
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. DATA GENERATOR WITH MULTI-DIVISION SUPPORT
# ==========================================
def generate_sample_dataset():
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Juni', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des']
    divisions = ['Division Alpha', 'Division Beta', 'Division Gamma']
    data = []
    np.random.seed(42)
    
    for div in divisions:
        div_mult = 1.0 if div == 'Division Alpha' else 0.6 if div == 'Division Beta' else 0.4
        for y in [2025, 2026]:
            for m_idx, m in enumerate(months):
                if m == 'Juni' and y == 2026: 
                    rev_act, rev_bud, cogs_act, cogs_bud, opex_act, opex_bud = 10000*div_mult, 8500*div_mult, 7500*div_mult, 5000*div_mult, 1200*div_mult, 800*div_mult
                    cash, ar, ap, ca, cl, inv = 4299*div_mult, 1828*div_mult, 977*div_mult, 6000*div_mult, 1500*div_mult, 1000*div_mult
                elif m == 'Mei' and y == 2026: 
                    rev_act, rev_bud, cogs_act, cogs_bud, opex_act, opex_bud = 25000*div_mult, 35000*div_mult, 15000*div_mult, 25000*div_mult, 1000*div_mult, 900*div_mult
                    cash, ar, ap, ca, cl, inv = 4480*div_mult, 1067*div_mult, 1200*div_mult, 6100*div_mult, 1600*div_mult, 1200*div_mult
                elif m == 'Mar' and y == 2026: 
                    rev_act, rev_bud, cogs_act, cogs_bud, opex_act, opex_bud = 17924*div_mult, 16298*div_mult, 10754*div_mult, 9452*div_mult, 2150*div_mult, 1629*div_mult
                    cash, ar, ap, ca, cl, inv = 4100*div_mult, 1100*div_mult, 1150*div_mult, 5900*div_mult, 1550*div_mult, 1100*div_mult
                else:
                    rev_act = int(np.random.uniform(12000, 22000) * div_mult)
                    rev_bud = int(rev_act * np.random.uniform(0.9, 1.1))
                    cogs_act, cogs_bud = int(rev_act * 0.6), int(rev_bud * 0.58)
                    opex_act, opex_bud = int(rev_act * 0.12), int(rev_bud * 0.10)
                    cash = int(rev_act * 0.4); ar = int(rev_act * 0.15); ap = int(cogs_act * 0.15)
                    inv = int(rev_act * 0.1); ca = cash + ar + inv; cl = ap + 1000*div_mult
                
                data.append({
                    'Divisi': div, 'Tahun': y, 'Bulan': m, 'Bulan_Num': m_idx + 1,
                    'Revenue_Actual': rev_act, 'Revenue_Budget': rev_bud,
                    'COGS_Actual': cogs_act, 'COGS_Budget': cogs_bud,
                    'OpEx_Actual': opex_act, 'OpEx_Budget': opex_bud,
                    'Net_Profit_Actual': rev_act - cogs_act - opex_act,
                    'Net_Profit_Budget': rev_bud - cogs_bud - opex_bud,
                    'Cash_Balance': cash, 'Accounts_Receivable': ar,
                    'Accounts_Payable': ap, 'Inventory': inv,
                    'Total_Current_Assets': ca, 'Total_Current_Liabilities': cl
                })
    return pd.DataFrame(data)

def convert_df_to_excel(df):
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Financial_KPI_Data')
    return output.getvalue()

# ==========================================
# 3. SIDEBAR CONTROLS & SELECTION
# ==========================================
st.sidebar.markdown("### 🏛️ C-EDSS Control")

sample_df = generate_sample_dataset()

st.sidebar.download_button(
    label="📥 Download Template Excel",
    data=convert_df_to_excel(sample_df),
    file_name="Template_Laporan_Keuangan.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    use_container_width=True
)

uploaded_file = st.sidebar.file_uploader("📂 Upload File Excel Laporan", type=["xlsx", "xls"])
raw_df = pd.read_excel(uploaded_file) if uploaded_file else sample_df

st.sidebar.markdown("---")
st.sidebar.markdown("### 🏢 Filter Unit Bisnis / Divisi")
div_options = ["All Divisions (Consolidated)"] + sorted(raw_df['Divisi'].unique().tolist()) if 'Divisi' in raw_df.columns else ["All Divisions (Consolidated)"]
selected_div = st.sidebar.selectbox("Pilih Divisi/SBU", div_options, index=0)

if selected_div != "All Divisions (Consolidated)" and 'Divisi' in raw_df.columns:
    df_filtered = raw_df[raw_df['Divisi'] == selected_div]
else:
    if 'Divisi' in raw_df.columns:
        df_filtered = raw_df.groupby(['Tahun', 'Bulan', 'Bulan_Num'], as_index=False).agg({
            'Revenue_Actual': 'sum', 'Revenue_Budget': 'sum',
            'COGS_Actual': 'sum', 'COGS_Budget': 'sum',
            'OpEx_Actual': 'sum', 'OpEx_Budget': 'sum',
            'Net_Profit_Actual': 'sum', 'Net_Profit_Budget': 'sum',
            'Cash_Balance': 'sum', 'Accounts_Receivable': 'sum',
            'Accounts_Payable': 'sum', 'Inventory': 'sum',
            'Total_Current_Assets': 'sum', 'Total_Current_Liabilities': 'sum'
        })
    else:
        df_filtered = raw_df

st.sidebar.markdown("---")
st.sidebar.markdown("### 🗓️ Filter Periode Komparasi")

years_available = sorted(df_filtered['Tahun'].unique().tolist())
selected_year = st.sidebar.selectbox("Pilih Tahun", years_available, index=len(years_available)-1)

df_year = df_filtered[df_filtered['Tahun'] == selected_year].sort_values('Bulan_Num')
months_list = df_year['Bulan'].tolist()

col_m1, col_m2 = st.sidebar.columns(2)
with col_m1: month_1 = st.selectbox("Periode Fokus", options=months_list, index=months_list.index('Juni') if 'Juni' in months_list else 5)
with col_m2: month_2 = st.selectbox("Periode Pembanding", options=months_list, index=months_list.index('Mei') if 'Mei' in months_list else 4)

row_m1 = df_year[df_year['Bulan'] == month_1].iloc[0]
row_m2 = df_year[df_year['Bulan'] == month_2].iloc[0]

# CALCULATION ENGINE
rev1, rev2, rev_bud1 = row_m1['Revenue_Actual'], row_m2['Revenue_Actual'], row_m1['Revenue_Budget']
cogs1, cogs2, cogs_bud1 = row_m1['COGS_Actual'], row_m2['COGS_Actual'], row_m1['COGS_Budget']
opex1, opex2, opex_bud1 = row_m1['OpEx_Actual'], row_m2['OpEx_Actual'], row_m1['OpEx_Budget']
net1, net2, net_bud1 = row_m1['Net_Profit_Actual'], row_m2['Net_Profit_Actual'], row_m1['Net_Profit_Budget']

gp1, gp2 = rev1 - cogs1, rev2 - cogs2
gpm1, gpm2 = (gp1 / rev1 * 100) if rev1 > 0 else 0, (gp2 / rev2 * 100) if rev2 > 0 else 0
npm1, npm2 = (net1 / rev1 * 100) if rev1 > 0 else 0, (net2 / rev2 * 100) if rev2 > 0 else 0

cash1, cash2 = row_m1['Cash_Balance'], row_m2['Cash_Balance']
ar1, ar2 = row_m1['Accounts_Receivable'], row_m2['Accounts_Receivable']
ap1, ap2 = row_m1['Accounts_Payable'], row_m2['Accounts_Payable']
ca1, ca2 = row_m1['Total_Current_Assets'], row_m2['Total_Current_Assets']
cl1, cl2 = row_m1['Total_Current_Liabilities'], row_m2['Total_Current_Liabilities']

curr_ratio1, curr_ratio2 = ca1 / cl1 if cl1 > 0 else 0, ca2 / cl2 if cl2 > 0 else 0
quick_ratio1, quick_ratio2 = (cash1 + ar1) / cl1 if cl1 > 0 else 0, (cash2 + ar2) / cl2 if cl2 > 0 else 0
cash_ratio1, cash_ratio2 = cash1 / cl1 if cl1 > 0 else 0, cash2 / cl2 if cl2 > 0 else 0
nwc1, nwc2 = ca1 - cl1, ca2 - cl2
dso1 = (ar1 / rev1 * 30) if rev1 > 0 else 0
dso2 = (ar2 / rev2 * 30) if rev2 > 0 else 0

# CASH BURN RATE & RUNWAY ANALYSIS
monthly_burn_rate = cogs1 + opex1
cash_runway_months = (cash1 / monthly_burn_rate) if monthly_burn_rate > 0 else 0

# FINANCIAL HEALTH SCORE CALCULATOR
health_score = 0
if rev1 >= rev_bud1: health_score += 20
if curr_ratio1 >= 1.5: health_score += 20
if quick_ratio1 >= 1.0: health_score += 20
if npm1 >= 10: health_score += 20
if (cogs1 / rev1) <= 0.6: health_score += 20

# ==========================================
# 4. HERO EXECUTIVE BANNER & TABS
# ==========================================
st.markdown(f"""
<div class="hero-banner">
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
        <div>
            <div class="hero-title">EXECUTIVE DECISION SUPPORT SYSTEM (C-EDSS)</div>
            <div class="hero-sub">UNIT: <b>{selected_div.upper()}</b> | PERIODE: <b>{month_1} {selected_year}</b> vs PEMBANDING: <b>{month_2} {selected_year}</b></div>
        </div>
        <div style="text-align: right; margin-top: 10px;">
            <span class="pill-green">🟢 STATUS: {'HEALTHY' if health_score>=80 else 'STABLE' if health_score>=50 else 'WARNING'}</span>
            <div style="font-size: 0.8rem; color: #cbd5e1; margin-top: 4px;">Score: <b>{health_score}/100</b></div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# TABS PYRAMID NAVIGATION WITH MODERN ICONS
tab_l1, tab_l2, tab_l3, tab_l4, tab_l5 = st.tabs([
    "🏛️ LEVEL 1: Executive Summary",
    "📊 LEVEL 2: Performance (P&L)",
    "💰 LEVEL 3: Position & Liquidity",
    "📈 LEVEL 4: Deep Analytics & EWS",
    "⚙️ LEVEL 5: Decision & What-If"
])

# ==========================================
# LEVEL 1: EXECUTIVE SUMMARY
# ==========================================
with tab_l1:
    # TOP 3 HERO KPI CARDS
    hk1, hk2, hk3 = st.columns(3)
    
    rev_mom_pct = ((rev1 - rev2) / rev2 * 100) if rev2 > 0 else 0
    rev_bud_pct = ((rev1 - rev_bud1) / rev_bud1 * 100) if rev_bud1 > 0 else 0
    
    with hk1:
        st.markdown(f"""
        <div class="hero-kpi-card hero-kpi-emerald">
            <div class="kpi-title">💵 TOTAL REVENUE ({month_1})</div>
            <div class="kpi-big-val">Rp {rev1:,.0f}</div>
            <div>
                <span class="{'pill-green' if rev_mom_pct>=0 else 'pill-red'}">{rev_mom_pct:+.1f}% vs {month_2}</span>
                <span class="{'pill-green' if rev_bud_pct>=0 else 'pill-red'}" style="margin-left:4px;">{rev_bud_pct:+.1f}% vs Target</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    net_mom_pct = ((net1 - net2) / abs(net2) * 100) if net2 != 0 else 0
    with hk2:
        st.markdown(f"""
        <div class="hero-kpi-card hero-kpi-indigo">
            <div class="kpi-title">💎 NET PROFIT ({month_1})</div>
            <div class="kpi-big-val">Rp {net1:,.0f}</div>
            <div>
                <span class="{'pill-green' if net_mom_pct>=0 else 'pill-red'}">{net_mom_pct:+.1f}% vs {month_2}</span>
                <span class="pill-amber" style="margin-left:4px;">NPM: {npm1:.1f}%</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    cash_mom_pct = ((cash1 - cash2) / cash2 * 100) if cash2 > 0 else 0
    with hk3:
        st.markdown(f"""
        <div class="hero-kpi-card hero-kpi-purple">
            <div class="kpi-title">💰 CASH BALANCE ({month_1})</div>
            <div class="kpi-big-val">Rp {cash1:,.0f}</div>
            <div>
                <span class="{'pill-green' if cash_mom_pct>=0 else 'pill-red'}">{cash_mom_pct:+.1f}% vs {month_2}</span>
                <span class="pill-green" style="margin-left:4px;">CR: {curr_ratio1:.2f}x</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    col_gauge, col_story = st.columns([1.2, 1.8])
    
    with col_gauge:
        st.markdown("<div class='pbi-card'>", unsafe_allow_html=True)
        st.markdown("#### ❤️ Financial Health Gauge")
        
        if health_score >= 80:
            bar_color = "#10b981"
            health_status_text = "EXCELLENT 🌟"
        elif health_score >= 50:
            bar_color = "#f59e0b"
            health_status_text = "AVERAGE ⚠️"
        else:
            bar_color = "#ef4444"
            health_status_text = "CRITICAL 🚨"
            
        fig_gauge = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = health_score,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': f"Status: <b>{health_status_text}</b>", 'font': {'size': 14, 'color': bar_color}},
            number = {'suffix': "/100", 'font': {'size': 36, 'color': '#0f172a', 'family': 'Segoe UI'}},
            gauge = {
                'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#94a3b8"},
                'bar': {'color': bar_color, 'thickness': 0.65},
                'bgcolor': "#f8fafc",
                'borderwidth': 1,
                'bordercolor': "#cbd5e1",
                'steps': [
                    {'range': [0, 50], 'color': '#fee2e2'},
                    {'range': [50, 80], 'color': '#fef3c7'},
                    {'range': [80, 100], 'color': '#dcfce7'}
                ]
            }
        ))
        fig_gauge.update_layout(height=260, margin=dict(l=20, r=20, t=10, b=10), paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_gauge, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col_story:
        st.markdown("<div class='pbi-card'>", unsafe_allow_html=True)
        st.markdown("#### 🤖 AI Executive Storytelling Card")
        
        st.markdown(f"""
        <div class="story-box-blue">
            📊 <b>[1. KINERJA PENJUALAN]</b> Revenue unit <b>{selected_div}</b> bulan <b>{month_1}</b> tercatat <b>Rp {rev1:,.0f}</b> 
            (<span style="color:{'#16a34a' if rev_bud_pct>=0 else '#dc2626'}; font-weight:bold;">{'Melampaui' if rev_bud_pct>=0 else 'Di Bawah'} Target Budget {rev_bud_pct:+.1f}%</span>). MoM vs {month_2}: <b>{rev_mom_pct:+.1f}%</b>.
        </div>
        <div class="story-box-indigo">
            🎯 <b>[2. PROFITABILITAS]</b> Net Profit Margin berada di tingkat <b>{npm1:.1f}%</b> (Pembanding {month_2}: <b>{npm2:.1f}%</b>). 
            Total Laba Bersih: <b>Rp {net1:,.0f}</b>. Permasalahan utama bersumber dari efisiensi porsi COGS.
        </div>
        <div class="story-box-green">
            ⚖️ <b>[3. WORKING CAPITAL & LIKUIDITAS]</b> Current Ratio tercatat aman di tingkat <b>{curr_ratio1:.2f}x</b> (Ideal ≥ 1.5x) dan Quick Ratio <b>{quick_ratio1:.2f}x</b>. Net Working Capital mencapai <b>Rp {nwc1:,.0f}</b>.
        </div>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# LEVEL 2: FINANCIAL PERFORMANCE (P&L)
# ==========================================
with tab_l2:
    st.markdown("<div class='pbi-card'>", unsafe_allow_html=True)
    st.markdown("### 📊 Komparasi Detail P&L Statement (Actual vs Budget vs Pembanding)")
    
    pnl_table_html = f"""
    <table class="custom-table">
        <thead>
            <tr>
                <th style="text-align:left;">Komponen Keuangan</th>
                <th>Actual ({month_1})</th>
                <th>Budget ({month_1})</th>
                <th>Actual ({month_2})</th>
                <th>Variance vs Target (Rp)</th>
                <th>Variance vs Target (%)</th>
                <th>Variance MoM (%)</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td style="text-align:left;"><b>💵 Revenue (Penjualan)</b></td>
                <td>Rp {rev1:,.0f}</td><td>Rp {rev_bud1:,.0f}</td><td>Rp {rev2:,.0f}</td>
                <td>{rev1-rev_bud1:+,.0f}</td>
                <td><b style="color:{'#16a34a' if rev1>=rev_bud1 else '#dc2626'};">{((rev1-rev_bud1)/rev_bud1*100):+.1f}%</b></td>
                <td><b style="color:{'#16a34a' if rev1>=rev2 else '#dc2626'};">{((rev1-rev2)/rev2*100):+.1f}%</b></td>
            </tr>
            <tr>
                <td style="text-align:left;"><b>🏭 COGS (HPP)</b></td>
                <td>Rp {cogs1:,.0f}</td><td>Rp {cogs_bud1:,.0f}</td><td>Rp {cogs2:,.0f}</td>
                <td>{cogs1-cogs_bud1:+,.0f}</td>
                <td><b style="color:{'#dc2626' if cogs1>cogs_bud1 else '#16a34a'};">{((cogs1-cogs_bud1)/cogs_bud1*100):+.1f}%</b></td>
                <td><b style="color:{'#dc2626' if cogs1>cogs2 else '#16a34a'};">{((cogs1-cogs2)/cogs2*100):+.1f}%</b></td>
            </tr>
            <tr>
                <td style="text-align:left;"><b>📈 Gross Profit</b></td>
                <td>Rp {gp1:,.0f}</td><td>Rp {rev_bud1-cogs_bud1:,.0f}</td><td>Rp {gp2:,.0f}</td>
                <td>{gp1-(rev_bud1-cogs_bud1):+,.0f}</td>
                <td><b style="color:{'#16a34a' if gp1>=(rev_bud1-cogs_bud1) else '#dc2626'};">{((gp1-(rev_bud1-cogs_bud1))/(rev_bud1-cogs_bud1)*100):+.1f}%</b></td>
                <td><b style="color:{'#16a34a' if gp1>=gp2 else '#dc2626'};">{((gp1-gp2)/gp2*100):+.1f}%</b></td>
            </tr>
            <tr>
                <td style="text-align:left;"><b>🏢 Operating Expenses (OpEx)</b></td>
                <td>Rp {opex1:,.0f}</td><td>Rp {opex_bud1:,.0f}</td><td>Rp {opex2:,.0f}</td>
                <td>{opex1-opex_bud1:+,.0f}</td>
                <td><b style="color:{'#dc2626' if opex1>opex_bud1 else '#16a34a'};">{((opex1-opex_bud1)/opex_bud1*100):+.1f}%</b></td>
                <td><b style="color:{'#dc2626' if opex1>opex2 else '#16a34a'};">{((opex1-opex2)/opex2*100):+.1f}%</b></td>
            </tr>
            <tr>
                <td style="text-align:left;"><b>💎 Net Profit</b></td>
                <td>Rp {net1:,.0f}</td><td>Rp {net_bud1:,.0f}</td><td>Rp {net2:,.0f}</td>
                <td>{net1-net_bud1:+,.0f}</td>
                <td><b style="color:{'#16a34a' if net1>=net_bud1 else '#dc2626'};">{((net1-net_bud1)/abs(net_bud1)*100):+.1f}%</b></td>
                <td><b style="color:{'#16a34a' if net1>=net2 else '#dc2626'};">{((net1-net2)/abs(net2)*100):+.1f}%</b></td>
            </tr>
        </tbody>
    </table>
    """
    st.html(pnl_table_html)
    st.markdown("</div>", unsafe_allow_html=True)

    col_wat, col_rad = st.columns([1.6, 1.2])
    with col_wat:
        st.markdown("<div class='pbi-card'>", unsafe_allow_html=True)
        st.markdown("#### 🌊 Waterfall Financial Driver Modern")
        
        fig_waterfall = go.Figure(go.Waterfall(
            orientation="v", measure=["relative", "relative", "total", "relative", "total"],
            x=["Revenue", "COGS", "Gross Profit", "OpEx", "Net Profit"],
            text=[f"+{rev1:,.0f}", f"-{cogs1:,.0f}", f"{gp1:,.0f}", f"-{opex1:,.0f}", f"{net1:,.0f}"],
            y=[rev1, -cogs1, 0, -opex1, 0],
            connector={"line":{"color":"#94a3b8"}},
            decreasing={"marker":{"color":"#ef4444"}},
            increasing={"marker":{"color":"#10b981"}},
            totals={"marker":{"color":"#1e3a8a"}}
        ))
        fig_waterfall.update_layout(height=320, margin=dict(l=10, r=10, t=10, b=10), template="plotly_white")
        st.plotly_chart(fig_waterfall, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col_rad:
        st.markdown("<div class='pbi-card'>", unsafe_allow_html=True)
        st.markdown("#### 🎯 Executive Radar Balance Chart")
        
        categories = ['Revenue Target', 'Gross Margin', 'Net Margin', 'Quick Ratio', 'Current Ratio']
        r_foc = [min(rev1/rev_bud1*100, 120), gpm1*2, npm1*3, quick_ratio1*30, curr_ratio1*25]
        
        fig_radar = go.Figure()
        fig_radar.add_trace(go.Scatterpolar(r=r_foc, theta=categories, fill='toself', name=month_1, fillcolor='rgba(56, 189, 248, 0.3)', line=dict(color='#0284c7')))
        fig_radar.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 120])), height=320, margin=dict(l=20, r=20, t=10, b=10))
        st.plotly_chart(fig_radar, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# LEVEL 3: FINANCIAL POSITION & CASH RUNWAY
# ==========================================
with tab_l3:
    st.markdown("<div class='pbi-card'>", unsafe_allow_html=True)
    st.markdown("### 💰 Balance Sheet Position, Liquidity & Working Capital")
    st.markdown("<br>", unsafe_allow_html=True)
    
    # 4 MODERN ROUNDED CONTAINER CARDS
    q1, q2, q3, q4 = st.columns(4)
    
    curr_var_val = curr_ratio1 - curr_ratio2
    quick_var_val = quick_ratio1 - quick_ratio2
    cash_var_val = cash_ratio1 - cash_ratio2
    nwc_var_val = nwc1 - nwc2
    
    with q1:
        st.markdown(f"""
        <div class="metric-card-box card-border-blue">
            <div class="card-metric-title">⚖️ Current Ratio</div>
            <div class="card-metric-val">{curr_ratio1:.2f}x</div>
            <div>
                <span class="{'pill-green' if curr_var_val>=0 else 'pill-red'}">
                    {'↑' if curr_var_val>=0 else '↓'} {curr_var_val:+.2f} vs {month_2}
                </span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with q2:
        st.markdown(f"""
        <div class="metric-card-box card-border-green">
            <div class="card-metric-title">🚀 Quick Ratio</div>
            <div class="card-metric-val">{quick_ratio1:.2f}x</div>
            <div>
                <span class="{'pill-green' if quick_var_val>=0 else 'pill-red'}">
                    {'↑' if quick_var_val>=0 else '↓'} {quick_var_val:+.2f} vs {month_2}
                </span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with q3:
        st.markdown(f"""
        <div class="metric-card-box card-border-amber">
            <div class="card-metric-title">🏦 Cash Ratio</div>
            <div class="card-metric-val">{cash_ratio1:.2f}x</div>
            <div>
                <span class="{'pill-green' if cash_var_val>=0 else 'pill-red'}">
                    {'↑' if cash_var_val>=0 else '↓'} {cash_var_val:+.2f} vs {month_2}
                </span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with q4:
        st.markdown(f"""
        <div class="metric-card-box card-border-purple">
            <div class="card-metric-title">💼 Net Working Capital</div>
            <div class="card-metric-val">Rp {nwc1:,.0f}</div>
            <div>
                <span class="{'pill-green' if nwc_var_val>=0 else 'pill-red'}">
                    {'↑' if nwc_var_val>=0 else '↓'} Rp {nwc_var_val:+,.0f} vs {month_2}
                </span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col_bs, col_ar = st.columns([1.4, 1.4])
    
    with col_bs:
        st.markdown("#### ⚖️ Balance Sheet Structure & Cash Runway")
        
        fig_bs = go.Figure()
        fig_bs.add_trace(go.Bar(y=['Aktiva / Pasiva'], x=[ca1], name='Current Assets', orientation='h', marker_color='#10b981'))
        fig_bs.add_trace(go.Bar(y=['Aktiva / Pasiva'], x=[cl1], name='Current Liabilities', orientation='h', marker_color='#ef4444'))
        fig_bs.add_trace(go.Bar(y=['Aktiva / Pasiva'], x=[nwc1], name='Working Capital Surplus', orientation='h', marker_color='#38bdf8'))
        
        fig_bs.update_layout(barmode='stack', height=180, margin=dict(l=10, r=10, t=10, b=10), template="plotly_white")
        st.plotly_chart(fig_bs, use_container_width=True)

        # CASH RUNWAY ANALYSIS CARD
        runway_cls = "story-box-green" if cash_runway_months >= 3 else "story-box-amber" if cash_runway_months >= 1.5 else "story-box-blue"
        st.markdown(f"""
        <div class="{runway_cls}">
            ⛽ <b>Monthly Cash Burn Rate:</b> Rp {monthly_burn_rate:,.0f} / bulan<br>
            ⏱️ <b>Cash Runway Resilience:</b> <b>{cash_runway_months:.1f} Bulan</b> ketahanan kas tanpa pendapatan baru.
        </div>
        """, unsafe_allow_html=True)

    with col_ar:
        st.markdown("#### 📥 Receivables (AR) & Payables (AP) Health")
        
        ar_growth_val = ((ar1 - ar2) / ar2 * 100) if ar2 > 0 else 0
        ap_growth_val = ((ap1 - ap2) / ap2 * 100) if ap2 > 0 else 0
        
        st.markdown(f"""
        <div class="story-box-blue">
            📥 <b>Saldo Piutang Dagang (AR {month_1}):</b> Rp {ar1:,.0f} 
            <span style="font-size:0.85rem; padding:2px 8px; border-radius:12px; background-color:{'#fee2e2' if ar_growth_val>15 else '#dcfce7'}; color:{'#b91c1c' if ar_growth_val>15 else '#15803d'}; font-weight:bold; margin-left:6px;">
                {ar_growth_val:+.1f}% vs {month_2} (Rp {ar2:,.0f})
            </span>
        </div>
        <div class="story-box-amber">
            ⏳ <b>Days Sales Outstanding (DSO Est.):</b> <b>{dso1:.0f} Hari</b> 
            <span style="font-size:0.85rem; color:#b45309; font-weight:bold; margin-left:6px;">
                (vs {month_2}: {dso2:.0f} Hari)
            </span>
        </div>
        <div class="story-box-indigo">
            📤 <b>Saldo Hutang Lancar (AP {month_1}):</b> Rp {ap1:,.0f} 
            <span style="font-size:0.85rem; padding:2px 8px; border-radius:12px; background-color:#f3e8ff; color:#6b21a8; font-weight:bold; margin-left:6px;">
                {ap_growth_val:+.1f}% vs {month_2} (Rp {ap2:,.0f})
            </span>
        </div>
        """, unsafe_allow_html=True)
        st.info(f"**AI Commentary:** Likuiditas jangka pendek sangat sehat. Total cadangan kas tunai (Rp {cash1:,.0f}) mampu mengkover seluruh kewajiban lancar AP.")
        
    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# LEVEL 4: DEEP ANALYTICS & EARLY WARNING
# ==========================================
with tab_l4:
    st.markdown("<div class='pbi-card'>", unsafe_allow_html=True)
    st.markdown("### 🚨 Early Warning System (EWS) & Quality of Earnings")
    
    ews_alerts = []
    if curr_ratio1 < 1.5: ews_alerts.append(("red", f"CRITICAL LIKUIDITAS: Current Ratio ({curr_ratio1:.2f}x) berada di bawah batas aman 1.5x."))
    else: ews_alerts.append(("green", f"LIKUIDITAS AMAN: Current Ratio ({curr_ratio1:.2f}x) memenuhi standar kesehatan modal kerja."))
    
    if ar1 > ar2 * 1.15: ews_alerts.append(("red", f"RISIKO PIUTANG: Piutang (AR) melonjak +{((ar1-ar2)/ar2*100):.1f}% dibanding {month_2}. Potensi menekan cashflow."))
    
    if gpm1 < gpm2: ews_alerts.append(("amber", f"PENURUNAN MARGIN KOTOR: Gross Margin turun dari {gpm2:.1f}% menjadi {gpm1:.1f}%. Pembengkakan COGS."))
    
    if npm1 < 10: ews_alerts.append(("amber", f"MARGIN BERSIH TERTEKAN: Net Margin ({npm1:.1f}%) di bawah batas ideal 10%."))
    
    for cls, msg in ews_alerts:
        st.markdown(f"<div class='ews-card-{cls}'>⚠️ {msg}</div>", unsafe_allow_html=True)
        
    st.markdown("<br>#### 📈 Trend Pergerakan Multi-Bulan (12 Bulan)", unsafe_allow_html=True)
    fig_trend = px.line(df_year, x="Bulan", y=["Revenue_Actual", "Net_Profit_Actual", "Cash_Balance"], markers=True)
    fig_trend.update_layout(height=320, template="plotly_white")
    st.plotly_chart(fig_trend, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# LEVEL 5: DECISION & MANAGEMENT EXECUTIVE DIRECTIVE
# ==========================================
with tab_l5:
    st.markdown("<div class='pbi-card'>", unsafe_allow_html=True)
    st.markdown("### ⚙️ Decision Priority Matrix & Management Executive Directive")
    
    col_d1, col_d2 = st.columns([1.5, 1.3])
    
    with col_d1:
        st.markdown("#### 🎯 Decision Priority Matrix")
        
        priority_table_html = """
        <table class="custom-table">
            <thead>
                <tr>
                    <th style="text-align:left;">Area Fokus</th>
                    <th>Impact</th>
                    <th>Urgency</th>
                    <th>Status</th>
                    <th style="text-align:left;">Action Plan</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td style="text-align:left;"><b>🏭 Harga Pokok Penjualan (COGS)</b></td>
                    <td>Very High</td>
                    <td>Critical</td>
                    <td><span class="pill-red">🔴 CRITICAL</span></td>
                    <td style="text-align:left;">Audit efisiensi bahan baku & negosiasi supplier.</td>
                </tr>
                <tr>
                    <td style="text-align:left;"><b>📥 Pengelolaan Piutang (AR)</b></td>
                    <td>High</td>
                    <td>High</td>
                    <td><span class="pill-red">🔴 CRITICAL</span></td>
                    <td style="text-align:left;">Intensifkan penagihan piutang >30 hari & ketat kriteria kredit.</td>
                </tr>
                <tr>
                    <td style="text-align:left;"><b>💵 Target Revenue</b></td>
                    <td>High</td>
                    <td>Medium</td>
                    <td><span class="pill-amber">🟡 HIGH</span></td>
                    <td style="text-align:left;">Evaluasi strategi sales dan dorong produk margin tinggi.</td>
                </tr>
                <tr>
                    <td style="text-align:left;"><b>🏢 Biaya Operasional (OpEx)</b></td>
                    <td>Medium</td>
                    <td>Medium</td>
                    <td><span class="pill-amber">🟡 MEDIUM</span></td>
                    <td style="text-align:left;">Pengetatan perjalanan dinas dan beban administrasi.</td>
                </tr>
            </tbody>
        </table>
        """
        st.html(priority_table_html)

    with col_d2:
        st.markdown("#### ⚡ What-If Sensitivity Simulation")
        sim_cogs_eff = st.slider("Simulasi Efisiensi COGS (%)", 0.0, 10.0, 3.0, step=0.5)
        sim_ar_coll = st.slider("Simulasi Collection Piutang AR (%)", 0.0, 30.0, 10.0, step=1.0)
        
        saved_cogs = cogs1 * (sim_cogs_eff / 100)
        new_net = net1 + saved_cogs
        new_npm = (new_net / rev1 * 100) if rev1 > 0 else 0
        added_cash = ar1 * (sim_ar_coll / 100)
        
        st.success(f"💡 **Dampak Efisiensi COGS {sim_cogs_eff}%:** Menambah Net Profit sebesar **+Rp {saved_cogs:,.0f}** (Margin naik ke **{new_npm:.1f}%**).")
        st.info(f"💡 **Dampak Collection AR {sim_ar_coll}%:** Menambah Cash Inflow sebesar **+Rp {added_cash:,.0f}**.")
        
    st.markdown("---")
    # EYE-CATCHING MANAGEMENT DIRECTIVE CARD
    st.markdown("#### 📝 Management Executive Directive & Approval Sign-off")
    st.caption("Ketikkan instruksi atau arahan resmi CFO/Manajemen di bawah ini untuk ditampilkan secara menonjol:")
    
    col_n1, col_n2 = st.columns([1, 2.5])
    
    with col_n1:
        note_priority = st.selectbox(
            "Tingkat Urgensi Instruksi:",
            ["URGENT (🔴 Red Alert)", "IMPORTANT (🟡 Gold Directive)", "INFO (🔵 General Notice)"],
            index=1
        )
        
    with col_n2:
        exec_notes = st.text_area(
            "Catatan & Arahan Eksekutif Manajemen:",
            value=f"1. Penurunan margin pada periode {month_1} dipengaruhi lonjakan biaya bahan baku pada divisi operasional.\n2. Tim Finance diinstruksikan mempercepat penagihan piutang sebelum akhir kuartal.",
            height=90
        )
    
    # RENDER DIRECTIVE BANNER DENGAN WARNA EYE-CATCHING PSIKOLOGIS
    if "URGENT" in note_priority:
        card_theme = "border-left: 6px solid #ef4444; background-color: #fef2f2; color: #991b1b;"
        badge_theme = "background-color: #ef4444; color: white;"
        priority_label = "🚨 DIREKSI / CFO INSTRUCTION: HIGH PRIORITY"
    elif "IMPORTANT" in note_priority:
        card_theme = "border-left: 6px solid #f59e0b; background-color: #fffbeb; color: #92400e;"
        badge_theme = "background-color: #f59e0b; color: white;"
        priority_label = "📣 OFFICIAL MANAGEMENT DIRECTIVE"
    else:
        card_theme = "border-left: 6px solid #0284c7; background-color: #f0f9ff; color: #0369a1;"
        badge_theme = "background-color: #0284c7; color: white;"
        priority_label = "📌 EXECUTIVE NOTICE & ROUTINE DIRECTION"

    formatted_notes = exec_notes.replace("\n", "<br>")
    
    st.markdown(f"""
    <div style="padding: 18px 22px; border-radius: 12px; margin-top: 14px; box-shadow: 0 4px 12px rgba(0,0,0,0.04); {card_theme}">
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <span style="font-size: 0.78rem; font-weight: 800; padding: 4px 12px; border-radius: 20px; letter-spacing: 0.05em; {badge_theme}">
                {priority_label}
            </span>
            <span style="font-size: 0.8rem; font-weight: 600; margin-left: 10px; opacity: 0.8;">
                Unit: {selected_div} | Periode: {month_1} {selected_year}
            </span>
        </div>
        <div style="font-size: 1rem; line-height: 1.7; font-weight: 600;">
            {formatted_notes}
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# EXPORT OPTIONS
# ==========================================
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("### 📥 Download / Export Analysis")

cb1, cb2 = st.columns(2)
with cb1:
    if st.button("📄 Convert & Download Dashboard to PDF", use_container_width=True):
        st.components.v1.html("<script>window.parent.focus(); window.parent.print();</script>", height=0)

with cb2:
    def generate_excel_report():
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            export_df = pd.DataFrame([
                {'Komponen Keuangan': 'Revenue', f'Actual {month_1}': rev1, f'Budget {month_1}': rev_bud1, f'Actual {month_2}': rev2},
                {'Komponen Keuangan': 'COGS', f'Actual {month_1}': cogs1, f'Budget {month_1}': cogs_bud1, f'Actual {month_2}': cogs2},
                {'Komponen Keuangan': 'Net Profit', f'Actual {month_1}': net1, f'Budget {month_1}': net_bud1, f'Actual {month_2}': net2},
            ])
            export_df.to_excel(writer, index=False, sheet_name='Komparasi_Laporan_Keuangan')
            notes_df = pd.DataFrame([{'Unit/Divisi': selected_div, 'Periode': f'{month_1} {selected_year}', 'Urgensi': note_priority, 'Catatan Eksekutif Manajemen': exec_notes}])
            notes_df.to_excel(writer, index=False, sheet_name='Management_Directive')
        return output.getvalue()

    st.download_button(
        label="📊 Export Data Komparasi ke Excel (.xlsx)",
        data=generate_excel_report(),
        file_name=f"Directive_Keuangan_{selected_div}_{month_1}_vs_{month_2}_{selected_year}.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        use_container_width=True
    )
