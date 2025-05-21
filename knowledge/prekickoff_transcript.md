*Generated for: TechNova x AI Solutions: SmartAssist Pre-Kickoff Call Transcript (rasha.gh22@gmail.com)*

# TechNova x AI Solutions: SmartAssist Pre-Kickoff Call Transcript

Mon, May 1, 2025

0:00 \- Jordan Taylor Hi everyone, I think we're all here now. Thanks for joining this pre-kickoff call for the SmartAssist project. Let's start with a quick round of introductions so everyone knows who's on the call. I'm Jordan Taylor, Lead Project Manager at AI Solutions. I'll be directly leading this project and overseeing the initiation phase, making sure we establish clear scope and deliverables before the development team gets started.

0:22 \- Sarah Chen Hi everyone, I'm Sarah Chen, CEO of TechNova. Really excited to be working with AI Solutions on this internal LLM solution. We've been wanting to implement something like this for a while to help our growing team stay efficient.

0:35 \- Alex Rivera Good to meet everyone. I'm Alex Rivera, CTO at TechNova. I'll be the main technical point of contact for this project. I've been researching various LLM approaches and looking forward to discussing the implementation details.

0:48 \- Maya Patel Hello, I'm Maya Patel, Head of Engineering at TechNova. I'll be working closely with the AI Solutions team on the technical aspects and will likely be the one maintaining the solution after it's built.

1:00 \- Jordan Taylor Great\! I've reviewed the initial project brief and the research analysis report. I'd like to start by confirming my understanding of what you're trying to achieve with SmartAssist, and then we can dive into some specific questions I have. From what I've gathered, you're looking to create an internal LLM solution that can help your team quickly access information across your company's knowledge base, reducing time spent searching and improving collaboration. Is that accurate?

1:28 \- Sarah Chen That's exactly right. As we've grown from 5 to 8 people in the last six months, we're starting to see knowledge silos forming. Our team is spending too much time searching for information across Notion, GitHub, Slack, and Google Drive, and we're seeing inconsistent documentation quality. The goal is to have a system that not only helps us find information quickly but also assists with tasks like code documentation.

1:53 \- Alex Rivera And just to add to that, we've calculated that our team is spending about 30% of their time just looking for information or answering the same questions repeatedly. For a small team like ours, that's a significant productivity hit. We believe an internal LLM solution can help us reclaim that time and improve our onboarding process for new hires.

2:13 \- Jordan Taylor That makes perfect sense. And based on the report, I see you're looking for a RAG-based system that can connect to your existing tools. One question I have is about the priority of integrations. The brief mentions GitHub, Notion, Slack, and Google Drive. Are all of these equally important, or should we prioritize certain integrations first?

2:35 \- Alex Rivera I'd say GitHub and Notion are the highest priorities, as that's where most of our technical documentation and codebase reside. Slack would be next, and then Google Drive. But ideally, we'd want all four integrated by the end of the project.

2:49 \- Maya Patel And if I could add \- with GitHub, we're particularly interested in making sure the system can understand our codebase and help with documentation. That's a big pain point for us right now.

3:02 \- Jordan Taylor Thanks for clarifying. Another question I have is about deployment. Are you looking for a self-hosted solution or would you prefer a cloud-based deployment? And do you have any specific security requirements we should be aware of?

3:16 \- Alex Rivera We'd definitely prefer a cloud-based solution, specifically on AWS since that's what we already use for our infrastructure. As for security, since we're dealing with our internal codebase and company information, we need to ensure the data remains within our security perimeter. We don't want any of our proprietary information leaving our systems or being used to train public models.

3:39 \- Jordan Taylor That makes sense. The report mentions a budget range of $20,000 to $25,000. Is this still accurate? And are there any specific constraints or considerations regarding the ongoing costs after deployment?

3:53 \- Sarah Chen Yes, that budget range is still accurate. We've set aside up to $25,000 for implementation. For ongoing costs, we're planning for around $650 per month for API usage and maintenance. We want to make sure this is sustainable long-term, so keeping those ongoing costs predictable is important for us.

4:13 \- Jordan Taylor For our engineer selection, we'll need to find people experienced with RAG systems, AWS deployments, and integrations with these specific tools. Are there any particular skills or experiences you'd prioritize in the team members?

4:29 \- Alex Rivera Definitely experience with OpenAI APIs and vector databases like Pinecone or Weaviate. Experience with Python for backend development and TypeScript/React for the frontend would be ideal. And anyone who has built internal knowledge management tools before would be a huge plus.

4:48 \- Maya Patel And if possible, finding someone who has experience with code understanding and documentation would be great, since that's such an important use case for us.

4:58 \- Jordan Taylor Got it. Now about the timeline \- the brief mentions a 3-month implementation period. Is there any flexibility there, or do you have any hard deadlines we should be aware of?

5:12 \- Sarah Chen We don't have a hard deadline, but we'd like to have the system up and running by mid-August if possible. We have two new engineers joining in September, and it would be great if we could use this system to help with their onboarding.

5:27 \- Jordan Taylor That's helpful context. Let's talk about success metrics. How will you measure whether this project has been successful? The report mentions several metrics like 50% reduction in search time and 80% accuracy in answering internal questions. Are these still the key metrics you're looking at?

5:45 \- Sarah Chen Yes, those are still our primary success metrics. The main goal is to save our team time, so that 50% reduction in search time is probably the most important one. We're also looking at reducing onboarding time for new hires from 4 weeks to 2 weeks.

6:02 \- Alex Rivera And from a technical perspective, we want to ensure the system has high accuracy. If it starts giving incorrect information, people will stop using it. So that 80% accuracy benchmark is important to us.

6:16 \- Jordan Taylor Makes sense. One more question \- will you have someone from your team who can work closely with our engineers during development? It's often helpful to have a dedicated point person who can answer questions and provide feedback as we go.

6:32 \- Maya Patel Yes, that will be me. I can allocate about 25% of my time during the project to work with your team. I'm familiar with all our systems and can help with any technical questions that come up.

6:45 \- Jordan Taylor Perfect\! That will be really valuable. I think I have most of what I need to create a comprehensive project scope document. Based on today's discussion, I'll put together a document outlining the scope, deliverables, timeline, and success metrics. I'll share it with you by the end of the week for your feedback. We should be able to have a team assembled within 7-10 business days after the scope document is approved.

7:08 \- Sarah Chen That sounds great. We're excited to get started. Is there anything else you need from us at this stage?

7:15 \- Jordan Taylor I think we have what we need for now. It would be helpful if Alex or Maya could share any additional documentation about your current systems \- particularly how your GitHub, Notion, Slack, and Google Drive are structured. That will help us understand the integration points better.

7:31 \- Alex Rivera Absolutely, I'll put together a document with that information and send it over by tomorrow.

7:38 \- Jordan Taylor Great\! If there are no other questions, I think we can wrap up. Thank you all for your time today. We'll be in touch soon with the project scope, and feel free to reach out if you think of anything else in the meantime.

7:52 \- Sarah Chen Thank you, Jordan. Looking forward to working with you.

7:58 \- Maya Patel Thanks, looking forward to the next steps.

8:00 \- Alex Rivera Thanks everyone, bye.

8:02 \- Jordan Taylor Bye, everyone\!