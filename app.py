
import streamlit as st

from auth import register_user, login_user
from reports import show_dashboard
from datasets import upload_dataset, view_datasets
from versions import add_version, view_versions
from preprocessing import preprocessing_page, view_preprocessing
from models import model_management, view_models
from performance import performance_management, view_performance
from organization import organization_page


# =========================================================
# 1. PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="MLDMS | Dataset Management",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# 2. CUSTOM STYLING
# =========================================================

st.markdown(
    """
    <style>
    @import url(
      'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap'
    );

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background: #F5F7FB;
    }

    [data-testid="stSidebar"] {
        background: #111C34;
    }

    [data-testid="stSidebar"] * {
        color: #F1F5F9;
    }

    [data-testid="stSidebar"] div[role="radiogroup"] label {
        padding: 8px 10px;
        border-radius: 9px;
    }

    [data-testid="stSidebar"] div[role="radiogroup"] label:hover {
        background: #263653;
    }

    .brand {
        color: #2563EB;
        font-size: 30px;
        font-weight: 800;
        letter-spacing: -1px;
        margin-bottom: 3px;
    }

    .brand-subtitle {
        color: #64748B;
        font-size: 13px;
        margin-bottom: 25px;
    }

    .hero {
        background: linear-gradient(135deg, #17294D, #2563EB);
        padding: 38px 32px;
        border-radius: 20px;
        color: white;
        min-height: 390px;
    }

    .hero h1 {
        color: white;
        font-size: 36px;
        line-height: 1.2;
        font-weight: 800;
    }

    .hero p {
        color: #E2E8F0;
        font-size: 15px;
        line-height: 1.8;
    }

    .login-heading {
        color: #17294D;
        font-size: 29px;
        font-weight: 800;
        margin-bottom: 5px;
    }

    .muted {
        color: #64748B;
        font-size: 14px;
        line-height: 1.7;
    }

    .section-title {
        color: #17294D;
        font-size: 26px;
        font-weight: 800;
        text-align: center;
    }

    .stButton button,
    .stFormSubmitButton button {
        border-radius: 9px;
        min-height: 42px;
        font-weight: 600;
    }

    [data-testid="stForm"] {
        background: white;
        padding: 22px;
        border: 1px solid #E2E8F0;
        border-radius: 16px;
    }

    .footer {
        text-align: center;
        color: #94A3B8;
        font-size: 12px;
        padding: 24px 0 10px 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# 3. SESSION STATE
# =========================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user" not in st.session_state:
    st.session_state.user = None

if "auth_page" not in st.session_state:
    st.session_state.auth_page = "Login"


# =========================================================
# 4. BRAND HEADER
# =========================================================

def show_brand():
    st.markdown(
        """
        <div class="brand">📊 MLDMS</div>
        <div class="brand-subtitle">
            Machine Learning Dataset Management System
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# 5. HOMEPAGE AUDIENCE SECTION
# =========================================================

def show_audience_section():
    st.markdown("---")

    st.markdown(
        '<div class="section-title">'
        'Built for machine learning teams'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <p style="text-align:center;color:#64748B;">
        Organize datasets, preprocessing records, model details,
        and evaluation metrics in one workspace.
        </p>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3, gap="large")

    with col1:
        with st.container(border=True):
            st.markdown("### 📊 Data Analysts")
            st.write(
                "Organize datasets, review metadata, "
                "and document preprocessing operations."
            )

    with col2:
        with st.container(border=True):
            st.markdown("### 🧠 ML Engineers")
            st.write(
                "Maintain dataset versions, model records, "
                "and evaluation metrics."
            )

    with col3:
        with st.container(border=True):
            st.markdown("### 🏢 Organization Teams")
            st.write(
                "Create organization workspaces and manage "
                "team memberships."
            )

    st.caption(
        "Designed to support team workflows. Actual organization-wide "
        "data isolation requires access controls in the database queries."
    )


# =========================================================
# 6. LOGIN PAGE
# =========================================================

def login_page():
    show_brand()

    left, right = st.columns([1.1, 0.9], gap="large")

    with left:
        st.markdown(
            """
            <div class="hero">
                <h1>Manage your ML datasets smarter.</h1>
                <p>
                    A centralized workspace to organize datasets,
                    maintain versions, document preprocessing,
                    and track model performance.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")

        with st.container(border=True):
            st.markdown("### 📁 Dataset Management")
            st.write("Keep dataset metadata and version history organized.")

        with st.container(border=True):
            st.markdown("### ⚙️ Preprocessing Records")
            st.write("Document the preprocessing steps applied to datasets.")

        with st.container(border=True):
            st.markdown("### 📈 Model Performance")
            st.write("Maintain model details and evaluation metrics.")

    with right:
        st.markdown(
            '<div class="login-heading">Welcome back</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<p class="muted">Log in to continue to your workspace.</p>',
            unsafe_allow_html=True
        )

        with st.form("login_form"):
            email = st.text_input(
                "Email address",
                placeholder="you@example.com"
            )

            password = st.text_input(
                "Password",
                type="password",
                placeholder="Enter your password"
            )

            submitted = st.form_submit_button(
                "Log In",
                use_container_width=True,
                type="primary"
            )

            if submitted:
                if not email.strip() or not password:
                    st.error("Please enter your email and password.")
                else:
                    user = login_user(email.strip(), password)

                    if user is not None:
                        st.session_state.user = user
                        st.session_state.logged_in = True
                        st.session_state.auth_page = "Login"
                        st.rerun()
                    else:
                        st.error(
                            "Invalid email or password. "
                            "Please check your details and try again."
                        )

        st.write("")
        st.markdown("Don't have an account?")

        if st.button("Create an Account", use_container_width=True):
            st.session_state.auth_page = "Register"
            st.rerun()

    show_audience_section()

    st.markdown(
        '<div class="footer">MLDMS · Dataset and experiment management</div>',
        unsafe_allow_html=True
    )


# =========================================================
# 7. REGISTRATION PAGE
# =========================================================

def register_page():
    show_brand()

    left, right = st.columns([1.0, 1.0], gap="large")

    with left:
        st.markdown(
            """
            <div class="hero">
                <h1>Start organizing your ML workflow.</h1>
                <p>
                    Create an account to manage dataset metadata,
                    versions, preprocessing records, model information,
                    and performance metrics.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")

        st.info(
            "After registration, you can create or join an "
            "organization workspace."
        )

    with right:
        st.markdown(
            '<div class="login-heading">Create your account</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<p class="muted">Register to access MLDMS.</p>',
            unsafe_allow_html=True
        )

        with st.form("register_form"):
            name = st.text_input(
                "Full name",
                placeholder="Enter your name"
            )

            email = st.text_input(
                "Email address",
                placeholder="you@example.com"
            )

            password = st.text_input(
                "Password",
                type="password",
                placeholder="At least 8 characters"
            )

            confirm_password = st.text_input(
                "Confirm password",
                type="password"
            )

            submitted = st.form_submit_button(
                "Create Account",
                use_container_width=True,
                type="primary"
            )

            if submitted:
                if not name.strip() or not email.strip():
                    st.error("Please complete all required fields.")

                elif len(password) < 8:
                    st.error("Password must contain at least 8 characters.")

                elif password != confirm_password:
                    st.error("The passwords do not match.")

                else:
                    success, message = register_user(
                        name.strip(),
                        email.strip(),
                        password,
                        role="User"
                    )

                    if success:
                        st.success(message)
                        st.session_state.auth_page = "Login"
                        st.rerun()
                    else:
                        st.error(message)

        st.write("")

        if st.button("Back to Login", use_container_width=True):
            st.session_state.auth_page = "Login"
            st.rerun()

    st.markdown(
        '<div class="footer">MLDMS · Create your workspace account</div>',
        unsafe_allow_html=True
    )


# =========================================================
# 8. LOGGED-IN SIDEBAR AND NAVIGATION
# =========================================================

def application_page():
    user = st.session_state.user

    with st.sidebar:
        st.markdown(
            """
            <h2 style="color:#60A5FA;margin-bottom:0;">📊 MLDMS</h2>
            <p style="color:#94A3B8;font-size:12px;">
                Dataset Management
            </p>
            """,
            unsafe_allow_html=True
        )

        st.divider()

        st.markdown("### 👤 My Account")
        st.write(user.get("name", "User"))
        st.caption(user.get("email", ""))
        st.caption("Role: " + str(user.get("role", "User")))

        st.divider()

        menu_options = [
            "Dashboard",
            "Company Workspace",
            "Upload Dataset",
            "Dataset Library",
            "Add Dataset Version",
            "Version History",
            "Preprocessing",
            "Preprocessing History",
            "Model Management",
            "Model Library",
            "Performance Management",
            "Performance Library",
        ]

        selected_page = st.radio(
            "Navigation",
            menu_options,
            index=0,
            label_visibility="collapsed",
            key="main_navigation"
        )

        st.divider()

        if st.button("🚪 Sign Out", use_container_width=True):
            st.session_state.logged_in = False
            st.session_state.user = None
            st.session_state.pop("main_navigation", None)
            st.session_state.auth_page = "Login"
            st.rerun()

    st.title("Machine Learning Dataset Management System")
    st.caption(
        "Manage datasets, versions, preprocessing, models, "
        "and performance records."
    )

    # Route the selected sidebar page to the existing module functions.
    if selected_page == "Dashboard":
        show_dashboard()

    elif selected_page == "Company Workspace":
        organization_page()

    elif selected_page == "Upload Dataset":
        upload_dataset()

    elif selected_page == "Dataset Library":
        view_datasets()

    elif selected_page == "Add Dataset Version":
        add_version()

    elif selected_page == "Version History":
        view_versions()

    elif selected_page == "Preprocessing":
        preprocessing_page()

    elif selected_page == "Preprocessing History":
        view_preprocessing()

    elif selected_page == "Model Management":
        model_management()

    elif selected_page == "Model Library":
        view_models()

    elif selected_page == "Performance Management":
        performance_management()

    elif selected_page == "Performance Library":
        view_performance()


# =========================================================
# 9. MAIN APPLICATION ROUTER
# =========================================================

if st.session_state.logged_in and st.session_state.user:
    application_page()

else:
    # Hide the sidebar while the user is logging in or registering.
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"] {
            display: none;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    if st.session_state.auth_page == "Register":
        register_page()
    else:
        login_page()

