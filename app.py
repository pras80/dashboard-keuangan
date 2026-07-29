import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import io

# ==========================================
# 1. PAGE CONFIG & LIGHT CORPORATE STYLING
# ==========================================
st.set_page_config(
    page_title="Executive Financial Analytics & Recommendations",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling (Template.net Inspired Clean Executive Light Theme)
st.markdown("""
<style>
    .stApp {
        background-color: #f8fafc;
        color: #0f172a;
        font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
    }
    
    [data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #e2e8f0;
    }
    
    .excel-card {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 20px;
        border: 1px solid #cbd5e1;
        box-shadow: 0 4px 12px rgba(15, 23, 42, 0.03);
        margin-bottom: 20px;
    }

    .kpi-wrapper {
        background: #ffffff;
        border-radius: 12px;
        border: 1px solid #cbd5e1;
        padding: 16px;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.04);
        margin-bottom: 16px;
        position: relative;
        overflow: hidden;
    }
    .kpi-accent-blue { border-top: 5px solid #2563eb; }
    .kpi-accent-green { border-top: 5px solid #16a34a; }
    .kpi-accent-amber { border-top: 5px solid #d97706; }
    .kpi-accent-navy { border-top: 5px solid #1e3a8a; }

    .kpi-label {
        font-size: 0.78rem;
        font-weight: 700;
        color: #64748b;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 4px;
    }
    .kpi-val {
        font-size: 1.8rem;
        font-weight: 800;
        color: #0f172a;
        margin: 4px 0;
        letter-spacing: -0.02em;
    }
    .kpi-pill-pos {
        background-color: #dcfce7;
        color: #15803d;
        padding: 3px 10px;
        border-radius: 20px;
        font-size: 0.78rem;
        font-weight: 700;
        display: inline-block;
    }
    .kpi-pill-neg {
        background-color: #fee2e2;
        color: #b91c1c;
        padding: 3px 10px;
        border-radius: 20px;
        font-size: 0.78rem;
        font-weight: 700;
        display: inline-block;
    }

    /* Clean Styled HTML Table */
    .table-container {
        background: #ffffff;
        border-radius: 10px;
        padding: 12px;
        border: 1px solid #cbd5e1;
        overflow-x: auto;
    }
    .custom-table {
        width: 100%;
        border-collapse: collapse;
        font-size: 0.86rem;
        text-align: center;
    }
    .custom-table th {
        background-color: #1e3a8a;
        color: #ffffff;
        padding: 10px 8px;
        border: 1px solid #1e40af;
        font-weight: 600;
    }
    .custom-table th.focus-header {
        background-color: #b45309 !important;
        border-color: #92400e !important;
    }
    .custom-table td {
        padding: 8px 6px;
        border-bottom: 1px solid #e2e8f0;
        color: #334155;
    }
    .custom-table td.focus-cell {
        background-color: #fffbeb;
        font-weight: 600;
    }
    .custom-table tr:hover td {
        background-color: #f8fafc;
    }

    /* Sparkbars */
    .spark-bg {
        background-color: #e2e8f0;
        width: 45px;
        height: 10px;
        border-radius: 3px;
        display: inline-block;
        vertical-align: middle;
    }
    .spark-fill-purple {
        background-color: #2563eb;
        height: 100%;
        border-radius: 3px;
    }
    .spark-fill-red {
        background-color: #dc2626;
        height: 100%;
        border-radius: 3px;
    }

    /* Distinct Alert Cards */
    .rec-box-blue {
        background-color: #f0f9ff;
        border-left: 5px solid #0284c7;
        color: #0369a1;
        padding: 14px 18px;
        border-radius: 8px;
        margin-bottom: 10px;
        font-size: 0.93rem;
        line-height: 1.5;
    }
    .rec-box-amber {
        background-color: #fffbeb;
        border-left: 5px solid #f59e0b;
        color: #92400e;
        padding: 14px 18px;
        border-radius: 8px;
        margin-bottom: 10px;
        font-size: 0.93rem;
        line-height: 1.5;
    }
    .rec-box-purple {
        background-color: #faf5ff;
        border-left: 5px solid #a855f7;
        color: #6b21a8;
        padding: 14px 18px;
        border-radius: 8px;
        margin-bottom: 10px;
        font-size: 0.93rem;
        line-height: 1.5;
    }
    .rec-box-emerald {
        background-color: #f0fdf4;
        border-left: 5px solid #10b981;
        color: #065f46;
        padding: 14px 18px;
        border-radius: 8px;
        margin-bottom: 10px;
        font-size: 0.93rem;
        line-height: 1.5;
    }
    .rec-box-teal {
        background-color: #f0fdfa;
        border-left: 5px solid #14b8a6;
        color: #115e59;
        padding: 14px 18px;
        border-radius: 8px;
        margin-bottom: 10px;
        font-size: 0.93rem;
        line-height: 1.5;
    }

    div.stButton > button:first-child {
        background-color: #dc2626 !important;
        color: white !important;
        border: none !important;
        font-weight: bold !important;
        font-size: 15px !important;
        padding: 10px 18px !important;
        border-radius: 8px !important;
        box-shadow: 0 4px 6px rgba(220, 38, 38, 0.2);
    }

    @media print {
        [data-testid="stSidebar"], .no-print, header, footer { display: none !important; }
        .stApp { background-color: #ffffff !important; }
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. DATA GENERATOR & SAMPLE EXCEL
# ==========================================
def generate_sample_dataset():
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Juni', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des']
    years = [2025, 2026]
    data = []
    
    np.random.seed(42)
    for y in years:
        for m_idx, m in enumerate(months):
            if m == 'Juni' and y == 2026:
                rev_act, rev_bud = 10000, 8500
                cogs_act, cogs_bud = 7500, 5000
                opex_act, opex_bud = 1200, 800
                net_act = 1300
                cash, ar, ap, ca, cl = 4299, 1828, 977, 6000, 1500
            elif m == 'Mei' and y == 2026:
                rev_act, rev_bud = 25000, 35000
                cogs_act, cogs_bud = 15000, 25000
                opex_act, opex_bud = 1000, 900
                net_act = 9000
                cash, ar, ap, ca, cl = 4480, 1067, 1200, 6100, 1600
            elif m == 'Mar' and y == 2026:
                rev_act, rev_bud = 17924, 16298
                cogs_act, cogs_bud = 10754, 9452
                opex_act, opex_bud = 2150, 1629
                net_act = 5020
                cash, ar, ap, ca, cl = 4100, 1100, 1150, 5900, 1550
            elif m == 'Feb' and y == 2026:
                rev_act, rev_bud = 13996, 14035
                cogs_act, cogs_bud = 8397, 8140
                opex_act, opex_bud = 1679, 1403
                net_act = 3920
                cash, ar, ap, ca, cl = 3900, 1150, 1100, 5800, 1500
            else:
                rev_act = int(np.random.uniform(12000, 22000))
                rev_bud = int(rev_act * np.random.uniform(0.9, 1.1))
                cogs_act = int(rev_act * 0.6)
                cogs_bud = int(rev_bud * 0.58)
                opex_act = int(rev_act * 0.12)
                opex_bud = int(rev_bud * 0.10)
                net_act = rev_act - cogs_act - opex_act
                cash = int(rev_act * 0.4)
                ar = int(rev_act * 0.1)
                ap = int(cogs_act * 0.15)
                ca = cash + ar + int(rev_act * 0.2)
                cl = ap + int(rev_act * 0.1)
            
            data.append({
                'Tahun': y,
                'Bulan': m,
                'Bulan_Num': m_idx + 1,
                'Revenue_Actual': rev_act,
                'Revenue_Budget': rev_bud,
                'COGS_Actual': cogs_act,
                'COGS_Budget': cogs_bud,
                'OpEx_Actual': opex_act,
                'OpEx_Budget': opex_bud,
                'Net_Profit_Actual': net_act,
                'Net_Profit_Budget': rev_bud - cogs_bud - opex_bud,
                'Cash_Balance': cash,
                'Accounts_Receivable': ar,
                'Accounts_Payable': ap,
                'Total_Current_Assets': ca,
                'Total_Current_Liabilities': cl
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
st.sidebar.markdown("### ⚙️ Control Center")

sample_df = generate_sample_dataset()

st.sidebar.download_button(
    label="📥 Download Template Excel",
    data=convert_df_to_excel(sample_df),
    file_name="Template_Laporan_Keuangan.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    use_container_width=True
)

uploaded_file = st.sidebar.file_uploader("📂 Upload File Excel Laporan", type=["xlsx", "xls"])
df = pd.read_excel(uploaded_file) if uploaded_file else sample_df

st.sidebar.markdown("---")
st.sidebar.markdown("### 🗓️ Filter Periode Komparasi")

years_available = sorted(df['Tahun'].unique().tolist())
selected_year = st.sidebar.selectbox("Pilih Tahun", years_available, index=len(years_available)-1)

df_year = df[df['Tahun'] == selected_year].sort_values('Bulan_Num')
months_list = df_year['Bulan'].tolist()

col_m1, col_m2 = st.sidebar.columns(2)
with col_m1:
    month_1 = st.selectbox("Bulan Fokus", options=months_list, index=months_list.index('Juni') if 'Juni' in months_list else 5)
with col_m2:
    month_2 = st.selectbox("Bulan Pembanding", options=months_list, index=months_list.index('Mei') if 'Mei' in months_list else 4)

if month_1 == month_2:
    st.sidebar.warning("⚠️ Pilih dua bulan berbeda untuk komparasi.")

row_m1 = df_year[df_year['Bulan'] == month_1].iloc[0]
row_m2 = df_year[df_year['Bulan'] == month_2].iloc[0]

# GLOBAL CALCULATIONS
rev_m1 = row_m1['Revenue_Actual']
rev_m2 = row_m2['Revenue_Actual']
rev_var_rp = rev_m1 - rev_m2
rev_var_pct = (rev_var_rp / rev_m2 * 100) if rev_m2 != 0 else 0

opex_m1 = row_m1['OpEx_Actual']
opex_m2 = row_m2['OpEx_Actual']
opex_var_rp = opex_m1 - opex_m2
opex_var_pct = (opex_var_rp / opex_m2 * 100) if opex_m2 != 0 else 0

cogs_m1 = row_m1['COGS_Actual']
cogs_m2 = row_m2['COGS_Actual']

net_m1 = row_m1['Net_Profit_Actual']
net_m2 = row_m2['Net_Profit_Actual']
net_var_rp = net_m1 - net_m2
net_var_pct = (net_var_rp / abs(net_m2) * 100) if net_m2 != 0 else 0

gp_m1_act = row_m1['Revenue_Actual'] - row_m1['COGS_Actual']
gp_m2_act = row_m2['Revenue_Actual'] - row_m2['COGS_Actual']
gp_m1_bud = row_m1['Revenue_Budget'] - row_m1['COGS_Budget']
gp_m2_bud = row_m2['Revenue_Budget'] - row_m2['COGS_Budget']

# ==========================================
# 4. DASHBOARD HEADER
# ==========================================
st.markdown("## 📊 Executive Financial Dashboard")
st.markdown(f"**Periode Fokus:** `{month_1} {selected_year}` &nbsp;|&nbsp; **Pembanding:** `{month_2} {selected_year}`")

st.markdown("<br>", unsafe_allow_html=True)

# DASHBOARD TABS
tab_kpi, tab_table = st.tabs(["📌 Executive Financial KPIs (Dashboard View)", "📋 Tabel Komparasi Detail (P&L Variance)"])

# ==========================================
# TAB 1: EXECUTIVE FINANCIAL KPIS
# ==========================================
with tab_kpi:
    inc_act = row_m1['Revenue_Actual']
    inc_prev = row_m2['Revenue_Actual']
    inc_mom_pct = ((inc_act - inc_prev) / inc_prev * 100) if inc_prev != 0 else 0
    
    net_act = row_m1['Net_Profit_Actual']
    net_prev = row_m2['Net_Profit_Actual']
    net_mom_pct = ((net_act - net_prev) / abs(net_prev) * 100) if net_prev != 0 else 0
    
    exp_act = row_m1['OpEx_Actual'] + row_m1['COGS_Actual']
    exp_prev = row_m2['OpEx_Actual'] + row_m2['COGS_Actual']
    exp_mom_pct = ((exp_act - exp_prev) / exp_prev * 100) if exp_prev != 0 else 0
    
    cash_act = row_m1['Cash_Balance']
    cash_prev = row_m2['Cash_Balance']
    cash_mom_pct = ((cash_act - cash_prev) / cash_prev * 100) if cash_prev != 0 else 0
    
    ar_act = row_m1['Accounts_Receivable']
    ar_prev = row_m2['Accounts_Receivable']
    ar_mom_pct = ((ar_act - ar_prev) / ar_prev * 100) if ar_prev != 0 else 0
    
    ap_act = row_m1['Accounts_Payable']
    ap_prev = row_m2['Accounts_Payable']
    ap_mom_pct = ((ap_act - ap_prev) / ap_prev * 100) if ap_prev != 0 else 0
    
    curr_ratio = row_m1['Total_Current_Assets'] / row_m1['Total_Current_Liabilities'] if row_m1['Total_Current_Liabilities'] > 0 else 0
    curr_ratio_prev = row_m2['Total_Current_Assets'] / row_m2['Total_Current_Liabilities'] if row_m2['Total_Current_Liabilities'] > 0 else 0
    curr_ratio_mom_pct = ((curr_ratio - curr_ratio_prev) / curr_ratio_prev * 100) if curr_ratio_prev != 0 else 0
    
    quick_assets = row_m1['Cash_Balance'] + row_m1['Accounts_Receivable']
    quick_assets_prev = row_m2['Cash_Balance'] + row_m2['Accounts_Receivable']
    quick_ratio = quick_assets / row_m1['Total_Current_Liabilities'] if row_m1['Total_Current_Liabilities'] > 0 else 0
    quick_ratio_prev = quick_assets_prev / row_m2['Total_Current_Liabilities'] if row_m2['Total_Current_Liabilities'] > 0 else 0
    quick_ratio_mom_pct = ((quick_ratio - quick_ratio_prev) / quick_ratio_prev * 100) if quick_ratio_prev != 0 else 0
    
    npm_pct = (net_act / inc_act * 100) if inc_act > 0 else 0
    pct_income_budget = (inc_act / row_m1['Revenue_Budget'] * 100) if row_m1['Revenue_Budget'] > 0 else 0
    pct_exp_budget = (exp_act / (row_m1['COGS_Budget'] + row_m1['OpEx_Budget']) * 100) if (row_m1['COGS_Budget'] + row_m1['OpEx_Budget']) > 0 else 0

    st.markdown("<br>", unsafe_allow_html=True)
    
    # ROW 1 KPI CARDS
    k_col1, k_col2, k_col3, k_col4, k_col5 = st.columns(5)
    
    with k_col1:
        pill_cls = "kpi-pill-pos" if inc_mom_pct >= 0 else "kpi-pill-neg"
        st.markdown(f"""
        <div class="kpi-wrapper kpi-accent-green">
            <div class="kpi-label">Income (Revenue)</div>
            <div class="kpi-val">{inc_act:,.0f}</div>
            <div class="{pill_cls}">{inc_mom_pct:+.1f}% vs {month_2}</div>
        </div>
        """, unsafe_allow_html=True)
        
    with k_col2:
        pill_cls = "kpi-pill-neg" if exp_mom_pct > 0 else "kpi-pill-pos"
        st.markdown(f"""
        <div class="kpi-wrapper kpi-accent-amber">
            <div class="kpi-label">Expenses (COGS+OpEx)</div>
            <div class="kpi-val">{exp_act:,.0f}</div>
            <div class="{pill_cls}">{exp_mom_pct:+.1f}% vs {month_2}</div>
        </div>
        """, unsafe_allow_html=True)
        
    with k_col3:
        st.markdown(f"""
        <div class="kpi-wrapper kpi-accent-green">
            <div class="kpi-label">% of Income Budget</div>
            <div class="kpi-val">{pct_income_budget:.0f}%</div>
            <div class="kpi-pill-pos">Target Achieved</div>
        </div>
        """, unsafe_allow_html=True)
        
    with k_col4:
        pill_cls = "kpi-pill-pos" if ar_mom_pct <= 0 else "kpi-pill-neg"
        st.markdown(f"""
        <div class="kpi-wrapper kpi-accent-blue">
            <div class="kpi-label">Accounts Receivable</div>
            <div class="kpi-val">{ar_act:,.0f}</div>
            <div class="{pill_cls}">{ar_mom_pct:+.1f}% vs {month_2}</div>
        </div>
        """, unsafe_allow_html=True)
        
    with k_col5:
        st.markdown(f"""
        <div class="kpi-wrapper kpi-accent-blue">
            <div class="kpi-label">Accounts Payable</div>
            <div class="kpi-val">{ap_act:,.0f}</div>
            <div class="kpi-pill-pos">{ap_mom_pct:+.1f}% vs {month_2}</div>
        </div>
        """, unsafe_allow_html=True)
        
    # ROW 2 KPI CARDS
    k_col6, k_col7, k_col8, k_col9, k_col10 = st.columns(5)
    
    with k_col6:
        pill_cls = "kpi-pill-pos" if net_mom_pct >= 0 else "kpi-pill-neg"
        st.markdown(f"""
        <div class="kpi-wrapper kpi-accent-green">
            <div class="kpi-label">Net Profit</div>
            <div class="kpi-val">{net_act:,.0f}</div>
            <div class="{pill_cls}">{net_mom_pct:+.1f}% vs {month_2}</div>
        </div>
        """, unsafe_allow_html=True)
        
    with k_col7:
        pill_cls = "kpi-pill-pos" if cash_mom_pct >= 0 else "kpi-pill-neg"
        st.markdown(f"""
        <div class="kpi-wrapper kpi-accent-navy">
            <div class="kpi-label">Cash Balance</div>
            <div class="kpi-val">{cash_act:,.0f}</div>
            <div class="{pill_cls}">{cash_mom_pct:+.1f}% vs {month_2}</div>
        </div>
        """, unsafe_allow_html=True)
        
    with k_col8:
        st.markdown(f"""
        <div class="kpi-wrapper kpi-accent-navy">
            <div class="kpi-label">% of Expenses Budget</div>
            <div class="kpi-val">{pct_exp_budget:.0f}%</div>
            <div class="kpi-pill-pos">Budget Realized</div>
        </div>
        """, unsafe_allow_html=True)
        
    with k_col9:
        st.markdown(f"""
        <div class="kpi-wrapper kpi-accent-blue">
            <div class="kpi-label">Quick Ratio</div>
            <div class="kpi-val">{quick_ratio:.2f}</div>
            <div class="kpi-pill-pos">{quick_ratio_mom_pct:+.1f}% vs {month_2}</div>
        </div>
        """, unsafe_allow_html=True)
        
    with k_col10:
        st.markdown(f"""
        <div class="kpi-wrapper kpi-accent-blue">
            <div class="kpi-label">Current Ratio</div>
            <div class="kpi-val">{curr_ratio:.2f}</div>
            <div class="kpi-pill-pos">{curr_ratio_mom_pct:+.1f}% vs {month_2}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # WATERFALL & SUMMARY LIST
    col_v1, col_v2 = st.columns([1.8, 1])
    
    with col_v1:
        st.markdown("<div class='excel-card'>", unsafe_allow_html=True)
        st.markdown("#### 📊 P&L Statement Waterfall Breakdown")
        
        fig_waterfall = go.Figure(go.Waterfall(
            name="P&L", orientation="v",
            measure=["relative", "relative", "total", "relative", "total"],
            x=["Total Income", "COGS", "Gross Profit", "OpEx", "Net Profit"],
            text=[f"+{inc_act:,.0f}", f"-{row_m1['COGS_Actual']:,.0f}", f"{(inc_act-row_m1['COGS_Actual']):,.0f}", f"-{row_m1['OpEx_Actual']:,.0f}", f"{net_act:,.0f}"],
            y=[inc_act, -row_m1['COGS_Actual'], 0, -row_m1['OpEx_Actual'], 0],
            connector={"line":{"color":"#94a3b8"}},
            decreasing={"marker":{"color":"#dc2626"}},
            increasing={"marker":{"color":"#16a34a"}},
            totals={"marker":{"color":"#1e3a8a"}}
        ))
        fig_waterfall.update_layout(template="plotly_white", paper_bgcolor="rgba(0,0,0,0)", height=320, margin=dict(l=10, r=10, t=10, b=10))
        st.plotly_chart(fig_waterfall, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
    with col_v2:
        st.markdown("<div class='excel-card'>", unsafe_allow_html=True)
        st.markdown("#### 📋 Executive KPI Summary List")
        
        kpi_list_df = pd.DataFrame([
            {"ID": 1, "KPIs": "Income Growth (MoM)", "Value": f"{inc_mom_pct:+.1f}%"},
            {"ID": 2, "KPIs": "Net Profit Growth (MoM)", "Value": f"{net_mom_pct:+.1f}%"},
            {"ID": 3, "KPIs": "Net Profit Margin %", "Value": f"{npm_pct:.1f}%"},
            {"ID": 4, "KPIs": "Expenses Change (MoM)", "Value": f"{exp_mom_pct:+.1f}%"},
            {"ID": 5, "KPIs": "Cash Balance Change", "Value": f"{cash_mom_pct:+.1f}%"},
            {"ID": 6, "KPIs": "Quick Ratio", "Value": f"{quick_ratio:.2f}"},
            {"ID": 7, "KPIs": "Current Ratio", "Value": f"{curr_ratio:.2f}"},
            {"ID": 8, "KPIs": "% of Income Budget", "Value": f"{pct_income_budget:.1f}%"},
            {"ID": 9, "KPIs": "% of Expenses Budget", "Value": f"{pct_exp_budget:.1f}%"}
        ])
        st.dataframe(kpi_list_df, use_container_width=True, hide_index=True)
        st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# TAB 2: TABEL KOMPARASI DETAIL
# ==========================================
with tab_table:
    st.markdown("### 📋 Komparasi Laporan Keuangan (Actual vs Budget)")

    def fmt_rp(val):
        if val < 0:
            return f"({abs(val):,.0f})"
        return f"{val:,.0f}"

    def fmt_pct(val):
        if val < 0:
            return f"<span style='color: #dc2626; font-weight: bold;'>-{abs(val):.0f}%</span>"
        return f"<span style='color: #16a34a; font-weight: bold;'>{val:.0f}%</span>"

    def get_status_icon(name, var_pct):
        is_cost = name in ['COGS', 'Opex']
        if is_cost:
            return "✅" if var_pct <= 0 else "❌"
        return "✅" if var_pct >= 0 else "❌"

    def get_mini_bar(var_pct):
        width = min(max(int(abs(var_pct) * 1.5), 12), 100)
        fill_cls = "spark-fill-purple" if var_pct >= 0 else "spark-fill-red"
        return f"<div class='spark-bg'><div class='{fill_cls}' style='width: {width}%;'></div></div>"

    components = [
        ("Revenue (Penjualan)", row_m1['Revenue_Actual'], row_m2['Revenue_Actual'], row_m1['Revenue_Budget'], row_m2['Revenue_Budget']),
        ("COGS", row_m1['COGS_Actual'], row_m2['COGS_Actual'], row_m1['COGS_Budget'], row_m2['COGS_Budget']),
        ("Gross Profit", gp_m1_act, gp_m2_act, gp_m1_bud, gp_m2_bud),
        ("Opex", row_m1['OpEx_Actual'], row_m2['OpEx_Actual'], row_m1['OpEx_Budget'], row_m2['OpEx_Budget']),
        ("Nett Profit", row_m1['Net_Profit_Actual'], row_m2['Net_Profit_Actual'], row_m1['Net_Profit_Budget'], row_m2['Net_Profit_Budget'])
    ]

    table_rows_html = ""
    for name, act1, act2, bud1, bud2 in components:
        var_foc_rp = act1 - bud1
        var_foc_pct = ((act1 - bud1) / abs(bud1) * 100) if bud1 != 0 else 0
        bar_foc = get_mini_bar(var_foc_pct)
        
        var_act_rp = act1 - act2
        var_act_pct = ((act1 - act2) / abs(act2) * 100) if act2 != 0 else 0
        bar_act = get_mini_bar(var_act_pct)
        
        var_bud_rp = bud1 - bud2
        var_bud_pct = ((bud1 - bud2) / abs(bud2) * 100) if bud2 != 0 else 0
        bar_bud = get_mini_bar(var_bud_pct)
        
        icon_foc = get_status_icon(name, var_foc_pct)
        
        table_rows_html += f"""
        <tr>
            <td style='text-align: left; font-weight: 600;'>{name}</td>
            <td>{fmt_rp(act1)} {icon_foc}</td>
            <td>{fmt_rp(act2)}</td>
            <td>{fmt_rp(bud1)}</td>
            <td>{fmt_rp(bud2)}</td>
            <td class='focus-cell'>{fmt_rp(var_foc_rp)}</td>
            <td class='focus-cell'>{fmt_pct(var_foc_pct)}</td>
            <td class='focus-cell'>{bar_foc}</td>
            <td>{fmt_rp(var_act_rp)}</td>
            <td>{fmt_pct(var_act_pct)}</td>
            <td>{bar_act}</td>
            <td>{fmt_rp(var_bud_rp)}</td>
            <td>{fmt_pct(var_bud_pct)}</td>
            <td>{bar_bud}</td>
        </tr>
        """

    full_table_html = f"""
    <div class="table-container">
        <table class="custom-table">
            <thead>
                <tr>
                    <th rowspan="2" style="text-align: left;">Komponen Keuangan</th>
                    <th colspan="2">Actual (Rp)</th>
                    <th colspan="2">Budget (Rp)</th>
                    <th colspan="3" class="focus-header">Variance Bulan Focus (vs Budget)</th>
                    <th colspan="3">Variance Actual ({month_1} vs {month_2})</th>
                    <th colspan="3">Variance Budget ({month_1} vs {month_2})</th>
                </tr>
                <tr>
                    <th>{month_1}</th>
                    <th>{month_2}</th>
                    <th>{month_1}</th>
                    <th>{month_2}</th>
                    <th class="focus-header">Rp</th>
                    <th class="focus-header">%</th>
                    <th class="focus-header">Trend</th>
                    <th>Rp</th>
                    <th>%</th>
                    <th>Trend</th>
                    <th>Rp</th>
                    <th>%</th>
                    <th>Trend</th>
                </tr>
            </thead>
            <tbody>
                {table_rows_html}
            </tbody>
        </table>
    </div>
    """

    st.html(full_table_html)

# ==========================================
# 5. CHARTS & VISUALS
# ==========================================
st.markdown("<br>", unsafe_allow_html=True)
col_c1, col_c2 = st.columns([1.6, 1])

with col_c1:
    st.markdown("<div class='excel-card'>", unsafe_allow_html=True)
    st.markdown("#### 📈 Perbandingan Actual (Bulan Fokus vs Pembanding)")
    
    chart_data = pd.DataFrame({
        'Komponen': ['Revenue', 'COGS', 'Gross Profit', 'OpEx', 'Net Profit'],
        month_1: [row_m1['Revenue_Actual'], row_m1['COGS_Actual'], gp_m1_act, row_m1['OpEx_Actual'], row_m1['Net_Profit_Actual']],
        month_2: [row_m2['Revenue_Actual'], row_m2['COGS_Actual'], gp_m2_act, row_m2['OpEx_Actual'], row_m2['Net_Profit_Actual']]
    })
    
    fig_comp = go.Figure()
    fig_comp.add_trace(go.Bar(x=chart_data['Komponen'], y=chart_data[month_1], name=month_1, marker_color='#1e3a8a'))
    fig_comp.add_trace(go.Bar(x=chart_data['Komponen'], y=chart_data[month_2], name=month_2, marker_color='#cbd5e1'))
    
    fig_comp.update_layout(
        barmode='group', template="plotly_white", paper_bgcolor='rgba(0,0,0,0)', height=320,
        margin=dict(l=10, r=10, t=10, b=10), legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    st.plotly_chart(fig_comp, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col_c2:
    st.markdown("<div class='excel-card'>", unsafe_allow_html=True)
    st.markdown(f"#### 🎯 Pencapaian Target Budget ({month_1})")
    
    rev_achieved_pct = (row_m1['Revenue_Actual'] / row_m1['Revenue_Budget']) * 100 if row_m1['Revenue_Budget'] > 0 else 0
    
    fig_gauge = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = rev_achieved_pct,
        number = {'suffix': "%"},
        title = {'text': f"Pencapaian Target Revenue", 'font': {'size': 13, 'color': '#64748b'}},
        gauge = {
            'axis': {'range': [0, 150]},
            'bar': {'color': "#16a34a"},
            'steps': [
                {'range': [0, 80], 'color': "#fee2e2"},
                {'range': [80, 100], 'color': "#fef3c7"},
                {'range': [100, 150], 'color': "#dcfce7"}
            ]
        }
    ))
    fig_gauge.update_layout(template="plotly_white", paper_bgcolor='rgba(0,0,0,0)', height=320, margin=dict(l=10, r=10, t=10, b=10))
    st.plotly_chart(fig_gauge, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# 6. GUARANTEED 5-BOX MULTI-FINANCIAL ANALYSIS
# ==========================================
st.markdown("<div class='excel-card'>", unsafe_allow_html=True)
st.markdown("### 💡 Hasil Analisis & Rekomendasi Manajemen Komprehensif")

# DIRECT UNCONDITIONAL ARRAY GENERATION
foc_rev_var = row_m1['Revenue_Actual'] - row_m1['Revenue_Budget']
foc_rev_pct = (foc_rev_var / row_m1['Revenue_Budget']) * 100 if row_m1['Revenue_Budget'] > 0 else 0

cogs_foc_var = row_m1['COGS_Actual'] - row_m1['COGS_Budget']
gpm_m1 = ((row_m1['Revenue_Actual'] - row_m1['COGS_Actual']) / row_m1['Revenue_Actual'] * 100) if row_m1['Revenue_Actual'] > 0 else 0
gpm_m2 = ((row_m2['Revenue_Actual'] - row_m2['COGS_Actual']) / row_m2['Revenue_Actual'] * 100) if row_m2['Revenue_Actual'] > 0 else 0

foc_opex_var = row_m1['OpEx_Actual'] - row_m1['OpEx_Budget']
foc_opex_pct = (foc_opex_var / row_m1['OpEx_Budget'] * 100) if row_m1['OpEx_Budget'] > 0 else 0

npm_m1 = (row_m1['Net_Profit_Actual'] / row_m1['Revenue_Actual'] * 100) if row_m1['Revenue_Actual'] > 0 else 0

ar_m1 = row_m1['Accounts_Receivable']
ar_m2 = row_m2['Accounts_Receivable']
ar_growth = ((ar_m1 - ar_m2) / ar_m2 * 100) if ar_m2 > 0 else 0

curr_r = row_m1['Total_Current_Assets'] / row_m1['Total_Current_Liabilities'] if row_m1['Total_Current_Liabilities'] > 0 else 0

# FORMATTED HTML BOXES FOR ALL 5 DIMENSIONS
box_1_rev = f"<b>[1. KINERJA PENJUALAN / REVENUE]</b> Target budget {month_1}: " + (f"<span style='color:#16a34a;'><b>TERCAPAI (+{foc_rev_pct:.1f}%)</b></span>. Surplus: Rp {foc_rev_var:,.0f}." if foc_rev_var >= 0 else f"<span style='color:#dc2626;'><b>TIDAK TERCAPAI ({foc_rev_pct:.1f}%)</b></span>. Defisit: Rp {abs(foc_rev_var):,.0f}.") + f"<br>MoM vs {month_2}: " + (f"Tumbuh <b>+{rev_var_pct:.1f}%</b>." if rev_var_rp >= 0 else f"Penurunan <b>{rev_var_pct:.1f}%</b> (Turun Rp {abs(rev_var_rp):,.0f}).")

box_2_cogs = f"<b>[2. HARGA POKOK PENJUALAN / COGS & GPM]</b> COGS {month_1}: Rp {row_m1['COGS_Actual']:,.0f} " + (f"(<span style='color:#dc2626;'><b>Overbudget Rp {cogs_foc_var:,.0f}</b></span>). Audit biaya baku produksi." if cogs_foc_var > 0 else "(<span style='color:#16a34a;'><b>Efisiensi di bawah budget</b></span>).") + f" Gross Profit Margin: <b>{gpm_m1:.1f}%</b> (Pembanding {month_2}: {gpm_m2:.1f}%)."

box_3_opex = f"<b>[3. BIAYA OPERASIONAL / OPEX CONTROL]</b> OpEx {month_1}: Rp {row_m1['OpEx_Actual']:,.0f} " + (f"(<span style='color:#dc2626;'><b>Overbudget +{foc_opex_pct:.1f}% / Rp {foc_opex_var:,.0f}</b></span>). Pengetatan biaya umum & administrasi." if foc_opex_var > 0 else "(<span style='color:#16a34a;'><b>Efisiensi dibawah budget</b></span>).")

box_4_net = f"<b>[4. PROFITABILITAS BERSIH / NET PROFIT]</b> Laba Bersih {month_1}: Rp {row_m1['Net_Profit_Actual']:,.0f} (NPM: <b>{npm_m1:.1f}%</b>). " + ("<span style='color:#b45309;'>🚨 Margin bersih tertekan (Ideal ≥ 10%). Tinjau efisiensi biaya.</span>" if npm_m1 < 10 else "<span style='color:#16a34a;'>✓ Tingkat profitabilitas dalam kondisi sehat.</span>")

box_5_wc = f"<b>[5. MODAL KERJA & LIKUIDITAS / AR & CURRENT RATIO]</b> Piutang Dagang (AR) {month_1}: Rp {ar_m1:,.0f} ({ar_growth:+.1f}% vs {month_2}). Current Ratio: <b>{curr_r:.2f}x</b> " + ("(<span style='color:#16a34a;'><b>Likuiditas Sehat ≥ 1.5x</b></span>)." if curr_r >= 1.5 else "(<span style='color:#dc2626;'><b>Di bawah batas aman 1.5x</b></span>. Percepat penagihan piutang).")

# RENDER ALL 5 BOXES
st.markdown(f"<div class='rec-box-blue'>📈 {box_1_rev}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='rec-box-amber'>📦 {box_2_cogs}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='rec-box-purple'>📉 {box_3_opex}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='rec-box-emerald'>🎯 {box_4_net}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='rec-box-teal'>🏦 {box_5_wc}</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# 7. EXPORT OPTIONS
# ==========================================
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("### 📥 Download / Export Hasil Analisis")

col_btn1, col_btn2 = st.columns(2)

with col_btn1:
    if st.button("📄 Convert & Download Dashboard to PDF", use_container_width=True):
        st.components.v1.html(
            """
            <script>
                window.parent.focus();
                window.parent.print();
            </script>
            """,
            height=0
        )

with col_btn2:
    def generate_excel_report():
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            export_df = pd.DataFrame([
                {
                    'Komponen Keuangan': name,
                    f'Actual {month_1}': act1,
                    f'Actual {month_2}': act2,
                    f'Budget {month_1}': bud1,
                    f'Budget {month_2}': bud2,
                    'Var Bulan Focus (Rp)': act1 - bud1,
                    'Var Bulan Focus (%)': f"{((act1 - bud1) / abs(bud1) * 100):.1f}%" if bud1 != 0 else "0%",
                    'Var Actual MoM (Rp)': act1 - act2,
                    'Var Actual MoM (%)': f"{((act1 - act2) / abs(act2) * 100):.1f}%" if act2 != 0 else "0%",
                    'Var Budget MoM (Rp)': bud1 - bud2,
                    'Var Budget MoM (%)': f"{((bud1 - bud2) / abs(bud2) * 100):.1f}%" if bud2 != 0 else "0%"
                } for name, act1, act2, bud1, bud2 in components
            ])
            export_df.to_excel(writer, index=False, sheet_name='Komparasi_Laporan_Keuangan')
            rec_df = pd.DataFrame({'Rekomendasi Manajemen': [box_1_rev, box_2_cogs, box_3_opex, box_4_net, box_5_wc]})
            rec_df.to_excel(writer, index=False, sheet_name='Analisis_Rekomendasi')
        return output.getvalue()

    st.download_button(
        label="📊 Export Data Komparasi ke Excel (.xlsx)",
        data=generate_excel_report(),
        file_name=f"Komparasi_Keuangan_{month_1}_vs_{month_2}_{selected_year}.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        use_container_width=True
    )