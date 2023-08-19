
import openai
import streamlit as st


def word_count(text):
    return len(text.split())

def main():
    st.title("IntroGPT")
    st.write("Generate Intelligent and Relevant Product/Service Cold Email Intros to Job Postings")
    job_description = st.text_input("In <500 words, enter the job description that you want to target")
    your_company_details = st.text_input("In <500 words, enter details about your product or service that you want to position")
    
    if word_count(job_description) > 500:
        st.warning("Job description should not exceed 500 words!")
        return

    if word_count(your_company_details) > 500:
        st.warning("Product/Service details should not exceed 500 words!")
        return
    
    if st.button("Generate Intro Email"):
        openai.api_key=st.secrets.openai_api_key
        response = openai.ChatCompletion.create(
        model='gpt-4-0613',
        messages=[
              {"role": "system", "content": """
             
              Objective:
              
              You are tasked to draft an email as an expert cold email writing agent.
              Use your expertise as an inside sales specialist to understand a job description 
              and pitch a product that can potentially replace the need for hiring a full-time person for that job.
              
              Below are the steps that you will have to follow.
              
              Understanding the Job Description: Read through the job posting provided to you.
              Identify the key responsibilities, skills required, and any other pertinent information about the role.
              
              Understanding the Product: Familiarize yourself with the details about the product given to you.
              Understand the primary functionalities and benefits of the product, especially those that correlate 
              with the responsibilities mentioned in the job posting.
              
              Drafting the Email:
              
              Introduction: Start by referencing the job posting the recipient has posted. 
              For instance, "I see that you are hiring for the role of [job role]."

              Body: Highlight the benefits and features of the product and how it can potentially carry out some, 
              if not all, of the tasks mentioned in the job posting. Mention its efficiency and why it could be 
              a worthwhile alternative to hiring a full-time employee.
              
              Tone: The email should be semi-formal. It should be professional yet approachable.
              
              Length: Ensure the email doesn't exceed 150 words.
              
              Engagement: End the email in a manner that piques the recipient's curiosity about the product 
              and invites them to seek more information or a demo.
              
              Conclusion: Conclude with a call to action, perhaps offering them a product demo or a more detailed discussion. 
              
              Review:
              
              After drafting, review the content to ensure it aligns with the provided guidelines and the objectives of the task.
              
              Inputs: You will be provided with two sets of information:
              
              Job Posting: A detailed description of a job role, including responsibilities, qualifications, and other specifics.
              Product Details: Information about the product's features, benefits, and how it can be a potential solution to the tasks outlined in the job posting.
              
              Output: A short, succinct email (not exceeding 150 words) that aligns with the above guidelines and effectively 
              pitches the product as an alternative to hiring a full-time employee based on the provided job posting. Also
              share a relevant subject line.

      
              """
              },
              {"role": "user", "content": f"""
      
              job posting by the potential customer: {job_description}

              product/service that you are pitching: {your_company_details}
    
              """},
              ],
              temperature=0.3
              )
      
        output = response["choices"][0]["message"]["content"]

        st.write(output)

# Run the app
if __name__ == "__main__":
    main()
