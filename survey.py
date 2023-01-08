import streamlit as st
from PIL import Image

def show_survey():
    page_bg_img = """
    <style>
    [data-testid = "stAppViewContainer"]{
        background-color: #fff;
        background-image:
        linear-gradient(90deg, transparent 79px, #abced4 79px, #abced4 81px, transparent 81px),
        linear-gradient(#eee .1em, transparent .1em);
        background-size: 100% 1.2em;
    }
    </style>
    """

    st.markdown(page_bg_img, unsafe_allow_html = True)


    st.title("Customer Survey")
    
    st.write("Bank accounts - we all have one - but, unlike electricity or the internet, not many of us give much thought to switching to a different service provider. This survey will reveal the reasons which would be most likely to push consumers towards making a change. Only one in four customers say they don't know what could cause them to switch, even though the majority describe generally favorable encounters with their bank. Everyone else is willing to be persuaded to act. Despite great customer satisfaction, most banks wager that their clients won't leave because of inertia rather than loyalty.")
    
    
    image1 = Image.open('Picture1.png')
    st.image(image1, caption = 'The reason why customer leave a bank')

    st.write("- That's a wager the banks may lose if agile digital rivals gain market share and onboarding becomes almost trivial.")
    st.write("- Poor handling of fraud situations is at the top of the list; according to 55% of respondents, this would prompt them to switch banks.")
    st.write("- Only 22% of respondents indicated that the lack of local branches would be a deciding factor for them, reflecting the reality that online banking is now the norm.")
    
    st.write("In addition, the reason may also be influenced by age. ")

    image2 = Image.open('Picture2.png')
    st.image(image2, caption = 'Churn Probability Per Age Group')

    st.write("- Younger clients don't seem to have as much of a need to switch banks because most of the perks they receive are generally the same across the sector. Older clients, on the other hand, might begin to consider their pensions, wills, taxes, and other obligations, which means they'll focus on obtaining the greatest price regardless of the bank.")
    st.write("- The older generation values customer service and face-to-face interaction more than the younger generation, who are on the complete opposite spectrum and prefer as little face-to-face interaction as possible, which is where today's banks are moving with digitization, so this could also be the reason.")
    st.write("- All in all, the peak churn rates seem to occur across the age groups of 50–60, 60–70, and 40–50 in that order.")


