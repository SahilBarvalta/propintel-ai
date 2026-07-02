import streamlit as st

from services.gemini_service import ask_gemini
from services.prompt_service import load_prompt
from services.rag_service import search_properties

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="PropIntel AI",
    page_icon="🏠",
    layout="wide"
)
st.markdown("""
<style>

/* App Background */
.main{
    background-color:#f5f7fb;
}

/* KPI Cards */
.kpi-card{
    background: linear-gradient(135deg,#1E3A8A,#2563EB);
    color:white;
    padding:20px;
    border-radius:15px;
    text-align:center;
    box-shadow:0 8px 18px rgba(0,0,0,.15);
    margin-bottom:10px;
}

.kpi-title{
    font-size:15px;
    opacity:.9;
}

.kpi-value{
    font-size:34px;
    font-weight:700;
    margin-top:8px;
}

/* Feature Cards */
.feature-card{
    background: linear-gradient(135deg,#0F172A,#334155);
    color:white;
    padding:25px;
    border-radius:15px;
    min-height:220px;
    box-shadow:0 8px 18px rgba(0,0,0,.15);
}

.feature-card h3{
    color:white;
    margin-bottom:15px;
}

.feature-card p{
    color:#E2E8F0;
    line-height:1.6;
}

</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>

.main {
    background-color:#f7f9fc;
}

div[data-testid="stMetric"]{
    border-radius:12px;
    border:1px solid #dbe4f0;
    padding:15px;
    background:white;
}

.stButton > button{
    width:100%;
    height:52px;
    border-radius:12px;
    font-size:18px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>

/* Main App */
.main {
    background-color: #f5f7fb;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background-color:#1e293b;
}

section[data-testid="stSidebar"] *{
    color:white;
}

/* Cards */
div[data-testid="stMetric"]{
    background:white;
    border-radius:12px;
    padding:15px;
    border:1px solid #dbe4f0;
}

/* Buttons */
.stButton>button{
    background:#2563eb;
    color:white;
    border-radius:10px;
    height:50px;
    width:100%;
    font-size:18px;
    font-weight:bold;
}

.stButton>button:hover{
    background:#1d4ed8;
}

/* Headers */
h1,h2,h3{
    color:#1e293b;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #

with st.sidebar:

    st.title("🏠 PropIntel AI")

    st.markdown("### AI-powered Property Intelligence")

    st.success("Version 0.8")

    st.markdown("---")

    st.markdown("### Platform")

    st.markdown("""
- 🤖 Gemini 2.5 Flash
- 🧠 Retrieval-Augmented Generation (RAG)
- 📊 Investment Recommendation Engine
- 🏘 2,000 Synthetic Property Listings
- ⭐ Investment Scoring
""")

    st.markdown("---")

    st.info("Technology Preview")

    st.markdown("---")

    st.markdown("""
<div style='text-align:center'>
<b>Built by</b>
<h3>Sahil Barvalta</h3>
Senior Product Manager<br>
AI • PropTech • Growth
</div>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #

st.title("🏠 PropIntel AI")

st.caption("AI-powered Property Intelligence Platform")

st.markdown("""
## Understand. Compare. Invest Smarter.

Helping investors discover and evaluate Dubai real estate opportunities using
AI-powered recommendations, structured property intelligence, and market insights.
""")

st.markdown("---")

hero1, hero2, hero3, hero4 = st.columns(4)

with hero1:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-title">🏘 Listings</div>
        <div class="kpi-value">2,000+</div>
    </div>
    """, unsafe_allow_html=True)

with hero2:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-title">🏙 Communities</div>
        <div class="kpi-value">10</div>
    </div>
    """, unsafe_allow_html=True)

with hero3:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-title">🏢 Developers</div>
        <div class="kpi-value">20</div>
    </div>
    """, unsafe_allow_html=True)

with hero4:
    st.markdown("""
    <div class="kpi-card">
        <div class="kpi-title">🤖 AI Model</div>
        <div class="kpi-value">Gemini 2.5</div>
    </div>
    """, unsafe_allow_html=True)

# ---------------- FORM ---------------- #

st.header("Investment Preferences")

col1, col2 = st.columns(2)

with col1:

    budget = st.number_input(
        "Investment Budget (AED)",
        min_value=100000,
        value=2000000,
        step=100000
    )

    property_type = st.selectbox(
        "Property Type",
        [
            "Apartment",
            "Villa",
            "Townhouse",
            "Penthouse"
        ]
    )

    investment_goal = st.selectbox(
        "Investment Goal",
        [
            "Rental Income",
            "Capital Appreciation",
            "Balanced"
        ]
    )

with col2:

    risk = st.selectbox(
        "Risk Appetite",
        [
            "Low",
            "Medium",
            "High"
        ]
    )

    horizon = st.selectbox(
        "Investment Horizon",
        [
            "1-3 Years",
            "3-5 Years",
            "5-10 Years",
            "10+ Years"
        ]
    )

    community = st.selectbox(
    "Community",
    [
        "Any Community",
        "Dubai Marina",
        "Downtown Dubai",
        "Business Bay",
        "Dubai Hills Estate",
        "JVC",
        "Palm Jumeirah",
        "Dubai Creek Harbour",
        "Arabian Ranches",
        "Dubai South",
        "MBR City"
    ]
)

st.markdown("""
<div style="
background:#274c46;
padding:18px;
border-radius:10px;
font-size:17px;
">
💡 Complete your investment profile and click
<b>Find Investment Opportunities</b>
to receive AI-powered recommendations.
</div>
""", unsafe_allow_html=True)

# ---------------- BUTTON ---------------- #

if st.button("🔍 Find Investment Opportunities"):

    matching_properties = search_properties(
        budget=budget,
        property_type=property_type,
        risk=risk,
        community=community
    )

    if matching_properties.empty:

        st.error("No matching properties found.")

    else:

        best_property = matching_properties.iloc[0]

        total_properties = len(matching_properties)

        average_price = int(
            matching_properties["Price_AED"].mean()
        )

        average_roi = (
            matching_properties["ROI"]
            .str.replace("%", "", regex=False)
            .astype(float)
            .mean()
        )

        average_yield = (
            matching_properties["Rental_Yield"]
            .str.replace("%", "", regex=False)
            .astype(float)
            .mean()
        )

        property_context = matching_properties.to_string(index=False)

        system_prompt = load_prompt()

        investment_prompt = f"""
Investment Budget: AED {budget}

Investment Goal: {investment_goal}

Property Type: {property_type}

Risk Appetite: {risk}

Investment Horizon: {horizon}

Preferred Community: {community if community else "No Preference"}

Recommend ONLY from the available properties.

Explain why.

Mention investment risks.

Do not guarantee returns.
"""

        full_prompt = f"""
{system_prompt}

Available Properties:

{property_context}

Investor Profile:

{investment_prompt}
"""

        with st.spinner("Searching investment opportunities..."):

            response = ask_gemini(full_prompt)

        st.success("Investment Analysis Complete")

        # ---------------- KPI CARDS ---------------- #

        k1, k2, k3, k4 = st.columns(4)

        with k1:
            st.metric(
                "Properties",
                total_properties
            )

        with k2:
            st.metric(
                "Average ROI",
                f"{average_roi:.1f}%"
            )

        with k3:
            st.metric(
                "Rental Yield",
                f"{average_yield:.1f}%"
            )

        with k4:
            st.metric(
                "Budget",
                f"AED {budget:,.0f}"
            )

        # ---------------- BEST PROPERTY ---------------- #

        st.markdown("---")

        st.subheader("🏆 Top Investment Opportunity")

        left, right = st.columns([3, 1])

        with left:

            st.markdown(f"""
### {best_property['Property']}

📍 **Community:** {best_property['Community']}

💰 **Price:** AED {best_property['Price_AED']:,}

📈 **ROI:** {best_property['ROI']}

🏡 **Rental Yield:** {best_property['Rental_Yield']}

⚠️ **Risk:** {best_property['Risk']}

🏢 **Developer:** {best_property['Developer']}
""")

        with right:

            st.metric(
                "Investment Score",
                f"{best_property['Investment_Score']}/100"
            )

        # ---------------- RESULTS ---------------- #

        tab1, tab2, tab3 = st.tabs(
            [
                "🤖 AI Analysis",
                "🏘 Properties",
                "ℹ️ Market Insights"
            ]
        )

        with tab1:

            st.subheader("📋 Executive Summary")
            st.write(response["summary"])

            st.subheader("✅ Advantages")
            for item in response["pros"]:
                st.success(item)

            st.subheader("⚠ Risks")
            for item in response["risks"]:
                st.warning(item)

            st.subheader("➡ Recommended Next Steps")
            for item in response["next_steps"]:
                st.info(item)

        with tab2:

            display_columns = [
                "Property",
                "Community",
                "Price_AED",
                "Investment_Score",
                "ROI",
                "Rental_Yield",
                "Risk"
            ]

            st.dataframe(
                matching_properties[display_columns],
                use_container_width=True,
                hide_index=True
            )

        with tab3:

            st.info("""
🚧 Coming Soon

• Community Comparison

• Market Trends

• Mortgage Calculator

• Investment Report

• AI Investment Agent
""")
st.subheader("Why PropIntel AI?")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
<div class="feature-card">
<h3>🤖 AI Investment Advisor</h3>

<p>
Receive personalized property investment recommendations powered by Gemini 2.5, RAG, and structured prompts.
</p>

</div>
""", unsafe_allow_html=True)

with c2:
    st.markdown("""
<div class="feature-card">
<h3>📊 Market Intelligence</h3>

<p>
Compare communities, rental yields, ROI, developers, and investment opportunities with AI-generated insights.
</p>

</div>
""", unsafe_allow_html=True)

with c3:
    st.markdown("""
<div class="feature-card">
<h3>🏘 Smart Property Search</h3>

<p>
Explore 2,000+ synthetic property listings using intelligent filters and AI-powered recommendations.
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("---")