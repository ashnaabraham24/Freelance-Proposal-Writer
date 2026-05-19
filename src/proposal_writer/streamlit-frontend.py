import streamlit as st

from proposal_writer.crew import ProposalWriter

def main():

    st.title("Freelance Proposal Writer")

    st.sidebar.title("Client Project")

    project_input = st.sidebar.text_area(
        "Describe client project",
        height=250
    )

    if st.sidebar.button("Generate Proposal"):

        if project_input:

            inputs = {
                "project_description": project_input
            }

            with st.spinner(
                "Generating proposal..."
            ):

                result = (
                    ProposalWriter()
                    .crew()
                    .kickoff(inputs=inputs)
                )

            st.session_state["proposal"] = (
                result.tasks_output[1].raw
            )

            st.session_state["pricing"] = (
                result.tasks_output[2].raw
            )

        else:

            st.sidebar.error(
                "Enter project details"
            )

    # ← THIS PART MUST BE OUTSIDE BUTTON

    if "proposal" in st.session_state:

        st.success("Proposal created!")

        tab1, tab2 = st.tabs(
            ["Proposal", "Pricing"]
        )

        with tab1:

            st.text_area(
                "Proposal",
                st.session_state["proposal"],
                height=500
            )

            st.download_button(
                "Download Proposal",
                st.session_state["proposal"],
                file_name="proposal.txt"
            )

        with tab2:

            st.text_area(
                "Pricing",
                st.session_state["pricing"],
                height=400
            )

            st.download_button(
                "Download Pricing",
                st.session_state["pricing"],
                file_name="pricing.txt"
            )


if __name__ == "__main__":
    main()