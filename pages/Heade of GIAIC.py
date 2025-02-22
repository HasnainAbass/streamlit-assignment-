import streamlit as st

st.title("Leadership of GIAIC Program !")

st.markdown("## Meet our Leadership")

tab1, tab2 , tab3 , tab4 = st.tabs(["Sir Zia Khan","Miss Hira khan","Sir Daniyal Nagori","Sir Ameen Alam"])

with tab1:
    st.image('images/sirZiakhan.jpg',caption='MR. ZIA KHAN')
    st.text("Mr. Zia Khan is a GenAI and Web 3.0 developer and nation-transforming social entrepreneur who has successfully completed numerous software projects and trained hundreds of thousands of software developers in the latest state-of-the-art technologies. ")
    st.text("He believes that underdeveloped countries can be economically transformed by imparting their youth with software development skills that are in great demand all over the world. He worked with the President of Pakistan and the Governor of provinces to launch mass-scale training programs for the unemployed and underprivileged youth of the country, training hundreds of thousands of participants.")
    st.text("In addition, the President of Pakistan awarded him Tamgha-e-Imtiaz (lit. 'Medal of Excellence'), state-organized honor in Pakistan and is given to civilians based on their achievements. He also received Microsoft's Most Valuable Professional (MVP) awards for eight consecutive years in client and cloud technologies. ")
    st.text("Currently, he is working as Chief Generative AI Officer as the Founder at Panacloud. He has had the honor of serving as Honorary Chief Operating Officer of the Governor Sindh Initiative for GenAI, Web3, and Metaverse, Lead Software Developer at Unisoncare Corp, Lead Software Engineer at Xenosys Corporation.")
    st.text("He has been involved for the past 17 years in an effort to make Pakistan a major tech hub and a leading provider of tech services to Silicon Valley, and as a culmination of tech education effort, he developed a mass IT education program to bring the emerging tech skills of AI, Blockchain, Cloud Native computing and IoT with the blessings of the Honorable President of Pakistan, Dr. Arif Alvi. He has also been a volunteer faculty at Saylani Welfare International Trust.")

    button = st.columns(4)
    with button[0]:
     st.link_button("More about Sir Zia", "https://www.piaic.org/")
    with button[1]:
     st.link_button("Detail's", "https://www.linkedin.com/in/ziaukhan/")
# ---------------------------------------------------------------------------------------
with tab2:
    st.image('images/MissHirakhan.jpg',caption='Chief Operating Officer in PIAIC Miss Hira')
    st.text("Miss Hira Khan is a GenAI and Web 3.0 developer and I am the Director of the Women Empowerment of the Presidential Initiative for Artificial Intelligence & Computing. The mission of PIAIC is to reshape Pakistan by revolutionizing education, research, and business by adopting latest, cutting-edge technologies. Experts are calling this the 4th industrial revolution. The mission is to train our workforce in the latest technologies and abuild a technology driven economy in both the domestic market as well as exports. I am a patron of the PIAIC program.")
    st.text("I co-founded Panacloud Pvt. Ltd. in 2012, which has been working in the technology education and services industry for the past 7 years. Prior to this I had been leading the Operation Badar Welfare Trust. Over the past 20 years, my team has collectively trained over 110,000 students, 30,000+ of which I am personally responsible for. I have been working with the President of Pakistan and the Governor of provinces to launch mass-scale training programs for the unemployed and underprivileged youth of the country, training hundreds of thousands of participants.")
    st.text("I have been involved for the past 17 years in an effort to make Pakistan a major tech hub and a leading provider of tech services to Silicon Valley, and as a culmination of tech education effort, I developed a mass IT education program to bring the emerging tech skills of AI, Blockchain, Cloud Native computing and IoT with the blessings of the Honorable President of Pakistan, Dr. Arif Alvi. I have also been a volunteer faculty at Saylani Welfare International Trust.")
    st.link_button("More about Miss Hira Khan", "https://www.linkedin.com/in/hirakhanofficial/")
# ---------------------------------------------------------------------------------------
with tab3:
   st.image('images/MissHirakhan.jpg',caption='Chief Operating Officer in PIAIC Miss Hira')
   st.text("Miss Hira Khan is a GenAI and Web 3.0 developer and I am the Director of the Women Empowerment of the Presidential Initiative for Artificial Intelligence & Computing. The mission of PIAIC is to reshape Pakistan by revolutionizing education, research, and business by adopting latest, cutting-edge technologies. Experts are calling this the 4th industrial revolution. The mission is to train our workforce in the latest technologies and abuild a technology driven economy in both the domestic market as well as exports. I am a patron of the PIAIC program.")

#     st.image('images/SirDaniyal.jpg',caption=' MR. Daniyal Nagori')
#     st.text("Mr. Daniyal Nagori is a GenAI and Web 3.0 developer and nation-transforming social entrepreneur who has successfully completed numerous software projects and trained hundreds of thousands of software developers in the latest state-of-the-art technologies. ")
#     st.text("he has been fortunate to be able to architect solutions in as wide an array as Cloud Native, Voice Computing/Chatbot development, Web, Mobile, AI, and Blockchain.")
#     st.link_button("More about Sir Daniyal Nagori", "https://www.linkedin.com/in/daniyalnagori/?originalSubdomain=pk")
# --------------------------------------------------------------------------------------
with tab4:
   st.image('images/MissHirakhan.jpg',caption='Chief Operating Officer in PIAIC Miss Hira')
   st.text("Miss Hira Khan is a GenAI and Web 3.0 developer and I am the Director of the Women Empowerment of the Presidential Initiative for Artificial Intelligence & Computing. The mission of PIAIC is to reshape Pakistan by revolutionizing education, research, and business by adopting latest, cutting-edge technologies. Experts are calling this the 4th industrial revolution. The mission is to train our workforce in the latest technologies and abuild a technology driven economy in both the domestic market as well as exports. I am a patron of the PIAIC program.")
#     st.image('images/SirAmeen.jpg',caption=' MR. Ameen Alam Bank Al-Beilaad UAE')
#     st.text("Mr. Ameen Alam is a GenAI and Web 3.0 developer and Experience in leading & executing multiple large scale IT programs, with experience of directing all aspects of the software project lifecycle with different project methodologies like Agile, Waterfall (Scrum, Kanban) ")
#     st.text("he has been Configuring networks SDN, VPC, network bridging, NAT, DHCP, subnets, IPs, and firewall rules, WAF, VPN, network port, network security best practice, for rack server, blade server, AWS, GCP, and on-premises infrastructure")
#     st.link_button("More about Sir Ameen Alam", "https://www.linkedin.com/in/ameen-alam/")
