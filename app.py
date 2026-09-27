import streamlit as st

st.set_page_config(
    page_title="ResolveIQ",
    page_icon="🧠"
)

st.title("🧠 ResolveIQ")
st.subheader("Organizational Escalation Intelligence")

st.divider()

st.header("Customer & Issue")

customer_id = st.text_input(
    "Customer ID",
    value="C102"
)

issue = st.text_input(
    "Issue",
    value="Payment failed"
)

description = st.text_area(
    "Description",
    value="Customer reports payment failure for the third time."
)

if st.button("🔍 Analyze Issue"):

    st.divider()

    st.header("Historical Memory")

    st.info(
        "Previous Case 1\n\n"
        "Issue: Payment failed\n\n"
        "Attempt: Bank verification\n\n"
        "Result: Failed"
    )

    st.warning(
        "Previous Case 2\n\n"
        "Issue: Payment failed\n\n"
        "Attempt: Retry payment\n\n"
        "Result: Failed"
    )

    st.divider()

    st.header("ResolveIQ Recommendation")

    st.error("⚠️ Recurring Issue")

    st.write("**Severity:** HIGH")

    st.success(
        "Recommendation: Escalate to Payment Operations"
    )

    st.write(
        "**Reason:** Previous troubleshooting attempts failed."
    )

st.divider()

st.caption("ResolveIQ — Remember → Recall → Learn → Improve")
