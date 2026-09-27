import streamlit as st

st.set_page_config(
    page_title="ResolveIQ",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 ResolveIQ")
st.subheader("Organizational Escalation Intelligence Agent")
st.caption("Remember → Recall → Learn → Improve")

st.divider()

# -------------------------
# Customer & Issue
# -------------------------

st.header("🎫 Customer & Issue")

customer_id = st.text_input(
    "Customer ID",
    value="C102"
)

issue = st.text_input(
    "Issue",
    value="Payment failed"
)

description = st.text_area(
    "Issue Description",
    value="Customer reports payment failure for the third time."
)

analyze = st.button(
    "🔍 Analyze Issue",
    use_container_width=True
)

# -------------------------
# Mock historical memory
# -------------------------

historical_cases = [
    {
        "case": "Case #C102-01",
        "attempt": "Bank verification",
        "result": "Resolved"
    },
    {
        "case": "Case #C102-02",
        "attempt": "Bank verification + Retry",
        "result": "Failed"
    },
    {
        "case": "Case #C102-03",
        "attempt": "Payment retry",
        "result": "Failed"
    }
]

if analyze:

    st.divider()

    # -------------------------
    # Historical Memory
    # -------------------------

    st.header("🧠 Historical Memory")

    st.write(
        f"ResolveIQ found previous cases related to customer **{customer_id}**."
    )

    for case in historical_cases:
        with st.container(border=True):
            st.write(f"**{case['case']}**")
            st.write(f"Attempted solution: {case['attempt']}")
            st.write(f"Result: {case['result']}")

    # -------------------------
    # Recommendation
    # -------------------------

    st.header("🤖 ResolveIQ Recommendation")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Issue Severity",
            "HIGH"
        )

    with col2:
        st.metric(
            "Recurring Issue",
            "YES"
        )

    st.warning(
        "⚠️ Escalation recommended"
    )

    st.success(
        "Recommendation: Escalate to Payment Operations"
    )

    st.info(
        "Reason: Similar troubleshooting attempts have failed "
        "in previous cases. Repeating the same troubleshooting "
        "is unlikely to resolve the issue."
    )

    # -------------------------
    # Final Resolution
    # -------------------------

    st.header("✅ Final Resolution")

    resolution = st.text_area(
        "Enter the final resolution after the issue is handled",
        placeholder="Example: Payment Operations identified a gateway configuration issue..."
    )

    if st.button(
        "💾 Save Resolution",
        use_container_width=True
    ):
        if resolution.strip():
            st.success(
                "Resolution recorded. ResolveIQ can use this outcome as future organizational memory."
            )
        else:
            st.warning(
                "Please enter the final resolution."
            )
