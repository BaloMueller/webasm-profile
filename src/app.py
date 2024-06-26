import streamlit as st
from PIL import Image
import requests
from io import BytesIO
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def main():
    st.set_page_config(page_title="Sebastian Müller - Strategic Technology Leader", layout="wide")

    # Contact Information
    col1, col2 = st.columns(2)
    with col1:
        # Header
        st.title("Sebastian Müller")
        st.subheader("Strategic Technology Leader & Visionary")

        # Contact Information
        st.write("📍 Ottobrunner Str. 34, 81737 München")
        st.write("📱 +49 175 5082001",)
        st.write("✉️ s@mlr.digital")
        st.write("🔗 [LinkedIn Profile](https://www.linkedin.com/in/sebamuller/)")
        st.write("🧑‍💻 [Github Profile](https://github.com/balomueller)")

    with col2:
        # Profile picture
        img_url = "https://avatars.githubusercontent.com/u/793558?v=4"
        response = requests.get(img_url)
        img = Image.open(BytesIO(response.content))
        st.image(img, use_column_width=True, caption="Sebastian Müller")
    
    # Summary
    st.header("Professional Summary")
    st.write("""
    Entrepreneurial CTO and technology leader with over 18 years of experience in
    building high-performing teams and delivering innovative, scalable software
    solutions. Proven track record of driving strategic technology initiatives, fostering
    cultural transformation, and achieving business growth through technology
    enablement. Skilled in stakeholder management, product development, and
    architectural design for secure, scalable, cloud-native platforms.
    """)

    st.divider()

    # Core Competencies
    st.header("Core Competencies")

    competencies = [
        "Strategic Planning", "Software Architecture", "Cloud & DevOps", 
        "Product Management", "Security & Compliance", "People Leadership", 
        "Agile Methodologies", "Process Optimization", "Technical Vision", 
        "Customer Engagement"
    ]

    # Create and generate a word cloud image:
    wordcloud = WordCloud(width=1600, height=800).generate(", ".join(competencies))

    # Display the generated image:
    plt.figure( figsize=(20,10), facecolor='k')
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.imshow(wordcloud)
    st.pyplot(plt.gcf())
    st.write(", ".join(competencies))

    st.divider()

    # Values
    st.header("Values")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Leadership")
        st.write("A powerful Team is always the key to success.")
    with col2:
        st.subheader("Ownership")
        st.write('Saying "somebody should…" is easy. "I will…" solves problems.')
    with col3:
        st.subheader("Customer focus")
        st.write("Understanding the customer pain is the key to create value.")

    st.divider()

    # Skills
    st.header("Skills")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Leadership Skills")
        leadership_skills = [
            "Strategic Planning",
            "Team Building and Leadership",
            "Efficient Hiring",
            "Agile Methodologies (Scrum, Kanban)",
            "Product Management and Development",
            "Stakeholder Management"
        ]
        for skill in leadership_skills:
            st.write(f"- {skill}")
    
    with col2:
        st.subheader("Technical Skills")
        technical_skills = [
            "Software Development: Python, C, Rust, Java, JavaScript",
            "Cloud Platforms: Azure, AWS, Google Cloud",
            "Databases: MySQL, Elasticsearch, Redis, Cassandra, Postgres",
            "DevOps: Kubernetes, Prometheus, Grafana, CI/CD pipelines",
            "Security: ISO 27001, Information Security Management"
        ]
        for skill in technical_skills:
            st.write(f"- {skill}")

    with col3:
        st.subheader("Soft Skills")
        soft_skills = [
            "Effective Communication",
            "Customer Focus",
            "Problem Solving",
            "Innovation and Creativity",
            "Sales and Negotiation",
            "Due Diligence Analysis, GAP Analysis and Issue Resolving Strategy"
        ]
        for skill in soft_skills:
            st.write(f"- {skill}")


    st.divider()

    # Professional Experience
    st.header("Professional Experience")

    st.subheader("CTO and Founder, rapitag GmbH")
    st.write("Feb 2017 - Mar 2024")
    rapitag_achievements = [
        "Co-founded and led the technical vision for an innovative IoT company, disrupting the retail and logistics industries with cutting-edge security devices and self-checkout solutions.",
        "Spearheaded the development of a highly scalable, cloud-native software platform encompassing iOS/Android apps, Python backend, MySQL datastore, Elasticsearch for BigData processing, and firmware in C and Rust.",
        "Built and managed a high-performing team of 30+ FTEs, scaling from inception to a €1M+ annual revenue business.",
        "Led the product development for 5 products from idea to mass production.",
        "Drove the strategic product roadmap, anticipating industry trends, and securing over 15 patents for disruptive technologies.",
        "Fostered a customer-centric culture, conducting extensive UX testing and directly engaging with Fortune 500 retail enterprises worldwide to secure multi-million-dollar contracts.",
        "Successfully orchestrated the majority stake sale of the company in March 2024."
    ]
    for achievement in rapitag_achievements:
        st.write(f"- {achievement}")

    st.subheader("Principal IT Consultant, Syngenio AG")
    st.write("Jan 2021 – Apr 2023")
    syngenio_achievements = [
        "Provided strategic consulting services to clients like Allianz, HVB Systems, and Telekom in next-generation banking, payments, and retail domains.",
        "Spearheaded product management, marketing, and sales for Syngenio's innovative payment platform, generating over €1M in revenue.",
        "Created and owned an innovative payment product with full P&L responsibility, capitalizing on industry trends and generating €300K+ in consulting revenue."
    ]
    for achievement in syngenio_achievements:
        st.write(f"- {achievement}")

    st.subheader("Head of IT Operations & Information Security Officer, intelliAd Media GmbH")
    st.write("2015 – 2017")
    intelliad_achievements = [
        "Led the IT Operations department, reducing downtime from 99.98% to 99.9999%, and managing over 1,000 virtual machines on AWS and 100+ physical servers.",
        "Implemented a scalable Kubernetes-based hosting platform, Elasticsearch logging cluster, and overhauled system backups for 1 PB of data.",
        "Planned and managed a BigData project driving all products and enabling advanced business analytics.",
        "Certified as Information Security Officer and led the company's successful ISO 27001 certification."
    ]
    for achievement in intelliad_achievements:
        st.write(f"- {achievement}")

    st.divider()

    # Education & Credentials
    st.header("Education & Credentials")
    credentials = [
        "Diploma in Computer Science, Wilhelm Büchner Hochschule (2009 - 2015)",
        "Certified Chief Information Security Officer",
        "Contributions to Apache Spark, MSpec, and other open-source projects",
        "Speaker at various tech conferences",
        "Former Organizer of Munich DevOps Community"
    ]
    for credential in credentials:
        st.write(f"- {credential}")


    st.toast("Get in touch with me now: s@mlr.digital", icon="👋")

if __name__ == "__main__":
    main()