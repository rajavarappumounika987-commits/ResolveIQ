import streamlit as st


def show_customer_input():
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

    return customer_id, issue, description


def show_recommendation():
    st.header("ResolveIQ Recommendation")

    st.error("⚠️ Recurring Issue")

    st.write("**Severity:** HIGH")

    st.success(
        "Recommendation: Escalate to Payment Operations"
    )

    st.write(
        "**Reason:** Previous troubleshooting attempts failed."
    )
