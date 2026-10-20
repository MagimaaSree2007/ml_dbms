
import streamlit as st
from database import get_connection


def create_organization(name, description=""):
    """Create a company workspace for the logged-in user."""

    user_id = st.session_state.user["user_id"]
    name = name.strip()

    if not name:
        return False, "Enter an organization name."

    conn = get_connection()
    cursor = conn.cursor()

    try:
        # Create the organization
        cursor.execute(
            """
            INSERT INTO Organizations (organization_name, created_by)
            VALUES (%s, %s)
            """,
            (name, user_id)
        )

        organization_id = cursor.lastrowid

        # Make the creator its organization admin
        cursor.execute(
            """
            INSERT INTO Organization_Members
                (organization_id, user_id, organization_role)
            VALUES (%s, %s, 'Org Admin')
            """,
            (organization_id, user_id)
        )

        conn.commit()
        return True, f"Workspace '{name}' created successfully."

    except Exception as e:
        conn.rollback()
        return False, f"Could not create workspace: {e}"

    finally:
        cursor.close()
        conn.close()


def get_user_organizations(user_id):
    """Return the organizations a user belongs to."""

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        cursor.execute(
            """
            SELECT
                o.organization_id,
                o.organization_name,
                om.organization_role
            FROM Organizations o
            JOIN Organization_Members om
                ON o.organization_id = om.organization_id
            WHERE om.user_id = %s
            ORDER BY o.organization_name
            """,
            (user_id,)
        )

        return cursor.fetchall()

    finally:
        cursor.close()
        conn.close()


def add_existing_member(organization_id, email, role):
    """Add an existing registered user to an organization."""

    current_user_id = st.session_state.user["user_id"]

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        # Confirm the current user is an organization admin
        cursor.execute(
            """
            SELECT organization_role
            FROM Organization_Members
            WHERE organization_id = %s AND user_id = %s
            """,
            (organization_id, current_user_id)
        )

        membership = cursor.fetchone()

        if not membership or membership["organization_role"] != "Org Admin":
            return False, "Only an organization admin can add members."

        # Find the registered user by email
        cursor.execute(
            "SELECT user_id FROM Users WHERE email = %s",
            (email.strip(),)
        )
        member = cursor.fetchone()

        if not member:
            return False, "This user must register before being added."

        cursor.execute(
            """
            INSERT INTO Organization_Members
                (organization_id, user_id, organization_role)
            VALUES (%s, %s, %s)
            """,
            (organization_id, member["user_id"], role)
        )

        conn.commit()
        return True, "Member added successfully."

    except Exception as e:
        conn.rollback()
        return False, f"Could not add member: {e}"

    finally:
        cursor.close()
        conn.close()


def organization_page():
    """Streamlit page for organization and team management."""

    st.title("🏢 Company Workspace")
    st.write(
        "Create an organization, view your team workspaces, "
        "and manage existing registered members."
    )

    user_id = st.session_state.user["user_id"]

    with st.expander("Create a company workspace"):
        with st.form("create_org_form"):
            org_name = st.text_input(
                "Company or organization name",
                placeholder="Example: ABC Analytics"
            )
            submitted = st.form_submit_button("Create Workspace")

            if submitted:
                success, message = create_organization(org_name)

                if success:
                    st.success(message)
                    st.rerun()
                else:
                    st.error(message)

    organizations = get_user_organizations(user_id)

    st.subheader("Your Organizations")

    if not organizations:
        st.info("You have not joined any organization yet.")
        return

    for org in organizations:
        with st.container(border=True):
            st.subheader(org["organization_name"])
            st.caption(
                f"Your role: {org['organization_role']}"
            )

            if org["organization_role"] == "Org Admin":
                with st.expander("Add a registered team member"):
                    with st.form(
                        f"add_member_{org['organization_id']}"
                    ):
                        email = st.text_input("Member's registered email")
                        role = st.selectbox(
                            "Assign role",
                            ["Data Analyst", "ML Engineer", "Viewer"]
                        )

                        add = st.form_submit_button("Add Member")

                        if add:
                            success, message = add_existing_member(
                                org["organization_id"],
                                email,
                                role
                            )

                            if success:
                                st.success(message)
                                st.rerun()
                            else:
                                st.error(message)
